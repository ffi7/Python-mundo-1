# se pode usar # para criar um comentario em 1 linha ou ''' para criar um comenterio entre mais de 1 linha
'''exemplo
P
Y
T
H
O
N
'''
# Modulos: bibliotecas de coisas adicionais ao python, como as extenções
# exemplo dos modulos:
# random(números aleatorios)
import random
n = random.random() # gera um número aleatorio entre 0 e 1
nI = random.randint(1, 10) # gera um número inteiro aletorio entre 1 e 10
print(n, '\n', nI)
# sortear mais de 1 número por vez
for i in range (15):
    print(random.randint(1, 100))
#-------------------------------------------------------------------------------------------------------------------------------- 
# math(ja vem com o python[funcionalidades extras da matemática])
# Funcionalidades da match: 
# ceil(arredondamento pra cima) [exemplo: 7.5 ---> 8.0]
# floor(arredondamento para baixp) [exemplo: 7.5 ---> 7.0]
# trunc({tuncar} elimina a virgula ou ponto para frente se fazer arredondamento nenhum) [exemplo: 7.5 ---> 7]
# pow(power guido, lá ele[potencia de outra forma sem ser os **])
# sqrt(square rote respectivamente quadrada raiz{outra forma sem ser ** 1 / 2})
# factorial(calculo de fatorial de um número[vou aprender na escola])
# import ...(seleciona o modulo) : importa todos as funcionalidades do modulo
# from ...(seleciona o modulo) import (coloca oque quer) : importa um especifico 
# exemplo:                              import math     from math import pow, ceil, sqrt
# n = int(input('digite um valor'))     n1 = math.pow(n)       n2 = pow(n)
# se quiser saber mais sobre esses modulos vá para o python.org e va na aba docs selecione a sua versão e procure math modules
# pacotes extras: python.org ---> PyPI
# instalar os pacotes extras: vai no terminal e digita pip install nome do PyPi
# atualizar o pip: pip install --upgrade pip
