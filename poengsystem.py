from scraper import overskrifter
from politiker import Politiker 


class Poengsystem:
    def __init__(self):
        self._antall_ganger = 0
        self._poeng = 0  

    def antall_ganger(self):
        pass

    def poeng(self):
        for i, overskrift in enumerate(overskrifter):
            viktighet = len(overskrifter)-i
            for politiker in self._politiker:
                if politiker._navn in overskrift:
                    self._poeng += viktighet
                    return self._poeng
