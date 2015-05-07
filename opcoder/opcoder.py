import re


class Opcoder:

    """
    def __init__(self, opcode_list):
        self.__lookup_dict = {}

        for (desc, name) in opcode_list:
            tmpdesc = desc
            lkpd = self.__lookup_dict
            ops = []
            while tmpdesc != '':
                if tmpdesc[0] in '01':
                    if tmpdesc[0] not in lkpd:
                        lkpd[tmpdesc[0]] = {}
                    lkpd = lkpd[tmpdesc[0]]
                    tmpdesc = tmpdesc[1:]
                else:
                    letter = tmpdesc[0]
                    counter = 0
                    while tmpdesc != '' and tmpdesc[0] == letter:
                        counter += 1
                        tmpdesc = tmpdesc[1:]
                    ops.append(counter)
            lkpd['$'] = (name, ops)

    def lookup(self, code, bits):
        mask = 2**(bits-1)
        entry = self.__lookup_dict

        while '$' not in entry and mask != 0:
            #print(mask, code, entry, mask & code)
            bit = '1' if (mask & code) != 0 else '0'
            try:
                entry = entry[bit]
            except KeyError:
                raise Exception("Error in lookup, invalid opcode")
            mask //= 2

        if '$' not in entry:
            raise Exception("Error in lookup, invalid opcode")

        name, ops = entry['$']
        opvals = []

        for op in ops:
            v = 0
            while op != 0:
                v *= 2
                v += 1 if (mask & code) != 0 else 0
                op -= 1
                mask //= 2
            opvals.append(v)

        return name, opvals
    """

    def __init__(self, opcodes):
        self.__opcodes = opcodes

    def lookup(self, code, bits):
        scode = bin(code)[2:]
        scode = '0' * (bits - len(scode)) + scode

        for regex in self.__opcodes:
            res = re.match(regex, scode)
            if res is not None:
                return self.__opcodes[regex]['repr']([int(x, 2) for x in res.groups()])