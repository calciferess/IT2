#Oppgave 3

print("Dette programmet kan beregne hva et beløp oppgitt i norske kroner blir i en av tre valutaer: ")
print("- Euro ")
print("- Svensk krone")
print("- Japansk yen")

EUR= 10.32
valuta1="euro"
SEK= 0.95
valuta2= "svensk krone"
JPY= 0.07
valuta3= "japansk yen"


norsk_beløp= int(input("Vennligst oppgi beløpet du vil konvertere: "))
ønsket_valuta= input("Vennligst oppgi hvilken valuta du vil bruke av de som ble oppgitt tidligere i programmet. : ")

norsk_eur= norsk_beløp/EUR
norsk_sek= norsk_beløp/SEK
norsk_jpy= norsk_beløp/JPY

if (ønsket_valuta.lower())==(valuta1.lower()):
    print(f"Beløpet du oppga {norsk_beløp} vil ha lik verdi som {norsk_eur:.2f} euro.")
elif (ønsket_valuta.lower())==(valuta2.lower()):
    print(f"Beløpet du oppga {norsk_beløp} vil ha lik verdi som {norsk_sek:.2f} svenske kroner.")
elif (ønsket_valuta.lower())==(valuta3.lower()):
    print(f"Beløpet du oppga {norsk_beløp} vil ha lik verdi som {norsk_jpy:.2f} japanske yen.")
else:
    print("Informasjonen du har oppgitt er ikke gyldig. Vennligst dobbelsjekk om du har oppgitt informasjon i tråd med det programmet spørr om. ")
    