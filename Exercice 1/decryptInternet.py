# between a and z
# no special characters, spaces, digits
# Vigenre Cipher
# Key between 1 and 80 in length
# Key only a-z

from collections import Counter
import string
import operator

print("Launch decrypt")

##### DATA
cipher = open("cipher", "r").read()
coincidenceTragetIndice = 0.0667
alphabet = list(string.ascii_lowercase)


def cesar(chaine, dec):
    alph = string.ascii_uppercase
    s = chaine.upper()
    return s.translate(str.maketrans(alph, alph[dec:] + alph[:dec]))


def testetout(chaine):
    for i in range(1, 26):
        print(i, cesar(chaine, -i))


def frequences(chaine):
    freq = [0] * 26
    for c in chaine:
        if c in string.ascii_uppercase:
            freq[ord(c) - ord('A')] += 1
        somme = sum(freq)
        freq = [v / somme * 1000.0 for v in freq]
        return freq


def cherche_cle_cesar(chaine):
    francais = [942, 102, 264, 339, 1587, 95, 104, 77, 841, 89, 0, 534, 324, 715, 514, 286, 106, 646, 790, 726, 624,
                215, 0, 30, 24, 32]
    corr = [0] * 26
    for dec in range(26):
        res = frequences(cesar(chaine, -dec))
        corr[dec] = sum(a * b for a, b in zip(res, francais))
    return corr.index(max(corr))


def autocesar(chaine):
    cle = cherche_cle_cesar(chaine)
    print("Clé : ", cle)
    return cesar(chaine, -cle)

def cherche_cle_vigenere(chaine,n) :
    return "".join( chr(ord('A')+cherche_cle_cesar(chaine[i::n])) for i in range(n))

def apparitions(chaine) :
    app = [0] * 26
    for c in chaine :
        if c in list(string.ascii_uppercase) :
            app[ord(c) - ord('A')] += 1
    return app

def indice_coincidence(chaine) :
    app = apparitions(chaine)
    s = sum (n*(n-1) for n in app)
    somme = sum(app)
    return s / (somme*(somme-1))



def liste_indices(chaine, n):
    res = [0]
    for i in range(1, n + 1):
        res.append(sum(indice_coincidence(chaine[k::i]) for k in range(i)))
        res[-1] /= i
    return res


def cherche_longueur_cle(chaine, seuil=0.0500, nmax=12):
    p=[]
    for lcle, i in enumerate(liste_indices(chaine, nmax)):
        if i > seuil:
            p.append((lcle, i))

    return min(p)

def dechiffre_vigenere(s,cle) :
    l=[]
    for i,c in enumerate(s) :
        if c in string.ascii_uppercase :
            c = ord(c)- ord(cle[i%len(cle)])
            c = chr(c % 26 + ord('A'))
        l.append(c)
    return "".join(l)

def dechiffre_vigenere(s,cle) :
    l=[]
    for i,c in enumerate(s) :
        if c in string.ascii_uppercase :
            c = ord(c)- ord(cle[i%len(cle)])
            c = chr(c % 26 + ord('A'))
        l.append(c)
    return "".join(l)


def vigenere_automatique(chaine) :
    lgcle,indice = cherche_longueur_cle(chaine)
    cle = cherche_cle_vigenere(chaine,lgcle)
    return dechiffre_vigenere(chaine,cle)

vigenere_automatique(cipher.upper())
cherche_longueur_cle(cipher)
