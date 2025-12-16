from math import cos, log

EPS = 1e-9

x_start = float(input("Введіть початкове значення x_start: "))
x_end = float(input("Введіть початкове значення x_end: "))
h = float(input("Введіть початкове значення h: "))

print(f"\n{'№':>5} | {'x':>12} | {'y':>15}")
print("-" * 40)

y_list = list()

point_number = 0

x = x_start
while x <= x_end + EPS:

    y = log(x ** 2 + 1) / (cos(x) + 2)
    y_list.append(y)

    point_number += 1
    print(f"{point_number:5d} | {x:12.6f} | {y:15.8f} | {'OK':>15}")

    x += h

if len(y_list) > 0:
    print(f"Максимальне значення y: {max(y_list):.8f}")
    print(f"Мінімальне значення y: {min(y_list):.8f}")
    print(f"Сума всіх елементів: {sum(y_list):.8f}")
    print(f"Середнє арифметичне: {sum(y_list)/len(y_list):.8f}")
    interval = [y for y in y_list if -2 - EPS < y < 2 + EPS]
    product = 1
    print(f"{interval = }")
    for y in interval:
        product += y

    if len(interval) > 0:
        print(f"Добуток елементів в інтервалі [-2; 2]: {product:.6f}")
    else:
        print("Елементів в інтервалі [-2; 2] немає")


