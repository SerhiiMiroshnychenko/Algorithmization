"""
Тестування варіанту 6
Автоматична перевірка всіх тестових випадків
"""

import math

def calculate_variant6(x):
    """Обчислення функції варіанту 6"""
    t = 1e-9
    
    # Перевірка чи x = 0 (невизначена точка)
    if abs(x) < t:
        return "Функція не визначена в точці x = 0"
    # Перевірка чи x у невизначеному інтервалі (4; 4.2]
    elif (4 - t) < x <= (4.2 + t):
        return "Функція не визначена на інтервалі (4; 4.2]"
    
    # Інтервал 1: x <= -2
    if x <= (-2 + t):
        radicand = x + 2
        
        # Перевірка radicand >= 0
        if radicand > -t:
            # Обробка випадку radicand = 0
            if radicand < t:
                sqrt_part = 0
            else:
                sqrt_part = math.sqrt(radicand)
            
            power_part = 5 ** (-math.sin(x))
            y = power_part * sqrt_part
            return f"x = {x}, y1 = {y:.6f}"
        else:
            return "Порушено ОДЗ: вираз під коренем від'ємний"
    
    # Інтервал 2: -2 < x < 0
    elif (-2 + t) < x < -t:
        # Перевірка sin(x) != 0 для котангенса
        if abs(math.sin(x)) > t:
            cotangent = math.cos(x) / math.sin(x)
            numerator = math.sin(x) ** 5 - math.pi * x
            y = numerator / cotangent
            return f"x = {x}, y2 = {y:.6f}"
        else:
            return "Порушено ОДЗ: sin(x) = 0, котангенс не визначений"
    
    # Інтервал 3: 0 < x <= 4
    elif t < x <= (4 - t):
        # Корінь 6-го степеня від x + додатково 0.628x
        y = x ** (1.0 / 6.0) + 0.628 * x
        return f"x = {x}, y3 = {y:.6f}"
    
    # Інтервал 4: x > 4.2
    elif x > (4.2 + t):
        # Перевірка sin(x) != 0 для котангенса
        if abs(math.sin(x)) > t:
            cotangent = math.cos(x) / math.sin(x)
            y = cotangent - math.exp(x)
            return f"x = {x}, y4 = {y:.6f}"
        else:
            return "Порушено ОДЗ: sin(x) = 0, котангенс не визначений"


# Тестові випадки з звіту
test_cases = [
    (-2.0, "Тест 1: Інтервал 1 (x ≤ -2), межа x = -2"),
    (-2.5, "Тест 2: Інтервал 1 (x ≤ -2), x < -2 - порушення ОДЗ"),
    (-1.0, "Тест 3: Інтервал 2 (-2 < x < 0)"),
    (0.0, "Тест 4: x = 0 (невизначена точка)"),
    (2.0, "Тест 5: Інтервал 3 (0 < x ≤ 4)"),
    (4.1, "Тест 6: Невизначений інтервал (4 < x ≤ 4.2)"),
    (5.0, "Тест 7: Інтервал 4 (x > 4.2)"),
    (2 * 3.141592653589793, "Тест 8: Порушення ОДЗ (ctg(x) при x = 2π)"),
]

print("=" * 70)
print("ТЕСТУВАННЯ ВАРІАНТУ 6")
print("=" * 70)

for x_value, description in test_cases:
    print(f"\n{description}")
    print(f"Input x = {x_value}")
    result = calculate_variant6(x_value)
    print(result)

print("\n" + "=" * 70)
print("ТЕСТУВАННЯ ЗАВЕРШЕНО")
print("=" * 70)

