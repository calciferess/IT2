

navn=["Per","Pål","Espen"]
print(navn)
print(navn[0])
heltall=list(range(1,5))
print(heltall)
tiere=list(range(10,101,10))
print(tiere)
partall=[(2*x)for x in range(1,11)]
print(partall)
jentenavn=[]
print(jentenavn)
jentenavn.append("Lise")
jentenavn.append("Kari")
jentenavn.insert(1,"Vibeke")
print(jentenavn)
jentenavn[0]="Dolly"
print(jentenavn)
if "Vibeke" in jentenavn:
    print("Vibeke er med!")
if "Lise" not in jentenavn:
    print("Lise er ikke med!")
posisjon=jentenavn.index("Vibeke")
print(posisjon)
jentenavn.remove("Vibeke")
print(jentenavn)
jentenavn.pop(1)
print(jentenavn)