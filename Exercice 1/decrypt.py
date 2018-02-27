#between a and z
#no special characters, spaces, digits
#Vigenre Cipher
#Key between 1 and 80 in length
#Key only a-z

from collections import Counter

print("Launch decrypt")

cipher = open("cipher", "r").read()
splittedCipher = []

nbOccurencesParTaille = [] #Indice = Taille de split
nbOccurencesMaximal= [] #Indice = Taille de split
rationbOccurences = [] #Indice = Taille de split

#For each key length possible
for i in range(1,80):
    dicoMotifOccurences = {}
    splittedCipher = []

    #We split the cipher into chunk of len(k)
    for j in range(0, len(cipher), i):
        splittedCipher.append(cipher[j:j + i])

    #We count the nb of each occurence
    dicoMotifOccurences = Counter(splittedCipher)

    #We store this nb of occurence, the maximum number of different motif
    nbOccurencesParTaille.append(len(dicoMotifOccurences))
    nbOccurencesMaximal.append(len(cipher) / i)
    rationbOccurences.append(nbOccurencesParTaille[i - 1] / nbOccurencesMaximal[i - 1])

for i in range(1,len(rationbOccurences)):
    print("Keylength = " + str(i) + " : " + str(rationbOccurences[i]))
#15 et 39

#d = {}
#d['cle'] = 'valeur'
#d['cle'] = 'valeur'
