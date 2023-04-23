# Задача 1. 
# Дано натуральное число N. 
# Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

# 60 -> 2, 2, 3, 5

def prime_factors(n):
    factors = []
    count = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
            count += 1
    if n > 1:
        factors.append(n)
        count += 1
    return factors, count

number = int(input('Введите число, множители которого нужно найти: '))
print(*prime_factors(number))
