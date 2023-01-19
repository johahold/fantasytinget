class Kjoretoy:
    def __init__(self, reg_nr,eier,modell,merke,type):
        self.reg_nr = reg_nr
        self.info = [eier, modell, merke, type]

    def hent_reg_nr(self):
        return self.reg_nr