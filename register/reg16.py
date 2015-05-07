from .register import Register, Endianness, Complement, BitFirst
from util.base_converter import BaseConverter


class Reg16(Register):

    def __init__(self, value=0, endianness=Endianness.LE, bitfirst=BitFirst.MSBF,
                 complement=Complement.COMP2):
        self.__value = value
        self.__endianness = endianness
        self.__bitfirst = bitfirst
        self.__carry = False
        self.__complement = complement

    def _reset(self, bit):
        if bit < 0 or bit > 15:
            raise Exception("NOPE.WAV")
        if self.__bitfirst == Register.BitFirst.MSBF:
            self._and(self.max_value - (2**bit))
        else:
            self._and(self.max_value - (2**(15-bit)))

    def _set(self, bit):
        if bit < 0 or bit > 15:
            raise Exception("NOPE.WAV")

        if self.__bitfirst == Register.BitFirst.MSBF:
            self._or(2**bit)
        else:
            self._or(2**(15-bit))

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
            temp %= self.max_value + 1
        self.__value = temp

    def _sub(self, value):
        # TODO: recheck thoroughly all this code.
        # TODO: check for underflow for too large values.
        temp = self.__value - value
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
        return (2**16)-1

    @property
    def bin(self):
        v = self.value_base(2)
        return '0' * (16 - len(v)) + v

    @property
    def hex(self):
        v = self.value_base(16)
        return '0' * (4 - len(v)) + v

    @property
    def bin_raw(self):
        v = self.bin
        if self.__endianness == Endianness.BE:
            return v
        elif self.__endianness == Endianness.LE:
            return v[8:16] + v[0:8]

    @property
    def hex_raw(self):
        v = self.hex
        if self.__endianness == Endianness.BE:
            return v
        elif self.__endianness == Endianness.LE:
            return v[2:4] + v[0:2]

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
