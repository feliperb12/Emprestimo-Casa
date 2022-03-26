casa= float(input('Qual o preço da casa? R$'))
salário=float(input('Qual é o seu salário? R$'))
anos= int(input('Quantos anos você quer financiar a casa?'))
prestação= casa/(anos*12)
MÍNIMO= salário*30/100
print(f'Para pagar uma casa que tem o valor de R${casa} em {anos} anos, a prestação será de R${prestação}')

if prestação<=MÍNIMO:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo não autorizado!')