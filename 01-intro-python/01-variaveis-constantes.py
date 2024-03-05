# Identificadores
# letra. número e _
# palavras reservadas: def, if, for, ...
# case sensitive

nome = "João"
Nome = "João"

# varáveis 
# identificador = valor

altura = 1.8 
idade = 22
nome = "Giovanni Foliene"
empregado = True

# constante
# python não tem constante
# DECLARAR TUDO MAIUSCULO 
pi = 3.14
PI = 3.14

# comentários única linha #

"""
Comentário de 
Multiplas 
Linhas
"""

# docstring 
# documentação de código de funções 
# classes, módulo, etc
# DEF abre função/ método
def somar (n1, n2):
    print("Aqui escreve")

def somar (n1, n2):
    """
    Função que soma dois números

    :param n1: primeiro número
    :param n2: segundo número
    :return: a soma dos parâmetros

    """
    return n1 + n2

