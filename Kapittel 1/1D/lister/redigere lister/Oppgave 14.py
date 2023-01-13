#Oppgave 14

import random

tilfeldige_tall = []

for i in range(1000):
    tilfeldig = random.uniform(1,100)
    tilfeldige_tall.append(tilfeldig)

tilfeldige_tall.sort()
print(f"Første og minste tall i listen: {tilfeldige_tall[0]}")
print(f"Siste og største tall i listen: {tilfeldige_tall[-1]}")

print(min(tilfeldige_tall))
print(max(tilfeldige_tall))

