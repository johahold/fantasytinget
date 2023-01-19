from passeringer import Passering
class Bompassering:
    def __init__(self,navn):
        self.passeringer = []
        self.navn = navn
    
    def dato_med_flest(self):
        x = [self.passeringer[i].hent_dato() for i in range(len(self.passeringer))]
        flest_passeringer = [0, 0]

        datoer = tuple(x)

        for dato in datoer:
            if datoer.count(dato) > flest_passeringer[0]:
                flest_passeringer = [datoer.count(dato), dato]
        return flest_passeringer[1]

        
    def bil_med_flest(self):
        x = [self.passeringer[i].hent_reg_nr() for i in range(len(self.passeringer))]
        flest_passeringer = [0, 0]

        reg_nr = tuple(x)

        for biler in reg_nr:
            if reg_nr.count(biler) > flest_passeringer[0]:
                flest_passeringer = [reg_nr.count(biler), biler]
        return flest_passeringer[1]
    
    def ny_passering(self, bil, dato, time):
        x = Passering(dato, time, bil)
        self.passeringer.append(x)