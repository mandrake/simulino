from .register import Register
from .reg8 import Reg8


class ProxyRegister16(Register):

    def __init__(self, low: Reg8, high: Reg8):
        self.__reg_low = low
        self.__reg_high = high

    def value_base(self, base):
        raise Exception("To be implemented")

    def max_value(self):
        return (2**16) - 1

    def lxor(self, mask):
        lmask, hmask = mask % 256, mask // 256
        self.__reg_low.lxor(lmask)
        self.__reg_high.lxor(hmask)

    def lor(self, mask):
        lmask, hmask = mask % 256, mask // 256
        self.__reg_low.lor(lmask)
        self.__reg_high.lor(hmask)

    def reset(self, bit):
        if bit not in range(0, 16):
            raise IndexError()
        if bit in range(0, 8):
            self.__reg_low.reset(bit)
        else:
            self.__reg_high.reset(bit - 7)

    def isset(self, bit):
        if bit not in range(0, 16):
            raise IndexError()
        if bit in range(0, 8):
            return self.__reg_low.isset(bit)
        else:
            return self.__reg_high.isset(bit - 7)

    def land(self, mask):
        lmask, hmask = mask % 256, mask // 256
        self.__reg_low.land(lmask)
        self.__reg_high.land(hmask)

    def set(self, bit):
        if bit not in range(0, 16):
            raise IndexError()
        if bit in range(0, 8):
            return self.__reg_low.set(bit)
        else:
            return self.__reg_high.set(bit - 7)

    def add(self, value):
        carry = ((value % 256) + self.__reg_low.unsigned_value) > 255
        self.__reg_low.add(value % 256)
        self.__reg_high.add((value // 256) + (1 if carry else 0))

    def sub(self, value):
        # TODO: Didn't really check this. Review.
        carry = (self.__reg_low.unsigned_value - (value % 256)) < 0
        self.__reg_low.sub(value % 256)
        self.__reg_high.sub((value // 256) + (1 if carry else 0))

    @property
    def unsigned_value(self):
        print(self.__reg_high.unsigned_value, self.__reg_low.unsigned_value)
        return self.__reg_low.unsigned_value + (self.__reg_high.unsigned_value * 256)