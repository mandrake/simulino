import re


class Opcoder:

    def __init__(self, opcodes):
        self.__opcodes = opcodes

    def lookup(self, code, bits):
        scode = bin(code)[2:]
        if len(scode) % bits != 0:
            scode = '0' * (bits - (len(scode) % bits)) + scode

        size = bits
        for regex in self.__opcodes:
            res = re.match(regex, scode[0:16])
            if res is not None:
                oc = self.__opcodes[regex]
                ops = [int(x, 2) for x in res.groups()]
                if 'extra' in oc:
                    ops.append(int(scode[16:16+8*oc['extra']]))
                    size += oc['extra']
                return oc['repr'](ops), size
        return '???', 16