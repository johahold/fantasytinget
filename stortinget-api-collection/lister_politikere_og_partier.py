import json
fil = open("stortinget-api-collection/politikere.json")
politikere_inp = fil.read()
fil.close()

fil = open("stortinget-api-collection/partier.json")
partier_inp = fil.read()
fil.close()

politikere_inp = json.loads(politikere_inp)
partier_inp = json.loads(partier_inp)

def politiker_liste():
    politikere_id = [politikere_inp["representanter_oversikt"]["representanter_liste"]["representant"][i]["id"] for i in range(len(politikere_inp["representanter_oversikt"]["representanter_liste"]["representant"]))]
    politikere = {}
    i=0
    for id in politikere_id:
        politikere[f"{id}"] = {
            "fornavn":f'{politikere_inp["representanter_oversikt"]["representanter_liste"]["representant"][i]["fornavn"]}',
            "etternavn":f'{politikere_inp["representanter_oversikt"]["representanter_liste"]["representant"][i]["etternavn"]}',
            "fyke":f'{politikere_inp["representanter_oversikt"]["representanter_liste"]["representant"][i]["fylke"]["navn"]}'
        }
        i+= 1
    
    return politikere

def partier_liste():
    partier_id = [partier_inp["partier_oversikt"]["partier_liste"]["parti"][i]["id"] for i in range(len(partier_inp["partier_oversikt"]["partier_liste"]["parti"]))]
    partier = {}
    i = 0
    for id in partier_id:
        partier[f"{id}"] = {
            "navn":f'{partier_inp["partier_oversikt"]["partier_liste"]["parti"][i]["navn"]}'
        }
        i+=1
    return partier