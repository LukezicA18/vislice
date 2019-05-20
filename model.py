import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = [] if crke == None else crke
    
    def napacne_crke(self):
        ugibane_crke = []
        for crka in self.crke:
            if crka not in self.geslo:
                ugibane_crke.append(crka)
        return ugibane_crke

    def pravilne_crke(self):
        ugibane_pravilne_crke = []
        for crka in self.crke:
            if crka in self.crke:
                ugibane_pravilne_crke.append(crka)
        return ugibane_pravilne_crke

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
            else:
                return True
    
    def poraz(self):
        if self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK:
            return PORAZ
    
    def pravilni_del_gesla(self):
        nova_beseda = ''
        for crka in self.geslo:
            if crka in self.crke:
                nova_beseda += '_'
        return nova_beseda

    def nepravilni_del_gesla(self):
        niz_nepravilnih_crk = ''
        for crka in self.geslo:
            if crka not in self.crke:
                niz_nepravilnih_crk += 'crka'
        return niz_nepravilnih_crk
    
    def nepravilni_ugibi(self):
        nepravilni_ugibi = ''
        for crka in self.geslo:
            if crka in self.napacne_crke():
                nepravilni_ugibi += crka + ' '
        return nepravilni_ugibi

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka not in self.geslo:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
        else:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA

bazen_besed = []       
with open('besede.txt', 'r') as d:
    for vrstica in d:
        bazen_besed.append(vrstica.upper().strip())

def nova_igra():
    return Igra(random.choice(bazen_besed))



ZACETEK = 'S'

class Vislice:
    def __init__(self):
        self.igre = {}
    
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre
    
    def ugibaj(self, id_igre, crka):
        igra = self.igre[id_igre][0] 
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)




    
        
    

