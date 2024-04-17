def Tabuada(numero):
    
    for multiplicador in range(1, 11):
        resultado = multiplicador * numero
        print (f'{numero} * {multiplicador} = {resultado}')
numero = int(input('digite seu número'))
Tabuada(numero)