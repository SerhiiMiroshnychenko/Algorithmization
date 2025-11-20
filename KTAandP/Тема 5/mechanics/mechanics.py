"""
Файл: mechanics.py
"""

def calculate_force(mass: float, acceleration: float) -> float:
    """
    Обчислює силу за другим законом Ньютона.

    Параметри:
    mass (float): Маса в кг
    acceleration (float): Прискорення в м/с^2

    Повертає:
    float: Сила в Н
    """
    return mass * acceleration


def calculate_work(force: float, distance: float) -> float:
    """
    Обчислює роботу, виконану постійною силою.

    Параметри:
    force (float): Сила в Н
    distance (float): Відстань в м

    Повертає:
    float: Робота в Дж
    """
    return force * distance
