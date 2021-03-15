#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
print('$$' * 8)
print('Calculo de PREÇO')
print('$$' * 8)
preço = float(input('\nQual o valor do Produto? R$'))
print('\n1 - À vista dinheiro/cheque')
print('2 - No cartão de credito')
pagamento = int(input('\nDigite o numero da opção desejada: '))
if pagamento == 1: #à vista dinheiro/cheque: 10% de desconto
    print('No pagamento à vista vc tem 10% de desconto e paga R${:.2f}'.format(preço - (preço * 10 / 100)))
elif pagamento == 2:
    parcela = int(input('Em quantas vezes quer pagar? '))
    if parcela == 1: #à vista no cartão: 5% de desconto
        print('No pagamento à vista no cartão vc tem 5% de desconto e paga R${:.2f}'.format(preço - (preço * 5 / 100)))
    elif parcela < 3: #em até 2x no cartão: preço normal
        print('O valor escolhido é de {}x de R${:.2f}'.format(parcela, preço / parcela))
    else: #3x ou mais no cartão: 20% de juros
        print('Na opção escolhida vc paga 20% de JUROS. {}x R${:.2f}'.format(parcela, (preço + preço * 20 /100) / parcela))
else:
    print('OPÇÃO INVALIDA.')
