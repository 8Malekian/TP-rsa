import tools
import string


def chiffrer(cle,pathtext):
    
    clepub=""
    textasauver=""
    try : 
        fichier = open (pathtext,"r")
        textachiffrer = fichier.read()
        print ("text: " +textachiffrer)
        fichier2 = open (cle,"r")
        clepub = fichier2.read()
        print ("clépub: "+clepub)
    except FileNotFoundError:
        print ("pas de clé ou pas de fichier")
    
    if tools.verifClepriv (clepub):
        n,e=tools.extractCle(clepub,"pub")
        blocklenght = len(str(n))-1
        tabtext =tools.getpeparetext(textachiffrer,blocklenght)
        for numbers in tabtext:
            if len(numbers) < blocklenght:
		
                while len(numbers) != blocklenght:
                    numbers = '0'+numbers
                    print (str(numbers))
            textasauver = textasauver + str (int(numbers)^e % n)
        fichier= open("messagechifre.txt",'w')
        fichier.write(textasauver)
        fichier.close
    print(textasauver)

