salario_joao = float(input('Digite o valor do salario de João: '))
valor_conta1 = float(
    input('Digite o valor da primeira conta que João deve pagar: '))
valor_conta2 = float(
    input('Digite o valor da segunda conta que João deve pagar: '))
multa = 0.02
valor_total_contas = valor_conta1 + valor_conta2
valor_multa = valor_total_contas * multa
valor_restante = salario_joao - valor_total_contas - valor_multa

print('Após o pagamento das duas contas, sobrará',
      valor_restante, 'reais para o João')
