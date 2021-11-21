"""
7. Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.

                Приклад словника (можете використовувати свій):

                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

                Вихідний результат:

                MIN: 10

                MAX: 60
"""

my_dict = {8: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('MIM: ', my_dict[key_min])
print('MAX: ', my_dict[key_max])
