# -*- coding: utf-8 -*-
from register.proxyregister import ProxyRegister16
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


class Status:

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

        self.__reg_X = ProxyRegister16(self.__reg_26, self.__reg_27)
        self.__reg_Y = ProxyRegister16(self.__reg_28, self.__reg_29)
        self.__reg_Z = ProxyRegister16(self.__reg_30, self.__reg_31)

        self.__status_reg = StatusReg()

        # Actually, it's a 14 bit register. But for now I'll leave it this way.
        self.__program_counter = Reg16()

        self.__mapping = {
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

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__mapping[item]
        elif isinstance(item, str):
            # Assumed in the form Rxx
            return self.__mapping[int(item[1:])]
        else:
            raise IndexError("Wrong index")

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