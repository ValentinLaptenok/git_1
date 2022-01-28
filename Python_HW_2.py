
import math

item_1 = 5
item_2 = 6
result_sum = item_1 + item_2
print(result_sum)

result_subtr = item_2 - item_1
print(result_subtr)

result_multi = item_1 * item_2
print(result_multi)

result_exp = item_1 ** item_2       # возведение в степень
print(result_exp)

result_m_exp = math.pow(item_1, item_2)     # возведение в степень с помощью math
print(result_m_exp)

print('====================')

result_s_root = item_2 ** (0.5)     # кв корень
print(result_s_root)

result_m_s_root = math.sqrt(item_2)     # кв корень math
print(result_m_s_root)

result_mp_s_root = pow(item_2, 0.5)     # кв корень pow
print(result_mp_s_root)

print('====================')

item_1 = 5          # odd  нечетное
item_2 = 6          # even четное
result_division = item_1 / item_2
print('result_division= ', result_division)

result_m_floor = math.floor(result_division)     # округлить до ближайшего целого меньшего чем result_division
print(result_m_floor)

result_m_ceil = math.ceil(result_division)   # result_division округлить до ближайшего целого большего чем result_division
print(result_m_ceil)

result_int = int(result_division)    # result_division округлить до ближайшего целого через явное приведение.
print('округлить до ближайшего целого через явное приведение', result_int)

result_no_division_loss = item_1 // item_2    # в которой вы разделите item_1 на item_2 без остатка.
print(result_no_division_loss)

result_division_loss = item_1 % item_2       #  остаток от деления item_1 на item_2
print(result_division_loss)

item_3 = 5          # присваивания
print(item_3)
item_3 += 10
print(item_3)
item_3 -=5
print(item_3)
item_3 *= 3
print(item_3)
item_3 /= 2
print(item_3)
item_3 **= 2
print(item_3)
item_3 **= (0.5)
print(item_3)
item_3 %= item_3
print(item_3)

print('====================')

b_item_t = True
b_item_f = False

b_item_relult_sum = b_item_t + b_item_f
print(b_item_relult_sum)

b_item_relult_subtr = b_item_t - b_item_f
print(b_item_relult_subtr)

b_item_relult_multi = b_item_t * b_item_f
print(b_item_relult_multi)

b_item_relult_division = b_item_t / b_item_f        # ожидаемая ошибка
print(b_item_relult_division)

b_item_1_int = int(b_item_t)
print(b_item_1_int)

b_item_2_int = int(b_item_f)
print(b_item_2_int)