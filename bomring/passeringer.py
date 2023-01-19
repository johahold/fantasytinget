class Passering:
    def __init__(self, time, dato,kjoretoy):
        self.kjoretoy = kjoretoy
        self.time = time
        self.dato = dato
    
    def hent_dato(self):
        return self.dato

    def hent_reg_nr(self):
        return self.kjoretoy.hent_reg_nr()

    def hent_time(self):
        return self.time