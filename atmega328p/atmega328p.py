from .status import Status


class ATMEGA328P:

    def __init__(self):
        self.__status = Status()

    def execute(self, opcode):
        raise Exception("bona ugo")