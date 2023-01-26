from poengsystem import Poengsystem

class Politiker:
    def __init__(self,pris,id,fylke, navn):
        self._pris = pris 
        self._id = id 
        self._fylke = fylke
        self._poeng = 0 
        self._navn = navn 
    def oppdater_poeng(self): 
        Poengsystem.poeng(self)
        self._poeng += Poengsystem.poeng() 
    

        