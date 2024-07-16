# abrir o arquivo 

arquivo = open("dados.txt")

# conteudo = arquivo.read()
# conteudo = arquivo.readlines()
# print (conteudo)
linhas = []
for linha in arquivo:
    linhas.append(linha.strip().lower())

print (linhas)

arquivo.close()

# bloco with 

with open("dados.txt") as arquivo2:
    conteudo = arquivo2.read()
    print (conteudo)

# escrever no arquivo
# w - substitui todo o conteúdo
# a - adicionar uma nova linha (a = append)
# with open("dados.txt", "w") as arquivo3:
#     arquivo3.write("FRUTASSSSSS")

with open("dados.txt", "a") as arquivo4:
    arquivo4.write("\nFRUTASSSSSS")

# ler o arquivo produtos.csv e
# carregar em memória uma lista
# na qual cada produto é um dict

def linha_para_produto(linha):
    dados = linha.strip().split(",")
    return {
        "nome": dados[0],
        "descricao": dados[1],
        "preco": float(dados[2]),
        "imagem": dados[3]
    } 

def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            produto = linha_para_produto(linha)
            produtos.append(produto)

        return produtos
    
print(obter_produtos())

def salvar_produto(nome, descricao, preco, imagem):
    texto = f"\n{nome}, {descricao}, {preco}, {imagem}"
    with open("produtos.csv", "a") as arquivo_produtos:
        arquivo_produtos.write(texto)

salvar_produto("Celular", "Tira foto", "1500", "celular.jpg")
salvar_produto("Tablet", "Não tira foto boa", "1700", "tablet.jpg")