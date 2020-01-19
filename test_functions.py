def f_prime(x):
    for i in range(2, x + 1):
        if x % i == 0: break
    return x == i
print('является ли простым числом', ':',f_prime(779))


def f_all_deviders(x):
    list = []
    for i in range(1, x + 1):
        if x % i == 0: list == list.insert(0, i)
    return list
print('список всех делителей без остатка', ':', f_all_deviders(779))


def f_max_prime_devider(x):
    list = f_all_deviders(x)
    list_2 = []
    for i in range (0, len(list)-1):
        if f_prime(list[i]): list_2 == list_2.insert(i, list[i])
    return list_2[0]
print('максимальный простой делитель без остатка', ':', f_max_prime_devider(779))

def f_max_devider(x):
    list = []
    for i in range(1, x + 1):
        if x % i == 0: list == list.insert(0, i)
    return list[0]
print('максимальный делитель без остатка', ':', f_max_devider(779))

