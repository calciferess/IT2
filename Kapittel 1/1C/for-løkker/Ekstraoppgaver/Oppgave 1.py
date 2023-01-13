#Oppgave 1
#a)
for i in range(2,21,2):
    print(i)

#b)
for i in range(1,21,2):
    print(i)

#c)
for i in range(0,101,2):
    tall=i*i
    print(tall)

#d)
nedre_grense= int(input("nedre grense: "))
øvre_grense= int(input("øvre grense: "))

for i in range(nedre_grense,øvre_grense,2):
    print(i)
