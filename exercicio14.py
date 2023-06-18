ano_nascimento = int(input('Digite o ano de nascimento da pessoa: '))
ano_atual = int(input('Digite o ano atual: '))
idade_anos = ano_atual - ano_nascimento
idade_meses = (ano_atual - ano_nascimento) * 12
idade_dias = (ano_atual - ano_nascimento) * 365
idade_semanas = (ano_atual - ano_nascimento) * 48

print('A idade da pessoa em anos é:', idade_anos, 'anos')
print('A idade da pessoa em meses é:', idade_meses, 'meses')
print('A idade da pessoa em dias é:', idade_dias, 'dias')
print('A idade da pessoa em semanas é:', idade_semanas, 'semanas')
