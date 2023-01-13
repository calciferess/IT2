#Oppgave 1b

print("Dette programmet beregner og skriver ut heltall og rest etter en divisjon mellom to heltall som brukeren oppgir i starten av programmet.")

tall1= int(input("Tall #1: "))
tall2= int(input("Tall #2: "))

rest= tall1%tall2
heltall= tall1//tall2

print("Heltall: ", heltall)
print("Rest: ", rest)
