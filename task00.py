# Задача 1.
# За день машина проезжает n километров. Сколько дней нужно чтобы проехать m километров?
# Не использовать условную функцию if и цикл.
# input       output
# n = 700     2
# m = 750

n = int (input('Введите n: '))
m = int (input('Введите m: '))
def arg (n, m):
    return (n + m - 1)//n 
res = arg(n, m)
print(res)