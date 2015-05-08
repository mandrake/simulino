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

    def __ADD(self, ops):
        rdst = getattr(self.status, ops[0].lower())
        rsrc = getattr(self.status, ops[1].lower())
        rdst._add(rsrc.unsigned_value)

    def __ADC(self, ops):
        print(ops)

    def __ADIW(self, ops):
        print(ops)

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