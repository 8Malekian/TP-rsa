import base64
import random
import tools

def dechiffrer(cle,pathtext):
    clepriv=""
    textalire="encour"
    try : 
        fichier = open (pathtext,"r")
        textadechiffrer = fichier.read()
        print (textadechiffrer)
        fichier2 = open (cle,"r")
        clepriv = fichier2.read()
        print (clepriv)
    except FileNotFoundError:
        print ("pas de clé ou pas de fichier")
    
    if tools.verifClepriv (clepriv):
        print('ici')
        n,d=tools.extractCle(clepriv,"privee")
        blocklenght = len(str(n))-1
        textalire = tools.gettext(textadechiffrer,blocklenght,n,d)


    print(textalire)    
