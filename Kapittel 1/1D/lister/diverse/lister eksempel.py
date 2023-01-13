#LISTER

navn=["Hans","Nils","Jens"]
print(navn[1])

for i in range(len(navn)):
    print(navn[1])

for personer in navn:
    print(personer)

tall=[3,6,8,2,5,7,3,88]
summen=0

#Summering 
for x in tall:
    summen=summen+x
print(summen)

størst= tall[0]
minst= tall[0]

for x in tall:
    if x > størst:
        størst = x
    if x < minst:
        minst = x
print(tall)
print("Minst:", minst)
print("Størst:", størst)

antall = 0
for x in tall: 
    if x ==3:
        antall = antall + 1
print("Antall treere: ", antall)

#Bytte rekkefølge på to elementer i lista
ekstra=tall[0]
tall[0]=tall[-1]
tall[-1]=ekstra
print(tall)