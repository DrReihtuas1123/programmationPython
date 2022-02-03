from math import sqrt
nbre = int(input('Entrez un nombre entier : '))
print('Les diviseurs de', nbre, 'sont : ')
for i in range(1,int(sqrt(nbre))+1) :
    if nbre%i == 0 :
        print(i,int(nbre/i), end=" ")
