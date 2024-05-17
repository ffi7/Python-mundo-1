# metodo sempre tem parentese variavel.metodo()
# ESTRUTURA SEQUENCIAL
'''
1 comando
2 comando
3 comando
.
.
.
'''
# ESTRUTURA COM IF\CONDIÇÃO
# Nesta condição sempre sera somente uma condição a ser executada
'''
if variavel.metodo(): # Bloco True
    1 # use tab para funcionar
    2
    3
    4
else: # Bloco False
    2
    3
    4
    1
variavel.metodo()
'''
exemplo = int(input('Quantos anos tem seu carro? '))
if exemplo <=3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
print('--FIM--') # esse funciona para os dois
# Condição Simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('Seu carro é novo!' if tempo<=3 else 'Seu carro é velho!')
print('--FIM--')
# Outros exemplos
n = str(input('Qual seu nome? ')).strip()
r = n.lower()
# Estrutura condicional simples
if 'felipe' in r:
    print('Que nome lindo você tem!')
print(f'Bom dia, {n}')
# Estrutura condicional composta
if 'felipe' in r:
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {n}')

n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite sua segunda nota '))
me = (n1 + n2)/2
print(f'A sua media foi {me:.1f}')
if me > 7.5:
    print('Sua media foi boa, PARABENS!')
if 6 <= me <= 7.5 :
    print('Você passou de ano, parabens!')
if me <= 5.9 :
    print('Sua media foi ruim, ESTUDE MAIS!')
