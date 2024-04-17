def contador(frase):
    numero_vogais = 0
    numero_consoantes = 0
    
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ]
    
    for char in frase:
        if char.isalpha():
            if char in vogais:
                numero_vogais += 1
            else:
                numero_consoantes += 1
            
    return (numero_vogais, numero_consoantes)

frase = input('digite uma frase: ')

vogais, consoantes = contador(frase)

print(f'esta frase tem um total de {vogais} vogais')
print(f'e tem um total de {consoantes} consoantes')

