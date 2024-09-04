#colocando os estados em um dicionario chave e valor
faturamento = {
"SP": 67836.43,
"RJ": 36678.66,
"MG": 29229.88,
"ES": 27165.48,
"Outros": 19849.53
}
#somando o futaremento de todos
futaramento_total = sum(faturamento.values())

#calculando o percentual de cada estado
percentual = {estado: (valor / futaramento_total) * 100 for estado, valor in faturamento.items()}

# resultado
for estado, percentual in percentual.items():
    print(f"Percentual de {estado}: {percentual:.2f}%")