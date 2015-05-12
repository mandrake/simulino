import re


class Opcoder:

    def __init__(self, opcodes):
        self.__opcodes = opcodes

    def lookup(self, code, bits):
        scode = bin(code)[2:]
        if len(scode) < bits:
            scode = '0' * (bits - len(scode)) + scode

        size = bits
        for regex in self.__opcodes:
            res = re.match(regex, scode)
            if res is not None:
                # {'repr': '...', 'abstract': '...'}
                oc = self.__opcodes[regex]
                ops = [int(x, 2) for x in res.groups()]
                return oc, ops, size

        return None, None, None