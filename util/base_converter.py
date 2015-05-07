import base64


class BaseConverter:

    __up_to_16 = '0123456789ABCDEF'

    @staticmethod
    def convert_value(value, base):
        if base < 0:
            raise Exception("You sure you want a number in base %d? Come on..." % base)
        if base > 16:
            raise Exception("No base %d here. Only bases up to 16 are supported." % base)

        ret = ''
        tmp = value

        while tmp != 0:
            ret = BaseConverter.__up_to_16[tmp % base] + ret
            tmp /= base

        return ret