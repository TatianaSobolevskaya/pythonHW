import math
item_1 = 2      # Создать переменную item_1 типа integer.
item_2 = 10     # Создать переменную item_2 типа integer.
result_sum = item_1 + item_2    # Создать переменную result_sum в которой вы суммируете item_1 и item_2.
print('result sum',result_sum)   # Вывести result_sum в консоль.
# Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = min(item_1, item_2, result_sum)-max(item_1,item_2,result_sum)
print('result_subtr =',result_subtr)   # Вывести result_subtr в консоль.
result_multi = item_1 * item_2   # Создать переменную result_multi в которой вы умножаете item_1 на item_2.
print('result multi =', result_multi) # Вывести result_multi в консоль.
result_exp = item_1 ** item_2   # Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
print('result_exp =', result_exp)   # Вывести result_exp в консоль.
# Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(item_1, item_2)
print('result_m_exp =', result_m_exp)    # Вывести result_m_exp в консоль.
# Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_1 ** (0.5)
print('result_s_root =', result_s_root)   # Вывести result_s_root в консоль.
# Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя
# библиотеку math.
result_m_s_root = math.sqrt(item_1)
print('result_m_s_root =', result_m_s_root)     # Вывести result_m_s_root в консоль.
# Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя
# библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_1, 0.5)
print('result_mp_s_root =', result_mp_s_root)   # Вывести result_mp_s_root в консоль.
item_1 = 7    # Присвоить переменной item_1 odd значение
item_2 = 4    # Присвоить переменной item_2 even значение
result_division = item_1/item_2   # Создать переменную result_division в которой вы разделите item_1 на item_2.
print('result division =', result_division) # Вывести result_division в консоль.
# Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)
print("Результат округления в меньшую сторону =", result_m_floor)     # Вывести result_m_floor в консоль.
# Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)
# Вывести result_m_ceil в консоль.
print("Результат округления в большую сторону =", result_m_ceil)
# Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(result_division)
# Вывести result_int в консоль.
print("Результат округления  =", result_int)
# Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1//item_2
# Вывести result_no_division_loss в консоль.
print("Результат деления  =", result_no_division_loss)
# Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2
# Вывести result_division_loss в консоль.
print("остаток от деления  =", result_division_loss)
# Создать переменную item_3 и присвоить ей целое число
item_3 = 1
# Прибавить 10 к item_3 с присвоением.
item_3 = item_3 + 10
# Вывести item_3 в консоль.
print("результат =", item_3)
# Отнять 5 от item_3 с присвоением.
item_3 = item_3 - 5
# Вывести item_3 в консоль.
print("рез. вычетания =", item_3)
# Умножить item_3 на 3 с присвоением.
item_3 = item_3 * 3
# Вывести item_3 в консоль.
print("рез. умножения =", item_3)
# Разделить item_3 на 2 с присвоением.
item_3 = item_3/2
# Вывести item_3 в консоль.
print("рез. деления =", item_3)
# Возвести в степень 2 item_3 с присвоением.
item_3 = item_3 ** 2
# Вывести item_3 в консоль.
print("рез. возведения в степень =", item_3)
# Найти квадратный корень item_3 с присвоением.
item_3 = math.pow(item_3, 0.5)
# Вывести item_3 в консоль.
print("рез. квадратного корня =", item_3)
# Присвоить остаток от деления item_3
item_3 = item_3 % 2
# Вывести item_3 в консоль.
print("рез. остаток от деления =", item_3)
# Создать переменную b_item_t и присвоить True
b_item_t = True
# Создать переменную b_item_f и присвоить False
b_item_f = False
# Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum = b_item_f + b_item_t
# Вывести b_item_relult_sum в консоль.
print("b item result sum", b_item_result_sum)
# Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_relult_subtr = b_item_t - b_item_f
# Вывести b_item_relult_subtr в консоль.
print("b item result subtr =", b_item_relult_subtr)
# Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_relult_multi = b_item_t * b_item_f
# Вывести b_item_relult_multi в консоль.
print("b item result multi =", b_item_relult_multi)
# Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
# Вывести b_item_relult_division в консоль. (Получить ошибку)
if b_item_f != 0:
    b_item_relult_division = b_item_t / b_item_f
    print("Результат деления =", b_item_relult_division)
else:
     print('Нельзя делить на ноль!')
# Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)
# Вывести b_item_1_int в консоль.
print("b item 1 int =", b_item_1_int)
# Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int
b_item_2_int = int(b_item_f)
# Вывести b_item_2_int в консоль.
print("b item 2 int =", b_item_2_int)