"""
Тестування варіанту 4
Автоматична перевірка всіх тестових випадків
"""

import math

def calculate_variant4(x):
    """Обчислення функції варіанту 4"""
    t = 1e-9
    
    # Перевірка чи x у невизначеному інтервалі [1.4; 1.7]
    if (1.4 - t) < x < (1.7 + t):
        return "Функція не визначена на інтервалі [1.4; 1.7]"
    
    # Інтервал 1: x <= 0
    if x <= t:
        y = x ** 3 + math.exp(-1.3 * x)
        return f"x = {x}, y1 = {y:.6f}"
    
    # Інтервал 2: 0 < x < 0.5
    elif t < x < (0.5 - t):
        y = math.exp(x) * math.sin(x) + 7.3
        return f"x = {x}, y2 = {y:.6f}"
    
    # Інтервал 3: 0.5 <= x < 1.4
    elif (0.5 - t) <= x < (1.4 - t):
        # Перевірка cos(x) != 0 для tan(x)
        if abs(math.cos(x)) > t:
            y = math.tan(x) / math.sqrt(5 + x * x)
            return f"x = {x}, y3 = {y:.6f}"
        else:
            return "Порушено ОДЗ: cos(x) = 0, tan(x) не визначений"
    
    # Інтервал 4: x > 1.7
    elif x > (1.7 + t):
        denominator = 11 * math.pi - 0.5 * x * x
        
        # Перевірка ділення на нуль
        if abs(denominator) > t:
            y = (x ** 7) / denominator
            return f"x = {x}, y4 = {y:.6f}"
        else:
            return "Порушено ОДЗ: ділення на нуль"


# Тестові випадки з звіту
test_cases = [
    (-1.0, "Тест 1: Інтервал 1 (x ≤ 0)"),
    (0.3, "Тест 2: Інтервал 2 (0 < x < 0.5)"),
    (1.0, "Тест 3: Інтервал 3 (0.5 ≤ x < 1.4)"),
    (1.5, "Тест 4: Невизначений інтервал [1.4; 1.7]"),
    (2.0, "Тест 5: Інтервал 4 (x > 1.7)"),
    (1.5707963267948966, "Тест 6: Порушення ОДЗ (tan(x) при x = π/2)"),
]

print("=" * 70)
print("ТЕСТУВАННЯ ВАРІАНТУ 4")
print("=" * 70)

for x_value, description in test_cases:
    print(f"\n{description}")
    print(f"Input x = {x_value}")
    result = calculate_variant4(x_value)
    print(result)

print("\n" + "=" * 70)
print("ТЕСТУВАННЯ ЗАВЕРШЕНО")
print("=" * 70)

