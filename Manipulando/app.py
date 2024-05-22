#open("caminho", "r")

#mode
# r - leitura
# a - append / Incrementar
# w - Escrita
# x - Criar arquivo
# r+ - leitura + escrita

arquivo = open("teste2.txt", "w")


# print(arquivo.readable())
# print(arquivo.read())
# lista = arquivo.readlines()
# print(lista)

arquivo.write("\nTerraforma")
arquivo.close()