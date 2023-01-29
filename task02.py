# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6
# 100 -> 1

number = int(input('Write three-digit number: '))

def sum (number):
    count = 0
    while number > 0:
        count = count + number % 10 
        number = number // 10 
    return count 
res = sum (number)
if number < 1000 and number > 99:
    print(res)
else:
    print('Number is not three-digit')