from math import sqrt
error = True
while error != False :
    try :
        nbre = int(input('Entrez un nombre entier positif : '))
    except :
        print('Vous êtes un benêt au cube!')
    else :
        error = False
        prem = True
        for i in range(2,int(sqrt(nbre)+1)) :
            if nbre%i == 0 :
                prem = False
        if prem == True and nbre != 1 :
            print(nbre, 'est premier')
        else :
            print(nbre, "n'est pas premier")
