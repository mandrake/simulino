from atmega328p.atmega328p import ATMEGA328P

ino = ATMEGA328P()
print(ino.execute(0x0FFF)[0])
print(ino.execute(0x96FF)[0])
print(ino.execute(0x23FF)[0])