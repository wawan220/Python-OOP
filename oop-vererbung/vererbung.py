class Tier:

    def __init__(self):
        print("tier initialesiert")
    
    def wer_bin_ich(self):
        print("ich bin ein tier!")

    def essen(self):
        print("essen")


class Hund(Tier):
    
    def __init__(self):
        Tier.__init__(self)
        print("Hund init")

    def wer_bin_ich(self):
        print("ich bin ein hund")

    def bellen(self):
        print("Wau! Wau!")


class Katze(Tier):
    def __init__(self):
        Tier.__init__(self)
        print("katze init")

    def klettern(self):
        print("kletern")

hund=Hund()
hund.essen()
hund.wer_bin_ich()
hund.bellen()



katze=Katze()
katze.essen()
katze.wer_bin_ich()
katze.klettern()