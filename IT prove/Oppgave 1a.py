#Oppgave 1a 

print("Dette programmet kan gjøre en rekke regneoperasjoner med tre forskjellige positive heltall du oppgir.")

tall1= int(input("Tall #1: "))
tall2= int(input("Tall #2: "))
tall3= int(input("Tall #3: "))

sum= tall1+tall2+tall3
gjennomsnitt= sum/3

print("Summen av tallene er: ",sum)
print("Gjennomsnittet av tallene er: ", gjennomsnitt)
if tall1>tall2:
    if tall1>3:
        print("Tall #1 er størst.")
elif tall2>tall1:
    if tall2>tall3:
        print("Tall #2 er størst.")
else:
    print("Tall #3 er størst.")
if tall1<tall2:
    if tall1<tall3:
        print("Tall #1 er minst.")
elif tall2<tall1:
    if tall2<tall3:
        print("Tall #2 er minst. ")
