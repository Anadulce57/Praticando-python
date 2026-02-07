#list = [1, 2, 3, 4, 5]
#print(len(list))

def count_elements(list):
    if list == []:
        return 0
    return 1 + count_elements(list[1:])

my_list= [1, 2, 3, 4, 5]
print(count_elements(my_list))