#Oppgave 10

byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"]

#a)
byer.remove("Stavaangir")
print(byer)

#b)
if "OSLOO" in byer:
    fjern_index = byer.index("OSLOO")
    byer.pop(fjern_index)

#c) 
byer.insert(3,"Stavanger")
byer.insert(0,"Oslo")
print(byer)
