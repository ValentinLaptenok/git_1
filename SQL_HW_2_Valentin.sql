
--Таблица employees
create table employees(
	id serial primary key,
	employee_name varchar(50) not null
);

--Наполнить таблицу employee 70 строками
insert into employees(employee_name)
values
	('Морозов Михаил'),
	('Прохорова Мария'),
	('Широков Тимофей'),
	('Смирнов Дмитрий'),
	('Панфилова Анна'),
	('Борисов Владислав'),
	('Булгакова Ангелина'),
	('Куликова Алиса'),
	('Савельев Артём'),
	('Дьяконов Дмитрий'),
	('Волкова Екатерина'),
	('Елисеев Константин'),
	('Муравьев Андрей'),
	('Титова Алиса'),
	('Шаров Тимур'),
	('Васильева Алина'),
	('Сорокин Тимофей'),
	('Малышев Даниил'),
	('Богданова Дарья'),
	('Морозов Марк'),
	('Леонова Елизавета'),
	('Маслова Мария'),
	('Кочергина Мирослава'),
	('Иванова Айлин'),
	('Парамонова Вероника'),
	('Богданова Варвара'),
	('Волков Дмитрий'),
	('Ефимова Вера'),
	('Максимов Григорий'),
	('Панфилов Артём'),
	('Балашов Дмитрий'),
	('Кондратьев Платон'),
	('Шишкин Александр'),
	('Смирнова Любовь'),
	('Андреева Ева'),
	('Егорова Дарья'),
	('Воронова Алёна'),
	('Попов Семён'),
	('Волкова Ульяна'),
	('Матвеев Даниил'),
	('Ильина Алиса'),
	('Антонова Алёна'),
	('Михайлова Полина'),
	('Иванов Даниил'),
	('Тарасова Алина'),
	('Калинин Тимофей'),
	('Мельникова Ника'),
	('Леонов Марк'),
	('Булатова Мария'),
	('Пименов Роберт'),
	('Кондратова Сафия'),
	('Березин Сергей'),
	('Новиков Артемий'),
	('Борисов Максим'),
	('Болдырев Александр'),
	('Куприянова Анастасия'),
	('Румянцев Тимофей'),
	('Новиков Матвей'),
	('Егорова Анастасия'),
	('Завьялова Варвара'),
	('Морозов Семён'),
	('Клюева Дарья'),
	('Лазарева Арина'),
	('Позднякова Елизавета'),
	('Климов Артём'),
	('Филатов Глеб'),
	('Киселева Елена'),
	('Филимонов Матвей'),
	('Фролова Екатерина'),
	('Коновалов Даниил');

--Таблица salary
create table salary(
	id serial primary key,
	monthly_salary int not null
);

--Наполнить таблицу salary 15 строками
insert into salary(monthly_salary)
values
	(1000),
	(1100),
	(1200),
	(1300),
	(1400),
	(1500),
	(1600),
	(1700),
	(1800),
	(1900),
	(2000),
	(2100),
	(2200),
	(2300),
	(2400),
	(2500);

--Таблица employee_salary
create table employee_salary(
	id serial primary key,
	employee_id int not null,
	salary_id int not null
);

--Наполнить таблицу employee_salary 40 строками
--в 10 строк из 40 вставить несуществующие employee_id

insert into employee_salary(employee_id, salary_id)
values
	(3, 7),
	(1, 4),
	(5, 9),
	(40, 13),
	(23, 4),
	(11, 2),
	(52, 10),
	(15, 13),
	(26, 4),
	(16, 1),
	(33, 7),
	(2, 16),
	(4, 15),
	(6, 14),
	(7, 13),
	(8, 12),
	(9, 11),
	(10, 10),
	(12, 9),
	(13, 8),
	(14, 7),
	(17, 6),
	(18, 5),
	(19, 4),
	(20, 3),
	(21, 2),
	(22, 1),
	(24, 16),
	(25, 15),
	(27, 14),
	(71, 13),
	(72, 12),
	(73, 11),
	(74, 10),
	(75, 9),
	(76, 8),
	(77, 7),
	(78, 6),
	(79, 5),
	(80, 4);
	
--Создать таблицу roles
create table roles(
	id serial primary key,
	role_name int not null unique
);

--Поменять тип столба role_name с int на varchar(30)
alter table roles 
	alter column role_name type varchar(30);

--Наполнить таблицу roles 20 строками
insert into roles(role_name)
values
	('Junior Python developer'),
	('Middle Python developer'),
	('Senior Python developer'),
	('Junior Java developer'),
	('Middle Java developer'),
	('Senior Java developer'),
	('Junior JavaScript developer'),
	('Middle JavaScript developer'),
	('Senior JavaScript developer'),
	('Junior Manual QA engineer'),
	('Middle Manual QA engineer'),
	('Senior Manual QA engineer'),
	('Project Manager'),
	('Designer'),
	('HR'),
	('CEO'),
	('Sales manager'),
	('Junior Automation QA engineer'),
	('Middle Automation QA engineer'),
	('Senior Automation QA engineer');


create table roles_employee(
	id serial primary key,
	employee_id int not null unique,
	role_id int not null,
	foreign key(employee_id)
		references employees(id),
	foreign key(role_id)
		references roles(id)
);

insert into roles_employee(employee_id, role_id)
values
	(7, 2),
	(20, 4),
	(3, 9),
	(5, 13),
	(23, 4),
	(11, 2),
	(10, 9),
	(22, 13),
	(21, 3),
	(34, 4),
	(6, 7),
	(40, 20),
	(41, 19),
	(42, 18),
	(43, 17),
	(44, 16),
	(45, 15),
	(46, 14),
	(47, 13),
	(48, 12),
	(49, 11),
	(50, 10),
	(51, 9),
	(52, 8),
	(53, 7),
	(54, 6),
	(55, 5),
	(56, 4),
	(57, 3),
	(58, 2),
	(59, 1),
	(60, 20),
	(61, 19),
	(62, 18),
	(63, 17),
	(64, 16),
	(65, 15),
	(66, 14),
	(67, 13),
	(68, 12);
	
select * from roles_employee;




