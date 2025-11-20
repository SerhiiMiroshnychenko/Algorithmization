# Файл: main.py

import mechanics

mass = 10.0
acceleration = 2.5
force = mechanics.calculate_force(mass, acceleration)
print(f"Сила: {force} Н")

distance = 5.0
work = mechanics.calculate_work(force, distance)
print(f"Робота: {work} Дж")

# from mechanics import calculate_force, calculate_work
#
# force = calculate_force(10.0, 2.5)
# work = calculate_work(force, 5.0)
# print(f"Сила: {force} Н, Робота: {work} Дж")
