from poengsystem import Poengsystem

class Politiker:
    def __init__(self,pris,id,fylke):
        self._pris = pris 
        self._id = id 
        self._fylke = fylke
        self._poeng = 0 
    def oppdater_poeng(self): 
        Poengsystem.poeng(self)
        self._poeng += Poengsystem.poeng() 
    

        