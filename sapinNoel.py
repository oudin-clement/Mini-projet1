nbligne=int(input("nombre de ligne : "))

sapin="^"

for i in range(0,nbligne):
    espace=""
    for y in range(i,nbligne):
        espace+=" "
    sapinnoel=espace+sapin
    print(sapinnoel)
    sapin+="^^"
    sapinnoel=""