from bomring.passeringer import Passering
class Bompassering:
    def __init__(self,navn):
        self.passeringer = []
        self.navn = navn
    
    def dato_med_flest(self):
        x = [self.passeringer[i].hent_dato() for i in range(len(self.passeringer))]
        flest_passeringer = [0, 0]

        datoer = set(x)

        for dato in datoer:
            if x.count(dato) > flest_passeringer[0]:
                flest_passeringer = [x.count(dato), dato]
        return flest_passeringer[1]

    # def time_med_flest(self):
    #     x = [self.passeringer[i].hent_time() for i in range(len(self.passeringer))]
    #     flest_passeringer = [0, 0]

    #     timer = set(x)

    #     for dato in timer:
    #         if x.count(dato) > flest_passeringer[0]:
    #             flest_passeringer = [x.count(dato), dato]
    #     return flest_passeringer[1]
        
    def bil_med_flest(self):
        x = [self.passeringer[i].hent_reg_nr() for i in range(len(self.passeringer))]
        flest_passeringer = [0, 0]

        reg_nr = set(x)

        for biler in reg_nr:
            if x.count(biler) > flest_passeringer[0]:
                flest_passeringer = [x.count(biler), biler]
        return flest_passeringer[1]
    
    def ny_passering(self, bil, dato, time):
        x = Passering(dato, time, bil)
        self.passeringer.append(x)