try:
    numero = int(input("Digite um número:  "))

    print(f"O valor escolhido foi {numero}")
    for divisao in range(1,11):
        print(f"{numero} * {divisao} = {numero * divisao}")

except ZeroDivisionError:
    print("Divisão por zero é impossível.")
except ValueError:
    print("Digite um valor válido.")
except:
    print("[ERRO]")


