"entrez 0 pour stopper"
HT=float(input("prix hors taxe : "))
while (HT!=0):
    tva=20
    ttc=HT*1+(tva/100)
    print(ttc)
    HT=float(input("prix hors taxe : "))