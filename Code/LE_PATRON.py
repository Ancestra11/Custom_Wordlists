import Ecrivain#, Avocat
import Chimiste

Ecri = Ecrivain.Ecrivain()
Chimi = Chimiste.Chimiste(Ecri.getPotentiel())

def LE_PATRON() :
    
    Ecri.Collecte()
    #Ecri.Ecriture()

    Chimi.LEET()
    In = Chimi.Infinity()
    Ecri.Ecriture(In)

if __name__ == "__main__" :
    LE_PATRON()
