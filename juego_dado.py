# Intrucción(es)
# Escriba un programa que simule varias partidas seguidas de este juego de dados.
# cada jugador tira 5 dados | la puntuacion es la suma de todos sus puntos sin contar los valores que coincidan con el minimo o el maximo obtenido
import random

def juego_dados():
    print("===========================")
    print("       Juego de Dados      ")
    print("===========================")
    num_partidas = 0
    lances = 5
    lista_num_player1 = []
    lista_num_player2 = []
    valores_dado = [1, 2, 3, 4 ,5 ,6]
    i = 1;
    if num_partidas == 0:
        print("\n¡Como mínimo se debe jugar una partida!\n")
        num_partidas = int(input("\n¿Cuántas partidas desea: "))
    
        player1 = input("\nNombre del Player 1: ")
        player2 = input("\nNombre del Player 2: ")
    
    
    while i <= num_partidas:
        print(f"\nPartida {i}:")
        while lances != 0:
            num_dados_player1 = random.choice(valores_dado)
            num_dados_player2 = random.choice(valores_dado)

            lista_num_player1.append(num_dados_player1)
            lista_num_player2.append(num_dados_player2)
            lances -= 1

        suma_player1 = sum(lista_num_player1)
        suma_player2 = sum(lista_num_player2)

        print(f"\nTirada de {player1}: {lista_num_player1} => {suma_player1} puntos.")
        print(f"\nTirada de {player2}: {lista_num_player2} => {suma_player2} puntos.")

        lances = 5
        lista_num_player1 = []
        lista_num_player2 = []
        
        if suma_player1 == suma_player2:
            print("\n¡Hubo empate!")
        elif suma_player1 > suma_player2:
            print(f"\n¡Ha ganado {player1}!")
        else:
            print(f"\n¡Ha ganado {player2}!")
        
        i += 1

    if i <= num_partidas:
        juego_dados()
    else:
        return 0


juego_dados()