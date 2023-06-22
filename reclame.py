from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_met_korting = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_met_korting} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

def gemiddelde(mijn_lijst):
    som = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde = som / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer