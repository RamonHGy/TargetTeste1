string = "Thanos gamora"
def inverter_string(s):
    string_invertida = ''
    comprimento = len(s)
    
    # Iterar sobre a string do final para o começo
    for i in range(comprimento - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida


# Inverter a string
resultado = inverter_string(string)

# Exibir o resultado
print(f"String invertida: {resultado}")
