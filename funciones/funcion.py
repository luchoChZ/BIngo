import random
def crear_el_maso(maso,palo):
    cont=0
    for i in range(2,54):
        cont=cont+1
        if(cont <= 13):
            maso.append(i)
            palo.append('C')#Corazone "♥"
        if((cont > 13) and (cont <= 26)):
            maso.append(i-13)
            palo.append('B')#Bastos "♠"
        if((cont > 26) and (cont <= 39)):
            maso.append(i-26)
            palo.append('F')#Flores "♣"
        if((cont > 39) and (cont <= 53)):
            maso.append(i-39)
            palo.append('D')#Diamantes "♦"

def imprimir_maso(mm,pp):
    for i in mm:
        if (pp[i]=='C'):
            print(mm[i],"♥", end=" "),
        if (pp[i]=='B'):
            print(mm[i],"♠", end=" "),
        if (pp[i]=='F'):
            print(mm[i],"♣", end=" "),
        if (pp[i]=='D'):
            print(mm[i],"♦",end=" "),
    print("\n")


def traeNumero(mm,indice):
    num=mm[indice]
    if num > 10:
        if num==11:
            num="J"
        if num==12:
            num="Q"
        if num==13:
            num="K"
        if num==14:
            num="A"
    return num


def imprime(mm,pp,c):
    for i in range(c):
        numero=traeNumero(mm,i)
        if (pp[i]=='C'):
            print(numero,"♥", end=" "),
        if (pp[i]=='B'):
            print(numero,"♠", end=" "),
        if (pp[i]=='F'):
            print(numero,"♣", end=" "),
        if (pp[i]=='D'):
            print(numero,"♦", end=" "),
      

def imprimir_maso_j(mm,pp,c,lis_jugad,indice,njugada):
    if c== 5:
        print("Cartas en la Mesa")
        imprime(mm,pp,c)
        print("\n")
    if c== 2:
        print(lis_jugad[indice])
        imprime(mm,pp,c)
        print("\n")
    if c== 6:
        print("Mano de: ",lis_jugad[indice],"=", end=" "),
        c=c-1
        imprime(mm,pp,c)
        print("Tiene un :",njugada)







