print('SIMULADOR DE EMPRÉSTIMOS')

casa = float(input('Digite o valor da casa: ').replace('.', '').replace(',', '.'))
sal = float(input('Digá seu salário: '))
anos1 = float(input('Em quantos anos você gostaria de parcelar? '))

cores = {'amarelo' : '\033[1;49;33m',
        'limpa' : '\033[m' ,
         'vermelho' : '\033[1;49;31m' }


meses = anos1 * 12
parcela = casa / meses


print('\n O valor da parcela será de R$ {:.1f}'.format(parcela))

if parcela > sal * 0.3:
    print('{} Que pena, parece que a parcela cobre 30% ou mais de seu salário! {}'.format(cores ['vermelho'] , cores['limpa']))
else:
    print('{} Parábens, você consegue pagar! {}'.format(cores ['amarelo'] , cores['limpa']))