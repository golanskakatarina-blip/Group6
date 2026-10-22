# Tekstspill om prosjektet med medborgerportalen

print("=== Prosjektleder Erling ===")
print("Det har gått seks uker siden prosjektet startet.")
print("Teamet opplever konflikter, og du må ta tre viktige beslutninger.")
print("Skriv A eller B for hvert valg.")

poeng = 0

# Situasjon 1
print("------------------------------")
print("SITUASJON 1: SILJE VS. ELIAS")
print("Silje og Elias er uenige om design og teknologi.")
print("A: Ha individuelle samtaler")
print("B: Ta konflikten opp i plenum")

valg1 = input("Hva velger du? ").upper()
while valg1 != "A" and valg1 != "B":
    valg1 = input("Ugyldig valg. Skriv A eller B: ").upper()

if valg1 == "A":
    print("Konsekvens: Kommunikasjonen i teamet blir bedre.")
    poeng = poeng + 1
elif valg1 == "B":
    print("Konsekvens: Spenningen i møtet øker.")
    poeng = poeng + 0

# Situasjon 2
print("------------------------------")
print("SITUASJON 2: HAMDI VS. HALLGEIR")
print("Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("A: Kalle inn til et felles møte")
print("B: Vente og se")

valg2 = input("Hva velger du? ").upper()
while valg2 != "A" and valg2 != "B":
    valg2 = input("Ugyldig valg. Skriv A eller B: ").upper()

if valg2 == "A":
    print("Konsekvens: De får en felles forståelse og finner et kompromiss.")
    poeng = poeng + 1
elif valg2 == "B":
    print("Konsekvens: Uenigheten vokser i bakgrunnen.")
    poeng = poeng + 0

# Situasjon 3
print("------------------------------")
print("SITUASJON 3: MOTIVASJONEN")
print("Fristen for den første prototypen nærmer seg, og motivasjonen synker.")
print("A: Arrangere en sosial teamaktivitet")
print("B: Kun fokusere på fremdrift")

valg3 = input("Hva velger du? ").upper()
while valg3 != "A" and valg3 != "B":
    valg3 = input("Ugyldig valg. Skriv A eller B: ").upper()

if valg3 == "A":
    print("Konsekvens: Samholdet blir sterkere og motivasjonen øker.")
    poeng = poeng + 1
elif valg3 == "B":
    print("Konsekvens: Presset øker og motivasjonen blir lavere.")
    poeng = poeng + 0

# Vis poengsum og sluttresultat
print("------------------------------")
print("Spillet er ferdig.")
print("Du fikk", poeng, "av 3 poeng.")

if poeng == 3:
    print("NORMING-FASEN")
    print("Teamet har gjenopprettet tilliten, samarbeidet fungerer bedre,")
    print("og prosjektet kan fortsette i en positiv retning.")
elif poeng == 1 or poeng == 2:
    print("DELVIS LØST")
    print("Noen konflikter er løst, men samarbeidet er fortsatt sårbart.")
else:
    print("PROSJEKTET FORSINKES")
    print("Konfliktene har svekket samarbeidet, og prosjektet risikerer forsinkelser.")