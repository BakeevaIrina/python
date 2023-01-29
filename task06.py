# Задача 6.
# Нужно определить счастливый билет. 
# 385916 -> yes
# 123456 -> NO

number = int(input('Введите номер билета: '))


def ticket(number):
    num1 = number // 1000 
    num2 = number % 1000  
    sum1 = 0
    sum2 = 0
    while num1 > 0 or num2 > 0:
        sum1 +=num1 % 10
        num1 = num1 //10
        sum2 += num2 % 10
        num2 = num2 // 10
    else:
        sum1 = sum1 - sum2
    return sum1
res = ticket(number)
if number < 1000000 and number >99999:
    if res == 0: print('YES')
    else: print('NO')
else: print('Номер билета должен быть шестизначным!')       