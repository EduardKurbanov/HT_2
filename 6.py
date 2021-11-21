"""
6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник. Дані можна "захардкодити".

        Sample Dictionary :

        dict_1 = {1:10, 2:20}

        dict_2 = {3:30, 4:40}

        dict_3 = {5:50, 6:60}

        Expected Result : dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dict_d1 = {1: 10, 2: 20}
dict_d2 = {3: 30, 4: 40}
dict_d3 = {5: 50, 6: 60}

for d in (dict_d1, dict_d2, dict_d3):
    dict_d1.update(d)
print("Expected Result : dict_1 = {0}".format(dict_d1))
