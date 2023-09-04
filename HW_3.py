int_item = 10    # Создать переменную int_item со значением 10
comp_item = 18   # Создать переменную comp_item со значением 18
mult_int = int_item*2    # Создать переменную mult_int в которй умножите int_item на 2
item_2 = True           # Создать переменную item_2 со значением True
item_3 = False          # Создать переменную item_3 со значением False
item_4 = 0              # Создать переменную item_4 со значением 0
item_5 = 1              # Создать переменную item_5 со значением 1

usd_item = 'USD'        # Создать переменную usd_item со значением ‘usd’
sd_usd_rate = 1         # Создать переменную usd_usd_rate со значением 1
eur_item = 'EUR'        # Создать переменную eur_item со значением ‘eur’
usd_eur_rate = 0.92     # Создать переменную usd_eur_rate со значением 0.92
uah_item = 'UAH'        # Создать переменную uah_item со значением ‘uah’
usd_uah_rate = 0.027    # Создать переменную usd_uah_rate со значением 0.027
chf_item = 'CHF'        # Создать переменную chf_item со значением ‘chf’
usd_chf_rate = 0.91     # Создать переменную usd_chf_rate со значением 0.91
rub_item = 'RUB'        # Создать переменную rub_item со значением ‘rub’
usd_rub_rate = 0.012    # Создать переменную usd_rub_rate со значением 0.012
byn_item = 'BYN'        # Создать переменную byn_item со значением ‘byn’
usd_byn_rate = 0.40     # Создать переменную usd_byn_rate со значением 0.40
if mult_int > comp_item:                # Сделать if в котором будет условие: если mult_int больше comp_item
    print('Переменная mult_int больше', comp_item)   # то вывести в консоль (“Переменная mult_int больше”, comp_item)
div_int = int_item/2        # Создать переменную div_int в которй разделить int_item на 2
if div_int < comp_item:          # Условие если div_int меньше, чем comp_int, то вывести в консоль
    print('Переменная div_int меньше',comp_item)
item_1 = 10 + int_item  # Создать переменную item_1 в которй прибавить 10 к переменной int_item
if item_1 < comp_item:          # Сделать if в котором будет условие: если item_1 меньше comp_item
    print('Переменная item_1 меньше', comp_item)
else:
    print('Переменная item_1 больше или равна',comp_item)

if item_2:          # Сделать if в котором будет условие: если item_2,
    print('Переменная item_2 =',item_2)  # то вывести в консоль (“Переменная item_2 = ”, item_2)
else:                  # иначе, вывести в консоль (“Переменная item_2 = ”, item_3)
    print('Переменная item_2',item_3)
if item_3:
    print('Переменная item_3 =', item_2)
else:
    print('Переменная item_3 =', item_3)
if item_5:
    print('Переменная item_5 =', item_5)
else:
    print('Переменная item_5 = ', item_4)
if item_4:
    print('Переменная item_4 =', item_5)
else:
    print('Переменная item_4 = ', item_4)
currency_convertor = item_2      # Создать переменную currency_convertor со значением item_2
# Сделать if в котором будет условие: если currency_convertor, то выполнять следующие шаги задания
# Внутри if currency_convertor сделать следующие If условия :
#                     31.1 Создать переменную currency_usd со значением usd_item
#                     31.2 Создать переменную target_currency со значением eur_item
#                     31.3 Создать переменную target_currency_amount значением 50
#                     31.4 Создать переменную currency_result со значением 0
#                     31.4 Сделать if в котором будет условие: если target_currency равен ‘eur’, то в теле этого if в
#                 значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и
#          usd_eur_rate. Результат вывести в консоль (target_currency_amount, eur_item, “=”, currency_result, usd_item)
#         31.5 Сделать elif в котором будет условие: если target_currency равен ‘uah’, то в теле этого if в значении
#            переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_uah_rate.
#                     Результат вывести в консоль (target_currency_amount, uah_item, “=”, currency_result, uah_item)
#                     31.6 Сделать elif с остальными валютами

if currency_convertor:
  currency_usd = usd_item
  target_currency = chf_item
  target_currency_amount = 50
  currency_result = 0
if target_currency == 'EUR':
    currency_result = target_currency_amount * usd_eur_rate
    print(target_currency_amount, eur_item, "=", currency_result, usd_item)
elif target_currency == 'UAH':
    currency_result = target_currency_amount * usd_uah_rate
    print(target_currency_amount, uah_item, "= ", currency_result, usd_item)
elif target_currency == 'RUB':
    currency_result = target_currency_amount * usd_rub_rate
    print(target_currency_amount, rub_item, "= ", currency_result, usd_item)
elif target_currency == 'BYN':
    currency_result = target_currency_amount * usd_byn_rate
    print(target_currency_amount, byn_item, "= ", currency_result, usd_item)
elif target_currency == 'CHF':
    currency_result = target_currency_amount * usd_chf_rate
    print(target_currency_amount, chf_item, "= ", currency_result, usd_item)
else:
    print('Переменная currency_convertor = ', item_3)







