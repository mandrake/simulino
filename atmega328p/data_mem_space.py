from .status import Status
from .ioregisters import IORegisters
from .memory import Memory


class DataMemorySpace:

    def __init__(self, status: Status, iodata: IORegisters, xiomem: Memory, datamem: Memory):
        self.__status = status
        self.__iodata = iodata
        self.__xiodata = xiomem
        self.__memory = datamem
        self.__reg_mapping = {
            # Register mapping
            0x00: self.__status.r0, 0x01: self.__status.r1, 0x02: self.__status.r2, 0x03: self.__status.r3,
            0x04: self.__status.r4, 0x05: self.__status.r5, 0x06: self.__status.r6, 0x07: self.__status.r7,
            0x08: self.__status.r8, 0x09: self.__status.r9, 0x0A: self.__status.r10, 0x0B: self.__status.r11,
            0x0C: self.__status.r12, 0x0D: self.__status.r13, 0x0E: self.__status.r14, 0x0F: self.__status.r15,
            0x10: self.__status.r16, 0x11: self.__status.r17, 0x12: self.__status.r18, 0x13: self.__status.r19,
            0x14: self.__status.r20, 0x15: self.__status.r21, 0x16: self.__status.r22, 0x17: self.__status.r23,
            0x18: self.__status.r24, 0x19: self.__status.r25, 0x1A: self.__status.r26, 0x1B: self.__status.r27,
            0x1C: self.__status.r28, 0x1D: self.__status.r29, 0x1E: self.__status.r30, 0x1F: self.__status.r31
        }
        self.__ioreg_mapping = {
            0x1E: self.__iodata.gpior0, 0x1F: self.__iodata.eecr,
            0x20: self.__iodata.eedr, 0x21: self.__iodata.eearl, 0x22: self.__iodata.eearh,
            0x2A: self.__iodata.gpior1, 0x2B: self.__iodata.gpior2,
            0x3D: self.__iodata.spl, 0x3E: self.__iodata.sph
        }

    def __getitem__(self, item):
        if item in range(0x0000, 0x0020):
            return self.__reg_mapping[item].unsigned_value
        elif item in range(0x0020, 0x0060):
            return self.__ioreg_mapping[item-0x0020].unsigned_value
        elif item in range(0x0060, 0x0100):
            return self.__xiodata[item-0x0060]
        else:
            return self.__memory[item-0x100]

    def __setitem__(self, key, value):
        if key in range(0x0000, 0x0020):
            self.__reg_mapping[key]._value = value
        elif key in range(0x0020, 0x0060):
            self.__ioreg_mapping[key-0x0020]._value = value
        elif key in range(0x0060, 0x0100):
            self.__xiodata[key-0x0060] = value
        else:
            self.__memory[key-0x0100] = value