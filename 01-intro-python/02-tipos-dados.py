# Tipos de dados
# int, float 
# string, list, tuple, set
# dict
# None

# int 
idade = 25
temperatura = 24

# float 
altura = 1.55
PI = 3.14

# string
nome = 'Giovanni Foliene'
Nome = "Giovanni Foliene"

# char?
letra = 'a'
letra = 'A'

# esse aqui é tipo array

print(nome [0])
print(Nome [-1])
print(nome[0:3])

# nome é um objeto da classe string
# logo, nome tem métodos, ou funções
print(nome.capitalize())
print(nome)

# interpolação de string e variáveis
nome = "João"
idade = 22
mensagem = f"Olá {nome}. Você tem {idade} anos"
print (mensagem)

# list
# lista de valores
# pode ser alterada
# lista vazia: habilidades = []
habilidades = ['Java', 'c#', 'css', 10, True]
print(habilidades[0])

# alterar o valor de habilidades
habilidades[0] = 'JavaScript'
print(habilidades[0])

# append: insere mais uma coisa na lista
# insert: insere mais uma coisa na lista onde você escolher

habilidades.insert(1, 'Kotlin') 
print (habilidades)

# Tupla
# 'Lista' de valores
# Não pode alterar, nem adicionar nem remover
# pra fazer isso, ao invés de colocar [], vc coloca () no início e no fim da lista
opcoes = ('sim', 'não', 'talvez')  

# for 
for opcao in opcoes:
    print(opcao)

# set, vc n tem controle sobre o que tá vindo do usuário
# pra fazer isso tem que colocar {}, abre e facha com chave 
# não inexado
# não permite elementos duplicados
# Digite a mensagem
# digite os emails de destino

emails = {'maria@gmail.com', 'maria@gmail.com'}
print(emails)


# dict
# dicionário
# chave : valor
# key : value

# site de emprego
"""
empresa = 'Google'
título = 'Engenheiro de Software'
salario = 20000.00
remoto = False
"""
# vaga
vaga = {
    'empresa': 'Google',
    'título': 'Engenheiro de Software',
    'salario': 20000.00,
    'remoto': False
}

print(vaga['salario'])
print(vaga['título'])

# none
nome = None

def gerar_boletim(prontuário):
    return 'boletim' # caso não
    return None