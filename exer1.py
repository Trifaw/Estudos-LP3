import random

def jogo_adivinhação():

    numeroAleatorio = random.randint(1, 100)
    
    while True:
        numeroUsuario = int(input("digite um número entre 1 e 100 e veja se você adivinhou: "))
    
        if numeroUsuario == numeroAleatorio:
            print ('Você acertou o número')
            break
        
            if numeroUsuario < numeroAleatorio:
                print ('o número é menor, jogue de novo')
            else:
                print('o número é maior, jogue de novo')
        else:


jogo_adivinhação()