from functions import f_prime, f_all_deviders, f_max_prime_devider, f_max_devider


def f_prime_test():
    y = f_prime(779)
    if y == 0 : print('test1 is ok')
    else : print('test1 is failed')
f_prime_test()


def f_all_deviders_test():
    list_all_deviders = [779, 41, 19, 1]
    list_y = f_all_deviders(779)
    if list_y == list_all_deviders : print('test1 is ok')
    else : print('test1 is failed')
f_all_deviders_test()

def f_max_prime_devider_test():
    max_prime_devider = 41
    y = f_max_prime_devider(779)
    if y == max_prime_devider : print('test1 is ok')
    else : print('test1 is failed')
f_max_prime_devider_test()

def f_max_devider_test():
    max_devider = 779
    y = f_max_devider(779)
    if y == max_devider : print('test1 is ok')
    else : print('test1 is failed')
f_max_devider_test()

# тоже c помощью Pytest не получается, хотя модуль pytest я добавил.
# При вводе команды pytest выводится сообщение, что:
#'pytest' is not recognized as an internal or external command,
# operable program or batch file.

def test_f_prime():
    assert f_prime(779) == 0
def test_f_all_deviders():
    assert f_all_deviders(779) == [779, 41, 19, 1]
def test_f_max_prime_devider():
    assert f_max_prime_devider(779) == 41
def test_f_max_devider():
    assert f_max_devider(779) == 779
