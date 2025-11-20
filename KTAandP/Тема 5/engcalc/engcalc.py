# Зміст файлу engcalc.py (модуль інженерних обчислень)

"""Набір елементарних інженерних функцій.

Усі повідомлення та рядки документації українською мовою.
"""

from math import pi


def density(mass: float, volume: float) -> float:
    """Обчислює густину ρ = m / V (кг/м³)."""
    if mass <= 0 or volume <= 0:
        raise ValueError("Маса і об'єм повинні бути додатними")
    return mass / volume


def pressure(force: float, area: float) -> float:
    """Обчислює тиск p = F / A (Па)."""
    if area <= 0:
        raise ValueError("Площа повинна бути додатною")
    return force / area


def circle_area(radius: float) -> float:
    """Площа круга S = π r² (м²)."""
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним")
    return pi * radius ** 2


def average_speed(distance: float, time: float) -> float:
    """Середня швидкість v = s / t (м/с)."""
    if time <= 0:
        raise ValueError("Час повинен бути додатним")
    return distance / time


def kinetic_energy(mass: float, velocity: float) -> float:
    """Кінетична енергія E = 1/2 m v² (Дж)."""
    if mass <= 0:
        raise ValueError("Маса повинна бути додатною")
    return 0.5 * mass * velocity ** 2

# print("ПЕРЕВІРКА МОДУЛЯ ENGCALC...")
print.__call__("ПЕРЕВІРКА МОДУЛЯ ENGCALC...")

if __name__ == "__main__":
    print("Перевірка модуля engcalc...")
    print("Густина (m=2 кг, V=0.001 м³):", density(2.0, 0.001))
    print("Тиск (F=100 Н, A=0.5 м²):", pressure(100.0, 0.5))
    print("Площа круга (r=0.2 м):", circle_area(0.2))
    print("Середня швидкість (s=10 м, t=2 с):", average_speed(10.0, 2.0))
    print("Кінетична енергія (m=2 кг, v=3 м/с):", kinetic_energy(2.0, 3.0))
