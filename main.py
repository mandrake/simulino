from atmega328p.tests.execution_test import test_overflow, test_and, test_asr, test_sreg
from atmega328p.atmega328p import ATMEGA328P

if __name__ == '__main__':
    """test_overflow()
    test_and()
    test_asr()
    test_sreg()"""

    ino = ATMEGA328P()
    program = open('./Blink.cpp.bin', 'rb').read()
    ino.load_program([program[2*i + 1] * 256 + program[2*i] for i in range(0, len(program)//2)])
    for i in range(0, 100):
        ino.execute()