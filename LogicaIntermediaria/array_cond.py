def conversao(lista):
    lista_modificada = []
    for num in lista:
        if num %2 == 0:
            lista_modificada.append(num*2)
        else:
            lista_modificada.append(num)
    
    lista_modificada.reverse()
    return lista_modificada

my_list = [1, 2, 3, 4, 5]
resultado = conversao(my_list)
print(f"Lista original {my_list}")
print(f"Lista modificada {resultado}")