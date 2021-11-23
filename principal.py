import random
import os
import time
from funciones import funcion as f
from funciones import Inicio
from funciones import jugadas
from funciones import ganador as g

#Variables
maso=[]
palo=[]
mJ1= []
mJ2=[]
mJ3=[]
mJ4=[]
pJ1=[]
pJ2=[]
pJ3=[]
pJ4=[]
masoMesa=[]
paloMesa=[]
jugadores=0
lis_jugad=[]
num=0
jugadasJ1=[]
jugadasJ2=[]
jugadasJ3=[]
jugadasJ4=[]

#Crea el maso y lo baraja
f.crear_el_maso(maso,palo)
for i in range(3):
    mapIndexPosition = list(zip(maso, palo))
    random.shuffle(mapIndexPosition)
    maso, palo = zip(*mapIndexPosition)
maso=list(maso)
palo=list(palo)

#num=4#borrar
#Preguntar cantidad de Jugadores
while (num<2) or (num>4):
    try:
        num=Inicio.menu(jugadores)
    except ValueError:
        print("Solo Número Enteros")
    if(num<2) or (num>4):
        print("Solo Números entre 2 y 4")
    if ValueError== True:
        num=1

Inicio.nombre_jugadores(lis_jugad,num)

#Repartir Cartas a los jugadores
if num >= 2:
    mJ1=Inicio.Rep_cartas(maso,palo,mJ1,2)        
    pJ1=Inicio.Rep_palos(maso,palo,pJ1,2)
    mJ2=Inicio.Rep_cartas(maso,palo,mJ2,2)        
    pJ2=Inicio.Rep_palos(maso,palo,pJ2,2)  
    f.imprimir_maso_j(mJ1,pJ1,2,lis_jugad,0,0)  #f.imprimir_maso_j Parametros = maso,palo,cantidad de cartas,nombre de jugados, numero de jugador, nombre de jugada
    f.imprimir_maso_j(mJ2,pJ2,2,lis_jugad,1,0) 
if num >= 3:
    mJ3=Inicio.Rep_cartas(maso,palo,mJ3,2)        
    pJ3=Inicio.Rep_palos(maso,palo,pJ3,2)   
    f.imprimir_maso_j(mJ3,pJ3,2,lis_jugad,2,0)
if num >= 4:
    mJ4=Inicio.Rep_cartas(maso,palo,mJ4,2)        
    pJ4=Inicio.Rep_palos(maso,palo,pJ4,2)
    f.imprimir_maso_j(mJ4,pJ4,2,lis_jugad,3,0)
    
#Repartir Cartas en la mesa
masoMesa=Inicio.Rep_cartas(maso,palo,masoMesa,5)        
paloMesa=Inicio.Rep_palos(maso,palo,paloMesa,5)
f.imprimir_maso_j(masoMesa,paloMesa,5,lis_jugad,5,0)

#Revisar Jugadas 
if num >= 2:
    jugadasJ1=jugadas.poker(masoMesa,paloMesa,mJ1,pJ1,0)     
    if jugadasJ1:
        jugadasJ1=jugadas.pasar_a_lista(jugadasJ1)
        f.imprimir_maso_j(jugadasJ1[7:12],jugadasJ1[12:18],6,lis_jugad,0,jugadasJ1[2])
    jugadasJ2=jugadas.poker(masoMesa,paloMesa,mJ2,pJ2,1)
    if jugadasJ2:
        jugadasJ2=jugadas.pasar_a_lista(jugadasJ2)
        f.imprimir_maso_j(jugadasJ2[7:12],jugadasJ2[12:18],6,lis_jugad,1,jugadasJ2[2])
if num >= 3:
    jugadasJ3=jugadas.poker(masoMesa,paloMesa,mJ3,pJ3,2)
    if jugadasJ3:
        jugadasJ3=jugadas.pasar_a_lista(jugadasJ3)
        f.imprimir_maso_j(jugadasJ3[7:12],jugadasJ3[12:18],6,lis_jugad,2,jugadasJ3[2])    
if num >= 4:
    jugadasJ4=jugadas.poker(masoMesa,paloMesa,mJ4,pJ4,3)
    if jugadasJ4:
        jugadasJ4=jugadas.pasar_a_lista(jugadasJ4)
        f.imprimir_maso_j(jugadasJ4[7:12],jugadasJ4[12:18],6,lis_jugad,3,jugadasJ4[2])        

g.quienGana(jugadasJ1,jugadasJ2,jugadasJ3,jugadasJ4,lis_jugad,num)


print("___Fin__")












