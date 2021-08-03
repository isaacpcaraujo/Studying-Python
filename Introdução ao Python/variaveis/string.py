# Armazenando uma string numa variável
mensagem = "Isso é uma string"
print(f'\n{mensagem}')
print('Tipo:', type(mensagem))

# Armazenando outra string numa outra variável
mensagem_2 = 'Isso também é uma string'
print(mensagem_2)
print('Tipo:', type(mensagem_2))

# Concatenando strings
nome = "aLbeRT"
sobrenome =  "eInsTEIn"
nome_completo = nome + ' ' + sobrenome
print('Concatenando:', nome_completo)

# Metódos de String
string = "aLbeRT eInsTEIn"
print("\n\nstr:", string)
# Utilização do método title().
print("str.title():", string.title())
# Utilização do método upper().
print("str.upper():", string.upper())
# Utilização do método lower().
print("str.lower():", string.lower())

ling_favorita = '   Python   '
print("\n\nling_favorita: " + ling_favorita + ".")
# Utilização do método rstrip(). Foi concatenado um ponto no final para verificar a utilização dos métodos
print("ling_favorita.rstrip(): " + ling_favorita.rstrip() + ".")
# Utilização do método lstrip().
print("ling_favorita.lstrip(): " + ling_favorita.lstrip() + ".")
# Utilização do método strip().
print("ling_favorita.strip(): " + ling_favorita.strip() + ".")