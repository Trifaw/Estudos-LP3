# operadores aritiméticos
# +, -, *, /, **

nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3

# numero elevado a outro 
# 10 elevado a 3
numero = 3
numero_elevado_2 = numero **2

# operadores lógicos 
# and, or, not

print(3 + 2)
print (True and True)
print (True and False)
print (False and True)
print (False and False)

print(3 + 2)
print (True or True)
print (True or False)
print (False or True)
print (False or False)

print(3 + 2)
print (not True) #false
print (not False) #true

# permitir a entrada
# - o usuário for funcionário E
# - o usuárionão estiver bloqueado E
# - hora atual estiver entre 8h e 18h

# permitir qualquer hora
# admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

horario_comercial = hora_atual >=8 and hora_atual <=18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado


if (funcionario_ativo and horario_comercial) or usuario_admin:
    print('acesso permitido')
    
idade = 25

maioridade = idade >=18

if maioridade >= 18:
    pass  # desconsidera isso

# operadores de comparação
# ==, !=, >, <, >=, <=
# == compara os valores, = atribuindo
# != diferente

# is, is not
# operadores de identidade
# comparar se os objetos ocupam os mesmo espaços de memória

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # true
print(a is b) # false

c = b
print(b is c) # true

# operador in, not in
# verificar se um elemento existe ou não em uma sequência
# str, list, tuple
opcoes = ('sim', 'não', 'talvez')
opcao = input ('digite uma opção')
opcao = opcao.lower()
opcao = opcao.strip()

if opcao in opcoes:
    print('ok')
else: 
    print ('não tem essa opção')
    
numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)
    
