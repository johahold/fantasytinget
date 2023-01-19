class Kjoretoy:
    def __init__(self, reg_nr,eier,modell,merke,type):
        self.reg_nr = reg_nr
        self.type = type
        self.info = [eier, modell, merke]


    def hent_reg_nr(self):
        return self.reg_nr

    def hent_type(self):
        return self.type