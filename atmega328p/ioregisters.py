from builtins import property
from register.proxyregister import ProxyRegister16
from register.reg16 import Reg16
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

        # TODO: implement __stack_pointer as a proxyregister
        # self.__stack_pointer = ProxyRegister16(self.__stack_pointer_low, self.__stack_pointer_high)
        self.__stack_pointer = Reg16()
        self.__eeprom_address = ProxyRegister16(self.__eeprom_address_low, self.__eeprom_address_high)

        self.__mapping = {
            0x1E: self.gpior0, 0x1F: self.eecr,
            0x20: self.eedr, 0x21: self.eearl, 0x22: self.eearh,
            0x2A: self.gpior1, 0x2B: self.gpior2,
            0x3D: self.spl, 0x3E: self.sph
        }

    def __getitem__(self, item):
        if item in self.__mapping:
            return self.__mapping[item]
        else:
            return Reg8()

    def __setitem__(self, key, value):
        if key in self.__mapping:
            self.__mapping[key]._value = value
        else:
            print("TODO: register " + str(key) + " not available yet.")

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
