#Oppgave 12

tall = [0, 1, 2, 0, 0, 3, 4, 5, 0, 0, 6, 0, 7, 0, 8, 0, 0, 0, 9, 10]

while 0 in tall:
    fjern_indeks = tall.index(0)
    tall.pop(fjern_indeks)

print(tall)
