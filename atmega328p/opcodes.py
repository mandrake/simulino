opcodes = {
    '000111([01])([01]{5})([01]{4})': {
        # ADC dest, src
        'repr': lambda x: 'ADC R%d, R%d' % (x[1], x[0] * 16 + x[2]),
        'abstract': lambda x: ('ADC', 'R%d' % x[1], 'R%d' % (x[0] * 16 + x[2]))
    },
    '000011([01])([01]{5})([01]{4})': {
        # ADD dest, src
        'repr': lambda x: 'ADD R%d, R%d' % (x[1], x[0] * 16 + x[2]),
        'abstract': lambda x: ('ADD', 'R%d' % x[1], 'R%d' % (x[0] * 16 + x[2]))
    },
    '10010110([01]{2})([01]{2})([01]{4})': {
        'repr': lambda x: 'ADIW R%d:R%d, R%d' % (
            [25, 27, 29, 31][x[1]],
            [24, 26, 28, 30][x[1]],
            x[0] * 16 + x[2]
        ),
        'abstract': lambda x: ('ADIW', x[1], x[0] * 16 + x[2])
    },
    '001000([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'AND R%d, R%d' % (x[1], x[0] * 16 + x[2]),
        'abstract': lambda x: ('AND', 'R%d' % x[1], 'R%d' % (x[0] * 16 + x[2]))
    },
    '0111([01]{4})([01]{4})([01]{4})': {
        'repr': lambda x: 'ANDI R%d, %d' % (x[1], x[0] * 16 + x[2]),
        'abstract': lambda x: ('ANDI', 'R%d' % x[1], x[0] * 16 + x[2])
    },
    '1001010([01]{5})0101': {
        'repr': lambda x: 'ASR R%d' % x[0],
    },
    '100101001([01]{3})1000': {
        'repr': lambda x: 'BCLR %d' % x[0]
    },
    '1111100([01]{5})0([01]{3})': {
        'repr': lambda x: 'BLD R%d, %d' % (x[0], x[1])
    },
    # These two opcodes have specialized equivalents
    #'111101([01]{7})([01]{3})': {
    #    # TODO: check the 2's complement here
    #    'repr': lambda x: 'BRBC %d, %d' % (x[1], x[0] if x[0] < 64 else -(128 - x[0]))
    #},
    #'111100([01]{7})([01]{3})': {
    #    # TODO: check the 2's complement here
    #    'repr': lambda x: 'BRBS %d, %d' % (x[1], x[0] if x[0] < 64 else -(128 - x[0]))
    #},

    # Duplicate
    #'111101([01]{7})000': {
    #    # TODO: check the 2's complement here
    #    'repr': lambda x: 'BRCC %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    #},
    '111100([01]{7})000': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRCS %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '1001010110011000': {
        'repr': lambda x: 'BREAK'
    },
    '111100([01]{7})001': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BREQ %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})100': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRGE %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})101': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRHC %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111100([01]{7})101': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRHS %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})111': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRID %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111100([01]{7})111': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRIE %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111100([01]{7})100': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRLT %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111100([01]{7})010': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRMI %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})001': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRNE %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})010': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRPL %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})000': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRSH %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})110': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRTC %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111100([01]{7})110': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRTS %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111101([01]{7})011': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRVC %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '111100([01]{7})011': {
        # TODO: check the 2's complement here
        'repr': lambda x: 'BRVS %d' % (x[0] if x[0] < 64 else -(128 - x[0]))
    },
    '100101000([01]{3})1000': {
        'repr': lambda x: 'BSET %d' % x[0]
    },
    '1111101([01]{5})0([01]{3})': {
        'repr': lambda x: 'BST R%d, %d' % (x[0], x[1])
    },
    '1001010([01]{5})111([01])': {
        'repr': lambda x: 'CALL %d' % (x[0] * 2 + x[1])
    },
    '10011000([01]{5})([01]{3})': {
        'repr': lambda x: 'CBI %d, %d' % (x[0], x[1])
    },
    '1001010010001000': {
        'repr': lambda x: 'CLC'
    },
    '1001010011011000': {
        'repr': lambda x: 'CLH'
    },
    '1001010011111000': {
        'repr': lambda x: 'CLI'
    },
    '1001010010101000': {
        'repr': lambda x: 'CLN'
    },
    '1001010011001000': {
        'repr': lambda x: 'CLS'
    },
    '1001010011101000': {
        'repr': lambda x: 'CLT'
    },
    '1001010010111000': {
        'repr': lambda x: 'CLV'
    },
    '1001010010011000': {
        'repr': lambda x: 'CLZ'
    },
    '1001010([01]{5})0000': {
        'repr': lambda x: 'COM %d' % x[0]
    },
    '000101([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'CP R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '000001([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'CPC R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '0011([01]{4})([01]{4})([01]{4})': {
        'repr': lambda x: 'CPI R%d, %d' % (x[1], x[0] * 16 + x[2])
    },
    '000100([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'CPSE R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '1001010([01]{5})1010': {
        'repr': lambda x: 'DEC R%d' % x[0]
    },
    '10010100([01]{4})1011': {
        'repr': lambda x: 'DES %d' % x[0]
    },
    '1001010100011001': {
        'repr': lambda x: 'EICALL'
    },
    '1001010000011001': {
        'repr': lambda x: 'EIJMP'
    },
    '1001010111011000': {
        'repr': lambda x: 'ELPM'
    },
    '1001000([01]{5})0110': {
        'repr': lambda x: 'ELPM R%d, Z' % x[0]
    },
    '1001000([01]{5})0111': {
        'repr': lambda x: 'ELPM R%d, Z+' % x[0]
    },
    '001001([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'EOR R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '000000110([01]{3})1([01]{3})': {
        'repr': lambda x: 'FMUL R%d, R%d' % (x[0] + 16, x[1] + 16)
    },
    '000000111([01]{3})0([01]{3})': {
        'repr': lambda x: 'FMULS R%d, R%d' % (x[0] + 16, x[1] + 16)
    },
    '000000111([01]{3})1([01]{3})': {
        'repr': lambda x: 'FMULSU R%d, R%d' % (x[0] + 16, x[1] + 16)
    },
    '1001010100001001': {
        'repr': lambda x: 'ICALL'
    },
    '1001010000001001': {
        'repr': lambda x: 'IJMP'
    },
    '10110([01]{2})([01]{5})([01]{3})': {
        'repr': lambda x: 'IN R%d, %d' % (x[1], x[0] * 16 + x[2])
    },
    '1001010([01]{5})0011': {
        'repr': lambda x: 'INC R%d' % x[0]
    },
    '1001010([01]{5})110([01])': {
        'repr': lambda x: 'JMP %d' % (x[10] * 2**17 + x[1] * 2**16 + x[2]),
        'extra': 2
    },
    '1001001([01]{5})0110': {
        'repr': lambda x: 'LAC R%d' % x[0]
    },
    '1001001([01]{5})0101': {
        'repr': lambda x: 'LAS R%d' % x[0]
    },
    '1001001([01]{5})0111': {
        'repr': lambda x: 'LAT R%d' % x[0]
    },
    '1001000([01]{5})1100': {
        'repr': lambda x: 'LD R%d, X' % x[0]
    },
    '1001000([01]{5})1101': {
        'repr': lambda x: 'LD R%d, X+' % x[0]
    },
    '1001000([01]{5})1110': {
        'repr': lambda x: 'LD R%d, -X' % x[0]
    },
    '1000000([01]{5})1000': {
        'repr': lambda x: 'LD R%d, Y' % x[0]
    },
    '1001000([01]{5})1001': {
        'repr': lambda x: 'LD R%d, Y+' % x[0]
    },
    '1001000([01]{5})1010': {
        'repr': lambda x: 'LD R%d, -Y' % x[0]
    },
    '10([01])0([01]{2})0([01]{5})1([01]{3})': {
        'repr': lambda x: 'LDD R%d, Y+%d' % (x[2], x[0] * 2**5 + x[1] * 2**3 + x[3])
    },
    '1110([01]{4})([01]{4})([01]{4})': {
        'repr': lambda x: 'LDI R%d, %d' % (x[1], x[0] * 2**4 + x[2])
    },
    '1001000([01]{5})0000': {
        'repr': lambda x: 'LDS R%d, %d' % (x[0], x[1]),
        'extra': 2
    },
    '10100([01]{3})([01]{4})([01]{4})': {
        'repr': lambda x: 'LDS R%d, %d' % (x[1], x[0] * 2**4 + x[2])
    },
    '1001010111001000': {
        'repr': lambda x: 'LPM'
    },
    '1001000([01]{5})0100': {
        'repr': lambda x: 'LPM R%d, Z' % x[0]
    },
    '1001000([01]{5})0101': {
        'repr': lambda x: 'LPM R%d, Z+' % x[0]
    },
    '1001010([01]{5})0110': {
        'repr': lambda x: 'LSR R%d' % x[0]
    },
    '001011([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'MOV R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '00000001([01]{4})([01]{4})': {
        'repr': lambda x: 'MOVW R%d:R%d, R%d:R%d' % (2*x[0] + 1, 2*x[0], 2*x[1] + 1, 2*x[1])
    },
    '100111([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'MUL R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '00000010([01]{4})([01]{4})': {
        'repr': lambda x: 'MULS R%d, R%d' % (x[0] + 16, x[1] + 16)
    },
    '000000100([01]{3})0([01]{3})': {
        'repr': lambda x: 'MULSU R%d, R%d' % (x[0] + 16, x[1] + 16)
    },
    '1001010([01]{5})0001': {
        'repr': lambda x: 'NEG R%d' % x[0]
    },
    '0000000000000000': {
        'repr': lambda x: 'NOP'
    },
    '001010([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'OR R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '0110([01]{4})([01]{4})([01]{4})': {
        'repr': lambda x: 'ORI R%d, %d' % (x[1] + 16, x[0] * 16 + x[2])
    },
    '10111([01]{2})([01]{5})([01]{4})': {
        'repr': lambda x: 'OUT R%d, %d' % (x[1], x[0] * 16 + x[2])
    },
    '1001000([01]{5})1111': {
        'repr': lambda x: 'POP R%d' % x[0]
    },
    '1001001([01]{5})1111': {
        'repr': lambda x: 'PUSH R%d' % x[0]
    },
    '1101([01]{12})': {
        'repr': lambda x: 'RCALL %d' % x[0]
    },
    '1001010100001000': {
        'repr': lambda x: 'RET'
    },
    '1001010100011000': {
        'repr': lambda x: 'RETI'
    },
    '1100([01]{12})': {
        'repr': lambda x: 'RJMP %d' % x[0]
    },
    '1001010([01]{5})0111': {
        'repr': lambda x: 'ROR R%d' % x[0]
    },
    '000010([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'SBC R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '0100([01]{4})([01]{4})([01]{4})': {
        'repr': lambda x: 'SBCI R%d, %d' % (x[1] + 16, x[0] * 16 + x[2])
    },
    '10011010([01]{5})([01]{3})': {
        'repr': lambda x: 'SBI %d, %d' % (x[0], x[1])
    },
    '10011001([01]{5})([01]{3})': {
        'repr': lambda x: 'SBIC %d, %d' % (x[0], x[1])
    },
    '10011011([01]{5})([01]{3})': {
        'repr': lambda x: 'SBIS %d, %d' % (x[0], x[1])
    },
    '10010111([01]{2})([01]{4})([01]{4})': {
        'repr': lambda x: 'SBIW R%d:R%d, %d' % (
            [25, 27, 29, 31][x[1]],
            [24, 26, 28, 30][x[1]],
            x[0] * 16 + x[2]
        )
    },
    #'0110([01]{4})([01]{4})([01]{4})': {
    #    'repr': lambda x: 'SBR R%d, %d' % (x[1] + 16, x[0] * 16 + x[2])
    #},
    '1111110([01]{5})0([01]{3})': {
        'repr': lambda x: 'SBRC R%d, %d' % (x[0], x[1])
    },
    '1111111([01]{5})0([01]{3})': {
        'repr': lambda x: 'SBRS R%d, %d' % (x[0], x[1])
    },
    '1001010000001000': {
        'repr': lambda x: 'SEC'
    },
    '1001010001011000': {
        'repr': lambda x: 'SEH'
    },
    '1001010001111000': {
        'repr': lambda x: 'SEI'
    },
    '1001010000101000': {
        'repr': lambda x: 'SEN'
    },
    '11101111([01]{4})1111': {
        'repr': lambda x: 'SER R%d' % (x[0] + 16)
    },
    '1001010001001000': {
        'repr': lambda x: 'SES'
    },
    '1001010001101000': {
        'repr': lambda x: 'SET'
    },
    '1001010000111000': {
        'repr': lambda x: 'SEV'
    },
    '1001010000011000': {
        'repr': lambda x: 'SEZ'
    },
    '1001010110001000': {
        'repr': lambda x: 'SLEEP'
    },
    '1001010111101000': {
        'repr': lambda x: 'SPM Z+'
    },
    '1001010111111000': {
        'repr': lambda x: 'SPM Z+'
    },
    '1001001([01]{5})1100': {
        'repr': lambda x: 'ST X, R%d' % x[0]
    },
    '1001001([01]{5})1101': {
        'repr': lambda x: 'ST X+, R%d' % x[0]
    },
    '1001001([01]{5})1110': {
        'repr': lambda x: 'ST -X, R%d' % x[0]
    },
    '1000001([01]{5})1000': {
        'repr': lambda x: 'ST Y, R%d' % x[0]
    },
    '1001001([01]{5})1001': {
        'repr': lambda x: 'ST Y+, R%d' % x[0]
    },
    '1001001([01]{5})1010': {
        'repr': lambda x: 'ST -Y, R%d' % x[0]
    },
    '10([01])0([01]{2})1([01]{5})1([01]{3})': {
        'repr': lambda x: 'ST Y+%d, R%d' % (x[0] * 2**5 + x[1] * 2**3 + x[3], x[2])
    },
    '1000001([01]{5})0000': {
        'repr': lambda x: 'ST X, R%d' % x[0]
    },
    '1000001([01]{5})0001': {
        'repr': lambda x: 'ST Z+, R%d' % x[0]
    },
    '1000001([01]{5})0010': {
        'repr': lambda x: 'ST -Z, R%d' % x[0]
    },
    '10([01])0([01]{2})1([01]{5})0([01]{3})': {
        'repr': lambda x: 'ST Z+%d, R%d' % (x[0] * 2**5 + x[1] * 2**3 + x[3], x[2])
    },
    '1001001([01]{5})0000': {
        'repr': lambda x: 'STS %d, R%d' % (x[1], x[0]),
        'extra': 2
    },
    '10101([01]{3})([01]{4})([01]{4})': {
        'repr': lambda x: 'STS %d, R%d' % (x[0] * 2**4 + x[2], x[1])
    },
    '000110([01])([01]{5})([01]{4})': {
        'repr': lambda x: 'SUB R%d, R%d' % (x[1], x[0] * 16 + x[2])
    },
    '0101([01]{4})([01]{4})([01]{4})': {
        'repr': lambda x: 'SUBI R%d, %d' % (x[0] * 16 + x[2], x[1])
    },
    '1001010([01]{5})0010': {
        'repr': lambda x: 'SWAP R%d' % x[0]
    },
    '1001010110101000': {
        'repr': lambda x: 'WDR'
    },
    '1001001([01]{5})0100': {
        'repr': lambda x: 'XCH Z, R%d' % x[0]
    }
}