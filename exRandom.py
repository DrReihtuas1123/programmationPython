from random import randint
compteur = 0
nmax = int(input('Entrez la limite : '))
for i in range(0,nmax) :
    if randint(1,6) == 6 :
        compteur +=1
print(compteur/nmax*100, '%')
