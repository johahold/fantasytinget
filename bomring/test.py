import json
from bomring.bompassering import Bompassering
from bomring.kjoretoy import Kjoretoy

fil = open("biler.json")
biler = json.load(fil)
fil.close()

fil = open("passeringer.json")
passeringer = json.load(fil)
fil.close()

alle_kjoretoy = {}

for bil in biler:
    alle_kjoretoy[bil[0]] = Kjoretoy(bil[0],bil[1], "Mercedes", "EL")


e18_sandvika_vest = Bompassering("e18_sandvika_vest")

for passering in passeringer:
    kjoretoy = alle_kjoretoy[passering[0]]
    e18_sandvika_vest.ny_passering(kjoretoy, passering[1], "09-10")

print(e18_sandvika_vest.dato_med_flest())







bil1 = Kjoretoy("BR36144", "Harald Holden", "2006", "Volvo", "Blyfri")
bil2 = Kjoretoy("BR70300", "Torill Holden", "2010", "Mercedes", "Diesel")
bil3 = Kjoretoy("ED90499", "Martin Hansen", "2019", "Mercedes", "El")

reg_punkt = Bompassering("Eggemoen")

reg_punkt.ny_passering(bil1, "09-10", "22-10-2023")
reg_punkt.ny_passering(bil2, "08-09", "30-4-2023")
reg_punkt.ny_passering(bil3, "09-10","21-1-2023")
reg_punkt.ny_passering(bil1, "09-10", "22-10-2023")

print(reg_punkt.dato_med_flest())

print(reg_punkt.bil_med_flest())


