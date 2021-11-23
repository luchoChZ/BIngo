def nombredejugador(j,jugador,n):
    j[6]=jugador[n]

def revizaGanador(j1,j2):
    if j1[0] < j2[0]:
        return j1
    if j1[0] > j2[0]:
        return j2
    else:
        if j1[3] > j2[3]:
            return j1
        if j1[3] < j2[3]:
            return j2
        else:
            if j1[4] > j2[4]:
                return j1
            if j1[4] < j2[4]:
                return j2
            else:
                if j1[5] > j2[5]:
                    return j1
                if j1[5] < j2[5]:
                    return j2
                else:
                    j1[6]= j1[6]+" y "+j2[6]
                    return j1
      
def quienGana(j1,j2,j3,j4,jugadores,num):
    if num>=2:
        nombredejugador(j1,jugadores,0)
        nombredejugador(j2,jugadores,1)
        j1=revizaGanador(j1,j2)
    if num>=3:
        nombredejugador(j3,jugadores,2)
        j1=revizaGanador(j1,j3)
    if num>=4:
        nombredejugador(j4,jugadores,3)
        j1=revizaGanador(j1,j4)

    print("El ganador es: ", j1[6])




    
