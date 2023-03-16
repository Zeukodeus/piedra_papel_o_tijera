import random

print ("1=> piedra")
print ("2=> papel")
print ("3=> tijera")

maquina = random.randint(1, 3)

jugador = int(input("ingrese el número: "))

if maquina==jugador :

    rta = "EMPATE"

elif jugador==1 and maquina==2 :

    rta = "GANÓ LA MÁQUINA , la máquina sacó papel y el jugador escogió piedra"

elif jugador==1 and maquina==3 :

    rta = "GANÓ EL JUGADOR , la máquina sacó tijera y el jugador escogió piedra"

elif jugador==2 and maquina==1 :

    rta = "GANÓ EL JUGADOR , la máquina sacó piedra y el jugador escogió papel"

elif jugador==2 and maquina==3 :

    rta = "GANÓ LA MÁQUINA , la máquina sacó tijera y el jugador escogió papel"

elif jugador==3 and maquina==1 :

    rta = "GANÓ LA MÁQUINA , la máquina sacó piedra y el jugador escogió tijera"

elif jugador==3 and maquina==2 :

    rta = "GANÓ EL JUGADOR , la máquina sacó papel y el jugador escogió tijera"

else :

    rta = "introduzca un número válido pendejo"

print (rta)