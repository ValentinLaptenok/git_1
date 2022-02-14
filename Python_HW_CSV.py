import random
import string
import csv
import datetime

# 1 Создать пустой empty.csv файл.

f_p = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/'
f_n = 'empty.csv'
f_name = f_p + f_n

f = open(f_name, 'w')
f.close()

# 2 Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/digits.csv'

with open(f_name, 'w', encoding='utf-8') as f:
    for i in range(150):
        f.write(str(random.randint(0, 150)))
        f.write('\n')

# 3 Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/names.csv'

with open(f_name, 'w', encoding='utf-8') as f:
    for i in range(100):
        f.write(''.join(random.choices(string.ascii_lowercase, k = random.randint(3, 10))))
        f.write('\n')

# 4 Вариант 1. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами
# что-то@gmail.com

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/emals.csv'

with open(f_name, 'w', encoding='utf-8') as f:
    for i in range(100):
        l = ''.join(random.choices(string.ascii_letters + string.digits, k = random.randint(3, 10))) + '@gmail.com'
        f.write(l)
        f.write('\n')

# 5 Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ),
# в котором будут 100 строк. Имя и часть email до @ должны совпадать.

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/nne.csv'

with open(f_name, 'w', encoding='utf-8') as f:
    columns = ['Number', 'Name', 'Email']
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

with open(f_name, 'a', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=columns)

    users = []
    for i in range(1, 101):
        l = {'Number': i, 'Name': str(i) + '_user', 'Email': str(i) + '_user@gmail.com'}
        users.append(l)

    writer.writerows(users)

# 6 Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number,
# в котором будут 300 строк с числами от 10 до 310

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/digits_2.csv'

l = []
for i in range(300):
    l.append(random.randint(10, 310))

with open(f_name, 'w', encoding='utf-8') as f:
    columns = ['Number']
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

with open(f_name, 'a', encoding='utf-8') as f:
    for i in range(300):
        f.write(str(l[i]))
        f.write('\n')

# 7 Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name,
# в котором будут 400 строк с разными именами

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/names_2.csv'

l = []
for i in range(400):
    n1 = ''.join(random.choices(string.ascii_uppercase, k = 1))
    n2 = ''.join(random.choices(string.ascii_lowercase, k = random.randint(3, 8)))
    l.append(n1 + n2)

with open(f_name, 'w', encoding='utf-8') as f:
    columns = ['name']
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

with open(f_name, 'a', encoding='utf-8') as f:
    for i in range(400):
        f.write(l[i])
        f.write('\n')

# 8 Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email,
# в котором будут 400 строк с разными имейлами что-то@gmail.com

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/emals_2.csv'

l = []
for i in range(400):
    l.append(''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 10))) + '@gmail.com')

with open(f_name, 'w', encoding='utf-8') as f:
    columns = ['email']
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

with open(f_name, 'a', encoding='utf-8') as f:
    for i in range(400):
        f.write(l[i])
        f.write('\n')

# 9 Вариант 2. Создать nne_2.csv файл с 3-мя полями (Number, Name, Email ),
# в котором будут 450 строк. Имя и часть email до @ должны совпадать.

f_name = '/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/nne_2.csv'

users = []
for i in range(1, 451):
    n1 = ''.join(random.choices(string.ascii_uppercase, k=1))
    n2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 5)))
    l = {'Number': i, 'Name': n1 + n2 + '_' + str(i), 'Email': n1 + n2 + '_' + str(i) + '@gmail.com'}
    users.append(l)

with open(f_name, 'w', encoding='utf-8') as f:
    columns = ['Number', 'Name', 'Email']
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

with open(f_name, 'a', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writerows(users)

# 10 Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем.
# Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# d) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)

with open(f_name, 'w', encoding='utf-8') as f:
    columns.append('Date')
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

with open(f_name, 'a', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    for i in range(450):
        if i >= 0 and i < 50:
            start_date = datetime.date(1980, 1, 1)
            end_date = datetime.date(1990, 12, 31)
        elif i >= 50 and i < 150:
            start_date = datetime.date(1991, 1, 1)
            end_date = datetime.date(2000, 12, 31)
        elif i >= 150 and i < 300:
            start_date = datetime.date(2001, 1, 1)
            end_date = datetime.date(2010, 12, 31)
        elif i >= 300 and i <= 450:
            start_date = datetime.date(2011, 1, 1)
            end_date = datetime.date(2021, 12, 31)

        time_between_dates = end_date - start_date          # случайные дата и время
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        t = datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59))
        users[i]['Date'] = datetime.datetime.combine(random_date, t)
    writer.writerows(users)

# 11. Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
# a) + Соберите имена из файла nne_2.csv.
# b) + недостающие 550 строк имён сгенерируйте.
# с) + Имена расположите в алфавитном порядке.
# d) + Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) + Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.

with open('/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/combo.csv', 'w') as f:
    columns = ['Name', 'Email', 'Date']
    writer = csv.DictWriter(f, fieldnames=columns)          # создал заголовки в combo
    writer.writeheader()

with open('/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/nne_2.csv', 'r') as f:
    reader = csv.DictReader(f)
    users = []
    for i in reader:                        # скопировал 450 имен из nne_2 в users
        l = {'Name': i['Name']}
        users.append(l)

for i in range(451, 1001):                              # добавил имена до 1000
    n1 = ''.join(random.choices(string.ascii_uppercase, k=1))
    n2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 5)))
    l = {'Name': n1 + n2 + '_' + str(i)}
    users.append(l)

sort_users = sorted(users, key=lambda x: x['Name'])         # сортировка по имени

with open('/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/nne_2.csv', 'r') as f:
    reader = csv.DictReader(f)
    ii = 0
    for i in reader:                                # первые 450 из nne_2 + дата
        users[ii]['Date'] = i['Date']
        ii += 1

for i in range(451, 1000):
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 2, 14)                       # добавил случайные даты
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    t = datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59))
    users[i]['Date'] = datetime.datetime.combine(random_date, t)

columns = ['Name', 'Email', 'Date', 'Phone', 'Gender', 'Salary']

for i in range(1000):
    users[i]['Email'] = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 10))) + '@gmail.com'
    p1 = random.randint(100, 999)
    p2 = random.randint(10, 99)
    p3 = random.randint(1000000, 9999999)
    users[i]['Phone'] = '+' + str(p1) + ' (' + str(p2) + ') ' + str(p3)
    l = ['man', 'woman']
    users[i]['Gender'] = random.choice(l)
    users[i]['Salary'] = random.randrange(1000, 3000, 200)

sort_users = sorted(users, key=lambda x: x['Name'])

with open('/Users/cerniksvetlana/Desktop/kursy/HOMEWORK/text_files/combo.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(sort_users)

