from tortugas import tortuga,tortuga_con_sorpresas
import random


def avanzar_trotuga (posicion,max_pasos):  
    return posicion + random.randint(1,max_pasos)

def resbalar (posicion,probabilidad,max_pasos_atras):
    if random.random()<probabilidad:
        pasos_atras = random.randint(1,max_pasos_atras)
        posicion = max (0,posicion-pasos_atras)
    return posicion 
    
def mostrar_posiciones(posicion_A,posicion_B):
    print(f"tortuga A esta en {posicion_A} tortuga B esta en {posicion_B}")

def anunciar_ganador(posicion_A,posicion_B,meta):
    if posicion_A>= meta and posicion_B>= meta :
           print ("empate")
    elif posicion_A>= meta :
           print ("gana la tortuga A")
    else:
           print("gana la tortuga B ")
