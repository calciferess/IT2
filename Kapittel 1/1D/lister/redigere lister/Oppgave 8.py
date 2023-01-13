#Oppgave 8 

tall=[1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]

while i in range(tall):
    if 3 in tall:
        fjern_indeks = tall.index(3)
        tall.pop(fjern_indeks)

print(tall)

