from spillere import Spillere 
class Stortinget: 
    def __init__(self): 
        self._tabell = []
    def hent_tabell(self):
        x = [self._tabell[i].hent_poeng() for i in range(len(self._tabell))]
        x.sort()
        return x

    def lag_tabell(self):
        pass