# pratica: 
import math 
n = int(input('Digite um valor '))
r = math.sqrt(n) # se tivesse colocado from lá em cima não precisaria do math na frente desse codígo 
print(f'A raiz desse valor é aproximadamente {math.ceil(r)}') # poderia colocar também o :2f para mostrar somente 2 casas após o ponto
import emoji
print(emoji.emojize('Python e divertido :thumbs_up:' ))
# desafios
from math import floor, trunc, pow, sqrt, cos, tan, sin, radians, hypot
import random
print('Olá, este é um progama que mostra a porção inteira de um número qualquer')
n2 = float(input('Digite um valor não inteiro '))
nt = trunc(n2) # ou usar int(n2)
print(f'A parte inteira desse número e {nt}')

print('Olá, este e um progama que qualculará a hipotenusa de um triângulo retângulo. Desque você nos de a medida do cateto adjacente e do cateto oposto')
ca = float(input('Digite o valor do cateto adjacente '))
co = float(input('Digite o valor do cateto oposto '))
h = hypot(co, ca) # ou sqrt( pow(ca, 2) + pow(co, 2) )
print(f'A hipotenusa deste triângulo retângulo é {h:.2f}')

print('Olá, este e um progama que lhe falara o cosseno, seno e a tangente de um ângulo qualquer ')
n4 = int(input('Digite o valor do ângulo '))
se = sin(radians(n4)) # coloca radians para colocar em graus centimetros, e oque e ultilizado no Brasil
co2 = cos(radians(n4))
ta = tan(radians(n4))
print(f'O seno deste ângulo é {se:.2f} , já o cosseno é {co2:.2f} e a tangente é {ta:.2f} ')

print('Olá, este é um progama que sorteia aleatorialmente 4 nomes e uma ordem entre esses quatro ')
m = input('Digite um nome ') # ou nomes = [input('Digite um nome: ') for _ in range(4)]
m11= input('digite outro nome ')
m22 = input('Digite o terceiro nome ')
m33 = input('Digite mais um nome ')
l = [m, m11, m22, m33] # lista: tudo entre[] e considerado uma lista
mst = random.choice(l)
print(f'O sorteado foi {mst}')
random.shuffle(l) # embaralhar
print(f'A ordem será {l}')
print('olá, este progama rodará um arquivo mp3 ') 
from soundplay import playsound
playsound('Curso Python/Desafios/A8/Damonte.mp3')
