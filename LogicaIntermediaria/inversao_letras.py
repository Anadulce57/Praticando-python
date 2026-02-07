def inverter_string(string):
    if len(string) <= 1:
        return string 
    return string[-1] + inverter_string(string[:-1])

text = input("Digite o seu texto pra conversão: ")
print(inverter_string(text))