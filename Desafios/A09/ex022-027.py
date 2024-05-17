'''D22'''
n = input('Qual seu nome completo? ')
P = n.upper()
p = n.lower()
L = len(''.join(n.split())) # ou pode ser len(n) - n.count(' ')
l = len(n.split()[0]) # ou n.find(' ')
print(f'''Seu nome com letras maiusculas é {P}, já seu nome com letras minusculas é {p}\nE seu nome possui {L} letras, já o seu primeiro nome possui {l} letras''' )
'''D23'''
'''ú = str(input('Digite um número de 4 digitos '))
print(f'Unidade: {ú[3]} \nDezena: {ú[2]}\nCentena: {ú[1]}\nMilhar: {ú[0]}')  não funciona, ainda não aprendi como faz, aula 10'''
num = int(input('Digite um número ate 9999 '))
u = num // 1 % 10
d = num // 10 % 10
cen = num // 100 % 10
mi = num // 1000 % 10
print(f'Unidade {u}\nDezena {d}\nCentena {cen}\nMilhar {mi}')
'''D24'''
C = str(input('Qual e o nome de sua cidade? ')).strip()
print(f'O nome da sua cidade começa com Santo? \n{C[:5].upper() == 'SANTO'}')
'''D25'''
N = str(input('Qual seu nome? ')).upper().split()
print(f'Seu nome tem Silva? ','SILVA' in N) # in e um operador e não um metodo
'''D26'''
f = str(input('Digite uma frase ')).upper().strip()
print(f'Nesta frase a letra A aparece {f.count('A')}\nO primeiro A aparece {f.find('A') + 1}\nO ultimo A aparece em {f.rfind('A') + 1}')
'''D27'''
Nome = input('Qual seu nome? ').strip()
ome = Nome.split()

print(f'Seu primeiro nome é {ome[0]}\nSeu ultimo nome é {ome[- 1]}')
