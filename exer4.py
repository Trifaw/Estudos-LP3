def contar_vogais_e_consoantes(frase):
    # Inicialize os contadores para vogais e consoantes
    num_vogais = 0
    num_consoantes = 0
    
    # Defina uma lista de vogais (tanto maiúsculas quanto minúsculas)
    vogais = "aeiouAEIOU"
    
    # Percorra cada caractere na frase
    for char in frase:
        # Verifique se o caractere é uma letra do alfabeto
        if char.isalpha():
            # Verifique se o caractere é uma vogal
            if char in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1
    
    # Retorne o número de vogais e consoantes encontradas na frase
    return num_vogais, num_consoantes

# Solicite ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Chame a função para contar vogais e consoantes
vogais, consoantes = contar_vogais_e_consoantes(frase)

# Exiba o resultado
print(f"Número de vogais: {vogais}")
print(f"Número de consoantes: {consoantes}")