
def Lib_obmen(kol_rub):                     # конвертирование в разные валюты
    print('Конвертированная сумма в USD =', int(kol_rub) / 2.5)
    print('Конвертированная сумма в EUR =', int(kol_rub) / 3)
    print('Конвертированная сумма в CHF =', int(kol_rub) / 2.82)
    print('Конвертированная сумма в GBP =', int(kol_rub) / 3.49)
    print('Конвертированная сумма в CNY =', int(kol_rub) / 0.4066)


def Lib_wwod_summ(kol_rub):     # проверка - введены символы, пробел или ничего, отрицательное число
    if kol_rub.isalpha():
        print('Вы ввели не число. Введите число.')
    if kol_rub.isspace() or len(str(kol_rub)) == 0:
        print('Вы ввели пустое поле. Введите число.')
    if len(str(kol_rub)) > 1 and str(kol_rub)[0]=='-':
        print('Введите положительное число.')

def Lib_vybor_val(valuta, kol_rub):     # проверка числа, выбор валюты из списка, конвертация
    if kol_rub.isnumeric():
        print('Вы ввели сумму', kol_rub, 'руб. и валюту', valuta)
        ll = {'USD': 2.5, 'EUR': 3, 'CHF': 2.82, 'GBP': 3.49, 'CNY': 0.406}
        for kk, vv in ll.items():
            if valuta == kk:
                print('конвертированная сумма в', valuta, '=', kol_rub / vv)
                exit()
