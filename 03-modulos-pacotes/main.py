import matematica as mt

print (mt.PI)
print (mt.somar(10.0, 4.2))
print (mt.sub(10.0, 4.2))

# ou 

from matematica import PI, sub

# não precisa colocar o nome na frente
print (PI)
print (sub(10.9, 4.9))

# IMPORTAR A FUNÇÃO MEDIA DO PACOTE ESTATISTICA E MODULO DESCRITIVA
from estatistica.descritiva import media
from estatistica.inferencial import valor