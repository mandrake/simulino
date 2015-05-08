from .status import Status
from opcoder.opcoder import Opcoder
from .opcodes import opcodes


class ATMEGA328P:

    def __init__(self):
        self.__status = Status()
        self.__opcodes = Opcoder(opcodes)

    def execute(self, opcode):
        return self.__opcodes.lookup(opcode, 16)

    def sbroscia(self, file):
        data = file.read()
        while data:
            a, b = self.execute(
                sum([x * y for (x, y) in zip(data[0:4], [2**24, 2**16, 2**8, 1])])
            )
            print(a)
            data = data[b//8:]