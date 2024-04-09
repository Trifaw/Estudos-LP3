# Função

print('Olá')
sum([1, 3, 5])


# quero somar uma lista de numeros
# usar a função sum()

# quero calcular a media de notas dos alunos
# 1. tem no python?
# 2. alguém já programou? (copiar ou adicionar dependencia)
# 3. você tem que declarar

# 1. Declaração
    # def nome_funcao(parametro1, parametro2):
    #   return valor
# 2. Chamada
print('Olá')
sum ([1, 3, 5])
# nome_funcao ('dad', 1)


# Função sem retorno e sem parametros
def imprimir_mensagem():
    print('socorro')
    
imprimir_mensagem()
imprimir_mensagem()



# Função sem retorno com parametros

# parametros vc argumentos

def saudacoes(nome):
    print(f'Bom dia (nome)')
    
# argumento para parâmetro nome 'maria'
saudacoes('maria')

# argumento para parâmetro nome
nome_completo = 'José da Silva'
saudacoes(nome_completo)



# Função com retorno e sem parametros
def obter_mensagem():
    return 'Socorro!'

mensagem = obter_mensagem()
print (mensagem)
# ou
print (obter_mensagem)

# Função com retorno com parametros
def gerar_saudacao(nome):
    return f'Bom dia {nome}'

print(gerar_saudacao('Pedro'))
print(gerar_saudacao('João'))

# retorno     parâmetro
#  não          não
#  não          sim
#  sim          não
#  sim          sim (ADEQUADO) (FUNÇÃO PURA)


# Imprimir saudação
# Saudacao = frase (dinâmica) nome (dinâmica)
# 'Bom dia pedro'
# 'boa tarde joão'

def saudacao(nome, frase):
    print (f'{frase}, {nome}')
    
saudacao('joão', 'bom dia')


def saudacao(nome, frase):
    return f'{frase}, {nome}'

print (saudacao('joao', 'bom dia'))

# Entrada
todas_as_notas = [
    [10.0, 3.0, 3.0],
    [0.0, 1.0, 3.0],
    [9.0, 7.0, 3.0],
]

# Saída [6.3, 6.0, 7.0]

def calcular_media(valores):
    return sum (valores / len(valores))

def calcular_medias_alunos(notas_alunos):
    # medias = []
    
    # for notas in notas_alunos:
    #     media = calcular_media(notas)
    #     medias.append(media)
        
    # return medias
    
    
    
    return [calcular_media(notas) for notas in notas_alunos]
    
def imprimir_medias(notas_alunos):
    medias = calcular_medias_alunos(notas_alunos)
    # lógica de enviar por email as medias
    
imprimir_medias(todas_as_notas)
enviar_medias_por_email(todas_as_notas)


# argumentos nomeados
def saudacao(nome, frase):
    return f'{frase} {nome}'

print(saudacao('João', 'Bom dia'))
print (saudacao(nome= 'João', frase='Bom dia'))
print (saudacao(frase='Bom dia', nome= 'João'))
print(saudacao('João', frase='Bom dia'))

# Parâmetro com valor padrão (default)
def saudacao(nome, frase= 'Bom dia'):
    return f'{frase} {nome}'
print (saudacao('João'))
print(saudacao('joao', 'boa tarde'))