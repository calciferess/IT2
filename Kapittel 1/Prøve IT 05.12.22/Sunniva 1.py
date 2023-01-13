#Prøve 05.12.22
#Oppgave 1

import random

bokklubb = ["Jonas","Ludvig","Gunnar","Knut","Jens","Jo","Henrik","Ivar","Agnar","Jørn"]

tilfeldig_tall = random.randint(0,10)

for i in bokklubb:
    førsteplass = bokklubb[tilfeldig_tall]
    bokklubb.pop(tilfeldig_tall)
    print(f"Førsteplass og vinneren av gavekortet på 1000 kroner er {førsteplass}!")
    for j in bokklubb:
        andreplass = bokklubb[tilfeldig_tall]
        bokklubb.pop(tilfeldig_tall)
        print(f"Andreplass og vinneren av gavekortet på 500 kroner er {andreplass}!")
        for k in bokklubb:
            tredjeplass = bokklubb[tilfeldig_tall]
            bokklubb.pop(tilfeldig_tall)
            print(f"Tredjeplass og vinneren av gavekortet på 250 kroner er {tredjeplass}!", end = "")
            print("")

