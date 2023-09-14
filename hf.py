"""Задача №10"""

def min_flips(coins):
    # Подсчитываем количество монеток с решкой
    count_heads = coins.count('Р')

    # Подсчитываем количество монеток с гербом
    count_tails = coins.count('О')

    # Возвращаем меньшее из двух значений
    return min(count_heads, count_tails)

# Пример использования функции
coins = 'РРРОРООРОРР'
flips = min_flips(coins)
print(flips)  # Выводит: 4


"""Задача №12"""

def find_numbers(sum_hint, product_hint):
    for x in range(1, 1001):
        for y in range(1, 1001):
            if x + y == sum_hint and x * y == product_hint:
                return x, y

    # Если не найдено подходящих чисел, возвращаем None
    return None

# Пример использования функции
sum_hint = 7
product_hint = 10
numbers = find_numbers(sum_hint, product_hint)
if numbers:
    x, y = numbers
    print(f"Задуманные числа Петей: {x}, {y}")
else:
    print("Числа не найдены")

# Вывод: Задуманные числа Петей: 2, 5



"""Задача №14"""
def powers_of_two(n):
    powers = []
    power = 0
    i = 1

    while i <= n:
        powers.append(i)
        power += 1
        i = 2**power

    return powers

# Пример использования функции
n = 50
result = powers_of_two(n)
print(result)

# Вывод: [1, 2, 4, 8, 16, 32]


