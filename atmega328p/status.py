# -*- coding: utf-8 -*-
from register.reg8 import Reg8
from register.reg16 import Reg16


class StatusReg(Reg8):
    CARRY_MASK = 0x01
    ZERO_MASK = 0x02
    NEG_MASK = 0x04
    OFLOW_MASK = 0x08
    SFLAG_MASK = 0x10
    HALFC_MASK = 0x20
    TRANS_MASK = 0x40
    INTER_MASK = 0x80

    @property
    def c(self):
        """
        :return: Carry Flag
        """
        return bool(self._value & self.CARRY_MASK)

    @property
    def z(self):
        """
        :return: Zero Flag
        """
        return bool(self._value & self.ZERO_MASK)

    @property
    def n(self):
        """
        :return: Negative Flag
        """
        return bool(self._value & self.NEG_MASK)

    @property
    def v(self):
        """
        :return: Two’s complement overflow indicator
        """
        return bool(self._value & self.OFLOW_MASK)

    @property
    def s(self):
        """
        :return: N ⊕ V, For signed tests
        """
        return bool(self._value & self.SFLAG_MASK)

    @property
    def h(self):
        """
        :return: Half Carry Flag
        """
        return bool(self._value & self.HALFC_MASK)

    @property
    def t(self):
        """
        :return: Transfer bit used by BLD and BST instructions
        """
        return bool(self._value & self.TRANS_MASK)

    @property
    def i(self):
        """
        :return: Global Interrupt Enable/Disable Flag
        """
        return bool(self._value & self.INTER_MASK)

    @c.setter
    def c(self, value):
        if value:
            self._value |= self.CARRY_MASK
        else:
            self._value &= self.max_value - self.CARRY_MASK

    @z.setter
    def z(self, value):
        if value:
            self._value |= self.ZERO_MASK
        else:
            self._value &= self.max_value - self.ZERO_MASK

    @n.setter
    def n(self, value):
        if value:
            self._value |= self.NEG_MASK
        else:
            self._value &= self.max_value - self.NEG_MASK

    @v.setter
    def v(self, value):
        if value:
            self._value |= self.OFLOW_MASK
        else:
            self._value &= self.max_value - self.OFLOW_MASK

    @s.setter
    def s(self, value):
        if value:
            self._value |= self.SFLAG_MASK
        else:
            self._value &= self.max_value - self.SFLAG_MASK

    @h.setter
    def h(self, value):
        if value:
            self._value |= self.HALFC_MASK
        else:
            self._value &= self.max_value - self.HALFC_MASK

    @t.setter
    def t(self, value):
        if value:
            self._value |= self.TRANS_MASK
        else:
            self._value &= self.max_value - self.TRANS_MASK

    @i.setter
    def i(self, value):
        if value:
            self._value |= self.INTER_MASK
        else:
            self._value &= self.max_value - self.INTER_MASK

    def set_c(self):
        self.c = True

    def set_z(self):
        self.z = True

    def set_n(self):
        self.n = True

    def set_v(self):
        self.v = True

    def set_s(self):
        self.s = True

    def set_h(self):
        self.h = True

    def set_t(self):
        self.t = True

    def set_i(self):
        self.i = True

    def rst_c(self):
        self.c = False

    def rst_z(self):
        self.z = False

    def rst_n(self):
        self.n = False

    def rst_v(self):
        self.v = False

    def rst_s(self):
        self.s = False

    def rst_h(self):
        self.h = False

    def rst_t(self):
        self.t = False

    def rst_i(self):
        self.i = False


class Status(object):

    def __init__(self):
        # General purpose registers
        self.__reg_0 = Reg8()
        self.__reg_1 = Reg8()
        self.__reg_2 = Reg8()
        self.__reg_3 = Reg8()
        self.__reg_4 = Reg8()
        self.__reg_5 = Reg8()
        self.__reg_6 = Reg8()
        self.__reg_7 = Reg8()
        self.__reg_8 = Reg8()
        self.__reg_9 = Reg8()
        self.__reg_10 = Reg8()
        self.__reg_11 = Reg8()
        self.__reg_12 = Reg8()
        self.__reg_13 = Reg8()
        self.__reg_14 = Reg8()
        self.__reg_15 = Reg8()
        self.__reg_16 = Reg8()
        self.__reg_17 = Reg8()
        self.__reg_18 = Reg8()
        self.__reg_19 = Reg8()
        self.__reg_20 = Reg8()
        self.__reg_21 = Reg8()
        self.__reg_22 = Reg8()
        self.__reg_23 = Reg8()
        self.__reg_24 = Reg8()
        self.__reg_25 = Reg8()
        self.__reg_26 = Reg8()
        self.__reg_27 = Reg8()
        self.__reg_28 = Reg8()
        self.__reg_29 = Reg8()
        self.__reg_30 = Reg8()
        self.__reg_31 = Reg8()

        # TODO: implement those two registers in terms of 26-27, 28-29 and 30-31
        self.__reg_X = Reg16()
        self.__reg_Y = Reg16()
        self.__reg_Z = Reg16()

        self.__status_reg = StatusReg()

        # Actually, it's a 14 bit register. But for now I'll leave it this way.
        self.__program_counter = Reg16()

    @property
    def r0(self):
        return self.__reg_0

    @property
    def r1(self):
        return self.__reg_1

    @property
    def r2(self):
        return self.__reg_2

    @property
    def r3(self):
        return self.__reg_3

    @property
    def r4(self):
        return self.__reg_4

    @property
    def r5(self):
        return self.__reg_5

    @property
    def r6(self):
        return self.__reg_6

    @property
    def r7(self):
        return self.__reg_7

    @property
    def r8(self):
        return self.__reg_8

    @property
    def r9(self):
        return self.__reg_9
    
    @property
    def r10(self):
        return self.__reg_10

    @property
    def r11(self):
        return self.__reg_11

    @property
    def r12(self):
        return self.__reg_12

    @property
    def r13(self):
        return self.__reg_13

    @property
    def r14(self):
        return self.__reg_14

    @property
    def r15(self):
        return self.__reg_15

    @property
    def r16(self):
        return self.__reg_16

    @property
    def r17(self):
        return self.__reg_17

    @property
    def r18(self):
        return self.__reg_18

    @property
    def r19(self):
        return self.__reg_19
    
    @property
    def r20(self):
        return self.__reg_20

    @property
    def r21(self):
        return self.__reg_21

    @property
    def r22(self):
        return self.__reg_22

    @property
    def r23(self):
        return self.__reg_23

    @property
    def r24(self):
        return self.__reg_24

    @property
    def r25(self):
        return self.__reg_25

    @property
    def r26(self):
        return self.__reg_26

    @property
    def r27(self):
        return self.__reg_27

    @property
    def r28(self):
        return self.__reg_28

    @property
    def r29(self):
        return self.__reg_29

    @property
    def r30(self):
        return self.__reg_30

    @property
    def r31(self):
        return self.__reg_31

    @property
    def xl(self):
        return self.r26

    @property
    def xh(self):
        return self.r27

    @property
    def yl(self):
        return self.r28

    @property
    def yh(self):
        return self.r29

    @property
    def zl(self):
        return self.r30

    @property
    def zh(self):
        return self.r31

    @property
    def x(self):
        return self.__reg_X

    @property
    def y(self):
        return self.__reg_Y

    @property
    def z(self):
        return self.__reg_Z

    @property
    def sreg(self):
        return self.__status_reg

    @property
    def pc(self):
        return self.__program_counter