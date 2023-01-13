#Lister pt 12488182129331

liste_1=[[1,2,3],[4,5,6],[7,8,9]]
print(liste_1)
liste_2=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(liste_2)

print(liste_2[0][0])
print(liste_2[1][1])
print(liste_2[2][2])

#Lage todim liste med stjerner
import random
todim=[]
ant_rader=5
ant_kolonner=2

for i in range(ant_rader):
    rad=["*"]*ant_kolonner
    todim.append(rad)
print(todim)

#Fyller inn tilfeldige tall i "stjernelista"
todim_2=[]

for i in range(ant_rader):
    for j in range(ant_kolonner):
        tall=random.randint(1,10) 
        todim_2[i][j]=tall
print(todim_2)

