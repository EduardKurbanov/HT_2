"""
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для

   роботи захардкодити свій.

                Приклад словника (не використовувати):

                {'a': 1, 'b': 3, 'c': 1, 'd': 5}

                Очікуваний результат:

                {'a': 1, 'b': 3, 'd': 5}
"""

input_raw = {"CPU": "AMD Phenom II X 2 550",
             "RAM": "Patriot psd32h1600 8GB",
             "Matherboard": "ASUS M4A78T-E",
             "HDD": "Samsung 320GB",
             "Power_supply": "380Wt",
             "RAM2": "Patriot psd32h1600 8GB",
             }

result = {}

for key, value in input_raw.items():
    if value not in result.values():
        result[key] = value

print(result)
