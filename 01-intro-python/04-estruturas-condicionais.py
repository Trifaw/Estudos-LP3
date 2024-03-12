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
        
