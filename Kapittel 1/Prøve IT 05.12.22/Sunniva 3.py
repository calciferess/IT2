#Prøve 05.12.22
#Oppgave 3
#NB! Fikk ikke denne helt til så den er ikke ferdig. 


elever = ["Torstein","Geir","Sigrun","Vibeke","Heidi","Thomas","Gry"]
klasse = ["3A","3B","3C","3A","3A","3B","3C"]
karakter = [4,6,2,1,5,4,6]

klasse_utvidet = [elever, klasse, karakter]
print(klasse_utvidet)

beste_karakter = karakter[0]

for i in range(len(beste_karakter)):
    if beste_karakter[i] > beste_karakter:
        høyest = karakter[i]
print(beste_karakter)

gitt_klasse = input("Klasse du vil beregne gjennomsnitt for: ")

for i in klasse_utvidet:
    if klasse == "gitt_klasse":

