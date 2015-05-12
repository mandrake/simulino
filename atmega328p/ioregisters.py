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

        self.__mapping = {
            0x1E: self.__iodata.gpior0, 0x1F: self.__iodata.eecr,
            0x20: self.__iodata.eedr, 0x21: self.__iodata.eearl, 0x22: self.__iodata.eearh,
            0x2A: self.__iodata.gpior1, 0x2B: self.__iodata.gpior2,
            0x3D: self.__iodata.spl, 0x3E: self.__iodata.sph
        }

    def __getitem__(self, item):
        return self.__mapping[item]

    def __setitem__(self, key, value):
        self.__mapping[key]._value = value

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
