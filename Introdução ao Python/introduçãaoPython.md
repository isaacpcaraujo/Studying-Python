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
~~~python 
py print(‘Hello world!’)
~~~

Curiosidade: A função *print()* possui um argumento nomeado *end*, que tem em sí, a atribuição do valor '\n', o que confere à função print uma quebra de linha a cada uso da função. Esse valor pode ser alterado.

~~~python 
print("Olá")
print("Pessoa")
~~~

Modificamos o argumento end='\n', para retirar a quebra de linha automática da função ***print()*** .

~~~python 
print("Olá", end=' ')
print("Pessoa")
~~~

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
~~~py
minha mensagem = 'Olá Python!'
~~~

Atribuindo o valor 'Olá Python!' a uma variável
~~~py
minha_mensagem = 'Olá Python!'
print(minha_mensagem)
~~~

Deletando nossa variável.
~~~py
del minha_mensagem
print(minha_mensagem)
~~~


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
~~~py
type(object)
~~~