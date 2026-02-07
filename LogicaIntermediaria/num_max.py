def max_num(list):
    if len(list) == 2:
        return list[0] if list[0] > list [1] else list[1]
    sub_max = max_num(list[1:])
    return sub_max if list[0] < sub_max else list[0]

my_list = [6, 2, 4]
print(max_num(my_list))