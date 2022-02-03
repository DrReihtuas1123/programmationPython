from math import pi
def a( ) :
    r = int(input('Entrez le rayon du cercle : '))
    A = pi * r**2
    P = 2*pi*r
    print('Aire :',A, '; Perimètre : ',P)

def b() :
    x = input('entrez un premier mot : ')
    y = input('entrez un deuxième mot : ')
    print(x,y)

def c() :
    x = int(input('entrez un premier nombre : '))
    y = int(input('entrez un deuxième nombre : '))
    somme = x + y
    produit = x*y
    print(x, '+', y, '=' , somme, 'et', x, '*', y, '=', produit)

def d() :
    x = float(input('entrez un premier nombre : '))
    y = float(input('entrez un deuxième nombre : '))
    somme = x + y
    produit = x + y
    print(x, '+', y, '=' , '%.4f', 'et', x, '*', y, '=', '%.4f' %somme,produit)

d()
