item = 'name '                                   # 1) Создать переменную типа String
item_1 = 2                                      # 2) Создать переменную типа Integer
item_2 = 2.2                                    # 3) Создать переменную типа Float
item_3 = bytes([46, 46, 46])                    # 4) Создать переменную типа Bytes
item_4 = list('abc')                            # 5) Создать переменную типа List
item_5 = tuple('abc')                           # 6) Создать переменную типа Tuple
item_6 = set("hello")                           # 7) Создать переменную типа Set
item_7 = frozenset("hello")                     # 8. Создать переменную типа Frozen set
item_8 = dict(one=1, two=2, three=3)            # 9) Создать переменную типа Dict
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print("String--> ", item, '\n'"Int-->", item_1, '\n'"Float-->",item_2, '\n'"Bytes-->",item_3, '\n'"List-->", item_4,
      '\n' "Tuple-->", item_5, '\n'"Set-->", item_6, '\n'"Frozen set-->", item_7, '\n'"Dict-->", item_8)
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
item_9 = 'last name '
item_10 = 'name of dog'
item_11 = item + item_9 + item_10
print(item_11)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(item, item_1)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(item, "+", item_1)