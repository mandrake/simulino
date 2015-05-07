from atmega328p.atmega328p import ATMEGA328P

ino = ATMEGA328P()
ino.execute(0x0FFF)
ino.execute(0x96FF)
ino.execute(0x23FF)
