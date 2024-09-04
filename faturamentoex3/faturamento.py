import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

# pegar os valores de faturamento que são maiores que 0
faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Encontrar o menor e o maior valor de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcular a média mensal
media_mensal = sum(faturamentos) / len(faturamentos)

# Calcular o número de dias com faturamento acima da média
dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

# Exibir os resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
