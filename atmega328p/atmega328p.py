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
        getattr(self, '_ATMEGA328P__' + ab[0])(ab[1:])

    def __ADD(self, ops, carry=False):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rd = rdst.unsigned_value
        rs = rsrc.unsigned_value
        rdst._add(rsrc.unsigned_value + (1 if carry and self.status.sreg.c else 0))
        rr = rdst.unsigned_value

        # c = ((rd & rs & 0x80) != 0) or ((rs & ~rr & 0x80) != 0) or ((rd & ~rr & 0x80) != 0)
        # h = ((rd & rs & 0x08) != 0) or ((rs & ~rr & 0x08) != 0) or ((rd & ~rr & 0x80) != 0)
        # v = ((rd & rs & ~rr & 0x80) != 0) or ((~rd & ~rs & rr & 0x80) != 0)
        # n = (rr & 0x80) != 0
        # z = (rr == 0)
        # s = n ^ v

        c = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)
        h = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x08)
        v = bool(((rd & rs & ~rr) | (~rd & ~rs & rr)) & 0x80)
        n = bool(rr & 0x80)
        z = bool(rr)
        s = n ^ v

        for flag in ['h', 's', 'v', 'n', 'z', 'c']:
            callback = getattr(self.status.sreg, 'set_' + flag)
            callback() if vars()[flag] else None

    def __ADC(self, ops):
        self.__ADD(ops, carry=True)

    def __ADIW(self, ops):
        dst = int(ops[0])
        immw = int(ops[1])
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
        c = bool(((rd & rs) | (rs & ~rr) | (rd & ~rr)) & 0x80)
        v = bool((~rd & rr & 0x80) != 0)
        n = bool(rr & 0x80)
        z = bool(rr + rdstl.unsigned_value)

        for flag in ['s', 'v', 'n', 'z', 'c']:
            callback = getattr(self.status.sreg, 'set_' + flag)
            callback() if vars()[flag] else None

    def __AND(self, ops):
        print(ops)

    def sbroscia(self, file):
        data = file.read()
        while data:
            a, b = self.__opcodes.lookup(
                sum([x * y for (x, y) in zip(data[0:4], [2**24, 2**16, 2**8, 1])]), 16
            )
            print(a)
            data = data[b//8:]