#Oppgave 2
i= 0
tall= int(input("skriv inn hvilket tall du vil se gangetabellen til: "))
øvre_grense= int(input("øvre grense: "))

for i in range(tall,øvre_grense,tall):
    print(i)

for i in range(øvre_grense):
    i=i+1
    print(tall*i)
