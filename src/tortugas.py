import random 
def tortuga (meta):
    posicion_A = 0 
    posicion_B=0
    while posicion_A<meta and posicion_B<meta :
        posicion_A += random.randint(1, 2)
        posicion_B += random.randint(1, 3)
        print (f"la tortuga A esta en{posicion_A} y la tortuga B esta en {posicion_B} ")

    if posicion_A>= meta and posicion_B>= meta :
        print ("empate")
    elif posicion_A>= meta :
        print ("gana la tortuga A")
    else:
        print("gana la tortuga B ")

def tortuga_con_sorpresas(meta,probabilidad):
    
    posicion_A = 0 
    posicion_B=0
    while posicion_A<meta and posicion_B<meta :
        posicion_A += random.randint(1, 2)
        posicion_B += random.randint(1, 3)
            
    if random.random()<probabilidad:
        pasos_atras=random.randint(1,3)
        posicion_B=max(0,posicion_B-pasos_atras)
    if random.random() < probabilidad:
        pasos_atras = random.randint(1, 3)
        posicion_A = max(0, posicion_A - pasos_atras)
        
    print (f"la tortuga A esta en{posicion_A} y la tortuga B esta en {posicion_B} ")
    
    if posicion_A>= meta and posicion_B>= meta :
        print ("empate")
    elif posicion_A>= meta :
        print ("gana la tortuga A")
    else:
        print("gana la tortuga B ")
        