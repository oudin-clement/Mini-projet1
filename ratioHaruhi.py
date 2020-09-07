p=68000
q=1800
n=3
liste=[[187000,15000],
[200,900],
[4200,100]]
ratioH=q/p
nban=0
for i in range(len(liste)):
    ratioan=liste[i][1]/liste[i][0]
    if ratioan>ratioH:
        nban+=1