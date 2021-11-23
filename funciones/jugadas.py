from statistics import mode

def pasar_a_lista(jug_Juga):
    m=[]
    for sublist in jug_Juga:
        for i in sublist:
            m.append(i)
    return m     

def borraCartaPalo(i,mm,pm,posibleJ):
    indice = mm.index(i+2)
    mm.remove(i+2)
    pm.pop(indice)
    posibleJ[i]=posibleJ[i]-1
    return mm,pm,posibleJ

def CualCartaMayor(posibleJ):
    for i in range(13):
        if posibleJ[i]==1:
            CartaMayor=i+2
    return CartaMayor

def revizaSiEscaleraReal(m):
    if ((m[0]==10) and (m[1]==11) and (m[2]==12) and (m[3]==13) and (m[4]==14)):
        return 1
    else:
        return 0


def revizaPoker(mm,pm,posibleJ):
    for i in range(2):
        cartasBorrar=1
        for i in range(13):
            if((posibleJ[i]>0) and (posibleJ[i]<4) and (cartasBorrar > 0)):
                borraCartaPalo(i,mm,pm,posibleJ)
                cartasBorrar=cartasBorrar-1
    return mm,pm

def revisaFull(mm,pm,posibleJ):
    if 1 in posibleJ:
        for i in range(2):
            cartasBorrar=1
            for i in range(13):
                if((posibleJ[i]>0) and (posibleJ[i]<2) and (cartasBorrar > 0)):
                    borraCartaPalo(i,mm,pm,posibleJ)
                    cartasBorrar=cartasBorrar-1
    else:
        for i in range(2):
            cartasBorrar=1
            for i in range(13):
                if((posibleJ[i]>0) and (posibleJ[i]<3) and (cartasBorrar > 0)):
                    borraCartaPalo(i,mm,pm,posibleJ)
                    cartasBorrar=cartasBorrar-1
    return mm,pm


def revizaColor(mm,pm):
    palos=['C','B','F','D']
    x=mode(pm)
    palos.remove(x)
    for i in range(2):
        if len(pm) > 5:
            for i in range(3):
                if palos[i] in pm:
                    indice = pm.index(palos[i])
                    pm.remove(palos[i])
                    mm.pop(indice)
    return mm,pm

def revizaColorCinco(mm,pm):
    for i in range(2):
        if len(pm) > 5:
            pm.pop(0)
            mm.pop(0)
    

def ocultaCartasRepetidas(posibleJ):
    axi=[]
    axi=posibleJ.copy()
    for i in range(2):
        cartasBorrar=1
        for i in range(13):
            if((axi[i]>1) and (axi[i]<4) and (cartasBorrar > 0)):
                axi[i]=axi[i]-1
                cartasBorrar=cartasBorrar-1    
    return axi


def SaloCinco(axi,cantidad):
    if(axi[12]==1 and axi[0]==1 and axi[1]==1 and axi[2]==1 and axi[3]==1 and axi[4]==0):
        for i in range(5,12):
            axi[i]=0
    else:
        if axi.count(1)>5:
            if axi[0]==1:
                if ((axi[1]==0) or (axi[2]==0) or (axi[2]==0)):
                    axi[0]=axi[0]-1
        if axi.count(1)>5:
            if axi[12]==1:
                if ((axi[11]==0) or (axi[10]==0) or (axi[9]==0) or (axi[8]==0)):
                    axi[12]=axi[12]-1
        for i in range(2):
            for i in range(2,13):
                if axi.count(1)>5:
                    if ((axi[i-2]==0) and (axi[i-1]==1)):
                        axi[i-1]=axi[i-1]-1
        for i in range(2):
            if axi.count(1)>5:
                indice = axi.index(1)
                axi[indice]=axi[indice]-1
 
def revizaSiEscalera(axi):
    indice = axi.index(1)
    fin=indice+5
    escalera=0
    cont=indice
    for i in range(indice,fin):
        if axi[cont]!=1:
            escalera=1
        cont=cont+1          
    if escalera==0:
        return 6
    if(axi[12]==1 and axi[0]==1 and axi[1]==1 and axi[2]==1 and axi[3]==1 and axi[4]==0):
        return 6  
    else:
        return 0


def masodeEscalera(mm,pm,axi,posibleJ):
    while len(mm) > 5:
        for i in range(13):
            if ((posibleJ[i]-axi[i])>=1):
                borraCartaPalo(i,mm,pm,posibleJ)
       
def reviza_un_trio(mm,pm,posibleJ):
    for i in range(2):
        cartasBorrar=1
        for i in range(13):
            if((posibleJ[i]>0) and (posibleJ[i]<3) and (cartasBorrar > 0)):
                borraCartaPalo(i,mm,pm,posibleJ)
                cartasBorrar=cartasBorrar-1
    if len(pm) > 5:
        pm.pop(0)
        mm.pop(0)
    return mm,pm  

def reviza_doblepareja(mm,pm,posibleJ):
    for i in range(2):
        cartasBorrar=1
        for i in range(13):
            if((posibleJ[i]>0) and (posibleJ[i]<2) and (cartasBorrar > 0)):
                borraCartaPalo(i,mm,pm,posibleJ)
                cartasBorrar=cartasBorrar-1
    if len(pm) > 5:
        pm.pop(0)
        mm.pop(0)
    return mm,pm

def reviza_pareja(mm,pm,posibleJ):
    for i in range(2):
        cartasBorrar=1
        for i in range(13):
            if((posibleJ[i]>0) and (posibleJ[i]<2) and (cartasBorrar > 0)):
                borraCartaPalo(i,mm,pm,posibleJ)
                cartasBorrar=cartasBorrar-1
    return mm,pm

def poker(mm,pm,mj,pj,numjugador):
    posibleJ=[]
    posi=[]
    posi2=[]
    Jugada=0
    puntos=0
    CualPareja1=0
    CualPareja2=0
    CartaMayor=0
    listaJugada=[]
    mm=mj+mm
    pm=pj+pm

    mm, pm = map(list, zip(*sorted(zip(mm, pm))))#Ordena la lista maso y palo 

    for i in range(2,15):
        posibleJ.append(mm.count(i))
        if (posibleJ[i-2]==4):
            Jugada=3
            CualPareja1=i
  
    if pm.count('C') >= 5 or pm.count('B') >= 5 or pm.count('F') >= 5 or pm.count('D') >= 5:
        noEntrar=0   #cuando es Escalera real devuelve 1
        if posibleJ.count(4)==1:
            noEntrar=1
        if (3 in posibleJ and 2 in posibleJ):
            noEntrar=1
        if posibleJ.count(3)==2:
            noEntrar=1
        if noEntrar==0:
            aximm=mm.copy()
            axipm=pm.copy()
            revizaColor(aximm,axipm)
            revizaColorCinco(aximm,axipm)
            Jugada=revizaSiEscaleraReal(aximm)
            if Jugada==1:
                mm=aximm.copy()
                pm=axipm.copy()
                nombreJugada="Escalera Real"
            else:
                aximm2=mm.copy()
                axipm2=pm.copy()
                revizaColor(aximm2,axipm2)
                for i in range(2,15):
                    posi.append(aximm2.count(i))
                if posi.count(1)>=5:
                    SaloCinco(posi,5)
                    Jugada=revizaSiEscalera(posi)
                if Jugada==6:#Caundo es escalera de Color
                    Jugada=2
                    masodeEscalera(mm,pm,posi,posibleJ)
                    CartaMayor = CualCartaMayor(posibleJ)
                    puntos=sum(mm)
                    nombreJugada="Escalera de Color"
                    
    if Jugada==3:#Cuando es Poker
        revizaPoker(mm,pm,posibleJ)
        CartaMayor = CualCartaMayor(posibleJ)
        puntos=sum(mm)
        nombreJugada="Poker"

    if (3 in posibleJ and 2 in posibleJ) and Jugada==0:#Hay que revizar cuando son 2 trios
        Jugada=4#cuando es un full
        revisaFull(mm,pm,posibleJ)
        CualPareja1=mode(mm)
        indice = posibleJ.index(2)
        CualPareja2 = indice+2
        puntos=sum(mm)
        nombreJugada="Ful"   

    if posibleJ.count(3)==2 and Jugada==0:
        Jugada=4#cuando es un full pero hay dos trios
        ind=posibleJ.index(3)
        posibleJ[ind]=posibleJ[ind]-1
        indice = posibleJ.index(1)
        indice2 = mm.index(indice+2)
        mm.remove(indice+2)
        pm.pop(indice2)
        mm.pop(0)
        pm.pop(0)
        CualPareja1=mode(mm)
        indice = posibleJ.index(2)
        CualPareja2 = indice+2
        puntos=sum(mm)
        nombreJugada="Ful" 
       
    if ((pm.count('C') >= 5 or pm.count('B') >= 5 or pm.count('F') >= 5 or pm.count('D') >= 5) and (Jugada ==0)):
        Jugada=5 #cuando es Color
        revizaColor(mm,pm)
        revizaColorCinco(mm,pm)
        puntos=sum(mm)
        CartaMayor = puntos
        nombreJugada="Color"

    if ((posibleJ.count(1)>=3) and (Jugada==0)):
        axi=ocultaCartasRepetidas(posibleJ)
        if axi.count(1)>=5:
            SaloCinco(axi,5)
            Jugada=revizaSiEscalera(axi)
        if Jugada==6:#Caundo es escalera
            masodeEscalera(mm,pm,axi,posibleJ)
            CartaMayor = CualCartaMayor(posibleJ)
            puntos=sum(mm)
            nombreJugada="Escalera"
        
    if 3 in posibleJ and Jugada==0:
        Jugada=7 #cuando es trio
        reviza_un_trio(mm,pm,posibleJ)
        CualPareja1=mode(mm)
        CartaMayor = CualCartaMayor(posibleJ)
        x=mode(mm)
        puntos=sum(mm)+(x*14)
        nombreJugada="Trio"

    if 2 in posibleJ and Jugada==0:
        if posibleJ.count(2)==2: 
            Jugada=8 #cuando hay doble pareja
            reviza_doblepareja(mm,pm,posibleJ)
        if posibleJ.count(2)==3:
            Jugada=8 #cuando hay tres pareja
            for i in range(2):
                pm.pop(0)
                mm.pop(0)
        if posibleJ.count(2)==1: #Solo hay una pareja
            Jugada=9 #cuando hay una pareja
            reviza_pareja(mm,pm,posibleJ)

    if Jugada==8:
        for i in range(2,15):
            posi2.append(mm.count(i))
        indice = posi2.index(2)
        CualPareja2 = indice+2
        posi2[indice]=posi2[indice]-1
        indice = posi2.index(2)
        CualPareja1 = indice+2
        CartaMayor = CualCartaMayor(posibleJ)
        puntos=sum(mm)
        nombreJugada="Doble pareja"

    if Jugada==9:
        indice = posibleJ.index(2)
        CualPareja1 = indice+2
        CartaMayor = CualCartaMayor(posibleJ)
        puntos=sum(mm)
        nombreJugada="Una pareja"   

    if posibleJ.count(1)==7 and Jugada==0:
        Jugada=10 #carta mayor
        reviza_pareja(mm,pm,posibleJ)
        CartaMayor = CualCartaMayor(posibleJ)
        puntos=sum(mm)
        nombreJugada="Carta Mayor"
           
    if Jugada>0:#si encuentra alguuna jugada devuelve los valores encontrados
        #listaJugada.extend(Jugada,puntos,nombreJugada,CualPareja1,CualPareja2,CartaMayor,numjugador)
        listaJugada.append(Jugada)
        listaJugada.append(puntos)
        listaJugada.append(nombreJugada)
        listaJugada.append(CualPareja1)
        listaJugada.append(CualPareja2)
        listaJugada.append(CartaMayor)
        listaJugada.append(numjugador)
        return listaJugada,mm,pm


    
