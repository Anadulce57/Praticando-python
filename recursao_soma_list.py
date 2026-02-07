def soma(list):
    if list == []:
        return 0
    return list[0] + soma(list[1:])

my_list = [2, 4, 6]
print(my_list)
print(f"Lista modificada pela soma: {soma(my_list)}")