minha_string = 'qualquer texto \n pedros'

print(minha_string.upper()) #Deixa toda a string em maiusculo
print(minha_string.lower()) #deixa a string minuscula
print(minha_string.capitalize()) # Deixa a primeira letra maiuscla
print(minha_string.replace('u', 'U', 1)) #muda a palavra 'qualquer' por 'nosso'. O número logo depois da virgula indica quantos 'u' serão deixados em maiusculo
print(len(minha_string)) #diz o tamanho sa váriavel, no caso seria quantas letras ela tem

x = 'texto' in minha_string
print(x)