"""
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".

   Елементами списку повинні бути як рядки, так і числа.
"""

while True:
    try:
        print("input through ','")
        enter_mas = list(input("input list: ").split(","))
        sent_str = ""
        for i in enter_mas:
            sent_str += str(i)
        print("{0} -> {1}".format(enter_mas, sent_str))

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)

        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
