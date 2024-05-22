def fome():
    tenho_sede = False
    tenho_fome = True

    if tenho_sede and tenho_fome:
        print("Vou a cozinha")
    elif tenho_sede and not tenho_fome:
        print("tomar uma coca")
    elif not(tenho_sede) and tenho_fome:
        print("Comer um sanduiche")
    else:
        print("Dormir")

fome()