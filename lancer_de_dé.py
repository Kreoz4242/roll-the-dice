#Import====================
import random
import os

#set value====================
nbd = int(input("enter your number of dice: "))
nbf = int(input("enter a number of faces: "))
somme = 0
ListePlace = 0

#set list====================
ListeDe = []

#roll the dice====================
for i in range(nbd):
    lancer = random.randint(1, nbf)
    ListeDe.append(lancer)

#clear====================
os.system("cls")

#print in the list ListePlace====================
print("dice: ", end="")
for i in range(nbd):
    print(ListeDe[int(ListePlace)], end=" ")
    ListePlace += 1

#print the sum of the dice====================
ListePlace = 0

for i in range(nbd):
    somme += ListeDe[int(ListePlace)]
    ListePlace += 1

print("\nThe sum of the dice is {}".format(somme))
