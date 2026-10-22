# Comprobaciones visibles de M1

Ejecuta el juego después de cada cambio y anota el resultado:
- ambas velocidades positivas: termina y anuncia una ganadora;  
- roja más rápida: gana la roja;
    RED_SPEED = 5, BLUE_SPEED = 2-> ¡Ha ganado la tortuga roja!
- azul más rápida: gana la azul;
    RED_SPEED = 2, BLUE_SPEED = 6-> ¡Ha ganado la tortuga azul!
- velocidades iguales: anuncia un empate (no puede ganar siempre la roja);
    RED_SPEED = 4, BLUE_SPEED = 4-> ¡Empate Las dos tortugas llegan a la vez
- alguna velocidad igual a cero o negativa: muestra el aviso y no inicia la carrera;
    RED_SPEED = 0, BLUE_SPEED = 3-> Muestra mensaje de error por consola y no inicia la carrera
    RED_SPEED = 4, BLUE_SPEED = -2-> Muestra mensaje de error por consola y se detiene
- antes de ejecutar, puedes justificar tu predicción usando las velocidades.

No se considera terminado si sólo funciona con una combinación concreta.
