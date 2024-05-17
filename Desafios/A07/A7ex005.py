'=' * 20 # coloca '=' 20 vezes, o mesmo vale para olá ou qualquer palavra
n = input('Qual seu nome? ') # se quiser ser explicito pode colocar str
print(f'Prazer em te conhecer {n:20}!') # : significa para escrever o n com 20 caracteres ou seja dará um esppaço de 20 caracteres entre gustavo e a proxima coisa escrita
print(f'Prazer em te conhecer {n:>20}!') # ou alinhado a esquerda com < ou centralizado com ^
print(f'Prazer em te conhecer {n:=^20}!') 
n1 = int(input('um valor '))
n2 = int(input('outro valor '))
print(f'a soma vale {n1 + n2}')
print(f'a subtração vale {n1 - n2}')
print(f'a multiplicação vale {n1 * n2}')
print(f'a divisão vale {n1 / n2}')
print(f'a potencia vale {n1 ** n2}')
print(f'a divisão inteira vale {n1 // n2}')
print(f'o resto da divisão e {n1 % n2}')
print(f'a raiz entre eles e {n1 **(1/n2)}') # mas como eu vou juntar todas esses print em 1 linha de codigo? ou só coloque end = ''
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
dt = n1 // n2
dr = n1 % n2
r = n1 ** (1/n2)
print(f' a soma entre eles vale {s}, a subtração entre eles vale {su}, a multiplicação entre eles vale {m},a potencia entre eles e {p}, a divisão deles é {d}, a divisão inteira deles é {dt}, o resto da divisão deles é {dr} e a raiz entre eles e {r}')
print(f'a divisão(com 2 caracteres) entre eles é {d:.2f}')
print(f'a soma vale {s}', end = ' ') # posso também no meio do codigo com \n
print(f'a raiz e igual a {r}', end = ' cavalo >>> ')
print(f'a divisão é {d} \n já a sua divisão inteira é {dt}')
# desafio 5:
n3 = int(input('Um valor' ))
n3s = n3 + 1
n3a = n3 - 1
print(f'o antecessor do seu número é {n3a}, já seu sucesor é {n3s}') 
