# Задача 3.
# В школе решили набрать 3 новых мат. класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть 2 учащихся. Известно кол-во учащихся в каждом из 3х классов.
# Выведите наименьшее чило парт, к-ое нужно приобрести для них.

# Input:  20 21 22 (ввод чисел не в одну строку)
# Output: 32

students1 = int(input('Number of students in class #1: '))
students2 = int(input('Number of students in class #2: '))
students3 = int(input('Number of students in class #3: '))

print(int(students1 // 2 + students1 % 2 + students2 // 2 + students2 % 2 + students3 // 2 + students3 % 2))
