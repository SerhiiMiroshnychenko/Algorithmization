from math import sin

T = 1e-9
n = int(input('n = '))

numbers = [((-1) ** i) * sin(i ** 2 + 1) / sin(i + 1) for i in range(n) if abs(sin(i + 1)) > T]
max_neg = max(num for num in numbers if num < -T)
res = f"Максимальний з від'ємних: {max_neg:.6f}" if max_neg else "Від'ємних елементів немає"

print(numbers, '\n', res)
