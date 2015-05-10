from .status import Status
from opcoder.opcoder import Opcoder
from .opcodes import opcodes


class ATMEGA328P:

    def __init__(self):
        self.status = Status()
        self.__opcodes = Opcoder(opcodes)

    def execute(self, opcode):
        lkp = self.__opcodes.lookup(opcode, 16)  # entry, opcode values, size
        op = lkp[0]  # has 'repr' and 'abstract'
        ab = op['abstract'](lkp[1])  # returns (opcode, operand1, operand2, ...)
        # TODO: This sucks.
        #self.c, self.t, self.z, self.h, self.v, self.p, self.n, self.i = \
        #    self.status.sreg.c, self.status.sreg.t, self.status.sreg.z, self.status.sreg.h, \
        #    self.status.sreg.
        getattr(self, '_ATMEGA328P__' + ab[0])(ab[1:])
        self.status.pc.inc()

    def __ADD(self, ops, carry=False):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rd = rdst.unsigned_value
        rs = rsrc.unsigned_value
        rdst.add(rsrc.unsigned_value + (1 if carry and self.status.sreg.c else 0))
        rr = rdst.unsigned_value

        # c = ((rd & rs & 0x80) != 0) or ((rs & ~rr & 0x80) != 0) or ((rd & ~rr & 0x80) != 0)
        # h = ((rd & rs & 0x08) != 0) or ((rs & ~rr & 0x08) != 0) or ((rd & ~rr & 0x80) != 0)
        # v = ((rd & rs & ~rr & 0x80) != 0) or ((~rd & ~rs & rr & 0x80) != 0)
        # n = (rr & 0x80) != 0
        # z = (rr == 0)
        # s = n ^ v

        self.status.sreg.c = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)
        self.status.sreg.h = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x08)
        self.status.sreg.v = bool(((rd & rs & ~rr) | (~rd & ~rs & rr)) & 0x80)
        self.status.sreg.n = bool(rr & 0x80)
        self.status.sreg.z = bool(rr)
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
        rr = rdsth = rdsth.unsigned_value

        self.status.sreg.c = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)
        self.status.sreg.v = bool((~rd & rr & 0x80) != 0)
        self.status.sreg.n = bool(rr & 0x80)
        self.status.sreg.z = bool(rr + rdstl.unsigned_value)
        self.status.sreg.s = self.status.sreg.n ^ self.status.sreg.v

    def __AND(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rdst.land(rsrc.unsigned_value)

        self.status.sreg.v = False
        self.status.sreg.n = bool(rdst.unsigned_value & 0x80)
        self.status.sreg.z = bool(rdst.unsigned_value)
        self.status.sreg.s = self.status.sreg.v ^ self.status.sreg.n

    def __ANDI(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        immb = ops[1]

        rdst.land(immb)

        self.status.sreg.v = False
        self.status.sreg.n = bool(rdst.unsigned_value & 0x80)
        self.status.sreg.z = bool(rdst.unsigned_value)
        self.status.sreg.s = self.status.sreg.v ^ self.status.sreg.n

    def __ASR(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        self.status.sreg.c = bool(rdst.unsigned_value % 2)
        rdst._value = (rdst._value & 0x80) + (rdst._value & 0x7F) // 2
        self.status.sreg.n = bool(rdst._value & 0x80)
        self.status.sreg.z = bool(rdst._value)
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

    def sbroscia(self, file):
        data = file.read()
        while data:
            a, b = self.__opcodes.lookup(
                sum([x * y for (x, y) in zip(data[0:4], [2**24, 2**16, 2**8, 1])]), 16
            )
            print(a)
            data = data[b//8:]
