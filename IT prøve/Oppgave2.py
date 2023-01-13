#Oppgave 2

setning= input("Vennligst skriv inn en valgfri setning som er mellom 15 og 30 tegn. Setning: ")
lengde_setning= len(setning)
halv_lengde= int(lengde_setning/2)
første_tegn= (setning[0:1])
siste_tegn= 2
første_halvdel= (setning[0:halv_lengde])
andre_halvdel= (setning[halv_lengde:30])

print("Din setning: ", setning)
print("Antall tegn i setningen: ", lengde_setning)
print("Første tegn i setningen: ", første_tegn)
print("Siste tegn i setningen: ", siste_tegn)
print("Første halvdel av setningen: ",første_halvdel)
print("Andre halvdel av setningen: ", andre_halvdel)
