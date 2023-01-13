#Kopiere lister 

karakter=[1,2,3,4,5,6]

ny_liste=karakter
print(ny_liste)
karakter[0]=0
ny_liste[-1]=9
print(karakter)
print(ny_liste)

ny_liste_2=list(karakter)
karakter[-1]=99
print(karakter)
print(ny_liste_2)

#Lister og matematikk 
tall=[1,2,3]
tall=tall*2
print(tall)
navn=("Elise","Liv","Mathilde")
navn=navn*2
print(navn)

nyetall=[1,2,3,4,5,6,7,8,9]
print(nyetall)
print(nyetall[:-1])

#Sortering
tallene=[1,6,1,0,2,5,0,5,6,9,3,8,9]
tallene.sort()
print(tallene)
tallene.sort(reverse=True)
print(tallene)
print(sorted(tallene))

bokstaver=["d","D","%","a","A","-","5"]
print(sorted(bokstaver))

import random
tall1=random.randint(-1,20)
print(tall1)
tall2=random.uniform(1,20)
print(tall2)

#Tilfeldige tall i liste 
tilfeldig_liste=[]
for i in range(10):
    tall=random.randint(1,100)  #NB! Fra/Til
    tilfeldig_liste.append(tall)
print(tilfeldig_liste)
print(sorted(tilfeldig_liste))

