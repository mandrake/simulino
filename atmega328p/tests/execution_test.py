from atmega328p.atmega328p import ATMEGA328P


def demo_overflow():
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
    print('carry:', ino.status.sreg.c)
    ino.execute(0x0FFF)  # ADD R31, R31 -> (20, 64)
    print('r30:', ino.status.r30.unsigned_value, 'r31:', ino.status.r31.unsigned_value)
    print('carry:', ino.status.sreg.c)