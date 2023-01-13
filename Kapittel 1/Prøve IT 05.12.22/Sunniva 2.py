#Prøve 05.12.22
#Oppgave 2

bredde = int(input("Oppgi ønsket bredde på kvadratet: "))
kvadrat = []
grunnlinje = bredde


for i in range(1,bredde):
  print("+ ", end="")
  for j in range(1,bredde):
    print("+ ", end="")
  print("")

i = 0
symbol = input("Skriv inn hvilket symbol du vil at trekanten skal tegnes med: ")

while i in range(1,bredde):
    høyde = i + 1
    print(f" {i} ")
   
while i < bredde:
    i = i + 1
    print(f" {symbol} "*i)
