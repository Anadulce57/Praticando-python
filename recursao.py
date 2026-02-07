"""
def sauda2(nome):
    print("Como vai " + nome + "?")

def tchau():
    print("ok, tchau!")

def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome)
    print("preparando pra dizer tchau...")
    tchau

sauda("Ana")
"""

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)
    
print(fat(3))