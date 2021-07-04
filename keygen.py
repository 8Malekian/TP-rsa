import tools
import random
import base64


def keygen (Noncle):

#création de 2 entrier premier n et q 

    p = tools.getPrime(32)
    q = tools.getPrime(32)
#on test pour ne pas avoir deux nombres identiques
    while p == q:
            q = tools.getPrime(32)

#calcul de n et m
    n = p*q
    m = (p-1)*(q-1)
    print(m)

#pour cette partie j'ai essayé beaucoup de chose et je ne suis pas arrivé tout seul a réduire le temps de a quelque chose de réalisable 
#J'ai demandé de l'aide et on m'a dit de regarder de coté du plus grand diviseur (gcd)et le l'inverse modulaire pour avoir e et d 
#https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu
#et la je suis arrivé avec une génération de clé.

#calcule de e
    while 1:
        e = random.randrange(2**(32 - 1), 2**(32))
        if gcd(e, m) == 1:
            break
    #print (e)

#calcul de d
    d = moduloInverse(e, m)
    #print (d) 

#création des clefs
    clepub  = base64.b64encode((hex(n)+'\n'+hex(e)).encode("utf-8"))
    clepriv = base64.b64encode((hex(n)+'\n'+hex(d)).encode("utf-8"))
    print("Clé publique :", (n,e))
    #print (hex(n))
    #print (hex(e))
    print (clepub)
    print("Clé privé :", (n,d))
    print (clepriv)
    print("Clé public :", (n,e))
#création des fichiers
    if Noncle == "vide":
        nonfichierpub = "monRSA.pub"
        nonfichierpriv ="monRSA.priv"
    else:
        nonfichierpub = Noncle + ".pub"
        nonfichierpriv = Noncle + ".priv"
    fichier = open(nonfichierpriv,"w")
    fichier.write ('---begin monRSA private key ---\n' + str(clepriv,'utf8') +'\n---end monRSA key ---\n')
    fichier.close()
    fichier = open(nonfichierpub,"w")
    fichier.write ('---begin monRSA public key ---\n' + str(clepub,'utf8') +'\n---end monRSA key ---\n')
    fichier.close()
 
 
def moduloInverse(a, m):
    "Calcul l'inverse de a modulo m avec l'algorithme d'euclide étendu" 
    if gcd(a, m) != 1:
        return None     
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def gcd(a, b):
    "Calcul le PGCD de a et b"
    while a != 0:
        a, b = b % a, a
    return b