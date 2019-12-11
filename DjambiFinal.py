import os
clear = lambda: os.system('cls')
vertical=0
horizontal=0
diagonal=0
cs=0
turnos = 1
terminar = 0
poder=0
contadorpoder=0
contadorturnos=1
r=0
piezas=0
ola=0
niuna=0
sig=0
casilla1=0
casilla2=0
casilla3=0
casilla4=0
casilla5=0
casilla6=0
casilla7=0
casilla8=0
primerturno=0
clc=0
abc=0
capturarrey=0
necroc=0
m1=0
m2=0
m3=0
m4=0
'''
MMN
RPM
LAM
 
112
341
561
 
1 = Militante
2 = Necromovil
3 = Reportero
4 = Provocador
5 = Lider
6 = Asesino
 
 
 
 
'''
'''
Inicio del menu
'''
print("     Bienvenido a Djambi.\n")
def impresion_pantalla():
    print(r"""
____   _                 _     _ 
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/                         

""")


def mensaje_salida():
    input("\nPresione la tecla intro para continuar...")
    clear()


tablero=[]
 
for y in range (0,11):
      
   tablero.append([00]*11)

#coordenadas
tablero[0][0]=0
tablero[0][1]=1
tablero[0][2]=2
tablero[0][3]=3
tablero[0][4]=4
tablero[0][5]=5
tablero[0][6]=6
tablero[0][7]=7
tablero[0][8]=8
tablero[0][9]=9


tablero[1][0]=1
tablero[2][0]=2
tablero[3][0]=3
tablero[4][0]=4
tablero[5][0]=5
tablero[6][0]=6
tablero[7][0]=7
tablero[8][0]=8
tablero[9][0]=9

tablero[0][10]=10
tablero[1][10]=10
tablero[2][10]=10
tablero[3][10]=10
tablero[4][10]=10
tablero[5][10]=10
tablero[6][10]=10
tablero[7][10]=10
tablero[8][10]=10
tablero[9][10]=10
tablero[10][10]=10

tablero[10][0]=10
tablero[10][1]=10
tablero[10][2]=10
tablero[10][3]=10
tablero[10][4]=10
tablero[10][5]=10
tablero[10][6]=10
tablero[10][7]=10
tablero[10][8]=10
tablero[10][9]=10

      
#Piezas jugador 1
tablero[1][1]=511
tablero[1][2]=610
tablero[1][3]=111
tablero[2][1]=310
tablero[2][2]=410
tablero[2][3]=111
tablero[3][1]=111
tablero[3][2]=111
tablero[3][3]=211
 
#Piezas jugador 2
tablero[3][4]=121
tablero[1][8]=621
tablero[1][9]=521
tablero[2][7]=121
tablero[2][8]=421
tablero[2][9]=321
tablero[3][7]=221
tablero[3][8]=121
tablero[3][9]=121
 
#Piezas jugador 3
tablero[7][1]=131
tablero[7][2]=131
tablero[7][3]=231
tablero[8][1]=331
tablero[8][2]=431
tablero[8][3]=131
tablero[9][1]=531
tablero[9][2]=631
tablero[9][3]=131

 
#Piezas jugador 4
tablero[7][7]=241
tablero[7][8]=141
tablero[7][9]=141
tablero[8][7]=141
tablero[8][8]=441
tablero[8][9]=341
tablero[9][7]=141
tablero[9][8]=641
tablero[9][9]=541
#MOVIMIENTO DE MILITANTE
impresion_pantalla()
print("Objetivo:\nCapturar a los demás líderes enemigos con el uso de las diferentes piezas.\n")
print("Movimientos:\nCada jugador moverá una de sus piezas en su turno, con la posibilidad de capturar en este movimiento a una ficha contraria. \nNinguna ficha puede desplazarse a través de una casilla ocupada por otra ficha (viva o capturada).\n")
print("Capturas:\nPara capturar una pieza enemiga, el usuario debe mover una de sus piezas con capacidad de captura a una casilla en la cual pueda capturar una pieza enemiga. Cada pieza captura de manera distinta, lo cual se explicará a detalle más adelante. \n")
mensaje_salida()
impresion_pantalla()
print("La letra M en el tablero representa a los Militantes, hay 4 militantes por equipo.\nLos militantes pueden moverse en una de las direcciones marcadas, con un máximo de 2 casillas.\nNo pueden capturar al líder. \nEl militante marcado de color amarillo muestra los posibles movimientos de un militante.")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==1):
            if(x==1 and y==3):
                print("\033[1;33;40m M", end ="")
                r=1
            elif(color==1 and status==1):
                print("\033[1;34;40m M", end ="")
            elif (color==1 and status==1 and x !=1 and x!=2):
                print("\033[1;37;40m 0", end ="")
            elif (color==1 and status==1 and x !=1 and y!=1):
                print("\033[1;36;40m 0", end ="")    
            elif(color==2 and status==1):
                print ("\033[1;37;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;37;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;37;40m 0", end ="")
            elif(status==0):
                print ("\033[1;35;40m M", end ="") 
        elif(r==0 and  x==2 and y==2 or x==2 and y==4 or x==3 and y==5 ):        
             print ("\033[1;36;40m 0", end ="")    
        elif((x==1 and y==1)or(x==1 and y==2) or(x==1 and y==4) or(x==1 and y==5) or(x==2 and y==3) or(x==2 and y==2)):    
             print ("\033[1;36;40m 0", end ="")               
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=1 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
         
        
              
    print("\033[1;37;40m\n")
mensaje_salida()
#MOVIMIENTO DE LIDER
impresion_pantalla()
print("La letra L en el tablero representa a los líderes.\nLos líderes pueden moverse en una de las direcciones marcadas, con un máximo de 8 casillas. \n")
print("El líder es la pieza más importante de Djambi, ya que tiene la capacidad de ocupar la casilla central, lo que le permite al jugador volver a hacer un movimiento después del turno de cada uno de sus adversarios. \n ")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==5):
            if (color==1 and status==1):
                print("\033[1;34;40m L", end ="")
            elif(color==2 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;36;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(status==0):
                print ("\033[1;37;40m 0", end ="")
        elif(x==1 and y>1 and y<10):   
            print("\033[1;36;40m 0", end="")
        elif(y==1 and x>1 and x<10):   
            print("\033[1;36;40m 0", end="") 
        elif(x==y and x>1):
            print("\033[1;36;40m 0", end="")                 
        elif (x==5 and y==5):
            print ("\033[1;36;40m ", end="")
        elif (pieza!=5 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\033[1;37;40m\n")
mensaje_salida()
#MOVIMIENTO DE ASESINO
impresion_pantalla()
print("La letra A en el tablero representa a los asesinos.\nLos asesinos pueden moverse en una de las direcciones marcadas, con un máximo de 8 casillas.\nCuando un asesino captura una pieza, se ve obligado a mover a dicha pieza a la posición en la que el asesino se encontraba antes de realizar la captura.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==6):
            if (color==1 and status==1):
                print("\033[1;34;40m A", end ="")
            elif(color==2 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;36;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;37;40m 0", end ="")
            elif(status==0):
                print ("\033[1;35;40m 0", end ="")
        elif(x==1 and y==0 or x==0 and y==1):
            print("\033[1;37;40m",tablero[x][y], end="")    
        elif((x==2 and y==1) or (x+1==y)):
            print("\033[1;36;40m 0", end="")                
        elif(x==1 and y>1 and y<10):   
            print("\033[1;36;40m 0", end="")
        elif(y==2 and x>1 or (x<2 and x>0)):   
            print("\033[1;36;40m 0", end="")            
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=6 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\033[1;37;40m\n")
mensaje_salida()
#MOVIMIENTO DE NECROMÓVIL
impresion_pantalla()
print("La letra N en el tablero representa a los necromóviles.\nLos necromóviles pueden moverse en una de las direcciones marcadas, con un máximo de 8 casillas.\nLos necromóviles no pueden capturar piezas, pero pueden mover piezas enemigas previamente capturadas a una casilla vacia, excepto la central.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==2):
            if (color==1 and status==1):
                print("\033[1;34;40m N", end ="")
            elif(color==2 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;36;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(status==0):
                print ("\033[1;35;40m N", end ="")
        elif(x==2 and y==4 or x==1 and y==5 or x==4 and y==2 or x==5 and y==1):
            print ("\033[1;36;40m 0", end ="")        
        elif(x==y and x>0):
            print ("\033[1;36;40m 0", end ="")
        elif(x==3 and x>0 and y>0):
            print ("\033[1;36;40m 0", end ="")
        elif(y==3 and y>0 and x>0):
            print ("\033[1;36;40m N", end ="")                    
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=2 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\033[1;37;40m\n")
mensaje_salida()
#MOVIMIENTO DE reportero
impresion_pantalla()
print("La letra R en el tablero representa a los reporteros.\nLos reporteros pueden moverse en una de las direcciones marcadas, con un máximo de 8 casillas.\nLos reporteros solo pueden capturar piezas adyacentes a ellos, de manera horizontal o vertical, pero nunca en diagonal.\nLa pieza capturada no se mueve de lugar.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==3):
            if (color==1 and status==1):
                print("\033[1;34;40m R", end ="")
            elif(color==2 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;36;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;37;40m 0", end ="")
            elif(status==0):
                print ("\033[1;35;40m 0", end ="")  
        elif(x==1 and y==2 or (x-1==y and x>1)):
            print ("\033[1;36;40m 0", end ="")

        elif(y==1 and x>0):
            print ("\033[1;36;40m 0", end ="")
        elif(x==2 and y>0):
            print ("\033[1;36;40m 0", end ="")              
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=3 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\033[1;37;40m\n")
mensaje_salida()
#MOVIMIENTO DE provocador
impresion_pantalla()
print("La letra P en el tablero representa a los provocadores.\nLos provocadores pueden moverse en una de las direcciones marcadas, con un máximo de 8 casillas.\nLos provocadores no pueden capturar piezas, pero pueden mover piezas enemigas que no han sido capturadas a cualquier casilla vacia, excepto la central.\n")
for x in range (0,10):
    for y in range (0,10):
        pieza=int(tablero[x][y]/100)   
        color=int((tablero[x][y]%100)/10)
        status=int(tablero[x][y]%10)
        if (pieza==4):
            if (color==1 and status==1):
                print("\033[1;34;40m P", end ="")
            elif(color==2 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(color==3 and status==1):
                print ("\033[1;36;40m 0", end ="")   
            elif(color==4 and status==1):
                print ("\033[1;36;40m 0", end ="")
            elif(status==0):
                print ("\033[1;35;40m 0", end ="") 
        elif(x==y and x>0 or x==1 and y==3 or x==3 and y==1):
            print ("\033[1;36;40m 0", end ="")          
        elif(x==2 and y>0 or y==2 and x>0):
            print ("\033[1;36;40m 0", end ="")         
        elif (x==5 and y==5):
            print ("\033[1;36;40m 0", end="")
        elif (pieza!=4 and pieza !=0):
            print ("\033[1;37;40m 0", end="")
        elif(pieza==0):  
            print("\033[1;37;40m",tablero[x][y], end="")  
           
        
              
    print("\033[1;37;40m\n")
mensaje_salida()
def actualizar():
    clear()
    print("\033[1;37;40m L = Líder. M = Militante. A = Asesino. R = Reportero. P = Provocador. N = Necromóvil.\nSolo se pueden ingresar números enteros del 1 al 9.\n")
    
    for x in range (0,10):
       for y in range (0,10):
           pieza=int(tablero[x][y]/100)   
           color=int((tablero[x][y]%100)/10)
           status=int(tablero[x][y]%10)
           if (pieza==1):
               if (color==1 and status==1):
                   print("\033[1;31;40m M", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;34;40m M", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m M", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m M", end ="")
               elif(status==0):
                   print ("\033[1;35;40m M", end ="")    
              
           elif (pieza==2):
               if (color==1 and status==1):
                   print("\033[1;31;40m N", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;34;40m N", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m N", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m N", end ="")
               elif(status==0):
                   print ("\033[1;35;40m N", end ="")    
           elif (pieza==3):
               if (color==1 and status==1):
                   print("\033[1;31;40m R", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;34;40m R", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m R", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m R", end ="")
               elif(status==0):
                   print ("\033[1;35;40m R", end ="")    
           elif (pieza==4):
               if (color==1 and status==1):
                   print("\033[1;31;40m P", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;34;40m P", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m P", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m P", end ="")
               elif(status==0):
                   print ("\033[1;35;40m P", end ="")    
           elif (pieza==5):
               if (color==1 and status==1):
                   print("\033[1;31;40m L", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;34;40m L", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m L", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m L", end ="")
               elif(status==0):
                   print ("\033[1;35;40m L", end ="")    
           elif (pieza==6):
               if (color==1 and status==1):
                   print("\033[1;31;40m A", end ="")
               elif(color==2 and status==1):
                   print ("\033[1;34;40m A", end ="")
               elif(color==3 and status==1):
                   print ("\033[1;33;40m A", end ="")   
               elif(color==4 and status==1):
                   print ("\033[1;32;40m A", end ="")
               elif(status==0):
                   print ("\033[1;35;40m A", end ="")    
           elif (x==5 and y==5):
               print ("\033[1;36;40m",tablero[x][y], end="")
           elif (pieza==0 and pieza!=10 ):
               print ("\033[1;37;40m",tablero[x][y], end="")
           
              
       print("\n")
    if(turnos==1):
      print("\033[1;31;40m Equipo ",turnos)
    elif(turnos==2):
      print("\033[1;34;40m Equipo ",turnos)
    elif(turnos==3):
      print("\033[1;33;40m Equipo ",turnos)
    elif(turnos==4):
      print("\033[1;32;40m Equipo ",turnos)


while(terminar == 0):
    #checar si un equipo tiene movimientos validos
    mov1=0
    mov2=0
    mov3=0
    mov4=0
    for x in range(1,10):
       for y in range(1,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(color==1 and mov1==0 and turnos==1):
             if(pieza==1 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov1=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov1=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov1=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov1=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov1=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov1=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov1=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov1=1
             if(pieza==2 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0 and tablero[x-1][y-1]%10==0)):
                   mov1=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0 and tablero[x-1][y]%10==0)):
                   mov1=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10 and tablero[x-1][y+1]%10==0)):
                   mov1=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0 and tablero[x][y-1]%10==0)):
                   mov1=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10 and tablero[x][y+1]%10==0)):
                   mov1=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0 and tablero[x+1][y-1]%10==0)):
                   mov1=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10 and tablero[x+1][y]%10==0)):
                   mov1=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10 and tablero[x+1][y+1]%10==0)):
                   mov1=1
             if(pieza==3 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0)):
                   mov1=1  
                elif((tablero[x-1][y]==0 and x-1>0)):
                   mov1=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10)):
                   mov1=1
                elif((tablero[x][y-1]==0 and y-1>0)):
                   mov1=1
                elif((tablero[x][y+1]==0 and y+1<10)):
                   mov1=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0)):
                   mov1=1
                elif((tablero[x+1][y]==0 and x+1<10)):
                   mov1=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10)):
                   mov1=1 
             if(pieza==4 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov1=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov1=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov1=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov1=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov1=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov1=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov1=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov1=1  
             if(pieza==5 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov1=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov1=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov1=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov1=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov1=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov1=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov1=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov1=1 
             if(pieza==6 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov1=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov1=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov1=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov1=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov1=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov1=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov1=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov1=1                            
          if(color==2 and mov2==0 and turnos==2):
             if(pieza==1 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov2=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov2=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov2=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov2=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov2=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov2=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov2=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov2=1
             if(pieza==2 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0 and tablero[x-1][y-1]%10==0)):
                   mov2=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0 and tablero[x-1][y]%10==0)):
                   mov2=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10 and tablero[x-1][y+1]%10==0)):
                   mov2=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0 and tablero[x][y-1]%10==0)):
                   mov2=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10 and tablero[x][y+1]%10==0)):
                   mov2=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0 and tablero[x+1][y-1]%10==0)):
                   mov2=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10 and tablero[x+1][y]%10==0)):
                   mov2=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10 and tablero[x+1][y+1]%10==0)):
                   mov2=1
             if(pieza==3 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0)):
                   mov2=1  
                elif((tablero[x-1][y]==0 and x-1>0)):
                   mov2=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10)):
                   mov2=1
                elif((tablero[x][y-1]==0 and y-1>0)):
                   mov2=1
                elif((tablero[x][y+1]==0 and y+1<10)):
                   mov2=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0)):
                   mov2=1
                elif((tablero[x+1][y]==0 and x+1<10)):
                   mov2=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10)):
                   mov2=1 
             if(pieza==4 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov2=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov2=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov2=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov2=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov2=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov2=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov2=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov2=1  
             if(pieza==5 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov2=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov2=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov2=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov2=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov2=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov2=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov2=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov2=1 
             if(pieza==6 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov2=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov2=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov2=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov2=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov2=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov2=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov2=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov2=1 
          if(color==3 and mov3==0 and turnos==3):
             if(pieza==1 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov3=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov3=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov3=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov3=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov3=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov3=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov3=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov3=1
             if(pieza==2 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0 and tablero[x-1][y-1]%10==0)):
                   mov3=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0 and tablero[x-1][y]%10==0)):
                   mov3=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10 and tablero[x-1][y+1]%10==0)):
                   mov3=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0 and tablero[x][y-1]%10==0)):
                   mov3=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10 and tablero[x][y+1]%10==0)):
                   mov3=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0 and tablero[x+1][y-1]%10==0)):
                   mov3=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10 and tablero[x+1][y]%10==0)):
                   mov3=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10 and tablero[x+1][y+1]%10==0)):
                   mov3=1
             if(pieza==3 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0)):
                   mov3=1  
                elif((tablero[x-1][y]==0 and x-1>0)):
                   mov3=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10)):
                   mov3=1
                elif((tablero[x][y-1]==0 and y-1>0)):
                   mov3=1
                elif((tablero[x][y+1]==0 and y+1<10)):
                   mov3=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0)):
                   mov3=1
                elif((tablero[x+1][y]==0 and x+1<10)):
                   mov3=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10)):
                   mov3=1 
             if(pieza==4 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov3=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov3=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov3=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov3=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov3=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov3=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov3=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov3=1  
             if(pieza==5 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov3=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov3=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov3=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov3=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov3=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov3=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov3=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov3=1 
             if(pieza==6 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov3=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov3=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov3=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov3=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov3=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov3=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov3=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov3=1
          if(color==4 and mov4==0 and turnos==4):
             if(pieza==1 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov4=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov4=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov4=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov4=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov4=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov4=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov4=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov4=1
             if(pieza==2 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0 and tablero[x-1][y-1]%10==0)):
                   mov4=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0 and tablero[x-1][y]%10==0)):
                   mov4=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10 and tablero[x-1][y+1]%10==0)):
                   mov4=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0 and tablero[x][y-1]%10==0)):
                   mov4=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10 and tablero[x][y+1]%10==0)):
                   mov4=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0 and tablero[x+1][y-1]%10==0)):
                   mov4=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10 and tablero[x+1][y]%10==0)):
                   mov4=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10 and tablero[x+1][y+1]%10==0)):
                   mov4=1
             if(pieza==3 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0)):
                   mov4=1  
                elif((tablero[x-1][y]==0 and x-1>0)):
                   mov4=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10)):
                   mov4=1
                elif((tablero[x][y-1]==0 and y-1>0)):
                   mov4=1
                elif((tablero[x][y+1]==0 and y+1<10)):
                   mov4=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0)):
                   mov4=1
                elif((tablero[x+1][y]==0 and x+1<10)):
                   mov4=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10)):
                   mov4=1 
             if(pieza==4 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov4=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov4=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov4=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov4=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov4=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov4=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov4=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov4=1  
             if(pieza==5 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov4=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov4=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov4=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov4=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov4=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov4=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov4=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov4=1 
             if(pieza==6 and status==1):
                if((tablero[x-1][y-1]==0 and x-1>0 and y-1>0) or (int((tablero[x-1][y-1]%100)/10!=color) and x-1>0 and y-1>0)):
                   mov4=1  
                elif((tablero[x-1][y]==0 and x-1>0) or (int((tablero[x-1][y]%100)/10!=color) and x-1>0)):
                   mov4=1
                elif((tablero[x-1][y+1]==0 and x-1>0 and y+1<10) or (int((tablero[x-1][y+1]%100)/10!=color) and x-1>0 and y+1<10)):
                   mov4=1
                elif((tablero[x][y-1]==0 and y-1>0) or (int((tablero[x][y-1]%100)/10!=color) and y-1>0)):
                   mov4=1
                elif((tablero[x][y+1]==0 and y+1<10) or (int((tablero[x][y+1]%100)/10!=color) and y+1<10)):
                   mov4=1
                elif((tablero[x+1][y-1]==0 and x+1<10 and y-1>0) or (int((tablero[x+1][y-1]%100)/10!=color) and x+1<10 and y-1>0)):
                   mov4=1
                elif((tablero[x+1][y]==0 and x+1<10) or (int((tablero[x+1][y]%100)/10!=color) and x+1<10)):
                   mov4=1
                elif((tablero[x+1][y+1]==0 and x+1<10 and y+1<10) or (int((tablero[x+1][y+1]%100)/10!=color) and x+1<10 and y+1<10)):
                   mov4=1      
    #si un equipo tiene 0 movimentos posibles matar la rey
    for x in range (0,10):
       for y in range (0,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(color==1 and pieza==5 and mov1==0 and status==1 and turnos==1):
             tablero[x][y]=tablero[x][y]-1
          if(color==2 and pieza==5 and mov2==0 and status==1 and turnos==2):
             tablero[x][y]=tablero[x][y]-1
          if(color==3 and pieza==5 and mov3==0 and status==1 and turnos==3):
             tablero[x][y]=tablero[x][y]-1
          if(color==4 and pieza==5 and mov4==0 and status==1 and turnos==4):
             tablero[x][y]=tablero[x][y]-1         
    
    #checar que ningue rey este encerrado por piezas capturadas y no tenga necromovil
    for x in range (0,10):
       for y in range (0,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(color==1 and pieza==2):
             necro1=int(tablero[x][y]%10)
          if(color==2 and pieza==2):
             necro2=int(tablero[x][y]%10)
          if(color==3 and pieza==2):
             necro3=int(tablero[x][y]%10)
          if(color==4 and pieza==2):
             necro4=int(tablero[x][y]%10)  
    casilla1=0
    casilla2=0
    casilla3=0
    casilla4=0
    casilla5=0
    casilla6=0
    casilla7=0
    casilla8=0              
    for x in range (0,10):
       for y in range (0,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          casilla1=0
          casilla2=0
          casilla3=0
          casilla4=0
          casilla5=0
          casilla6=0
          casilla7=0
          casilla8=0 
          if(color==1 and pieza==5 and necro1==0 and status==1):
             if((tablero[x-1][y-1]!=0 and tablero[x-1][y-1]%10==0) or x-1<1 or y-1<1):
                casilla1=1
             if((tablero[x-1][y]!=0 and tablero[x-1][y]%10==0) or x-1<1):   
                casilla2=1
             if((tablero[x-1][y+1]!=0 and tablero[x-1][y+1]%10==0) or x-1<1 or y+1>9):   
                casilla3=1   
             if((tablero[x][y-1]!=0 and tablero[x][y-1]%10==0) or y-1<1):   
                casilla4=1
             if((tablero[x][y+1]!=0 and tablero[x][y+1]%10==0) or y+1>9):   
                casilla5=1
             if((tablero[x+1][y-1]!=0 and tablero[x+1][y-1]%10==0) or y-1<1 or x+1>9):   
                casilla6=1 
             if((tablero[x+1][y]!=0 and tablero[x+1][y]%10==0) or x+1>9):   
                casilla7=1     
             if((tablero[x+1][y+1]!=0 and tablero[x+1][y+1]%10==0) or y+1>9 or x+1>9):   
                casilla8=1         
             if(casilla1+casilla2+casilla3+casilla4+casilla5+casilla6+casilla7+casilla8==8): 
                tablero[x][y]=tablero[x][y]-1
          casilla1=0
          casilla2=0
          casilla3=0
          casilla4=0
          casilla5=0
          casilla6=0
          casilla7=0
          casilla8=0       
          if(color==2 and pieza==5 and necro2==0 and status==1):
             if((tablero[x-1][y-1]!=0 and tablero[x-1][y-1]%10==0) or x-1<1 or y-1<1):
                casilla1=1
             if((tablero[x-1][y]!=0 and tablero[x-1][y]%10==0) or x-1<1):   
                casilla2=1
             if((tablero[x-1][y+1]!=0 and tablero[x-1][y+1]%10==0) or x-1<1 or y+1>9):   
                casilla3=1   
             if((tablero[x][y-1]!=0 and tablero[x][y-1]%10==0) or y-1<1):   
                casilla4=1
             if((tablero[x][y+1]!=0 and tablero[x][y+1]%10==0) or y+1>9):   
                casilla5=1
             if((tablero[x+1][y-1]!=0 and tablero[x+1][y-1]%10==0) or y-1<1 or x+1>9):   
                casilla6=1 
             if((tablero[x+1][y]!=0 and tablero[x+1][y]%10==0) or x+1>9):   
                casilla7=1     
             if((tablero[x+1][y+1]!=0 and tablero[x+1][y+1]%10==0) or y+1>9 or x+1>9):   
                casilla8=1              
             if(casilla1+casilla2+casilla3+casilla4+casilla5+casilla6+casilla7+casilla8==8): 
                tablero[x][y]=tablero[x][y]-1
          casilla1=0
          casilla2=0
          casilla3=0
          casilla4=0
          casilla5=0
          casilla6=0
          casilla7=0
          casilla8=0    
          if(color==3 and pieza==5 and necro3==0 and status==1):
             if((tablero[x-1][y-1]!=0 and tablero[x-1][y-1]%10==0) or x-1<1 or y-1<1):
                casilla1=1
             if((tablero[x-1][y]!=0 and tablero[x-1][y]%10==0) or x-1<1):   
                casilla2=1
             if((tablero[x-1][y+1]!=0 and tablero[x-1][y+1]%10==0) or x-1<1 or y+1>9):   
                casilla3=1   
             if((tablero[x][y-1]!=0 and tablero[x][y-1]%10==0) or y-1<1):   
                casilla4=1
             if((tablero[x][y+1]!=0 and tablero[x][y+1]%10==0) or y+1>9):   
                casilla5=1
             if((tablero[x+1][y-1]!=0 and tablero[x+1][y-1]%10==0) or y-1<1 or x+1>9):   
                casilla6=1 
             if((tablero[x+1][y]!=0 and tablero[x+1][y]%10==0) or x+1>9):   
                casilla7=1     
             if((tablero[x+1][y+1]!=0 and tablero[x+1][y+1]%10==0) or y+1>9 or x+1>9):   
                casilla8=1              
             if(casilla1+casilla2+casilla3+casilla4+casilla5+casilla6+casilla7+casilla8==8): 
                tablero[x][y]=tablero[x][y]-1
          casilla1=0
          casilla2=0
          casilla3=0
          casilla4=0
          casilla5=0
          casilla6=0
          casilla7=0
          casilla8=0    
          if(color==4 and pieza==5 and necro4==0 and status==1):
             if((tablero[x-1][y-1]!=0 and tablero[x-1][y-1]%10==0) or x-1<1 or y-1<1):
                casilla1=1
             if((tablero[x-1][y]!=0 and tablero[x-1][y]%10==0) or x-1<1):   
                casilla2=1
             if((tablero[x-1][y+1]!=0 and tablero[x-1][y+1]%10==0) or x-1<1 or y+1>9):   
                casilla3=1   
             if((tablero[x][y-1]!=0 and tablero[x][y-1]%10==0) or y-1<1):   
                casilla4=1
             if((tablero[x][y+1]!=0 and tablero[x][y+1]%10==0) or y+1>9):   
                casilla5=1
             if((tablero[x+1][y-1]!=0 and tablero[x+1][y-1]%10==0) or y-1<1 or x+1>9):   
                casilla6=1 
             if((tablero[x+1][y]!=0 and tablero[x+1][y]%10==0) or x+1>9):   
                casilla7=1     
             if((tablero[x+1][y+1]!=0 and tablero[x+1][y+1]%10==0) or y+1>9 or x+1>9):   
                casilla8=1              
             if(casilla1+casilla2+casilla3+casilla4+casilla5+casilla6+casilla7+casilla8==8): 
                tablero[x][y]=tablero[x][y]-1
    for x in range(1,10):
       for y in range(1,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(pieza==5 and color==1 and status==0 and m1==0):
             clear()
             print("El equipo rojo ha sido eliminado.\n")
             input("Presione en intro para continuar...")
             m1=1
          elif(pieza==5 and color==2 and status==0 and m2==0):
             clear()
             print("El equipo Azul ha sido eliminado.\n")
             input("Presione en intro para continuar...")
             m2=1
          elif(pieza==5 and color==3 and status==0 and m3==0):
             clear()
             print("El equipo Amarillo ha sido eliminado.\n")
             input("Presione en intro para continuar...")
             m3=1
          elif(pieza==5 and color==4 and status==0 and m4==0):
             clear()
             print("El equipo verde ha sido eliminado.\n")
             input("Presione en intro para continuar...")
             m4=1                 
                
    #checar si el rey esta vivo para turnos         
    actualizar()
    
    for x in range (0,10):
       for y in range (0,10):
           pieza=int(tablero[x][y]/100)   
           color=int((tablero[x][y]%100)/10)
           status=int(tablero[x][y]%10)
           if (pieza==5 and color==1):
              sr1=status
           if (pieza==5 and color==2):
              sr2=status
           if (pieza==5 and color==3):
              sr3=status
           if (pieza==5 and color==4):
              sr4=status    
    '''
    Aqui empieza turnos
    '''
    

    if (turnos == 1 and sr1==1):
        reiniciar = 0
        
        while(reiniciar == 0):
            reiniciar = 1
            ola=0
            while(ola==0):
               ola=1
               while True:
                  try:
                     inicio = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  print("",end="")
                  sig=1
                  niuna=0
               else:   
                  print("Debe ingresar un valor entre 1 y 9.") 
                  ola=0
                  sig=0
                  niuna=0
               if(sig==1):       
                  for z in range (1,10):
                     gg = int((tablero[inicio][z]%100)/10)
                     if(gg==turnos):
                        niuna=0
                        break   
                     else:
                        niuna=1
               if(niuna==1):
                  print("No tienes pieza en esa fila.")
                  ola=0      
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0  
            
            #checar si la pieza seleccionada tiene movimientos posibles 
            posp=0
            pieza=int(tablero[inicio][inicio2]/100) 
            status= int(tablero[inicio][inicio2]%10)
            color=turnos 
            if(pieza==1 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1
            if(pieza==2 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0 and tablero[inicio-1][inicio2-1]%10==0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0 and tablero[inicio-1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10 and tablero[inicio-1][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0 and tablero[inicio][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10 and tablero[inicio][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0 and tablero[inicio+1][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10 and tablero[inicio+1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10 and tablero[inicio+1][inicio2+1]%10==0)):
                   posp=1
            if(pieza==3 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(pieza==4 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==5 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==6 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(posp==0):
               print("La pieza seleccionada no tiene movimientos posibles.")
               reiniciar = 0
               
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("Ingrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("Ingrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            if(tablero[final][final2!=0]):
               br=(int(tablero[final][final2]%100)/10)
               if((br==1 and sr1==0) or (br==2 and sr2==0) or (br==3 and sr3==0) or (br==4 and sr4==0)):
                  print("No puedes capturar las piezas de un lider capturado")
                  reiniciar=1
            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(tablero[5][5]!=0 and int(tablero[inicio][inicio2]/100)==1 and final==5 and final2==5):
                print("Los militantes no pueden capturar a un lider si este se encuentra en la casilla central.")
                reiniciar = 1      
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5 and tablero[final][final2]==0):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden capturar piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                     
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                       
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey=0 
        if(tablero[final][final2]%10==1): 
            capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        necro=0
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           necro=1
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.") 
                 reiniciar=0    
                
           tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int(temporal/100)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           if(final==5 and final2==5 and int(tablero[5][5]/100)==5):
              clc=1
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar=1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 reiniciar=0

                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar = 1
              
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos")
                 reiniciar=0
              if(filam==5 and columnam ==5):
                 print("Las piezas muertas no pueden ocupar el centro.")
                 reiniciar=0
           if(reiniciar==1):     
              tablero[inicio][inicio2]=0 
              tablero[filam][columnam] = temporal
        #capturar con reportero
        repors=0
       
        if(tablero[final-1][final2]!=0 and final-1>0 and tablero[final-1][final2]%10==1 and int((tablero[final-1][final2]%100)/10)!=turnos):
           repors=1  
        if(tablero[final][final2-1]!=0 and final2-1>0 and tablero[final][final2-1]%10==1 and int((tablero[final][final2-1]%100)/10)!=turnos):
           repors=1
        if(tablero[final][final2+1]!=0 and final2+1<10 and tablero[final][final2+1]%10==1 and int((tablero[final][final2+1]%100)/10)!=turnos):
           repors=1               
        if(tablero[final+1][final2]!=0 and final+1<10 and tablero[final+1][final2]%10==1 and int((tablero[final+1][final2]%100)/10)!=turnos):
           repors=1
        
        if(pieza==3 and repors==1):
           actualizar()
           reiniciar==0         
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40m¿Desea capturar alguna pieza con el reportero? (1.-si 0.-no )   . \n"))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar números enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 ó 0.")
           
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero solo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(int((tablero[filam][columnam]%100)/10)==turnos):
                    print("No puedes capturar piezas de tu mismo equipo")      
                    reiniciar=0
                 if(int(tablero[filam][columnam]/100)==5 and filam==5 and columnam==5): 
                    capturarrey= tablero[filam][columnam]   
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal
        # si te comes un rey en el centro con otra pieza que no sea el rey 
        if(((int(tablero[5][5]/100)!=5) and int(tablero[5][5]/100)!=0) or (((int(tablero[x][y]/100)==5) and (int(tablero[x][y]%10))==0 )) and necroc==0):
           if(tablero[4][4]==0):
              tablero[4][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][5]==0):
              tablero[4][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][6]==0):
              tablero[4][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][4]==0):
              tablero[5][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][6]==0):
              tablero[5][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][4]==0):
              tablero[6][4]=tablero[5][5]
              tablero[5][5]=0  
           elif(tablero[6][5]==0):
              tablero[6][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][6]==0):
              tablero[6][6]=tablero[5][5]
              tablero[5][5]=0                   
        #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
            
           
           
           

    if (turnos == 2 and sr2==1):
        reiniciar = 0
        
        while(reiniciar == 0):
            reiniciar = 1
            ola=0
            while(ola==0):
               ola=1
               while True:
                  try:
                     inicio = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  print("",end="")
                  sig=1
                  niuna=0
               else:   
                  print("Debe ingresar un valor entre 1 y 9.") 
                  ola=0
                  sig=0
                  niuna=0
               if(sig==1):       
                  for z in range (1,10):
                     gg = int((tablero[inicio][z]%100)/10)
                     if(gg==turnos):
                        niuna=0
                        break   
                     else:
                        niuna=1
               if(niuna==1):
                  print("No tienes pieza en esa fila.")
                  ola=0      
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0  
            
            #checar si la pieza seleccionada tiene movimientos posibles 
            posp=0
            pieza=int(tablero[inicio][inicio2]/100) 
            status= int(tablero[inicio][inicio2]%10)
            color=turnos 
            if(pieza==1 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1
            if(pieza==2 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0 and tablero[inicio-1][inicio2-1]%10==0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0 and tablero[inicio-1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10 and tablero[inicio-1][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0 and tablero[inicio][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10 and tablero[inicio][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0 and tablero[inicio+1][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10 and tablero[inicio+1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10 and tablero[inicio+1][inicio2+1]%10==0)):
                   posp=1
            if(pieza==3 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(pieza==4 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==5 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==6 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(posp==0):
               print("La pieza seleccionada no tiene movimientos posibles.")
               reiniciar = 0
               
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("Ingrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("Ingrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            if(tablero[final][final2!=0]):
               br=(int(tablero[final][final2]%100)/10)
               if((br==1 and sr1==0) or (br==2 and sr2==0) or (br==3 and sr3==0) or (br==4 and sr4==0)):
                  print("No puedes capturar las piezas de un lider capturado")
                  reiniciar=1
            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(tablero[5][5]!=0 and int(tablero[inicio][inicio2]/100)==1 and final==5 and final2==5):
                print("Los militantes no pueden capturar a un lider si este se encuentra en la casilla central.")
                reiniciar = 1      
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5 and tablero[final][final2]==0):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden capturar piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                     
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                       
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey=0 
        if(tablero[final][final2]%10==1): 
            capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        necro=0
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           necro=1
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.") 
                 reiniciar=0    
                
           tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int(temporal/100)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           if(final==5 and final2==5 and int(tablero[5][5]/100)==5):
              clc=1
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar=1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 reiniciar=0

                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar = 1
              
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos")
                 reiniciar=0
              if(filam==5 and columnam ==5):
                 print("Las piezas muertas no pueden ocupar el centro.")
                 reiniciar=0
           if(reiniciar==1):     
              tablero[inicio][inicio2]=0 
              tablero[filam][columnam] = temporal
        #capturar con reportero
        repors=0
       
        if(tablero[final-1][final2]!=0 and final-1>0 and tablero[final-1][final2]%10==1 and int((tablero[final-1][final2]%100)/10)!=turnos):
           repors=1  
        if(tablero[final][final2-1]!=0 and final2-1>0 and tablero[final][final2-1]%10==1 and int((tablero[final][final2-1]%100)/10)!=turnos):
           repors=1
        if(tablero[final][final2+1]!=0 and final2+1<10 and tablero[final][final2+1]%10==1 and int((tablero[final][final2+1]%100)/10)!=turnos):
           repors=1               
        if(tablero[final+1][final2]!=0 and final+1<10 and tablero[final+1][final2]%10==1 and int((tablero[final+1][final2]%100)/10)!=turnos):
           repors=1
        
        if(pieza==3 and repors==1):
           actualizar()
           reiniciar==0         
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40m¿Desea capturar alguna pieza con el reportero? (1.-si 0.-no )   . \n"))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar números enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 ó 0.")
           
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero solo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(int((tablero[filam][columnam]%100)/10)==turnos):
                    print("No puedes capturar piezas de tu mismo equipo")      
                    reiniciar=0
                 if(int(tablero[filam][columnam]/100)==5 and filam==5 and columnam==5): 
                    capturarrey= tablero[filam][columnam]   
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal
        # si te comes un rey en el centro con otra pieza que no sea el rey 
        if(((int(tablero[5][5]/100)!=5) and int(tablero[5][5]/100)!=0) or (((int(tablero[x][y]/100)==5) and (int(tablero[x][y]%10))==0 )) and necroc==0):
           if(tablero[4][4]==0):
              tablero[4][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][5]==0):
              tablero[4][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][6]==0):
              tablero[4][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][4]==0):
              tablero[5][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][6]==0):
              tablero[5][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][4]==0):
              tablero[6][4]=tablero[5][5]
              tablero[5][5]=0  
           elif(tablero[6][5]==0):
              tablero[6][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][6]==0):
              tablero[6][6]=tablero[5][5]
              tablero[5][5]=0                   
        #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
                   
                   
                   
                   
    
    if (turnos == 3 and sr3==1):
        reiniciar = 0
        
        while(reiniciar == 0):
            reiniciar = 1
            ola=0
            while(ola==0):
               ola=1
               while True:
                  try:
                     inicio = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  print("",end="")
                  sig=1
                  niuna=0
               else:   
                  print("Debe ingresar un valor entre 1 y 9.") 
                  ola=0
                  sig=0
                  niuna=0
               if(sig==1):       
                  for z in range (1,10):
                     gg = int((tablero[inicio][z]%100)/10)
                     if(gg==turnos):
                        niuna=0
                        break   
                     else:
                        niuna=1
               if(niuna==1):
                  print("No tienes pieza en esa fila.")
                  ola=0      
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0  
            
            #checar si la pieza seleccionada tiene movimientos posibles 
            posp=0
            pieza=int(tablero[inicio][inicio2]/100) 
            status= int(tablero[inicio][inicio2]%10)
            color=turnos 
            if(pieza==1 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1
            if(pieza==2 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0 and tablero[inicio-1][inicio2-1]%10==0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0 and tablero[inicio-1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10 and tablero[inicio-1][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0 and tablero[inicio][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10 and tablero[inicio][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0 and tablero[inicio+1][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10 and tablero[inicio+1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10 and tablero[inicio+1][inicio2+1]%10==0)):
                   posp=1
            if(pieza==3 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(pieza==4 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==5 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==6 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(posp==0):
               print("La pieza seleccionada no tiene movimientos posibles.")
               reiniciar = 0
               
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("Ingrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("Ingrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            if(tablero[final][final2!=0]):
               br=(int(tablero[final][final2]%100)/10)
               if((br==1 and sr1==0) or (br==2 and sr2==0) or (br==3 and sr3==0) or (br==4 and sr4==0)):
                  print("No puedes capturar las piezas de un lider capturado")
                  reiniciar=1
            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(tablero[5][5]!=0 and int(tablero[inicio][inicio2]/100)==1 and final==5 and final2==5):
                print("Los militantes no pueden capturar a un lider si este se encuentra en la casilla central.")
                reiniciar = 1      
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5 and tablero[final][final2]==0):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden capturar piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                     
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                       
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey=0 
        if(tablero[final][final2]%10==1): 
            capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        necro=0
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           necro=1
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.") 
                 reiniciar=0    
                
           tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int(temporal/100)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           if(final==5 and final2==5 and int(tablero[5][5]/100)==5):
              clc=1
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar=1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 reiniciar=0

                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar = 1
              
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos")
                 reiniciar=0
              if(filam==5 and columnam ==5):
                 print("Las piezas muertas no pueden ocupar el centro.")
                 reiniciar=0
           if(reiniciar==1):     
              tablero[inicio][inicio2]=0 
              tablero[filam][columnam] = temporal
        #capturar con reportero
        repors=0
       
        if(tablero[final-1][final2]!=0 and final-1>0 and tablero[final-1][final2]%10==1 and int((tablero[final-1][final2]%100)/10)!=turnos):
           repors=1  
        if(tablero[final][final2-1]!=0 and final2-1>0 and tablero[final][final2-1]%10==1 and int((tablero[final][final2-1]%100)/10)!=turnos):
           repors=1
        if(tablero[final][final2+1]!=0 and final2+1<10 and tablero[final][final2+1]%10==1 and int((tablero[final][final2+1]%100)/10)!=turnos):
           repors=1               
        if(tablero[final+1][final2]!=0 and final+1<10 and tablero[final+1][final2]%10==1 and int((tablero[final+1][final2]%100)/10)!=turnos):
           repors=1
        
        if(pieza==3 and repors==1):
           actualizar()
           reiniciar==0         
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40m¿Desea capturar alguna pieza con el reportero? (1.-si 0.-no )   . \n"))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar números enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 ó 0.")
           
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero solo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(int((tablero[filam][columnam]%100)/10)==turnos):
                    print("No puedes capturar piezas de tu mismo equipo")      
                    reiniciar=0
                 if(int(tablero[filam][columnam]/100)==5 and filam==5 and columnam==5): 
                    capturarrey= tablero[filam][columnam]   
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal
        # si te comes un rey en el centro con otra pieza que no sea el rey 
        if(((int(tablero[5][5]/100)!=5) and int(tablero[5][5]/100)!=0) or (((int(tablero[x][y]/100)==5) and (int(tablero[x][y]%10))==0 )) and necroc==0):
           if(tablero[4][4]==0):
              tablero[4][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][5]==0):
              tablero[4][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][6]==0):
              tablero[4][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][4]==0):
              tablero[5][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][6]==0):
              tablero[5][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][4]==0):
              tablero[6][4]=tablero[5][5]
              tablero[5][5]=0  
           elif(tablero[6][5]==0):
              tablero[6][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][6]==0):
              tablero[6][6]=tablero[5][5]
              tablero[5][5]=0                   
        #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
                   
                   
        
    if(turnos == 4 and sr4==1):
        reiniciar = 0
        while(reiniciar == 0):
            reiniciar = 1
            ola=0
            while(ola==0):
               ola=1
               while True:
                  try:
                     inicio = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(inicio<10 and inicio>0):
                  print("",end="")
                  sig=1
                  niuna=0
               else:   
                  print("Debe ingresar un valor entre 1 y 9.") 
                  ola=0
                  sig=0
                  niuna=0
               if(sig==1):       
                  for z in range (1,10):
                     gg = int((tablero[inicio][z]%100)/10)
                     if(gg==turnos):
                        niuna=0
                        break   
                     else:
                        niuna=1
               if(niuna==1):
                  print("No tienes pieza en esa fila.")
                  ola=0      
            while True:
               while True:
                  try:
                     inicio2 = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que desea mover.\n"))
                     break
                  except ValueError:
                     print("Sólo numero enteros entre 1 y 9.")
                     
               if(inicio2<10 and inicio2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            
            if(tablero[inicio][inicio2]== 0):
              print("No hay pieza en ese lugar.")
              reiniciar = 0
            if(tablero[inicio][inicio2]%10==10):
               print("No puedes seleccionar piezas capturadas.")
               reiniciar=0  
            
            #checar si la pieza seleccionada tiene movimientos posibles 
            posp=0
            pieza=int(tablero[inicio][inicio2]/100) 
            status= int(tablero[inicio][inicio2]%10)
            color=turnos 
            if(pieza==1 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1
            if(pieza==2 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0 and tablero[inicio-1][inicio2-1]%10==0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0 and tablero[inicio-1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10 and tablero[inicio-1][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0 and tablero[inicio][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10 and tablero[inicio][inicio2+1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0 and tablero[inicio+1][inicio2-1]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10 and tablero[inicio+1][inicio2]%10==0)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10 and tablero[inicio+1][inicio2+1]%10==0)):
                   posp=1
            if(pieza==3 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(pieza==4 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==5 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1  
            if(pieza==6 and status==1):
                if((tablero[inicio-1][inicio2-1]==0 and inicio-1>0 and inicio2-1>0) or (int((tablero[inicio-1][inicio2-1]%100)/10)!=color and inicio-1>0 and inicio2-1>0)):
                   posp=1  
                elif((tablero[inicio-1][inicio2]==0 and inicio-1>0) or (int((tablero[inicio-1][inicio2]%100)/10)!=color and inicio-1>0)):
                   posp=1
                elif((tablero[inicio-1][inicio2+1]==0 and inicio-1>0 and inicio2+1<10) or (int((tablero[inicio-1][inicio2+1]%100)/10)!=color and inicio-1>0 and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio][inicio2-1]==0 and inicio2-1>0) or (int((tablero[inicio][inicio2-1]%100)/10)!=color and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio][inicio2+1]==0 and inicio2+1<10) or (int((tablero[inicio][inicio2+1]%100)/10)!=color and inicio2+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2-1]==0 and inicio+1<10 and inicio2-1>0) or (int((tablero[inicio+1][inicio2-1]%100)/10)!=color and inicio+1<10 and inicio2-1>0)):
                   posp=1
                elif((tablero[inicio+1][inicio2]==0 and inicio+1<10) or (int((tablero[inicio+1][inicio2]%100)/10)!=color and inicio+1<10)):
                   posp=1
                elif((tablero[inicio+1][inicio2+1]==0 and inicio+1<10 and inicio2+1<10) or (int((tablero[inicio+1][inicio2+1]%100)/10)!=color and inicio+1<10 and inicio2+1<10)):
                   posp=1 
            if(posp==0):
               print("La pieza seleccionada no tiene movimientos posibles.")
               reiniciar = 0
               
            
            
            if(((tablero[inicio][inicio2]%100)/10 != turnos + 0.1) and tablero[inicio][inicio2]!= 0 ):
               print("Esa pieza no es de tu equipo.")
               reiniciar = 0
            
              
               
                
        while (reiniciar==1):
            reiniciar = 0
            while True:
               while True:
                  try:
                     final = int(input("Ingrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final<10 and final>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            while True:
               while True:
                  try:
                     final2 = int(input("Ingrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover su pieza seleccionada.\n"))
                     break
                  except ValueError:
                     print("Sólo números enteros entre 1 y 9.")
               if(final2<10 and final2>0):
                  break
               print("Debe ingresar un valor entre 1 y 9.")
            if(tablero[final][final2!=0]):
               br=(int(tablero[final][final2]%100)/10)
               if((br==1 and sr1==0) or (br==2 and sr2==0) or (br==3 and sr3==0) or (br==4 and sr4==0)):
                  print("No puedes capturar las piezas de un lider capturado")
                  reiniciar=1
            if(tablero[final][final2] == tablero[inicio][inicio2] and tablero[final][final2] != 0 ):
                print("No se puede mover al mismo lugar.")
                reiniciar = 1
            if(tablero[5][5]!=0 and int(tablero[inicio][inicio2]/100)==1 and final==5 and final2==5):
                print("Los militantes no pueden capturar a un lider si este se encuentra en la casilla central.")
                reiniciar = 1      
            if(int(tablero[inicio][inicio2]/100)!=5 and final==5 and final2==5 and tablero[final][final2]==0):
                print("Sólo el líder puede estar en la posicion central.")
                reiniciar = 1     
            if((tablero[final][final2]%100)/10 == turnos + 0.1 and tablero[final][final2] != tablero[inicio][inicio2]   ):
                print("No se pueden capturar piezas de tu mismo equipo.")
                reiniciar = 1
            if(tablero[inicio][inicio2]/100==1.11 and (final-inicio<-2 or final-inicio>2 or final2-inicio2<-2 or final2-inicio2>2)):
               print("Los militantes sólo pueden moverse una o dos casillas.")
               reiniciar =1
               #movimientos
            if(inicio2==final2):
               vertical=1
               print("", end ="")
            elif(inicio==final):
               horizontal=1
               print("", end ="")   
            elif((inicio+1==final and inicio2+1==final2) or (inicio+2==final and inicio2+2==final2) or (inicio+3==final and inicio2+3==final2) or (inicio+4==final and inicio2+4==final2) or (inicio+5==final and inicio2+5==final2) or (inicio+6==final and inicio2+6==final2) or (inicio+7==final and inicio2+7==final2) or (inicio+8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=1
            elif((inicio-1==final and inicio2-1==final2) or (inicio-2==final and inicio2-2==final2) or (inicio-3==final and inicio2-3==final2) or (inicio-4==final and inicio2-4==final2) or (inicio-5==final and inicio2-5==final2) or (inicio-6==final and inicio2-6==final2) or (inicio-7==final and inicio2-7==final2) or (inicio-8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=2
            elif((inicio-1==final and inicio2+1==final2) or (inicio-2==final and inicio2+2==final2) or (inicio-3==final and inicio2+3==final2) or (inicio-4==final and inicio2+4==final2) or (inicio-5==final and inicio2+5==final2) or (inicio-6==final and inicio2+6==final2) or (inicio-7==final and inicio2+7==final2) or (inicio-8==final and inicio2+8==final2)):   
               print("", end ="")
               diagonal=3
            elif((inicio+1==final and inicio2-1==final2) or (inicio+2==final and inicio2-2==final2) or (inicio+3==final and inicio2-3==final2) or (inicio+4==final and inicio2-4==final2) or (inicio+5==final and inicio2-5==final2) or (inicio+6==final and inicio2-6==final2) or (inicio+7==final and inicio2-7==final2) or (inicio+8==final and inicio2-8==final2)):   
               print("", end ="")
               diagonal=4
            else:   
               print("Las piezas solo se pueden mover de manera vertical, horizontal o diagonal.")
               
               reiniciar=1
            com=int(tablero[inicio][inicio2]/100)    
            if(tablero[final][final2]!=0 and tablero[final][final2]%10==0 and com!=2):
               print("No puedes capturar piezas capturadas.")
               reiniciar=1
            if(tablero[final][final2]%10==1 and com==2):
               print("No puedes situarte sobre otras piezas vivas con el necromóvil.")
               reiniciar=1  
            if(com==3 and tablero[final][final2]!=0):
               print("No puedes capturar piezas directamente encima de ellas con el reportero.")
               reiniciar=1   
            if(horizontal==1):
               if(final2-inicio2>0):
                  for k in range(inicio2,final2-1,1):
                     if(tablero[inicio][k+1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
               if(final2-inicio2<0):        
                  for k in range(inicio2,final2+1,-1):
                     if(tablero[inicio][k-1]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               horizontal=0
                     
            if(vertical==1):
               if(final-inicio>0):
                  for k in range(inicio,final-1,1):
                     if(tablero[k+1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
               if(final-inicio<0):
                  for k in range(inicio,final+1,-1):
                     if(tablero[k-1][inicio2]!=0):
                        print("No se pueden saltar piezas.")
                        reiniciar=1
               vertical=0
            if(diagonal==1):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio+k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==2):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio-k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                
            if(diagonal==3):
               for k in range(1,final-inicio-1):
                  if(tablero[inicio-k][inicio2+k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                     
                        
            if(diagonal==4):
               for k in range(1,inicio-final-1):
                  if(tablero[inicio+k][inicio2-k]!=0):
                     print("No se pueden saltar piezas.")
                     reiniciar=1
                     break 
               diagonal=0
                                       
#empezar a capturar xdxd  o movimiento xdxd
        capturarrey=0 
        if(tablero[final][final2]%10==1): 
            capturarrey= tablero[final][final2]         
        pieza=int(tablero[inicio][inicio2]/100)          
        #cuando solo mueves         
        if(tablero[final][final2] == 0):         
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
        
        #capturar con necromovil
        necro=0
        if(pieza==2 and tablero[inicio][inicio2] != 0 ):
           reiniciar = 0
           necro=1
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or(filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro.") 
                 reiniciar=0    
                
           tablero[filam][columnam] = temporal
        #capturar con provocador o diplomatico
        if(pieza==4 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           
           temporal=tablero[final][final2]
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = 0
           while (reiniciar==0):
              reiniciar = 1
              
              actualizar()
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar numero enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza seleccionada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
               
              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5 and int(temporal/100)!= 5)):
                 print("Las piezas sólo pueden ocupar lugares vacíos o no pueden ocupar el centro si son un líder.")
                 reiniciar=0
                 
           if(temporal%10==1):      
              tablero[filam][columnam] = temporal
             
        #capturar con líder
        if(pieza==5 and tablero[inicio][inicio2] != 0):
           if(final==5 and final2==5 and int(tablero[5][5]/100)==5):
              clc=1
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar=1
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Debes ingresar un numero entero entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0 or (filam==5 and columnam==5)):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos y no se pueden poner en el centro.")
                 reiniciar=0

                 
           tablero[inicio][inicio2]=0      
           tablero[filam][columnam] = temporal
           



              
           #capturar con militante
        if(pieza==1 and tablero[inicio][inicio2] != 0):
           reiniciar = 0
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           while (reiniciar==0):
              reiniciar = 1
              
              while True:
                  while True:
                     try:
                        filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(filam<10 and filam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0
              while True:
                  while True:
                     try:
                        columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la casilla a la que quiere mover la pieza capturada.\n"))
                        break
                     except ValueError:
                        print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                  if(columnam<10 and columnam>0):
                     break
                  print("Debe ingresar un valor entre 1 y 9.")
                  reiniciar=0

              if(tablero[filam][columnam]!=0):
                 print("Las piezas capturadas sólo pueden ocupar lugares vacíos")
                 reiniciar=0
              if(filam==5 and columnam ==5):
                 print("Las piezas muertas no pueden ocupar el centro.")
                 reiniciar=0
           if(reiniciar==1):     
              tablero[inicio][inicio2]=0 
              tablero[filam][columnam] = temporal
        #capturar con reportero
        repors=0
       
        if(tablero[final-1][final2]!=0 and final-1>0 and tablero[final-1][final2]%10==1 and int((tablero[final-1][final2]%100)/10)!=turnos):
           repors=1  
        if(tablero[final][final2-1]!=0 and final2-1>0 and tablero[final][final2-1]%10==1 and int((tablero[final][final2-1]%100)/10)!=turnos):
           repors=1
        if(tablero[final][final2+1]!=0 and final2+1<10 and tablero[final][final2+1]%10==1 and int((tablero[final][final2+1]%100)/10)!=turnos):
           repors=1               
        if(tablero[final+1][final2]!=0 and final+1<10 and tablero[final+1][final2]%10==1 and int((tablero[final+1][final2]%100)/10)!=turnos):
           repors=1
        
        if(pieza==3 and repors==1):
           actualizar()
           reiniciar==0         
           while True:
              while True:
                 try:
                    cr= int(input("\033[1;37;40m¿Desea capturar alguna pieza con el reportero? (1.-si 0.-no )   . \n"))
                    break
                 except ValueError:
                     print("Sólo se pueden ingresar números enteros entre 1 y 9.")
              if(cr==0 or cr==1):
                  break
              print("Debe ingresar 1 ó 0.")
           
           if(cr==1):
               while (reiniciar==0):
                 reiniciar=1 
                 while True:
                    while True:
                       try:
                          filam = int(input("\033[1;37;40mIngrese el número (en dígito) de la fila en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(filam<10 and filam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 while True:
                    while True:
                       try:
                          columnam = int(input("\033[1;37;40mIngrese el número (en dígito) de la columna en la que se ubica la pieza que quiere capturar.\n"))
                          break
                       except ValueError:
                           print("Sólo se pueden ingresar números enteros entre 1 y 9.")
                    if(columnam<10 and columnam>0):
                       break
                    print("Debe ingresar un valor entre 1 y 9.")
                    reiniciar=0
                 if((final+1==filam and final2==columnam) or (final-1==filam and final2==columnam) or (final==filam and final2==columnam+1) or (final==filam and final2==columnam-1)):
                     print("", end="")
                 else:
                     print("El reportero solo puede capturar piezas adyacentes horizontales o verticales.")
                     reiniciar=0
                 if(tablero[filam][columnam]==0):
                    print("No hay pieza ahí para capturar.")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(tablero[filam][columnam]!=0 and tablero[filam][columnam]%10==0 ):
                    print("No puedes capturar piezas capturadas")
                    reiniciar=0
                 if(int((tablero[filam][columnam]%100)/10)==turnos):
                    print("No puedes capturar piezas de tu mismo equipo")      
                    reiniciar=0
                 if(int(tablero[filam][columnam]/100)==5 and filam==5 and columnam==5): 
                    capturarrey= tablero[filam][columnam]   
               tablero[inicio][inicio2]=0 
               tablero[filam][columnam] = tablero[filam][columnam]-1
              
        #capturar con asesino
        if(pieza==6 and tablero[inicio][inicio2] != 0):
           temporal=tablero[final][final2]-1
           tablero[final][final2] = tablero[inicio][inicio2]
           tablero[inicio][inicio2] = temporal
        # si te comes un rey en el centro con otra pieza que no sea el rey 
        if(((int(tablero[5][5]/100)!=5) and int(tablero[5][5]/100)!=0) or (((int(tablero[x][y]/100)==5) and (int(tablero[x][y]%10))==0 )) and necroc==0):
           if(tablero[4][4]==0):
              tablero[4][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][5]==0):
              tablero[4][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[4][6]==0):
              tablero[4][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][4]==0):
              tablero[5][4]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[5][6]==0):
              tablero[5][6]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][4]==0):
              tablero[6][4]=tablero[5][5]
              tablero[5][5]=0  
           elif(tablero[6][5]==0):
              tablero[6][5]=tablero[5][5]
              tablero[5][5]=0
           elif(tablero[6][6]==0):
              tablero[6][6]=tablero[5][5]
              tablero[5][5]=0                   
        #darte las piezas de otro equipo si te comes un rey
        eq=int((capturarrey%100)/10)
        suma=(((turnos*10)+1))-((eq*10)+1)
        if(int(capturarrey/100)==5):
           cs=0
           for x in range (0,10):
              for y in range (0,10):
                 cs=cs+1 
                 pieza=int(tablero[x][y]/100)   
                 color=int((tablero[x][y]%100)/10)
                 status=int(tablero[x][y]%10)
                 if(pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==2 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==3 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(cs==4 and pieza==1 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma   
                 if(pieza==2 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==3 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==4 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==5 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                 if(pieza==6 and color==eq and status==1):
                    tablero[x][y]=tablero[x][y]+suma
                   
                   
                   
    
    if(turnos==1 and sr1==0):  
      contadorpoder=0
    if(turnos==2 and sr2==0):  
      contadorpoder=0
    if(turnos==3 and sr3==0):  
      contadorpoder=0
    if(turnos==4 and sr4==0):  
      contadorpoder=0      

    #ver si hay rey en centro            
    if(tablero[5][5]!=0 and tablero[5][5]%10==1):
       poder=1
    if(tablero[5][5]==0):
       poder=0

   #turnos normales    
    if(poder==0 and primerturno==0):    
       if(turnos>4):
          turnos = 0 
       turnos = turnos + 1 
         
#esto funciona si hay 4 reyes
    #turnos repetidos
    if(primerturno==1 and poder==0):
      turnos=turnos+contadorturnos
      primerturno=0
      contadorturnos=1
          
    #si comes con lider a lider en centro
    if(clc==1):
       clc=0
       contadorpoder=0
       contadorturnos=1    
    #turnos repetidos   
    if(poder==1):
       if(contadorpoder==0):
          turnos=turnos+contadorturnos
          contadorturnos=contadorturnos+1       
          if(contadorturnos>=4):
             contadorturnos=1  
       elif(contadorpoder==1):
          turnos=int((tablero[5][5]%100)/10)
          contadorpoder=-1
       contadorpoder=contadorpoder+1  
       primerturno=1

    #checar que solo haya un rey vivo
    for x in range (0,10):
       for y in range (0,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(color==1 and pieza==5):
             rey1=tablero[x][y]
             s1=status
          if(color==2 and pieza==5):
             rey2=tablero[x][y]
             s2=status
          if(color==3 and pieza==5):
             rey3=tablero[x][y]
             s3=status
          if(color==4 and pieza==5):
             rey4=tablero[x][y]
             s4=status
    if(s1+s2+s3+s4==1):
       terminar=1
    #si hay un lider en el centro rodeado de piezas muertas y no hay necromovil
    for x in range (0,10):
       for y in range (0,10):
          pieza=int(tablero[x][y]/100)   
          color=int((tablero[x][y]%100)/10)
          status=int(tablero[x][y]%10)
          if(color==1 and pieza==2):
             necro1=int(tablero[x][y]%10)
          if(color==2 and pieza==2):
             necro2=int(tablero[x][y]%10)
          if(color==3 and pieza==2):
             necro3=int(tablero[x][y]%10)
          if(color==4 and pieza==2):
             necro4=int(tablero[x][y]%10) 
    if(necro1+necro2+necro3+necro4==0):         
       nnrg=0
       if(tablero[4][4]!=0 and tablero[4][4]%10==0):
          nnrg=nnrg+1
       
       if(tablero[4][5]!=0 and tablero[4][5]%10==0):
          nnrg=nnrg+1
       
       if(tablero[4][6]!=0 and tablero[4][6]%10==0):
          nnrg=nnrg+1
       
       if(tablero[5][4]!=0 and tablero[5][4]%10==0):
          nnrg=nnrg+1
       
       if(tablero[5][6]!=0 and tablero[5][6]%10==0):
          nnrg=nnrg+1
       
       if(tablero[6][4]!=0 and tablero[6][4]%10==0):
          nnrg=nnrg+1
         
       if(tablero[6][5]!=0 and tablero[6][5]%10==0):
          nnrg=nnrg+1
       
       if(tablero[6][6]!=0 and tablero[6][6]%10==0):
          nnrg=nnrg+1
       if(nnrg==8): 
          terminar=1
          if(int((tablero[5][5]%100)/10)==1):
             s2=0
             s3=0
             s4=0
          if(int((tablero[5][5]%100)/10)==2):
             s1=0
             s3=0
             s4=0
          if(int((tablero[5][5]%100)/10)==3):
             s2=0
             s1=0
             s4=0
          if(int((tablero[5][5]%100)/10)==4):
             s2=0
             s3=0
             s1=0
           
    



          
clear()
print("Game over.")
if(s1==1):
   print("Ha ganado el jugador 1 (rojo).")
if(s2==1):
   print("Ha ganado el jugador 2 (azul).")
if(s3==1):
   print("Ha ganado el jugador 3 (amarillo).")
if(s4==1):
   print("Ha ganado el jugador 4 (verde).")  
actualizar()    
input("Pulse la tecla intro para salir...")        
    




   



    
