
def fazer_big_mac(nome):
    print(f"o hamburguer é {nome}")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}")

def fazer_combo_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)

def soma_num(num1,num2):
    return num1 + num2

resultado = soma_num(15,22)
print(resultado)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([1,234,56,78,355464,6,36,56,45645646,656345,45])
print(resultado)
