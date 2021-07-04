import keygen
import decrypt
import crypt
import sys
import base64

def helpi():
    print ("Script monRSA par MC \n" +  
    "Syntaxe : \n" + 
    "     monRSA <commande> [<clé>] [<texte>] [switchs]\n" +
    "Commande :\n" +
    "     keygen : Génére une paire de clé\n" +
    "     crytp : Chiffre <texte> pour le clé publique <clé>\n" +
    "     decrytp: Déchiffre <texte> pour le clé privée <clé>\n" +
    "     help : Affiche ce manuel\n" +
    "Clé :\n" +
    "     Un fichier qui contient une clé publique monRSA (\"crypt\") ou une clé privée (\"\decrypt\"\))\n"+
    "Texte :\n" +
    "     Une phrase en clair (\"crypt\") ou une phrase chiffrée (\"decrypt\")\n" +
    "Switchs\n"+
    "     -f <file> permet de choisir le nom des clé générés, monRSA.pub et monRSA.priv par défaut"
        )



def main(argv):
    again = True
    while again:
        arguments = len(sys.argv) - 1  
        command = ["keygen","crypt","decrypt"] 
        if arguments == 4 or arguments ==3 and argv[0] in command :
            if argv[0] == "keygen" :
                if arguments == 4:
                    nonCle = argv[3]
                else:
                    nonCle = "vide"
                keygen.keygen(nonCle)
            elif argv[0] == "decrypt" :
                decrypt.dechiffrer(argv[1],argv[2])
            elif argv[0] == "crypt" :
                crypt.chiffrer(argv[1],argv[2])
        else :
            helpi()
        




if __name__ == "__main__":
    main(sys.argv[1:])

