from register.reg8 import Reg8
from register.reg16 import Reg16


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