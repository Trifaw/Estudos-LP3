# crie um programa que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras

# compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
# compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
# compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
# compras iguais ou superiores a R$ 500,00 - 15% de desconto

valor = float (input('qual o valor da compra? R$ '))
if valor <= 9.99:
    desconto = valor
    preço = valor - desconto
    print ('Você não tem desconto')
    print ('O valor a pagar é de: R$ ', preço)
elif valor >= 10.00 and valor <= 99.99:
    desconto = valor * 0.05
    preço = valor - desconto
    print ('Você recebeu um desconto de 5%')
    print ('Seu novo preço é de R$ ', preço)
elif valor >= 100.00 and valor <= 499.99:
    desconto = valor * 0.10
    preço = valor - desconto
    print ('Você recebeu um desconto de 10%')
    print ('Seu novo preço é de R$ ', preço)
else:
    desconto = valor * 0.15
    preço = valor - desconto
    print ('Você recebeu um desconto de 15%')
    print ('Seu novo preço é de R$ ', preço)

