#Oppgave 1c
import math

print("Dette programmet kan beregne volumet av en kule basert på radiusen du oppgir.")

radius= int(input("Radius: "))
volum_kule= (4/3)*(math.pi)*(radius**3)

print("Volumet av kulen er: ",volum_kule)
