from unit06_pac1 import my_module2


try:
    if my_module2.a == 'pac1\\my_module2.py':
        print('1')
except NameError:
    print('2')


from unit06_pac1.pac2 import my_module1


try:
    if my_module1.a == 'pac1\\pac2\\my_module1.py':
        print('3')
except NameError:
    print('4')
