import random as r # importara como r input('Em qual número eu pensei? ')
from time import sleep 
'''D28'''
print('shh, o computador está pensando')
nr =  r.randint(0, 5)
print('...')
sleep(1) # coloca um delay
print('=-=' * 21)
print('o computador pensou em um número de 0 a 5. tente adivinhar... ')
print('=-=' * 21)
j = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...!')
sleep(3)
if j == nr:
    print('Parabéns você acertou!')
else:
    print(f'Que pena você errou!, o número era {nr}. Mais sorte na proxima')
'''D29'''
v = float(input('Qual e a velocidade atual do carro? '))
print('tenha um bom dia, dirija com cuidado!')
if v > 80:
    print(f'MULTADO! Você exedeu o limite permitido que era de 80km/h, e pagará R${(v - 80) * 7}') # velocidade - 80 pois e o limite de velocidade
'''D30'''
nu = int(input('Digite um número '))
np = nu/2 
print('PROCESSANDO...')
sleep(3)
if np == int(np):# ou N % 2 == 0
    print('Esse número e par!')
else:
    print('Esse número e impar!')
'''D31'''
print('Bem vindo(a), este é um progama que calculará o preço de uma viagem de onibus sendo que a cada km custa R$0,50. Porém para viagems com mais de 200km cada km custará R$0.45.')
v = float(input('Quantos quilometros quadrados você percorera nesta viagem de onibus: km: '))
if v <= 200:
    print(f'O preço da viagem será R${v/2 :.2f}')
else:
    print(f'O preço da viagem será R${v * 0.45 :.2f}.')
'''D32'''
from datetime import date
print('Este progama irá lhe dizer se um ano qualquer e ou não e bissexto, coloque 0 para o ano atual')
A = int(input('Digite o ano '))
if A == 0:
    A = date.today().year
if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:# != diferente
    print(f'O ano {A} é bissexto')
else:
    print(f'O ano {A} não e bissexto')
'''D33'''
# pode fazer com muitos ifs mas tem outra maneira sem if
nn = float('Digite o primeiro número ')
nm = float('Digite o segundo valor ')
mn = float('Digite o terceiro valor')
l = [nn, nm, mn]
l_or = sorted(l)
print(f'O menor número e {l_or[0]}\nO maior número e {l_or[2]}')
'''D34'''
print('Este e um progama que irá calcular o aumento de salario de um funcionario, se o salario atual dele for maior que R$1250,00 o aumento será de 10%, porem se for menor ou igual que R$1250,00 o aumento sera de 15%.')
s = float(input('Qual e o salario deste funcionario? R$'))
print('Processando...')
sleep(3)
if s > 1250.00:
    print(f'O novo salario deste funcionario será R${s * 0.1 + s :.2f}')
else:
    print(f'O novo salario deste funcionario será R${s * 0.15 + s :.2f}')
'''D35'''
print("Este e um progama que lhe falará se 3 retas podem formar um triângulo")
r1 = float(input('Digite o valor da primeira reta '))
r2 = float(input('Digite ovalor da segunda reta '))
r3 = float(input('Digite o valor da terceira reta '))
print('PROCESSANDO...')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')
