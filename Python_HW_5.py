import random
import string

# 1 Написать скрипт который создаст список целых чисел.

l = [i+1 for i in range(70)]

# 2 Написать скрипт который создаст список целых чётных чисел.

l = [i+1 for i in range(1, 140, 2)]

# 3 Написать скрипт который в создаст список целых нечётных чисел

l = [i+1 for i in range(0, 140, 2)]

# 4 Написать скрипт который из списка целых чисел выведет чётные числа.

ll = []
l = [i+1 for i in range(70)]
for i in range(70):
    if l[i] % 2 == 0:
        ll.append(l[i])
print(ll)

# 5 Написать скрипт который из списка целых чисел выведет нечётные числа.

ll = []
l = [i+1 for i in range(70)]
for i in range(70):
    if l[i] % 2 != 0:
        ll.append(l[i])
print(ll)

# 6 Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.

ll = []
l = [i+1 for i in range(70)]
for i in range(70):
    if l[i] % 2 == 0:
        if l[i] % 5 == 0:
            ll.append(l[i])
print(ll)

# 7 Написать скрипт который из списка целых чисел выведет количество чётных чисел которые делятся на 5 без остатка.

ll = []
l = [i+1 for i in range(70)]
for i in range(70):
    if l[i] % 2 == 0:
        if l[i] % 5 == 0:
            ll.append(l[i])
print(len(ll))

# 8 Написать скрипт который создаст список целых рандомных чисел.

l_random = []
for i in range(70):
    l_random.append(random.randint(1, 150))
print(l_random)

# 9 Написать !!! функцию !!!которая, получив на вход любой из выше созданных списков,
# разобьёт его на списки по 5 элементов.

def list_5_elem(l_random):
    for i in range(0,70,5):
        l = l_random[i:i+5]
        print(l)
list_5_elem(l_random)

# 10 Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка,
# список чётных и список нечётных чисел.

def l_cet_necet(l_random):
    l_cet = []
    l_necet = []
    for i in l_random:
        if i % 2 == 0:
            l_cet.append(i)
        else:
            l_necet.append(i)
    print(l_cet, '\n', l_necet)

l_cet_necet(l_random)

# 11 Написать скрипт который сгенерирует список под названием 5_stars из списков
# по 5 элементов целых чисел.

five_stars = []
for ii in range(0, 5):
    l = []
    for i in range(0, 5):
        l.append(random.randint(1, 30))
    five_stars.append(l)
print(five_stars)

# 12 Написать скрипт который выведет список из сумм каждого внутреннего списка из 5_stars

l = []
for i in range(5):
    l.append(sum(five_stars[i]))
print(l)

# 13 Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка.
# В одном списке внутренние списки из 5_stars сумма чисел которых >= 100,
# а другой сумма чисел которых < 100. Если какого-то списка не получится,
# то вместо него вернуть текст “No lists”

def five_stars_bol_men(five_stars):
    for i in range(0, 5):
        if sum(five_stars[i]) >= 100:
            l_sum_bol.append(five_stars[i])
        else:
            l_sum_men.append(five_stars[i])
    return(l_sum_bol, l_sum_men)

l_sum_bol = []
l_sum_men = []
five_stars_bol_men(five_stars)
if len(l_sum_bol) > 0:
    print('lists >=100:', l_sum_bol)
else:
    print('No lists >=100')
if len(l_sum_men) > 0:
    print('lists <100:', l_sum_men)
else:
    print('No lists <100')

# 14 Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок
# вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.

vozr = int(input('Enter your age: '))   # предположим доход 1000 за вычетом всех расходов, роста зарплаты нет
def kubyshka(vozr):
    dohod = []
    mont = 0

    for sal in range(0, 101000, 1000):
        mont += 1
        if sal == 10000:
            vozr += mont // 12
            dohod.append([vozr, sal])
        if sal == 20000:
            vozr += mont // 12
            dohod.append([vozr, sal])
        if sal == 30000:
            vozr += mont // 12
            dohod.append([vozr, sal])
        if sal == 50000:
            vozr += mont // 12
            dohod.append([vozr, sal])
        if sal == 100000:
            vozr += mont // 12
            dohod.append([vozr, sal])
    for i in range(0, 5):
        print('Sum', dohod[i][1], 'in', dohod[i][0], 'yo')
kubyshka(vozr)

# 15 Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа
# выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа.
# Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании
# активностей которые может делать QA. Free implementation of function body logic

start_zp = int(input('Enter start salary: '))
kol_let = int(input('Enter number of years of work: '))
def rost_zp(start_zp, kol_let):
    skills = [0.1, 0.2, 0.3, 0.4, 0.5]
    for i in range(1, kol_let+1):
        if i > 5:
            print('Salary in', i, 'year =', int(start_zp * 2.5))
        else:
            s = 0
            for ii in range(i):
                s += skills[ii]
            s += 1
            print('Salary in', i, 'year =', int(start_zp * s))

rost_zp(start_zp, kol_let)

# 16 Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.

name_user = []
for i in range(10):
    name_user.append(''.join(random.choices(string.ascii_letters, k = 5)))
for i in range(10):
    print(name_user[i])

# 17 Написать скрипт который сгенерирует список имён файлов. К каждому имени
# файла надо прикрепить номер итерации цикла как порядковый номер.

name_file = []
for i in range(10):
    name_file.append('file_name' + str(i) + '.py')

for i in range(10):
    print(name_file[i])

# 18 Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором
# 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.

name_date = []
for i in range(10):
    l = []
    l.append('name_user' + str(i))
    l.append('date_create')
    name_date.append(l)
for i in range(10):
    print(name_date[i])

# 19 Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список
# в котором: 0-й - элемент - это имя пользователя, 1-й - элемент - это логин, 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),4-й - элемент - это дата регистрации

employees = []
for i in range(10):
    l = []
    l.append('name_user' + str(i))
    l.append('login_user' + str(i))
    l.append('password' + str(i))
    l.append('email' + str(i) + '@gmail.com')
    l.append('date_create')
    employees.append(l)
for i in range(10):
    print(employees[i])

# 20 Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно),

family = []
for i in range(10):
    l = []
    l.append(employees[i][1])
    l.append(employees[i][0])
    ll = ['married', 'free']
    l.append(random.choice(ll))
    family.append(l)

for i in range(10):
    print(family[i])

# 21 Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)

gender = []
for i in range(10):
    l = []
    l.append(employees[i][1])
    l.append(employees[i][0])
    ll = ['man', 'woman']
    l.append(random.choice(ll))
    gender.append(l)

for i in range(10):
    print(gender[i])

# 22 Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)

salary = []
for i in range(10):
    l = []
    l.append(employees[i][1])
    l.append(employees[i][0])
    l.append(random.randrange(300, 5000, 500))
    salary.append(l)

for i in range(10):
    print(salary[i])

# 23 Написать скрипт который создаст список имён работников из salary у которых ЗП от 1500$ до 3000$

zp_1500_3000 = []
for i in range(10):
    if salary[i][2] >= 1500 and salary[i][2] <= 3000:
        zp_1500_3000.append(salary[i][1])

print(zp_1500_3000)

# 24 Написать скрипт который создаст список имён мужчин из gender.

man_gender = []
for i in range(10):
    if gender[i][2] == 'man':
        man_gender.append(gender[i][1])

print(man_gender)

# 25 Написать скрипт который создаст список имён женщин из gender.

woman_gender = []
for i in range(10):
    if gender[i][2] == 'woman':
        woman_gender.append(gender[i][1])

print(woman_gender)

# 26 Написать скрипт который создаст список имён неженатых мужчин из family.

free_man = []
for i in range(10):
    if family[i][2] == 'free' and gender[i][2] == 'man':
        free_man.append(family[i][1])

print(free_man)

# 27 Написать скрипт который создаст список имён незамужних женщин из family.

free_woman = []
for i in range(10):
    if family[i][2] == 'free' and gender[i][2] == 'woman':
        free_woman.append(family[i][1])

print(free_woman)

# 28. Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$.
# Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций

free_man_1500 = []
for i in range(10):
    if family[i][2] == 'free' and gender[i][2] == 'man' and salary[i][2] >= 1500:
        free_man_1500.append(employees[i][0])

print(free_man_1500)

# 28 functions
def employees_f():
    employees = []
    for i in range(10):
        l = []
        l.append('name_user' + str(i))
        l.append('login_user' + str(i))
        l.append('password' + str(i))
        l.append('email' + str(i) + '@gmail.com')
        l.append('date_create')
        employees.append(l)
    return(employees)

def family_f(employees):
    family = []
    for i in range(10):
        l = []
        l.append(employees[i][1])
        l.append(employees[i][0])
        ll = ['married', 'free']
        l.append(random.choice(ll))
        family.append(l)
    return(family)

def gender_f(employees):
    gender = []
    for i in range(10):
        l = []
        l.append(employees[i][1])
        l.append(employees[i][0])
        ll = ['man', 'woman']
        l.append(random.choice(ll))
        gender.append(l)
    return(gender)

def salary_f(employees):
    salary = []
    for i in range(10):
        l = []
        l.append(employees[i][1])
        l.append(employees[i][0])
        l.append(random.randrange(300, 5000, 500))
        salary.append(l)
    return(salary)

employees_f()
family_f(employees)
gender_f(employees)
salary_f(employees)

free_man_1500 = []
for i in range(10):
    if family[i][2] == 'free' and gender[i][2] == 'man' and salary[i][2] >= 1500:
        free_man_1500.append(employees[i][0])

for i in range(len(free_man_1500)):
    print(free_man_1500[i])
