poule=int(input("poule : "))
chien=int(input("chien : "))
vache=int(input("vache : "))
ami=int(input("ami : "))
assert type(poule)==int,"poule doit etre un entier"
assert type(chien)==int,"chien doit etre un entier"
assert type(vache)==int,"vache doit etre un entier"
assert type(ami)==int,"ami doit etre un entier"
def amende(poule:int,chien:int,vache:int,ami:int)->int:
    point= poule+3*chien+5*vache+10*ami
    print("points perdu ",point)
    if point>=100:
        print("Plus de pint sur le permi")
    permi = point/100
    return 200*permi

somme= amende(poule,chien,vache,ami)
if somme == 0:
    print("Rien à payer")
else :
    print("Amande a payer : ",somme,"€")
