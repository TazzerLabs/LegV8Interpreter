from state import registers, flags

rM = 0
rN = 0
rD = 0
iM = 0

#Takes a uint and returns a int64. If the original value would
#require more than 64 bits, MSBs will be dropped until result
#is within range
def s64(value):
    return -(value & 0x8000000000000000) | (value & 0x7fffffffffffffff)

def add(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = registers[rN].int + registers[rM].int

def addi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int + iM

def adds(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = s64(registers[rN].int + registers[rM].int)
    #show stored result as int and hex
    print(registers[rD].int, ' ', registers[rD])
    if not registers[rD].int:
        flags[0] = 1
    if registers[rD].int < 0:
        flags[1] = 1
    if (registers[rD].int < registers[rN].int + registers[rM].int):
        flags[2] = 1
        flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    print(flags)


def addis(args):
    return

def aand(args):
    return

def andi(args):
    return

def ands(args):
    return

def andis(args):
    return

def b(args):
    return

def bcond(args):
    return

def bl(args):
    return

def br(args):
    return

def cbz(args):
    return

def cbnz(args):
    return

def eor(args):
    return

def eori(args):
    return

def ldur(args):
    return

def ldurb(args):
    return

def ldurh(args):
    return

def ldursw(args):
    return

def ldxr(args):
    return

def lsl(args):
    return

def lsr(args):
    return

def orr(args):
    return

def orri(args):
    return

def sub(args):
    return

def subi(args):
    return

def subs(args):
    return

def subis(args):
    return

def stur(args):
    return

def sturb(args):
    return

def sturh(args):
    return

def sturw(args):
    return

def stxr(args):
    return
