from enum import Enum

__author__ = 'Alessandro'


class Endianness(Enum):
    LE = 0
    BE = 1


class BitFirst(Enum):
    MSBF = 0
    LSBF = 1


class Complement(Enum):
    COMP1 = 0
    COMP2 = 1


class Register(object):

    @property
    def value(self):
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def bin(self):
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def hex(self):
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def bin_raw(self):
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def hex_raw(self):
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _set(self, bit):
        """
        Sets the i-th bit of the register.

        :param bit The bit to be set
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _reset(self, bit):
        """
        Clears the i-th bit of the register.

        :param bit The bit to be reset
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _and(self, mask):
        """
        Applies a mask with bitwise and to the register.

        :param mask The mask to be applied.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _or(self, mask):
        """
        Applies a mask with bitwise or to the register.

        :param mask The mask to be applied
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _xor(self, mask):
        """
        Applies a mask with bitwise xor to the register.

        :param mask The mask to be applied
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _add(self, value):
        """
        Adds a value to the register.

        :param value The value to be added.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _sub(self, value):
        """
        Subtracts a value from the register.

        :param value The value to be subtracted.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def _carry(self):
        """
        Returns true if the last operation raised a carry.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def max_value(self):
        """
        Returns the maximum value for the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")


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
        temp = self.__value - value
        if temp < 0:
            self.__carry = True
            if self.__complement == Complement.COMP1:
                self.__value = self.max_value - temp
            elif self.__complement == Complement.COMP2:
                self.__value = self.max_value - temp

    def _carry(self):
        return self.__carry

    @property
    def max_value(self):
        return (2**8)-1

    @property
    def value(self):
        return self.__value


class R16(Register):
    pass


class R32(Register):
    pass


class R64(Register):
    pass