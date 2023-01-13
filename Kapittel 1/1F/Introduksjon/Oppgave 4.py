#Oppgave 4 
import random

tilfeldig = random.randint(1,3)

def tilfeldig_hilsen():
    if tilfeldig == 1:
        print("Hei!")
    if tilfeldig == 2:
        print("Hallo!")
    if tilfeldig == 3:
        print("God dag!")

tilfeldig_hilsen()