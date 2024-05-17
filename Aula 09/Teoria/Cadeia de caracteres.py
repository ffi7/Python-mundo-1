# 'curso em Video python' isto e uma cadeia de caracteres ou uma str, sempre está entre ' ' ou entre " " ou """ """ ou ''' '''
Frase = 'Curso em Vídeo Python' # vai guardar na memoria, mas como? 
# cria varios miniespaços e coloca cada caracteres (e vai colocando um número para cada caractere) em um desses miniespaço: como se fosse varios quadrados, ou: 
# -C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n- (V e diferente de v, letras maisculas são diferentes de minusculas)
#  0 1 2 3 4 5 6 7 8 9 ... 20  no total da 21 microespaços na memoria. E tudo que está em um espaço de memoria(sempre começa com 0)
# Fatiamento(pegar pedaços da str) de str: 
print(Frase[9]) # [] é a estrutura que indentifica uma lista + pra frente
print(Frase[3:9]) # seleciona uma mini cadeia dentro da cadeia maior, ou seja vai do 3 ate o 9 porem excluira o 9, então ficara: so em 
print(Frase[2:21]) # mas não tem o 21 vai ate o 20, porem ele vai parar no 20 pois não conta o ultimo, então vai ficar: rso em Vídeo Python
print(Frase[3:9:2]) # por causa do 2 vai saltar de 2 em 2, vai ficar: s mV
print(Frase[:5]) # começa do caractere 0, ou seja e igual a [0:5]
print(Frase[4:]) # so dei o inicio portanto vai do 4 ate o fim, mesma coisa de [4:21]
print(Frase[2::3]) # vai do 9 ate o 21, porem como tem o 3 ele vai pular de 3 em 3.
# Análise(pegar informações da str) da str
print(len(Frase)) # len significa comprimento, ou seja 21 caracteres
print(Frase.count('o')) # conta quantas vezes aparece o 'o' minusculo, está e a diferença entre o 'O' e o 'o'
print(Frase.count('O'))
print(Frase.count('o', 0, 13)) # fatiamento do 0 ate o 13(12) + a contagem de quantas vezes aparece o 'o', aparece 1 vez pois não conta o ultimo
print(Frase.find('deo')) # quantas vezes ele encontrou o 'deo', vai mostrar em que momento começou o 'deo'
print(Frase.find('Androide')) # não existe então ele mostrara -1
print('Curso' in Frase) # falara se tem a str 'Curso' se sim então mostrara True, se não mostrara False
# transformação(uma lista de str e imutavel mas pode ser mudado atraves de metodos) da str
print(Frase.replace('Python', 'Androide')) # substituira 'Python' por 'Androide', mas não armazena, para armazenar e usar em outro print seria necessario uma variavel
print(Frase.upper()) # colocara tudo em maiuscula, sempre coloque ()
print(Frase.upper().count('O'))
print(Frase.lower()) # colocara tudo em minusculo
print(Frase.capitalize()) # colocara tudo em minusculo, e a primeira letra ficara em maiusculo
print(Frase.title()) # analizara quantas palavras tem na str, localizando os espaços(cada espaço sera uma nova palavra), e colocara cada inicial de uma palavra em maiuscula
# divisão
print(Frase.split()) # não armazena
r = Frase.split()# (tem mais funções)# dividira a str a partir dos espaços: então ficara assim 'Curso'(0,1,2,3,4) 'em'(0,1) 'Vídeo'(0,1,,2,3,4) ..., e armazenará em uma nova lista 
print(r[2] [1]) 
print('-'.join(r)) # junta os elementos que forão separados no split e colocara - entre elas, se quiser colocar espaço basta substituir o '-' por ' '
print(('-').join(Frase))

frase = '   Aprenda Python   '
print(len(frase))
print(frase.strip()) # remove os espaços inuteis, exemplo: '   Aprenda Python   ', ficara: 'Aprenda Python'
print(frase.rstrip()) # remove somente os espaços inuteis da direita
print(frase.lstrip()) # remove somente os espaços inuteis da esquerda
print(len(frase.strip()))
