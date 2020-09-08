from random import*

n=randint(1,100)
reponse=""
essai=0
while reponse!=n:
    reponse=int(input("->"))
    if reponse > n:
        print("trop grand!")
    else:
        print("trop petit!")
    essai+=1
print("gagné en ",essai," coups")