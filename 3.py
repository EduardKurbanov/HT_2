"""
3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".

        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]

        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""

list_l = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
list_l = [i for i in list_l if i]
print("Expected output: {0}".format(list_l))
