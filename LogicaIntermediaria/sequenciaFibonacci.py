# Com loops
"""
n = int(input("Quantos termos de Fibonacci você quer? "))

a = 0
b = 1

if n <= 0:
    print("Por favor, insira um número positivo.")
elif n == 1:
    print([a])

elif n == 2:
    print([a, b])

else:
    my_list = []

    my_list.extend([a, b])
    for _ in range(n - 2): # Se N for 2, range(0) não roda 
        proximo = a + b # for _ -> utilizo a função range para gerar uma sequencia de números que não etá em função de i eu não uso i só quero que siga uma sequência 
        my_list.append(proximo)
        a = b
        b = proximo
    
    print(my_list)
"""

# Mas se eu fizesse por função??

def gerar_fibonacci(n_termos):
    if n_termos <= 0:
        return []
    elif n_termos == 1:
        return [0]
    elif n_termos == 2:
        return [0, 1]
    else:
        a, b = 0, 1
        fibonacci_sequence = []
        fibonacci_sequence.extend([a, b])

        for _ in range(n_termos - 2):
            proximo = a + b
            fibonacci_sequence.append(proximo)
            a = b 
            b = proximo
        
        return fibonacci_sequence

num_t = int(input("Quantos termos de Fibonacci você quer? "))

if num_t <= 0:
    print("Por favor, insira um número positivo.")
else: 
    resultado = gerar_fibonacci(num_t)
    print(f"Os primeiros {num_t} termos são: {resultado}")