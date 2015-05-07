from .status import Status
from opcoder.opcoder import Opcoder
from .opcodes import opcodes


class ATMEGA328P:

    def __init__(self):
        self.__status = Status()
        self.__opcodes = Opcoder(opcodes)

    def execute(self, opcode):
        print(self.__opcodes.lookup(opcode, 16))