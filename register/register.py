from enum import Enum


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
    def bin(self):
        """
        Binary actual value of the register.

        :return: binary string representing the value of the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def bin_raw(self):
        """
        Binary value of the register as stored in memory (lowest address first).

        :return: binary string representing the value of the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def hex(self):
        """
        Hexadecimal actual value of the register.

        :return: hexadecimal string representing the value of the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def hex_raw(self):
        """
        Hexadecimal value of the register as stored in memory (lowest address first).

        :return: hexadecimal string representing the value of the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def signed_value(self):
        """
        Signed value of the register.

        :return: signed value of the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    @property
    def unsigned_value(self):
        """
        Unsigned value of the register.

        :return: unsigned value of the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def value_base(self, base):
        """
        Value in custom base of the register.

        :param base: the base of the representation wanted.
        :return: string representing the value of the register in the given base.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def set(self, bit):
        """
        Sets the i-th bit of the register.

        :param bit: The bit to be set
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def isset(self, bit):
        """
        Tells if the i-th bit of the register is set

        :param bit: The bit to check
        :return: True if the bit-th bit is set, False otherwise.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def reset(self, bit):
        """
        Clears the i-th bit of the register.

        :param bit The bit to be reset
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def clear(self, bit):
        """
        Clears the i-th bit of the register (a shortend for reset).

        :param bit The bit to be reset
        """
        self.reset(bit)

    def land(self, mask):
        """
        Applies a mask with bitwise and to the register.

        :param mask The mask to be applied.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def lor(self, mask):
        """
        Applies a mask with bitwise or to the register.

        :param mask The mask to be applied
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def lxor(self, mask):
        """
        Applies a mask with bitwise xor to the register.

        :param mask The mask to be applied
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def add(self, value):
        """
        Adds a value to the register.

        :param value The value to be added.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def inc(self):
        """
        Adds 1 to the register (a shorthand for add(1)).
        """
        self.add(1)

    def sub(self, value):
        """
        Subtracts a value from the register.

        :param value: The value to be subtracted.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")

    def dec(self):
        """
        Subtracts 1 to the register (a shorthand for sub(1)).
        """
        self.sub(1)

    @property
    def max_value(self):
        """
        Returns the maximum unsigned value for the register.
        :return: Max unsigned value for the register.
        """
        raise NotImplementedError("Look somewhere else, dumbo.")
