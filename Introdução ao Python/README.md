# **Iniciando no Python** #

**O que é Python?**

* Python é uma linguagem de programação de alto nível, orientada a objetos, de tipagem dinâmica e multiparadigma. Foi lançada em 1991, por Guido Van Rossum.

* Um dos pontos fortes da linguagem é a combinação de uma sintaxe concisa e clara com bibliotecas poderosas, frameworks e módulos de terceiros. Vale ressaltar que Python prioriza a legibilidade do código sobre a velocidade ou expressividade.

**Por que Python?**

> “Todos os anos eu avalio se devo continuar usando Python ou se devo mudar para uma linguagem diferente – talvez uma que seja mais nova no mundo da programação. Porém, continuo focando em Python por diversos motivos. Python é uma linguagem extremamente eficiente: seus programas farão mais com menos linhas de código, se comparados ao que muitas outras linguagens exigiriam. A sintaxe de Python também ajudará você a escrever um código “limpo”. Seu código será fácil de ler, fácil de depurar, fácil de estender e de expandir, quando comparado com outras linguagens. As pessoas usam Python para muitos propósitos: criar jogos, construir aplicações web, resolver problemas de negócios e desenvolver ferramentas internas em todo tipo de empresas interessantes. Python também é intensamente usada em áreas científicas para pesquisa acadêmica e trabalhos aplicados.” 

-> Texto retirado do Livro **Curso Intensivo de Python**, de Eric Matthes


## **Hello World** ##

Uma crença de longa data no mundo da programação é que exibir uma mensagem ‘Hello world!’ na tela como seu primeiro programa em uma nova linguagem trará sorte.

Em Python, podemos escrever o programa Hello World com uma linha: 
```python 
print("Hello world!")
```

Curiosidade: A função *print()* possui um argumento nomeado *end*, que tem em sí, a atribuição do valor '\n', o que confere à função print uma quebra de linha a cada uso da função. Esse valor pode ser alterado.

```python 
print("Olá")
print("Pessoa")
```

Modificamos o argumento end='\n', para retirar a quebra de linha automática da função ***print()*** .

```python 
print("Olá", end=' ')
print("Pessoa")
```

# **Variáveis e tipos de dados simples** #

## **Introdução** ##

As variáveis são recipientes para armazenamento de valores de dados. Ao contrário de outras linguagens de programação, Python não tem nenhum comando para declarar uma variável.

> Uma variável é criada no momento em que se lhe atribui um valor pela primeira vez. Podemos mudar o valor de uma variável em nosso programa a qualquer momento, e Python sempre manterá o controle do valor atual.

> Caso deseje limpar uma variável, você pode escrever ***del VARIÁVEL***. Perceba que ao tentarmos printar "mensagem", Python retornará um erro, pois nossa variável foi deletada na linha anterior.

 **Nomeando variáveis**

Ao usar variáveis em Python, é preciso seguir algumas regras e diretrizes. Quebrar algumas dessas regras provocará erros:

* Espaços não são permitidos em nomes de variáveis, mas underlines podem ser usados para separar palavras em nomes de variáveis;
* Evite usar palavras reservadas e nomes de funções em Python como nomes de variáveis;
* Nomes de variáveis devem ser concisos, porém descritivos;
* Aprender a criar bons nomes de variáveis, em especial quando seus programas se tornarem mais interessantes e complicados, pode exigir um pouco de prática.


Nomeando uma variável de maneira errada
```py
minha mensagem = 'Olá Python!'
```

Atribuindo o valor 'Olá Python!' a uma variável
```py
minha_mensagem = 'Olá Python!'
print(minha_mensagem)
```

Deletando nossa variável.
```py
del minha_mensagem
print(minha_mensagem)
```


 **Tipos de dados** 

Python possui os seguintes tipos de dados padrão:

| **TIPOS**  |          **EXEMPLOS**          |
|:----------:|:----------------------------:  |
| Textual    | *str*                          |
| Numericas  | *int, float, complex*          |
| Sequências | *list, tuple, range*           |
| Mapeamento | *dict*                         |
| Conjuntos  | *set, frozenset*               |
| Booleano   | *bool*                         |
| Binário    | *bytes, bytearray, memoryview* |

## **Strings** ##

Uma string é simplesmente uma série de caracteres. Tudo que estiver entre aspas é considerada uma string em Python.

> Você pode usar aspas simples ou duplas em torno de suas strings, assim: *"Isso é uma string"* . Com a função *type()* podemos verificar o tipo do dado das nossas variáveis.

O argumento da função type é um objeto python
```py
type(object)
```

Armazenando uma string numa variável
```py
mensagem = "Isso é uma string"
print(mensagem)
print(type(mensagem))
```

**Concatenando Strings**

Muitas vezes, será conveniente combinar strings, que basicamente significa juntar duas strings numa só.

> Python usa o símbolo de adição "*+*" para concatenar strings.

```py
nome = "aLbeRT"
sobrenome =  "eInsTEIn"
nome_completo = nome + ' ' + sobrenome
print(nome_completo)
```

### **Métodos** ###

Um método nada mais é do que uma função embutida. Nesse caso o método tem o objetivo de modificar a string.

 **Mudando para letras maiúsculas e minúsculas em uma string usando métodos** 

> **.title()** exibe cada palavra com uma letra maiúscula no início;

> **.upper()** exibe todas as palavras com letra maiúscula;

> **.lower()** exibe todas as palavras com letra minúscula.

```py
string.title()
string.upper()
string.lower()
```

**Tratamento de espaços em branco**

> Para garantir que não haja espaços em branco do lado direito de uma string, utilize o método **.rstrip()**.

> Para garantir que não haja espaços em branco do lado esquerdo de uma string usando o método **.lstrip()**. 

> Para garantir que não haja espaços em branco dos dois lados ao mesmo tempo com **.strip()**.

```py
string.rstrip()
string.lstrip()
string.strip()
```

 Existem diversos outros métodos a serem explorados: https://www.w3schools.com/python/python_strings_methods.asp


 **Acrescentando espaços em branco em strings com tabulações e quebras de linha** 

Em programação, espaços em branco se referem a qualquer caractere que não é mostrado, como espaços, tabulações e símbolos de fim de linha.

> Para acrescentar uma tabulação em seu texto, utilize a combinação de caracteres "*\t*"

> Para acrescentar uma quebra de linha em uma string, utilize a combinação de caracteres "*\n*"

```py
print("Prezadxs, \n\n\t Segue em anexo...")
```

Normalmente, a utilização dos métodos não altera a variável permanentemente, portanto é necessário alterar o valor original dela para que a variável tenha seu valor substituído.

## **Inteiros e Pontos Flutuantes** ##

Python trata números de várias maneiras diferentes, de acordo com o modo como são usados. 

> **INTEIRO**: Python chama de número inteiro qualquer número sem um ponto decimal.

> **FLOAT**: Python chama de número de ponto flutuante (*float*) qualquer número com um ponto decimal.

```py
var_int = 2
var_float = 2.0
print("var_int type =", type(var_int))
print("var_float type =", type(var_float))
```

**Operadores**

| **Operador** |   **Descrição**  |
|:------------:|:----------------:|
|       +      |       SOMA       |
|       -      |     SUBTRAÇÃO    |
|       *      |   MULTIPLICAÇÃO  |
|       /      |      DIVISÃO     |
|      **      |    POTENCIAÇÃO   |
|      //      |  DIVISÃO INTEIRA |
|       %      | RESTO DA DIVISÃO |

Abaixo a simbologia utilizada para realizar operações matemáticas. Também é possível a formulação de equações com Python. (Recomendado estudar a biblioteca Numpy)

> Soma
```py
2+2
```

> Subtração
```py
2-2
```

> Multiplicação
~~~py
2*3
~~~

> Divisão
```py
2/2
```

 
Potenciação
```py
2**3
```

> Divisão Inteira: Retorna somente o a parte inteira da divisão
```py
7.5//2
```

Resto de: Retorna o resto da divisão
```py
5%2
```

**Precisão de pontos flutuantes**

Na maioria das ocasiões, podemos usar decimais sem nos preocupar com o modo como eles se comportam, sem se preocupar com a precisão deles. No entanto, é necessário ter cuidado, pois, às vezes, **você poderá obter um número arbitrário de casas decimais em sua resposta** como no exemplo abaixo.

```py
var_float = 3*0.1
print(var_float)
```

O código acima retornará o valor 0.30000000000000004. Para solucionar esse problema de precisão, utilizaremos a função **round()** na nossa variável:

```py
# A função round tem como argumentos a variável numerica utilizada e a quantidade de digitos nas casas decimais
round(var_numerica, digitos)
```

 **Evitando erros de tipo utilizando a função print()**

Com frequência, você vai querer usar o valor de uma variável numérica em uma mensagem. Entretanto, podem ocorrer erros relacionados a função **print()** por conta da tipagem das variáveis. 

```py
idade = 20
print('eu tenho '+ idade + ' anos!')
```

O código acima implicará num TypeError (Erro de tipo). Não é possível concatenar um número inteiro com uma string. Para solucionar este problema podemos converter a variável inteira idade em uma string utilizando a função **str()**.
```py
idade = 20
print('eu tenho ' + str(idade) + ' anos!')
```

Também podemos utilizar a string formatada literalmente na função **print()**. Estas strings podem conter campos de substituição, que são expressões delimitadas por chaves **{}**.

```py
idade = 20
print(f'eu tenho {idade} anos!')
```

Continua...