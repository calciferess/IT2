#Oppgave 16

n = 8
liste = []

 
for i in range(n):
    bruker_tall = int(input("Skriv et tall: "))
    liste.append(bruker_tall)

storst = liste[0]
minst = liste[0]

for i in range(len(liste)):
    if liste[i] > storst:
        storst = liste[i]
    if liste[i] < minst:
        minst = liste[i]

print(minst)
print(storst)
print(min(liste))
print(max(liste))

    