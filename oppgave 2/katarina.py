print ("Hei, Erling")
print ("Etter å ha snakket med Silje, Elias, Hamdi og Hallgeir, \n"
"   skal du hjelpe de med å løse deres konflikter. \n"
"   Du får nå flere alternativer å velge mellom. \n"
"   Dette er et spill som skal hjelpe deg å velge riktig løsning. Lykke til!")
print ("Velg mellom 1 av 2 alternativene for å kunne gå videre i spillet.")

print ("Situasjon 1: Silje og Elias er uenig om design og teknologi \n"
"   Alternativ A: Individuelle samtaler \n"
"   Alternativ B: Tar det opp i plenum \n")

point = 0

valg = input ("Hva velger du? (A/B): ").upper()

while valg not in ["A", "B"]:
    print("Ugyldig valg. Vennligst velg A eller B.")
    valg = input("Hva velger du? (A/B): ").upper()  
if valg == "A":
    print("Du valgte individuelle samtaler. \n"
"   Dette kan hjelpe med å løse konflikten på en mer personlig måte.")
    point = 1
else:
    print("Du valgte å ta det opp i plenum. \n"
"   Dette kan føre til at konflikten eskalerer og skaper mer spenning i teamet.")
    point = 0

print ("-------------------------------")
print ("Situasjon 2: Hamdi og Hallgeir er uenige om digitale folkemøter \n"
"   Alternativ A: Kaller inn til felles møte \n"
"   Alternativ B: Venter og ser om konflikten løser seg selv \n")

valg = input ("Hva velger du? (A/B): ").upper()

while valg not in ["A", "B"]:
    print("Ugyldig valg. Vennligst velg A eller B.")
    valg = input("Hva velger du? (A/B): ").upper()  

if valg == "A":
    print("Du valgte å kalle inn til felles møte. \n"
    "Dette kan hjelpe med å løse konflikten raskt og effektivt.")
    point += 1
else:
    print("Du valgte å vente og se om konflikten løser seg selv. \n"
    "Dette kan føre til at konflikten eskalerer.")
    point += 0

print ("-------------------------------")
print ("Situasjonen 3: Motivasjon. Fristen nærmer seg og energien synker. \n"
"   Alternativ A: Social teamaktivitet \n"
"   Alternativ B: Kun fokus på fremdrift \n")

valg = input ("Hva velger du? (A/B): ").upper()

while valg not in ["A", "B"]:
    print("Ugyldig valg. Vennligst velg A eller B.")
    valg = input("Hva velger du? (A/B): ").upper()  

if valg == "A":
    print("Du valgte en sosial teamaktivitet. \n"
    "Dette kan hjelpe med å øke motivasjonen og energien i teamet.")
    point += 1
else:
    print("Du valgte å kun fokusere på fremdrift. \n"
    "Dette kan føre til at teamet blir mer stresset og mindre motivert.")
    point += 0

print ("-------------------------------")
print ("Norming-fasen: 3 poeng \n"
       "Delvis løst: 1-2 poeng \n"
       "Prosjektet forsinket: 0 poeng \n")
print("Hei, du fikk", point, "poeng.")

if point == 3:
    print("Gratulerer! Du har valgt de beste alternativene \n"
"   for å løse konfliktene og motivere teamet. \n"
"   Teamet er nå i norming-fasen og prosjektet går fremover.")
elif point == 2:
    print("Bra jobba! Du har valgt noen gode alternativer, \n" 
"   men det er fortsatt rom for forbedring. \n"
"   Teamet er på vei til norming-fasen.")
elif point == 1:
    print("Du har valgt noen dårlige alternativer, \n"
"   og teamet kan fortsatt ha konflikter og lav motivasjon. \n"
"   Det er viktig å jobbe med å forbedre situasjonen.")
else:
    print("Dessverre, du har valgt de dårligste alternativene, \n"
"   og teamet har mistet motivasjonen og energien. \n"
"   Prosjektet kan bli forsinket eller mislykkes. \n"
"   Det er viktig å ta tak i situasjonen og finne bedre løsninger.")