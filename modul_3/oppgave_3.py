brus = 24.90
smørbrød = 45 
banan = 8.50 

totalsum = brus + smørbrød + banan
print("Totalsum:", totalsum)

totalsum_med_mva = totalsum * 1.25
print("Totalsum med mva:", totalsum_med_mva)

pris_per_person = totalsum_med_mva / 4 
print("Pris per person:", pris_per_person)

prisforskjell = smørbrød - banan
print("Prisforskjell:", prisforskjell)

print(type(smørbrød + brus))

print(type(pris_per_person))

#Refleksjon 

#Spørsmål 1: Når jeg slo smørdbrød som er heltall og brus som er desimaltall ble svaret datatypen float som er desimaltall.

#Spørsmål 2: Datatypen ble float når jeg delte mellom 4. Jeg ble ikke overrasket, fordi prisen per person ble 24.5 og derfor trenger en desimal.

#Spørsmål 3: Det er en fordel å bruke variabler, fordi man bare trenger å endre tallet ett sted hvis det er en endring. 