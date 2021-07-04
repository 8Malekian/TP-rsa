import random
import base64
import codecs
import string
#methode pour valider les nombres premier
# liste des nombres premiers
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
					31, 37, 41, 43, 47, 53, 59, 61, 67,
					71, 73, 79, 83, 89, 97, 101, 103,
					107, 109, 113, 127, 131, 137, 139,
					149, 151, 157, 163, 167, 173, 179,
					181, 191, 193, 197, 199, 211, 223,
					227, 229, 233, 239, 241, 251, 257,
					263, 269, 271, 277, 281, 283, 293,
					307, 311, 313, 317, 331, 337, 347, 349]



#la methode de Miller Rabin 
def isMillerRabinPassed(mrc):
	maxDivisionsByTwo = 0
	ec = mrc-1
	while ec % 2 == 0:
		ec >>= 1
		maxDivisionsByTwo += 1
	assert(2**maxDivisionsByTwo * ec == mrc-1)

	def trialComposite(round_tester):
		if pow(round_tester, ec, mrc) == 1:
			return False
		for i in range(maxDivisionsByTwo):
			if pow(round_tester, 2**i * ec, mrc) == mrc-1:
				return False
		return True

	numberOfRabinTrials = 20
	for i in range(numberOfRabinTrials):
		round_tester = random.randrange(2, mrc)
		if trialComposite(round_tester):
			return False
	return True

def nombrealiatoire(n):
	return random.randrange(2**(n-1)+1, 2**n - 1)

def getLowLevelPrime(n):
	while True:
		nball = nombrealiatoire(n)
		# Test si il est divisible par le nombre premier
		for div in first_primes_list:
			if nball % div == 0 and div**2 <= nball:
				break
		else: return nball

def getPrime(n):
	while True:
		#on test si il est potentiellement premier avec les nombres premiers plus petit		
		prime_candidate = getLowLevelPrime(n)
		#on valide en utilisant la methode de miller rabin 
		if not isMillerRabinPassed(prime_candidate):
			continue
		else:
			return prime_candidate

##################################################################################################################

#methode pour controler le format des clé et les extraire
def verifClepriv(key):
	print("verifkey"+key)
	return (key.startswith('---begin monRSA private key ---') and key.endswith('---end monRSA key ---\n'))

def verifClepub(key):
	print("verifkey"+key)
	return (key.startswith('---begin monRSA public key ---') and key.endswith('---end monRSA key ---\n'))

def extractCle(key,cletype):
	
	if cletype == 'privee':
		imputtrim = key.replace('---begin monRSA private key ---\n','').replace ('\n---end monRSA key ---\n','')
	else:
		imputtrim = key.replace('---begin monRSA public key ---\n','').replace ('\n---end monRSA key ---\n','')
	print(imputtrim)
	
	imput = base64.b64decode(imputtrim.encode('utf-8', "ignore"))
	print(imput)
	a,b =imput.decode('utf-8',"ignore").split("\n")
	print (a)
	print (b)
	print ("en nombre")
	print (int (a,0))
	print (int (b,0))   
	
	return (int (a,0),int (b,0))

def getKey(key,cletype):
	if cletype == "pub":
		return (10366967400304701187, 3041824717)
	else: 
		return (10366967400304701187, 1183037804013585925)

def getpeparetext(text,blocksize):
	preparedtext = [] 
	text = text.lower()
	LETTERS = {letter: str(index) for index, letter in enumerate(string.ascii_lowercase, start=1)} 
	numbers=''
	for character in text:
		if character in LETTERS:
			if int(LETTERS[character]) <10:
				numbers = numbers+"0"+LETTERS[character]
			else:
				numbers= numbers+LETTERS[character]
	print (numbers)
	if len(numbers) > blocksize:
		while len (numbers)>blocksize:
			preparedtext.insert(0,numbers[- blocksize:])
			numbers = numbers[:- blocksize]
	preparedtext.insert(0,numbers)
	print (str(numbers))
	return preparedtext

def gettext(text,blocksize,n,d):
	tab =[]
	textdechiffrer =""
	textfinal =""
	while len (text)>= blocksize:
		tab.append(text[0:blocksize])
		text = text[blocksize:]
		print(tab)
	for number in tab:
		textdechiffrer= textdechiffrer +str(int(number)^d%n)
	while len(textdechiffrer)>=2:
		textfinal = textfinal + chr(int(textdechiffrer[0:2]))
		textdechiffrer =textdechiffrer[2:]
	return textfinal