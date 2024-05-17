print('Olá, este é uma calculadora que mostra o dobro, o triplo e a raiz quadrada de um número' )
n = float(input('Digite um valor '))
dob = n * 2
tri = n * 3
r1 = n ** (1/2)
print(f'o dobro do seu número é {dob} \n o triplo desse número é {tri} \n já sua raiz quadrada é {r1}')
print('olá, iremos te ajudar a descobrir a media da sua nota')
nt = float(input('Qual foi a nota da sua primeira prova? '))
nt2 = float(input('Qual foi a nota da sua segunda prova? '))
ntf = (nt + nt2) / 2
print(f'a sua media é {ntf}')
print('Olá, este é um conversor de metros para quilometros, para centrimetros e para milímetros')
me = float(input('Digite uma distancia em metros '))
km = me * 1000
ce = me / 100
mil = me / 1000 # ou ce / 10
print(f'o seu valor em quiklometros é {km}km \n o seu valor em metros é {me}m \n o seu valor em centimetros e {ce}cm \n e o seu valor em milimetros é {mil}mm')
print('Olá, este e um progama que calcula automaticamente as tabuadas de 1 a 10 de um número escolhido por você')
ntq = float(input('Digite um valor '))
nt1 = ntq * 1
nt2 = ntq * 2
nt3 = ntq * 3
nt4 = ntq * 4
nt5 = ntq * 5 
nt6 = ntq * 6
nt7 = ntq * 7
nt8 = ntq * 8
nt9 = ntq * 9 
nt10 = ntq * 10
print(f'o seu número na tabuada em ordem crescente de 1 a 10 te valor de: \n {nt1} \n {nt2} \n {nt3} \n {nt4} \n {nt5} \n {nt6} \n {nt7} \n {nt8} \n {nt9} \n {nt10}')
print('Olá, este e um progama que converte o seu dinheiro em reais para dólares americanos(2018)')
nRS = float(input('Quantos reais você possui? R$ '))
nD = nRS / 5.03
print(f'você pode comprar {nD} dólares, no dia 18/03/2024')
print('Olá, iremos ajudar você a descobrir quantos reais e litros de tinta você gatará para pintar uma parede')
pl = float(input('Qual a largura dessa parede? '))
pa = float(input('Qual a altura dessa parede? '))
A = pl * pa
tl = A / 2
RSlt = tl * 41.31
print(f'você precisará de {tl} litos de tinta, e considerando que um litro de tinta está valendo R$40.31 você pagará {RSlt} ')
print('Olá, iremos te ajudara descobrir o preço de um produto em uma liquidação de 5%')
pe = float(input('Qual o preço desse produto? '))
pf = pe * (5 / 100) # mais rapido se fosse: = pe - (pe * 5 / 100)
pff = pe - pf
print(f'Apos o desconto de 5% você pagará {pff:.2} reais')
print('Olá, iremos ajudar você a calcular o seu salário após um aumento de 15%')
sa = float(input('Qual o seu salário? '))
sf = sa / (15 / 100) # mais rapido se fosse: sf = sa - (sa / 15 / 100)
sff = sa + sf
print(f'Após esse aumento você ganhará {sff:.2}')
print('Olá, este e um conversor de temperatura, graus Celsius para graus fahrenheit')
C = float(input('Escolha uma temperatura em graus Celsius '))
F = (C * 1.8) + 32 # ou 9 * C / 5 + 32 se parentese pois aplica se a ordem de precendencia
print(f'{C}°C equivale a {F} fahrenheit')
print('Olá, este e um progama que fara o calculo de quanto você vai pagar por um carro alugado que custa R$60.00 por dia e R$0.15 por km')
ld = float(input('Por quantos dias o carro foi alugado? '))
lk = float(input('Quantos km foram rodados? '))
vf = (id * 60) + (0.15 * lk)
print(f'No final do aluguel você pagará R${vf:.2}')
