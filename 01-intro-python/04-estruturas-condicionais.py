# if
# if condição:
#     codigo
#  codigo


idade = 20 
if idade >= 18:
    print ('maior de idade')
    print ("jkdk")
# if/else
idade = 20 
if idade >= 18:
    print ('maior de idade')
    print ("jkdk")
else: 
    print ('menor de idade')    

# if/elif/else
# criança 0 a 12, adolescente 13 a 17,
# adulto 18 a 59, idoso +60

if idade > 0 and idade <=12:
    print('criança')

if idade >= 12 and idade <=17:
    print('adolescente')

if idade >= 18 and idade <=59:
    print('adulto')
    
if idade >59:
    print('idoso')
    
# elif

if idade <= 12:
    print ('criança')
elif idade <=17:
    print ('adolescente')
elif idade <=59:
    print ('adulto')
else:
    print('idoso')
    
# condições aninhadas

email = 'admin@email.com'
senha = '123'

if email == 'admin@email.com':
    if senha == '123':
        print ('liberado')
    else:
        print ('erro')
else:
    print ('erro')
    
    
if email == 'admin@email.com' and senha == '123':
    print ('liberado')
else:
    print('erro')
    
    
# entrada email, senha
# saida true ou false

def liberar_acesso(email, senha):
    if email == 'admin@email.com' and senha == '123':
        return True
    else: 
        return False
    
# não precisa do boolean, pq ao 'and', já retorna esse valor
def liberar_acesso(email, senha):
    if email == 'admin@email.com' and senha == '123':
        print('liberado')
        
# operador ternário 
idade = 20
# maior ou menor
status = ''

if idade >= 18:
    status = 'maior'
else:
    status = 'menor'
    
status = 'maior' if idade >= 18 else 'menor'

# match
dia = 3
match dia:
    case 1:
        print ('domingo')
    case 2: 
        print ('segunda')
    case 3:
        print ('terça')
    case _: 
        print ('dia inválido')
        
match dia: 
    case 1 | 7:
        print ('Fim de Semana')
    case 2 | 3| 4| 5| 6:
        print ('Dia útil')
    case _:
        print ('dia inválido')
        
