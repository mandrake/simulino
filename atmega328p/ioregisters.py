from builtins import property
from register.proxyregister import ProxyRegister16
from register.reg8 import Reg8


class IORegisters:
    def __init__(self):

        self.__stack_pointer_low = Reg8()
        self.__stack_pointer_high = Reg8()
        self.__eeprom_address_low = Reg8()
        self.__eeprom_address_high = Reg8()
        self.__eeprom_data = Reg8()
        self.__eeprom_control = Reg8()
        self.__gpio_r0 = Reg8()
        self.__gpio_r1 = Reg8()
        self.__gpio_r2 = Reg8()

        self.__stack_pointer = ProxyRegister16(self.__stack_pointer_low, self.__stack_pointer_high)
        self.__eeprom_address = ProxyRegister16(self.__eeprom_address_low, self.__eeprom_address_high)

    @property
    def sp(self):
        return self.__stack_pointer

    @property
    def spl(self):
        return self.__stack_pointer_low

    @property
    def sph(self):
        return self.__stack_pointer_high

    @property
    def eear(self):
        return self.__eeprom_address

    @property
    def eearl(self):
        return self.__eeprom_address_low

    @property
    def eearh(self):
        return self.__eeprom_address_high
    
    @property
    def eedr(self):
        return self.__eeprom_data

    @property
    def eecr(self):
        return self.__eeprom_control

    @property
    def gpior0(self):
        return self.__gpio_r0

    @property
    def gpior1(self):
        return self.__gpio_r1

    @property
    def gpior2(self):
        return self.__gpio_r2
