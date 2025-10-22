"""
Тестування варіанту 5
Автоматична перевірка всіх тестових випадків
"""

import math

def calculate_variant5(x):
    """Обчислення функції варіанту 5"""
    t = 1e-9
    
    # Перевірка чи x у невизначеному інтервалі [2; 2.2)
    if (2 - t) <= x < (2.2 - t):
        return "Функція не визначена на інтервалі [2; 2.2)"
    
    # Інтервал 1: x < -2
    if x < (-2 + t):
        # Перевірка sin(x) != 0 для котангенса
        if abs(math.sin(x)) > t:
            cotangent = math.cos(x) / math.sin(x)
            y = cotangent - math.exp(x * x)
            return f"x = {x}, y1 = {y:.6f}"
        else:
            return "Порушено ОДЗ: sin(x) = 0, котангенс не визначений"
    
    # Інтервал 2: -2 < x <= 0
    elif (-2 + t) < x <= t:
        # cos(x) - 1.1 завжди != 0, оскільки -1 <= cos(x) <= 1
        denominator = math.cos(x) - 1.1
        y = 3 / denominator
        return f"x = {x}, y2 = {y:.6f}"
    
    # Інтервал 3: 0 < x < 2
    elif t < x < (2 - t):
        y = (x ** 5) * math.sin(x) + 0.5
        return f"x = {x}, y3 = {y:.6f}"
    
    # Інтервал 4: x >= 2.2
    elif x >= (2.2 - t):
        radicand = math.cos(x) ** 2
        # Кубічний корінь завжди визначений
        y = radicand ** (1.0 / 3.0)
        return f"x = {x}, y4 = {y:.6f}"


# Тестові випадки з звіту
test_cases = [
    (-3.0, "Тест 1: Інтервал 1 (x < -2)"),
    (-1.0, "Тест 2: Інтервал 2 (-2 < x ≤ 0)"),
    (1.5, "Тест 3: Інтервал 3 (0 < x < 2)"),
    (2.1, "Тест 4: Невизначений інтервал [2; 2.2)"),
    (3.0, "Тест 5: Інтервал 4 (x ≥ 2.2)"),
    (-3.141592653589793, "Тест 6: Порушення ОДЗ (ctg(x) при x = -π)"),
    (0.0, "Тест 7: Межа між інтервалами (x = 0)"),
]

print("=" * 70)
print("ТЕСТУВАННЯ ВАРІАНТУ 5")
print("=" * 70)

for x_value, description in test_cases:
    print(f"\n{description}")
    print(f"Input x = {x_value}")
    result = calculate_variant5(x_value)
    print(result)

print("\n" + "=" * 70)
print("ТЕСТУВАННЯ ЗАВЕРШЕНО")
print("=" * 70)

