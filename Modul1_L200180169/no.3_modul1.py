# Nomer 3
def JumlahHurufVokal(string):
        vok = 0
        for i in string.lower():
            if i in 'aiueo':
                vok += 1
        vokal = len(string)
        return(vokal,vok)
        print()
        
def JumlahHurufKonsonan(string):
        kons = 0
        for i in string.lower():
            if i in 'qwrtypsdfghjklzxcvbnm':
                kons += 1
        konsonan = len(string)
        return(konsonan,kons)
        print()
