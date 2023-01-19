from passeringer import Passering
from bompassering import Bompassering
from bil import Kjoretoy

bil1 = Kjoretoy("BR36144", "Harald Holden", "2006", "Volvo", "V70")
bil2 = Kjoretoy("BR70300", "Torill Holden", "2010", "Mercedes", "B")
bil3 = Kjoretoy("PG90499", "Martin Hansen", "2019", "Audi", "A3")

reg_punkt = Bompassering("Eggemoen")

reg_punkt.ny_passering(bil1,"22-10-2023", "09-10")
reg_punkt.ny_passering(bil2,"30-4-2023", "08-09")
reg_punkt.ny_passering(bil3,"22-10-2023", "09-10")
reg_punkt.ny_passering(bil1,"12-10-2023", "09-10")

print(reg_punkt.dato_med_flest())