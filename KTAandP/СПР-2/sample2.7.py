import math
import random

t = 1e-12
N = 20
a, b = -20, 40

number  = input('n = ')
n = int(number) if number else N

random.seed(42)
x = []
yy = []

for i in range(n):
    # xi = random.random() * (b - a) + a
    xi = random.randint(a, b)
    x.append(xi)
    cos_val  = math.cos(xi / 3) ** 3
    if abs(cos_val) > t:
        tg = (math.sin(xi / 3) ** 3) / cos_val
        root_expr = tg - (2 ** xi)
        if abs(root_expr) > t and abs(xi) > t:
            root = (abs(root_expr) / root_expr) * (abs(root_expr) ** (1/3))
            y = (3 ** math.cos(xi)) - 7.5 * xi - root + math.log(abs(xi))
            yy.append(y)
            print(f"y[{len(yy) - 1}] = {y:.6f}")

if len(yy) > 0:



    print(f"\nКількість елементів y[]: {len(yy)}")
    print(f"Сума від'ємних елементів: {sum([y for y in yy if y < -t]):.6f}")
    print(f"Середнє значення: {sum(yy) / len(yy):.6f}")
    print(f"Мінімальний елемент: {min(yy):.6f}")
    print(f"Максимальний елемент: {max(yy):.6f}")

    interval = [y for y in yy if -1.5 - t < y < 1.5 + t]
    product = 1
    print(f"{interval = }")
    for y in interval:
        product += y

    if len(interval) > 0:
        print(f"Добуток елементів в інтервалі [-1.5; 1.5]: {product:.6f}")
    else:
        print("Елементів в інтервалі [-1.5; 1.5] немає")
else:
    print("Список порожній")


# Варіант 1
"""
Кількість елементів y[]: 20
Сума від'ємних елементів: -243.270316
Середнє значення: 335.851013
Мінімальний елемент: -83.084515
Максимальний елемент: 4889.065975
Елементів в інтервалі [-1.5; 1.5] немає
"""

# Варіант 2
"""
Кількість елементів y[]: 20
Сума від'ємних елементів: -243.270316
Середнє значення: 335.851013
Мінімальний елемент: -83.084515
Максимальний елемент: 4889.065975
interval = []
Елементів в інтервалі [-1.5; 1.5] немає
"""
