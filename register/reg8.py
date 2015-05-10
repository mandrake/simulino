from .register import Register, Endianness, Complement, BitFirst
from util.base_converter import BaseConverter


class Reg8(Register):

    def __init__(self, value=0, endianness=Endianness.LE, bitfirst=BitFirst.MSBF,
                 complement=Complement.COMP2):
        self._value = value
        self.__endianness = endianness
        self.__bitfirst = bitfirst
        self.__complement = complement

    def reset(self, bit):
        if bit < 0 or bit > 7:
            raise Exception("NOPE.WAV")
        if self.__bitfirst == Register.BitFirst.MSBF:
            self.land(self.max_value - (2**bit))
        else:
            self.land(self.max_value - (2**(7-bit)))

    def set(self, bit):
        if bit < 0 or bit > 7:
            raise Exception("NOPE.WAV")

        if self.__bitfirst == Register.BitFirst.MSBF:
            self.lor(2**bit)
        else:
            self.lor(2**(7-bit))

    def land(self, mask):
        if mask < 0 or mask > self.max_value:
            raise Exception("NOPE.WAV")

        self._value &= mask

    def lor(self, mask):
        if mask < 0 or mask > self.max_value:
            raise Exception("NOPE.WAV")

        self._value |= mask

    def lxor(self, mask):
        if mask < 0 or mask > self.max_value:
            raise Exception("NOPE.WAV")

        self._value ^= mask

    def add(self, value):
        temp = self._value + value
        if temp > self.max_value:
            temp %= self.max_value + 1
        self._value = temp

    def sub(self, value):
        # TODO: recheck thoroughly all this code.
        # TODO: check for underflow for too large values.
        temp = self._value - value
        if temp < 0:
            if self.__complement == Complement.COMP1:
                self._value = self.max_value + temp
            elif self.__complement == Complement.COMP2:
                self._value = self.max_value + temp + 1

    @property
    def max_value(self):
        return (2**8)-1

    @property
    def bin(self):
        v = self.value_base(2)
        return '0' * (8 - len(v)) + v

    @property
    def hex(self):
        v = self.value_base(16)
        return '0' * (2 - len(v)) + v

    @property
    def bin_raw(self):
        return self.bin

    @property
    def hex_raw(self):
        return self.hex

    @property
    def unsigned_value(self):
        return self._value

    @property
    def signed_value(self):
        # TODO: recheck thoroughly all this code.
        if self._value > (self.max_value - 1) / 2:
            if self.__complement == Complement.COMP1:
                return -(self.max_value - self._value)
            elif self.__complement == Complement.COMP2:
                return -((self.max_value - self._value) + 1)
        else:
            return self._value

    def value_base(self, base):
        return BaseConverter.convert_value(self._value, base)
