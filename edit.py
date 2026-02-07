def contagem(n):
    # Caso Base: Condição de parada. Quando n chega a 0, paramos.
    if n <= 0:
        print("Fim da contagem!")   
        return # Parar a execução da chamada atual
    # Passo Recursivo:
    print(n) # Faz o trabalho para o problema atual (imprime n)
    contagem(n - 1) # Chama a si mesma para resolver uma versão menor do problema (n-1)

# Testando:
print(contagem(3))
