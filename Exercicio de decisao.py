sal_empregados = int(input("Digite o salario dos trabalhadores: "))
if sal_empregados<=280:
    percentual = 20
    perc_aum_sal = sal_empregados * 2/10
    novo_sal = perc_aum_sal + sal_empregados
elif 280<sal_empregados<=700:
    percentual = 15
    perc_aum_sal = sal_empregados*15/100
    novo_sal = perc_aum_sal + sal_empregados
elif 700<sal_empregados<=1500:
    percentual = 10
    perc_aum_sal = sal_empregados * 1/10
    novo_sal = perc_aum_sal + sal_empregados
print(f'O salario antes do reajuste é {sal_empregados}!')
print(f'O percentual aplicado foi {percentual}%')
print(f'O valor do aumento é de {perc_aum_sal}')
print(f'O novo salario vai ser: {novo_sal}')
print("\nFIM DO PROGRAMA")