def menu(jugadores):
    print("****************************************************")
    print("                   Bienvenido ")
    print("                 Juego de Póker ")
    print("")
    print("          Seleccione la cantidad de Jugadores ")
    print("")
    print("          Presione")
    print("          2 Dos Jugadores")
    print("          3 Tres Jugadores")
    print("          4 Cuatro Jugadores")
    print("")
    print("****************************************************")
    jugadores = int(input("Digite un número:  "))
    return jugadores

#Lista de jugadores
def nombre_jugadores(lis_jugad,num):
    for i in range(num):
        lis_jugad.append(input("Escriba el Nombre del Jugador  "))
    return lis_jugad

#Reparte cartas a los jugadores y la mesa
def Rep_cartas(maso,palo,m,c):
    for i in range(c):
        m.append(maso.pop())
        m=list(m)
    return m

#Reparte palos a los jugadores y la mesa
def Rep_palos(maso,palo,p,c):
    for i in range(c):
        p.append(palo.pop())
        p=list(p)
    return p
