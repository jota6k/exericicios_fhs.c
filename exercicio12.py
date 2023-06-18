salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_funcionario = float(
    input("Digite o valor do salário do funcionário: "))

percentual_funcionario = salario_funcionario / salario_minimo

print("O funcionario recebe", percentual_funcionario, "salários mínimos.")
