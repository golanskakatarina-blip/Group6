POENG = 0 
print("Velkommen til Erlings prosjekt!")
print("Erling leder et team som utvikler en digital medborgerportal.")
print("Det har oppstått konflikter i teamet.")
print("Du skal hjelpe Erling med å ta tre vikige valg.")

#Situasjon 1
print("\nSituasjon 1: Silje og Elias")
print("Silje og Elias er uenige om design og teknologi.")
print("Hva skal Erling gjøre?")
print("A: Ha induviduelle samtaler med dem.")
print("B: Ta opp konflikten foran hele teamet.")

valg1 = input("Velg A eller B: ").strip().upper()

if valg1 == "A":
    print("Erling snakker med dem hver for seg.")
    print("kommunikasjonen blir bedre.")
    POENG = POENG + 1
elif valg1 == "B":
    print("Erling tar opp konflikten i plenum.")
    print("Det blir mer spenning i møtet.")
else:
        print("ugyldig valg. Du får 0 poeng.")

#situasjon 2
print("\nsituasjon 2: Hamdi og Hallgeir")
print("Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("Hva skal Erling gjøre?")
print("A: kalle inn til et felles møte.")
print("B: Vente og se om de løser konflikten selv.")

valg2 = input("Velg A eller B: ").strip().upper()

if valg2 == "A":
    print("Erling arrangerer et felles møte.")
    print("De får bedre forståelse for hverandre.")
    POENG = POENG + 1
elif valg2 == "B":
    print("Erling velger å vente.")
    print("uenigheten fortsetter å vokse.")
else:
    print("ugyldig valg. Du får 0 poeng.")

# Situasjon 3
print("\nSituasjon 3: Motivasjon i teamet")
print("Fristen nærmer seg, og motivasjonen i teamet synker.")
print("Hva skal Erling gjøre?")
print("A: Arrangere en sosial teamaktivitet.")
print("B: Bare fokusere på fremddrift.")

valg3 = input("velg A eller B: ").strip().upper()

if valg3 =="A":
    print("Erling arrangerer en sosial aktivitet.")
    print("Samholdet og motivasjonen blir bedre.")
    POENG = POENG + 1
elif valg3 == "B":
    print("Erling velger å bare fokusere på arbeidet.")
    print("Presset øker, og motivasjonen synker.")
else:
    print("Ugyldig valg. Du får 0 poeng.")

#Avslutning 
print("\nHistorien er ferdig")
print("Du fikk", POENG, "av 3 poeng.")

if POENG == 3:
    print("Resultatet: Teamet går videre til norming-fasen!")
    print("Konfliktene løses, og samrbeidet blir bedre.")
elif POENG == 1 or POENG == 2:
    print("Resultat: Konfliktene er delvis løst.")
    print("Teamet samarbeider, men har fortsatt utfordinger.")
else:
    print("Resultat: Prosjektet blir forsinket.")
    print("Konfliktene fortsetter, og samholdet blir dårligere.")

print("\nTakk for at du spilte!")

    
