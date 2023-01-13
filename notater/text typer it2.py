from cgitb import text
from opcode import haslocal


text="dette er en mergeliG setning"
#alle små bokstave
print(text.lower())
#alle store bokstaver
print(text.upper())
#starten av settningen får str bokstav
print(text.capitalize())
#gir hver ord stor bokstav
print(text.title())
#viser hvor dette ligger i tekster
print(text.index("g"))
#antal led i teksten
print(len(text))

#viser antal tegn
hallo="Hallo¡"
print(len(hallo))



