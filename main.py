import sqlite3 as sq

with sq.connect("students.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby TEXT NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    birthday TEXT NOT NULL,
    points TEXT NOT NULL
    )""")

    cursor.execute("""INSERT" INTO student (hobby, name ,surname, birthday, points
    ) 
    VALUES
    (Андрей", "Иванов", "Футбол", 15.02.2002, 90)
    ("Мария", "Петрова", "Рисование", 25.07.2001, 85)
    ("Дмитрий", "Сидоров", "Шахматы", 10.11.2000, 92)
    ("Елена", "Смирнова", "Танцы", 03.05.2003, 88)
    ("Алексей", "Кузнецов", "Велосипед", 18.09.2002, 80)
    ("Анастасия", "Попова", "Пение", 12.01.2001, 95)
    ("Сергей", "Лебедев", "Рисование", 29.03.2000, 78)
    ("Виктория", "Соколовская", "Плавание", 22.12.2003, 87) 
    ("Михаил", "Морозов", "Фотография", 05.08.2001, 83)
    ("Ольга", "Федорова", "Волейбол", 11.06.2002, 91)
    """)


    cursor.execute("""SELECT * FROM students WHERE LENGTH(last_name) > 10""")

for i in cursor.fetchall():
    print(i)


    cursor.execute("""UPDATE students SET first_name = 'genius' WHERE points > 10""")

    cursor.execute("""SELECT * FROM students WHERE first_name = 'genius'""")

for i in cursor.fetchall():
    print(i)


    cursor.execute("""DELETE FROM students WHERE id % 2 = 0""")

    cursor.execute("""SELECT * FROM students""")

for i in cursor.fetchall():
    print(i)


