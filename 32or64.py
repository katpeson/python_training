#Just trying to figure out if I got 32 or 64 bit
import struct
print struct.calcsize("P") * 8
