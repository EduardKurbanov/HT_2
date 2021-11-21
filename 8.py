"""
8. Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа,

   а значення для цих ключів - це квадрат ключа.

        Приклад виводу при введеному значенні 5 :

        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

while True:
    try:
        in_num = int(input("enter the number: "))
        dict_d = {x: x ** 2 for x in range(in_num + 1)}
        print(dict_d)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
