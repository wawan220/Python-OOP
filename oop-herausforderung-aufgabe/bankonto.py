

class Bankkonto:
    def __init__(self, inhaber:str,kontostand:float):
        self.inhaber=inhaber
        self.kontostand=kontostand

    def einzahlen(self,betrag:float):
        self.kontostand+=betrag
        print(f"es wurde eingezahlt: >{betrag:.2f}€")
        print(f"aktueller kontostand: >{self.kontostand:.2f}€")

    def abbuchungen(self,betrag:float):
        if self.kontostand>=betrag:
            self.kontostand-=betrag
            print(f"es wurde abgebucht: >{betrag:.2f}€")
            print(f"aktueller kontostand: >{self.kontostand:.2f}€")
        else:
            print(f"leider kann der betrag {betrag:.2f}€ nicht abgebucht werden.")
            print("Kontostand zu niedrieg")
            print(f"aktueller Kontostand: >{self.kontostand:.2f}€")
    
    def __str__(self):
        return f"der aktuelle kontostand beträgt:\n > {self.kontostand:.2f}€"



konto1=Bankkonto(inhaber="waldi",kontostand=500)
#print(f"{konto1.kontostand:.2f}")
konto1.einzahlen(10.10)
#print(f"{konto1.kontostand:.2f}")
konto1.abbuchungen(60.10)
#print(f"{konto1.kontostand:.2f}")
konto1.abbuchungen(450)
#print(f"{konto1.kontostand:.2f}")
konto1.einzahlen(10)
#print(f"{konto1.kontostand:.2f}")
konto1.abbuchungen(20)
#print(f"{konto1.kontostand:.2f}")
print(konto1)

