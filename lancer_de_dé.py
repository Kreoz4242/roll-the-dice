#Import====================
import random
import os

#set value====================
nbd = int(input("entrez votre nombre de dé: "))
nbf = int(input("entrez un nombre de faces: "))
somme = 0
ListePlace = 0

#set list====================
ListeDe = []

#lancement de dé====================
for i in range(nbd):
    lancer = random.randint(1, nbf)
    ListeDe.append(lancer)

#clear====================
os.system("cls")

#print l'interieur de la liste ListePlace====================
print("Les dés sont: ", end="")
for i in range(nbd):
    print(ListeDe[int(ListePlace)], end=" ")
    ListePlace += 1

#print de la somme des dés====================
ListePlace = 0

for i in range(nbd):
    somme += ListeDe[int(ListePlace)]
    ListePlace += 1

print("\nLa somme des dés est de {}".format(somme))