import Ecrivain, Avocat
import Chimiste
def main() :
    Ecri = Ecrivain.Ecrivain()
    Ecri.Collecte()
    Ecri.Ecriture()

    Chimi = Chimiste.Chimiste(Ecri.getPotentiel())
    Chimi.Modifications()

if __name__ == "__main__" :
    main()
