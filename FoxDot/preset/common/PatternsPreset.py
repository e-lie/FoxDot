from FoxDot import P, linvar, sinvar, var, PWhite, Pattern, PTri

dynvars = {}

bar_length = 4

# See theory of rhythm by Malcolm Braff
rhythms = {
"half" : P[1/2],
"swing100" : P[4/10,6/10],
"swing" : P[3/10,7/10],
"triplet" : P[1/3],
"binlet" : P[1/2,1/4,1/4],
"cubalet" : P[4/10,3/10,3/10],
"binlet2" : P[1/4,1/2,1/4],
"gnawa" : P[3/10,4/10,3/10],
"quarter" : P[1/4],
"brazlet" : P[3/10,1/5,1/5,3/10],
"brazlet100" : P[1/3,1/6,1/6,1/3],
"quintuplet" : P[1/5],
"brafflet" : P[3/12,2/12,2/12,2/12,3/12,2/12],
"clave" : P[3/15,3/15,4/15,2/15,3/15]*bar_length,
"clave23" : P[3/16,3/16,4/16,2/16,4/16]*bar_length,
"cascara" : P[2/16,2/16,1/16,2/16,1/16,2/16,1/16,2/16,2/16,1/16]*bar_length,
}

pan_rotations = {
    "rot16" : linvar([0, 5.9], [16, 0]),
    "rotrand1" : sinvar([0, 5.9], [7, 22, 4, 16]),
    "rotrand2" : sinvar([0, 5.9], [17, 13, 7]),
    "drot32" : P[range(32)]/32*6,
}

# panning rotation using pattern rather than vars for use with mpan
def drot(duration=16, number_of_channels=6):
    if isinstance(duration, int):
        return P[range(duration)]/duration*number_of_channels
    elif isinstance(duration, (Pattern, list)):
        return PTri(duration)/sum(duration)*number_of_channels

pauses = {
    "pa16" : var([1, 0, 1], [6, 4, 6]),
    "pa16_2" : var([1, 0, 1], [2, 4, 10]),
    "pa32" : var([1, 0], [24, 8]),
    "pa32_2" : var([1, 0, 1], [16, 8, 8]),
    "pa64" : var([1, 0, 1], [12, 16, 36]),
}

amp_patterns = {
    "amprm" : PWhite(.8, 1.1)[:77],
    "amprl" : PWhite(.5, 1.3)[:77],
    "amprs" : PWhite(.9, 1)[:77],
}

dynvars |= rhythms | pauses | amp_patterns | pan_rotations

for dynvar,value in dynvars.items():
    globals()[dynvar] = value
