var_int = 2
var_float = 2.0
print("var_int type =", type(var_int))
print("var_float type =", type(var_float))

# Operadores Matemáticos
print("\n\nExemplo Soma:")
print("2 + 2 =", 2+2)
print("\nExemplo Subtração:")
print("2 - 2 =", 2-2)
print("\nExemplo Multiplicação:")
print("2 * 3 =", 2+2)
print("\nExemplo Divisão:")
print("2 / 2 =", 2/2)
print("\nExemplo Potenciação:")
print("2 ** 3 =", 2**3)
print("\nExemplo Divisão Inteira: Retorna somente o a parte inteira da divisão")
print("7.5 // 2 =", 7.5//2)
print("\nExemplo Resto de: Retorna o resto da divisão")
print("5 % 2 =", 5%2)

# Problemas com pontos flutuantes
var_float = 3*0.1
print("\n\nSem arredondamento:", var_float)
var_float = round(var_float, 2)
print("Com arredondamento:", var_float)

# Printando valores numericos
idade = 21
print(f'\n\neu tenho {idade} anos!')