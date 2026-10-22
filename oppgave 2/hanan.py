class Storyline:
    def __init__(self): #konstruktør, initialisere de tre valgvariablene
        self.first = 0
        self.second = 0
        self.third = 0

    def giveChoice(self, beslutning): #spør om prompt
        try:
            question = int(input())
        except ValueError:
            print("Try again, input must be a number (0 or 1)")
            self.giveChoice(beslutning)
            return

        if question not in (0, 1):
            print("Try again, input only 0 or 1")
            self.giveChoice(beslutning)
            return

        setattr(self, beslutning, question) #stores the result, samme som object.name=value name er string variable


print("___________________________________________________________________")
print("Som prosjektleder, må man ta flere beslutninger for å nå målet.")
print("___________________________________________________________________")
story = Storyline() #objekt heter story
print("Første situasjon: Silje vs Elias er uenige om design og teknologi.")
print("     Alternativ 0: Ta det opp i plenum")
print("     Alternativ 1: Bedre kommunikasjon i teamet")
story.giveChoice("first") #giveChoice er en metode, vi kjører metoden på objektet story
print("___________________________________________________________________")
print("Andre situasjon: Hamdi vs Hallgeir er uenige om digitale folkemøter")
print("     Alternativ 0: Venter og ser")
print("     Alternativ 1: Kaller inn til felles møte")
story.giveChoice("second")
print("___________________________________________________________________")
print("Tredje situasjon: Fristen nærmer seg og energien synker")
print("     Alternativ 0: Kun fokus på fremdrift")
print("     Alternativ 1: Finne på sosial teamaktivitet")
story.giveChoice("third")
print("___________________________________________________________________")

point = story.first + story.second + story.third 
#print("Poengsum: ", point, " av 3")

if point == 3:
    print("Du er i norming-fasen")
elif point == 0:
    print("Prosjektet er forsinket")
else:
    print("Konfliktene er delvis løst. Her ser du hva som har skjedd:")

    if story.first == 0:
        print("     Det blir økt spenning i gruppa etter å ha tatt det opp i plenum.")
    else: print("     Prosjektmedlemmene blir bedre på kommunikasjon med hverandre")
    if story.second == 0:
        print("     Uenigheten mellom Hamdi og Hallgeir vokser i bakgrunnen")
    else: print("     Det blir en felles forståelse og kompromiss.")
    if story.third == 0:
        print("     Det er økt press og lavere motivasjon i gruppa")
    else: print("     Det er sterkere samhold og høyere motivasjon")