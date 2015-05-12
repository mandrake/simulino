from .status import Status
from .ioregisters import IORegisters
from .memory import Memory


class DataMemorySpace:

    def __init__(self, status: Status, iodata: IORegisters, xiomem: Memory, datamem: Memory):
        self.__status = status
        self.__iodata = iodata
        self.__xiodata = xiomem
        self.__memory = datamem

    def __getitem__(self, item):
        if item in range(0x0000, 0x0020):
            return self.__status[item].unsigned_value
        elif item in range(0x0020, 0x0060):
            return self.__iodata[item-0x0020].unsigned_value
        elif item in range(0x0060, 0x0100):
            return self.__xiodata[item-0x0060]
        else:
            return self.__memory[item-0x100]

    def __setitem__(self, key, value):
        if key in range(0x0000, 0x0020):
            self.__status[key]._value = value
        elif key in range(0x0020, 0x0060):
            self.__iodata[key-0x0020]._value = value
        elif key in range(0x0060, 0x0100):
            self.__xiodata[key-0x0060] = value
        else:
            self.__memory[key-0x0100] = value