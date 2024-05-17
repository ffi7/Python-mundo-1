variavel = ('exemplo')
print(f'este {variavel} e demais !')
n1 = int(input("digite um valor "))
ms1= str(input('Qual seu nome? '))# str não e necessario, automaticamente o input tem classe string
n2 = float(input('digite um valor '))
s = n1 + n2
print(type(n1))
print(type(ms1))
print(type(n2))
# serve para deixar uma nota, sera ignorado na hora do terminal
print ('o valor que você digitou é {n1}, seu nome é {ms1}, o segundo valor que você digitou é {n2}, e a soma entre {n1} e {n2} vale {s} ')
n = bool(input('digite um valor'))# A resposta sera True se tiver um valor, porem se não for colocado nenhum valor a resposta sera False
print(n)  # bool tem quase a mesma função de is...({isnumeric()}, {isalpha()}[sé e letra], {isalnum()}[é número e letra, ex: 3A 4b 7 oi], {isupper()}[somente letra maiscula, ex: OI], etc...) exemplo se oque for digitado for um número e o print estiver assim print(n.isnumeric) a resposta sera True porem se não for um número a resposta sera False
# sempre deixar uma linha vazia no final
