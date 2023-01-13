#eksempel 

verdensdeler = ["Nord-Amerika", "Sør-Amerika", "Afrika", "Oseania", "Antarktis"]

#løkker med indekser
for i in range(5):
    print(f"Indeks{i} - Verdi: {verdensdeler[i]}")

#range bestemt av lengden på listen 
for j in range(len(verdensdeler)):
    print(verdensdeler[j])

#løkker uten indekser 

for x in verdensdeler:
    print(x)

for verdensdel in verdensdeler:
    print(verdensdeler)

#Vanlige algoritmet som involverer lister
tall = [2, 4, 6, 8, 10]

total = 0

for x in tall:
    total = total + x

print(sum(tall))

#Størst og minst verdi i en liste
tall = [2, 4, 6, 8, 10]

storst = tall[0]

for i in range(len(tall)):
    if tall[i] > storst: 
        storst = tall[i]

print(storst)

for x in tall:
    if x > storst:
        storst = x

print(storst)

#Telle forekomster av en verdi
tall = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]

nuller = 0
enere = 0

for x in tall:
    if x == 0:
        nuller = nuller + 1
    if x == 1:
        enere = enere + 1

print(f"Nuller: {nuller}, enere: {enere}.")

#Fylle en liste med input()
#eksempel
n = 10    # antall tall
tall = []

for i in range(n):
    bruker_tall = int(input("Skriv et tall: "))
    tall.append(bruker_tall)

print(tall)

#Bytte plass på verdier
tall= [2,4,6,8,10]

tall[0] = tall[-1]
tall[-1] = tall[0]

midlertidig = tall[0]
tall[0] = tall[-1]
tall[-1] = midlertidig

#Skrive ut flere verdier på en ryddig måte 
navn = "Pål"
karakterer = [3,4,6,6,5,4]

karaktertekst = ""
for i in range(len(karakterer)):
    karaktertekst += str(karakterer[i])

print(f"{navn} fikk karakterene {karaktertekst}")

karaktertekst = ""
for i in range(len(karakterer)):
    if i > 0:
        karaktertekst += ", "
    karaktertekst += str(karakterer[i])

print(f"{navn} fikk karakterene {karaktertekst}")


