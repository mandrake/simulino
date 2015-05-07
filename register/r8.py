from .register import Register, Endianness, Complement
from util.base_converter import BaseConverter


class R8(Register):

    def __init__(self, value=0, endianness=Endianness.BE, bitfirst=Register.BitFirst.MSBF,
                 complement=Complement.COMP2):
        self.__value = value
        self.__endianness = endianness
        self.__bitfirst = bitfirst
        self.__carry = False
        self.__complement = complement

    def _reset(self, bit):
        if bit < 0 or bit > 7:
            raise Exception("NOPE.WAV")
        if self.__bitfirst == Register.BitFirst.MSBF:
            self._and(self.max_value - (2**bit))
        else:
            self._and(self.max_value - (2**(7-bit)))

    def _set(self, bit):
        if bit < 0 or bit > 7:
            raise Exception("NOPE.WAV")

        if self.__bitfirst == Register.BitFirst.MSBF:
            self._or(2**bit)
        else:
            self._or(2**(7-bit))

    def _and(self, mask):
        if mask < 0 or mask > self.max_value:
            raise Exception("NOPE.WAV")

        self.__value &= mask

    def _or(self, mask):
        if mask < 0 or mask > self.max_value:
            raise Exception("NOPE.WAV")

        self.__value |= mask

    def _xor(self, mask):
        if mask < 0 or mask > self.max_value:
            raise Exception("NOPE.WAV")

        self.__value ^= mask

    def _add(self, value):
        temp = self.__value + value
        if temp > self.max_value:
            self.__carry = True
        self.__value = temp % self.max_value

    def _sub(self, value):
        # TODO: recheck thoroughly all this code.
        temp = self.__value - value
        temp %= self.max_value + 1
        if temp < 0:
            self.__carry = True
            if self.__complement == Complement.COMP1:
                self.__value = self.max_value + temp
            elif self.__complement == Complement.COMP2:
                self.__value = self.max_value + temp + 1

    def _carry(self):
        return self.__carry

    @property
    def max_value(self):
        return (2**8)-1

    @property
    def bin(self):
        self.value_base(2)

    @property
    def hex(self):
        self.value_base(16)

    @property
    def bin_raw(self):
        return self.bin

    @property
    def hex_raw(self):
        return self.hex

    @property
    def unsigned_value(self):
        return self.__value

    @property
    def signed_value(self):
        # TODO: recheck thoroughly all this code.
        if self.__value > (self.max_value - 1) / 2:
            if self.__complement == Complement.COMP1:
                return -(self.max_value - self.__value)
            elif self.__complement == Complement.COMP2:
                return -((self.max_value - self.__value) + 1)
        else:
            return self.__value

    def value_base(self, base):
        return BaseConverter.convert_value(self.__value, base)