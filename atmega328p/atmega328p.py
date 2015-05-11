from copy import deepcopy

from arch.avr import opcodes
from atmega328p.data_mem_space import DataMemorySpace
from atmega328p.ioregisters import IORegisters
from atmega328p.memory import Memory
from .status import Status
from opcoder.opcoder import Opcoder


class ATMEGA328P:

    def __init__(self):
        self.status = Status()
        self.ioregs = IORegisters()
        self.xiomem = Memory(160)
        self.sram = Memory(2048)
        # Used for instructions like CPSE, it should be explicitly reset every time.
        self.skip = False
        self.__opcodes = Opcoder(opcodes)
        self.__data_mem_space = DataMemorySpace(self.status, self.ioreg, self.xiomem, self.sram)
        # On board flash memory
        self.__program_mem_space = Memory(32*1024, 2)

    def execute(self, opcode):
        lkp = self.__opcodes.lookup(opcode, 16)  # entry, opcode values, size
        op = lkp[0]  # has 'repr' and 'abstract'
        ab = op['abstract'](lkp[1])  # returns (opcode, operand1, operand2, ...)
        # TODO: This sucks.
        getattr(self, '_ATMEGA328P__' + ab[0])(ab[1:])
        self.status.pc.inc()

    def __stack_push_pc(self):
        self.__data_mem_space[self.ioregs.sp] = (self.status.pc + 2) // 256
        self.__data_mem_space[self.ioregs.sp-1] = (self.status.pc + 2) % 256
        self.ioregs.sp.sub(2)

    def __stack_pop_pc(self):
        self.status.pc._value = self.__data_mem_space[self.ioregs.sp+1] * 256 + \
                                self.__data_mem_space[self.ioregs.sp+2]
        self.ioregs.sp.add(2)

    def __ADD(self, ops, carry=False):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rd = rdst.unsigned_value
        rs = rsrc.unsigned_value
        rdst.add(rsrc.unsigned_value + (1 if carry and self.status.sreg.c else 0))
        rr = rdst.unsigned_value

        self.status.sreg.c = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)
        self.status.sreg.h = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x08)
        self.status.sreg.v = bool(((rd & rs & ~rr) | (~rd & ~rs & rr)) & 0x80)
        self.status.sreg.n = bool(rr & 0x80)
        self.status.sreg.z = not bool(rr)
        self.status.sreg.s = self.status.sreg.n ^ self.status.sreg.v

    def __ADC(self, ops):
        self.__ADD(ops, carry=True)

    def __ADIW(self, ops):
        dst = ops[0]
        immw = ops[1]
        rdsth = getattr(self.status, 'r' + [25, 27, 29, 31][dst])
        rdstl = getattr(self.status, 'r' + [24, 26, 28, 39][dst])

        rd = rdstl.unsigned_value
        rs = immw % 256
        rdstl._add(rs)
        rr = rdstl.unsigned_value
        ctmp = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)

        rd = rdsth.unsigned_value
        rs = immw // 256
        rdsth._add(rs + (1 if ctmp else 0))
        rr = rdsth.unsigned_value

        self.status.sreg.c = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)
        self.status.sreg.v = bool((~rd & rr & 0x80) != 0)
        self.status.sreg.n = bool(rr & 0x80)
        self.status.sreg.z = not bool(rr + rdstl.unsigned_value)
        self.status.sreg.s = self.status.sreg.n ^ self.status.sreg.v

    def __AND(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rdst.land(rsrc.unsigned_value)

        self.status.sreg.v = False
        self.status.sreg.n = rdst.isset(7)
        self.status.sreg.z = not bool(rdst.unsigned_value)
        self.status.sreg.s = self.status.sreg.v ^ self.status.sreg.n

    def __ANDI(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        immb = ops[1]

        rdst.land(immb)

        self.status.sreg.v = False
        self.status.sreg.n = rdst.isset(7)
        self.status.sreg.z = not bool(rdst.unsigned_value)
        self.status.sreg.s = self.status.sreg.v ^ self.status.sreg.n

    def __ASR(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        self.status.sreg.c = bool(rdst.unsigned_value % 2)
        rdst._value = (rdst._value & 0x80) + (rdst._value & 0x7F) // 2
        self.status.sreg.n = rdst.isset(7)
        self.status.sreg.z = not bool(rdst._value)
        self.status.sreg.v = self.status.sreg.n ^ self.status.sreg.c
        self.status.sreg.s = self.status.sreg.n ^ self.status.sreg.v

    def __BCLR(self, ops):
        self.status.sreg.reset(ops[0])

    def __BLD(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        if self.status.sreg.t:
            rdst.set(ops[1])
        else:
            rdst.reset(ops[1])

    def __BRBC(self, ops):
        branch = not self.status.sreg.isset(ops[0])
        if branch:
            self.status.pc.add(ops[1]) if ops[1] >= 0 else self.status.pc.sub(-ops[1])

    def __BRBS(self, ops):
        branch = self.status.sreg.isset(ops[0])
        if branch:
            self.status.pc.add(ops[1]) if ops[1] >= 0 else self.status.pc.sub(-ops[1])

    def __BREAK(self, ops):
        # TODO: implement stop mode (is it really necessary?)
        pass

    def __BSET(self, ops):
        self.status.sreg.set(ops[0])

    def __BST(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        self.status.sreg.t = rdst.isset(ops[1])

    def __CALL(self, ops):
        self.__stack_push_pc()
        self.status.pc._value = ops[0]

    def __CBI(self, ops):
        # TODO: avoid address constants
        self.__data_mem_space[0x20 + ops[0]] &= 255 - (2**ops[1])

    def __CBR(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rdst.land(256 - ops[1])

        self.status.sreg.v = False
        self.status.sreg.n = rdst.isset(7)
        self.status.sreg.z = not bool(rdst.unsigned_value)
        self.status.sreg.s = self.status.sreg.v ^ self.status.sreg.n

    def __COM(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rdst.lxor(0xff)

    def __CP(self, ops, carry=False, immediate=False):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rrrr = deepcopy(rdst)
        if carry:
            rrrr.sub(rsrc.unsigned_value + 1 if self.status.sreg.c else 0)
        elif immediate:
            rrrr.sub(rsrc.unsigned_value + 1 if self.status.sreg.i else 0)
        else:
            rrrr.sub(rsrc.unsigned_value)
        rd = rdst.unsigned_value
        rs = rsrc.unsigned_value
        rr = rrrr.unsigned_value

        self.status.sreg.c = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)
        self.status.sreg.h = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x08)
        self.status.sreg.v = bool(((rd & rs & ~rr) | (~rd & ~rs & rr)) & 0x80)
        self.status.sreg.n = bool(rr & 0x80)
        self.status.sreg.z = not bool(rr)
        self.status.sreg.s = self.status.sreg.n ^ self.status.sreg.v

    def __CPC(self, ops):
        self.__CP(self, ops, carry=True)

    def __CPI(self, ops):
        self.__CP(self, ops, immediate=True)

    def __CPSE(self, ops):
        r1 = getattr(self.status, ops[0].lower())
        r2 = getattr(self.status, ops[1].lower())

        if r1.unsigned_value == r2.unsigned_value:
            self.skip = True

    def __DEC(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rdst.dec()

        self.status.sreg.z = not bool(rdst.unsigned_value)
        self.status.sreg.n = rdst.isset(7)
        self.status.sreg.v = rdst.unsigned_value == 0x7F
        self.status.sreg.s = self.status.sreg.n ^ self.status.sreg.v

    def __DES(self, ops):
        raise Exception("Not here, actually")

    def __EOR(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rdst.lxor(rsrc.unsigned_value)

        self.status.sreg.v = False
        self.status.sreg.n = rdst.isset(7)
        self.status.sreg.s = self.status.sreg.v ^ self.status.sreg.n
        self.status.sreg.z = not bool(rdst)

    def __FMUL(self, ops, signed=(False, False)):
        # TODO: Check more thoroughly
        mul1 = getattr(self.status, ops[0].lower())
        mul2 = getattr(self.status, ops[1].lower())

        mul1v = mul1.unsigned_value + (0xFF00 if mul1.isset(7) and signed[0] else 0)
        mul2v = mul2.unsigned_value + (0xFF00 if mul2.isset(7) and signed[1] else 0)

        result = (mul1v * mul2v * 2) & 0x1FFFF

        self.status.sreg.c = bool(result & 0x10000)
        result &= 0xFFFF
        self.status.sreg.z = not bool(result)

        self.status.r1._value = result // 256
        self.status.r0._value = result % 256

    def __FMULS(self, ops):
        self.__FMUL(ops, (True, True))

    def __FMULSU(self, ops):
        self.__FMUL(ops, (True, False))

    def __ICALL(self, ops):
        self.__stack_push_pc()
        self.status.pc._value = self.status.z._value

    def __IJMP(self, ops):
        self.status.pc._value = self.status.z._value

    def __IN(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rdst._value = self.__data_mem_space[0x20 + ops[1]]

    def __INC(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rdst.add(1)

        self.status.sreg.v = rdst._value == 0x80
        self.status.sreg.z = not bool(rdst._value)
        self.status.sreg.n = rdst.isset(7)
        self.status.sreg.s = self.status.sreg.n ^ self.status.sreg.v

    def __JMP(self, ops):
        self.status.pc._value = ops[1]

    def __LAC(self, ops):
        #rsrc = getattr(self.status, ops[0].lower())
        #self.status.z._value = self.status.z._value & (0xFF - rsrc._value)
        raise Exception("LAC instruction not available on this CPU")

    def __LAS(self, ops):
        raise Exception("LAS instruction not available on this CPU")

    def __LAT(self, ops):
        raise Exception("LAT instruction not available on this CPU")

    def __LD(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        if 'X' in ops[1]:
            if ops[1] == '-X':
                self.status.x.dec()
            rdst._value = self.__data_mem_space[self.status.x.unsigned_value]
            if ops[1] == 'X+':
                self.status.x.inc()
        elif 'Y' in ops[1]:
            if ops[1] == '-Y':
                self.status.y.dec()
            if len(ops) == 3:
                rdst._value = self.__data_mem_space[self.status.y.unsigned_value + ops[2]]
            else:
                rdst._value = self.__data_mem_space[self.status.y.unsigned_value]
            if ops[1] == 'Y+':
                self.status.y.inc()
        elif 'Z' in ops[1]:
            if ops[1] == '-Z':
                self.status.z.dec()
            if len(ops) == 3:
                rdst._value = self.__data_mem_space[self.status.z.unsigned_value + ops[2]]
            else:
                rdst._value = self.__data_mem_space[self.status.z.unsigned_value]
            if ops[1] == 'Z+':
                self.status.z.inc()

    def __LDI(self, ops):
        getattr(self.status, ops[0].lower())._value = ops[1]

    def __LDS(self, ops):
        getattr(self.status, ops[0].lower())._value = self.__data_mem_space[ops[1]]

    def __LPM(self, ops):
        if len(ops) == 0:
            self.status.r0._value = self.__program_mem_space[self.status.z._value]
        else:
            # TODO: check for spurious arguments?
            rdst = getattr(self.status, ops[0].lower())
            rdst._value = self.__program_mem_space[self.status.z._value]
            if ops[1] == 'Z+':
                self.status.z.inc()

    def sbroscia(self, file):
        data = file.read()
        while data:
            a, b = self.__opcodes.lookup(
                sum([x * y for (x, y) in zip(data[0:4], [2**24, 2**16, 2**8, 1])]), 16
            )
            print(a)
            data = data[b//8:]
