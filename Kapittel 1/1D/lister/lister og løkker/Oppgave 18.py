#Oppgave 18 

tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]

total = 0

for x in tall:
    total = total + x

gjennomsnitt = total / len(tall)

print(f"Sum: {total}")
print(f"Gjennomsnit: {gjennomsnitt}")

