from spillere import Spillere 
class Stortinget: 
    def __init__(self): 
        self._tabell = []
    def hent_tabell(self):
        self.tabell.sort()
        x = [self.tabell[i].hent_navn() for i in range(len(self._tabell))]
        return x

    def lag_tabell(self):
        pass