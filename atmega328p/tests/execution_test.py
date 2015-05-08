from atmega328p.atmega328p import ATMEGA328P


def test_overflow():
    ino = ATMEGA328P()
    ino.status.r31._add(10)
    # R30, R31 = (0, 10)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    ino.execute(0x0FEF)  # ADD R30, R31 -> (10, 10)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    ino.execute(0x0FEF)  # ADD R30, R31 -> (20, 10)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    ino.execute(0x0FFF)  # ADD R31, R31 -> (20, 20)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    ino.execute(0x0FFF)  # ADD R31, R31 -> (20, 40)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    ino.execute(0x0FFF)  # ADD R31, R31 -> (20, 80)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    ino.execute(0x0FFF)  # ADD R31, R31 -> (20, 160) = (20, -96)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.signed_value)
    assert ino.status.r31.unsigned_value == 160 and ino.status.r31.signed_value == -96
    print('carry:', ino.status.sreg.c)
    ino.execute(0x0FFF)  # ADD R31, R31 -> (20, 64)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    print('carry:', ino.status.sreg.c)


def test_and():
    ino = ATMEGA328P()
    ino.status.r0._xor(ino.status.r0.unsigned_value)
    ino.status.r0._add(0b00001111)
    ino.status.r1._xor(ino.status.r1.unsigned_value)
    ino.execute(0x2001)  # AND R0, R1
    assert ino.status.r0.unsigned_value == 0b00000000
    ino.status.r0._add(0b00001111)
    ino.status.r1._add(0b00001010)
    ino.execute(0x2001)  # AND R0, R1
    assert ino.status.r0.unsigned_value == 0b00001010
    ino.status.r0._xor(ino.status.r0.unsigned_value)
    ino.status.r0._add(0b11111111)
    ino.execute(0x7E0C)  # ANDI R0, 0xEC
    assert ino.status.r0.unsigned_value == 0xEC


def test_asr():
    ino = ATMEGA328P()
    ino.status.r0._value = 0x80
    ino.execute(0x9405)  # ASR R0
    assert ino.status.r0._value == 0x80 and not ino.status.sreg.c and ino.status.sreg.n
    ino.status.r0._value = 0x85
    ino.execute(0x9405)  # ASR R0
    assert ino.status.r0._value == 0x82 and ino.status.sreg.c and ino.status.sreg.n