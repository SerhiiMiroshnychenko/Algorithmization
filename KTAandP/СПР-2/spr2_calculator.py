"""
Практична робота №2: Ітераційні обчислення
Комплексний калькулятор для всіх 23 варіантів

Програма запитує номер варіанту та вихідні дані,
виконує табуляцію функції та обробку списку результатів.
"""

import math

# Константа точності
EPS = 1e-9


def calculate_function(variant, x):
    """
    Calculate function value for given variant and x.
    Returns (y, is_valid, error_message)
    """
    
    if variant == 1:
        # y = sin(x)/(x²+1) + cos(2x)
        y = math.sin(x) / (x * x + 1) + math.cos(2 * x)
        return (y, True, "")
    
    elif variant == 2:
        # y = ln(x+3) - e^(-x)
        if x + 3 > EPS:
            y = math.log(x + 3) - math.exp(-x)
            return (y, True, "")
        else:
            return (0, False, "x + 3 ≤ 0")
    
    elif variant == 3:
        # y = √|x| · sin(x) + x²
        y = math.sqrt(abs(x)) * math.sin(x) + x * x
        return (y, True, "")
    
    elif variant == 4:
        # y = (e^x - e^(-x))/2 + ln(x²+1)
        y = (math.exp(x) - math.exp(-x)) / 2 + math.log(x * x + 1)
        return (y, True, "")
    
    elif variant == 5:
        # y = cos(x) / √(x²+4)
        y = math.cos(x) / math.sqrt(x * x + 4)
        return (y, True, "")
    
    elif variant == 6:
        # y = tan(x) - 1/(x²+1)
        if abs(math.cos(x)) > EPS:
            y = math.tan(x) - 1 / (x * x + 1)
            return (y, True, "")
        else:
            return (0, False, "cos(x) = 0")
    
    elif variant == 7:
        # y = x · e^(-x²) + sin(πx)
        y = x * math.exp(-x * x) + math.sin(math.pi * x)
        return (y, True, "")
    
    elif variant == 8:
        # y = ln(x²+1) / (cos(x)+2)
        y = math.log(x * x + 1) / (math.cos(x) + 2)
        return (y, True, "")
    
    elif variant == 9:
        # y = √(x+5) - sin(2x)
        if x + 5 >= -EPS:
            y = math.sqrt(max(0, x + 5)) - math.sin(2 * x)
            return (y, True, "")
        else:
            return (0, False, "x + 5 < 0")
    
    elif variant == 10:
        # y = (x³-x) / (e^x+1)
        y = (x ** 3 - x) / (math.exp(x) + 1)
        return (y, True, "")
    
    elif variant == 11:
        # y = arctan(x) + 1/(x²+2)
        y = math.atan(x) + 1 / (x * x + 2)
        return (y, True, "")
    
    elif variant == 12:
        # y = cos²(x) - sin²(x) + e^(-|x|)
        y = math.cos(x) ** 2 - math.sin(x) ** 2 + math.exp(-abs(x))
        return (y, True, "")
    
    elif variant == 13:
        # y = (sin(x)+cos(x)) / √(x²+1)
        y = (math.sin(x) + math.cos(x)) / math.sqrt(x * x + 1)
        return (y, True, "")
    
    elif variant == 14:
        # y = ln(x²+2) · e^(-x)
        y = math.log(x * x + 2) * math.exp(-x)
        return (y, True, "")
    
    elif variant == 15:
        # y = x·sin(x) / (x²+3)
        y = x * math.sin(x) / (x * x + 3)
        return (y, True, "")
    
    elif variant == 16:
        # y = √(x²+1) - ln(x²+2)
        y = math.sqrt(x * x + 1) - math.log(x * x + 2)
        return (y, True, "")
    
    elif variant == 17:
        # y = e^(sin(x)) - cos(x²)
        y = math.exp(math.sin(x)) - math.cos(x * x)
        return (y, True, "")
    
    elif variant == 18:
        # y = arcsin(0.5x) / (x²+1), |0.5x| ≤ 1
        if abs(0.5 * x) <= 1 + EPS:
            arg = max(-1, min(1, 0.5 * x))  # Clamp to [-1, 1]
            y = math.asin(arg) / (x * x + 1)
            return (y, True, "")
        else:
            return (0, False, "|0.5x| > 1")
    
    elif variant == 19:
        # y = x² · e^(-x) + sin(2πx)
        y = x * x * math.exp(-x) + math.sin(2 * math.pi * x)
        return (y, True, "")
    
    elif variant == 20:
        # y = cos(x) / (1 + e^(-x))
        y = math.cos(x) / (1 + math.exp(-x))
        return (y, True, "")
    
    elif variant == 21:
        # y = ln(e^x+1) - x²/2
        y = math.log(math.exp(x) + 1) - x * x / 2
        return (y, True, "")
    
    elif variant == 22:
        # y = sin(x)·cos(x) + 1/√(x²+5)
        y = math.sin(x) * math.cos(x) + 1 / math.sqrt(x * x + 5)
        return (y, True, "")
    
    elif variant == 23:
        # y = e^(-x²) / √(x²+1) + arctan(x)
        y = math.exp(-x * x) / math.sqrt(x * x + 1) + math.atan(x)
        return (y, True, "")
    
    else:
        return (0, False, "Невідомий варіант")


def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_additional_condition(variant, y_list):
    """
    Calculate additional condition for given variant.
    Returns (result_value, result_count, description)
    """
    
    if len(y_list) == 0:
        return (0, 0, "Список порожній")
    
    # Calculate basic statistics first (needed for some variants)
    total = 0.0
    for y in y_list:
        total += y
    average = total / len(y_list)
    
    min_y = y_list[0]
    max_y = y_list[0]
    for y in y_list:
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    
    if variant == 1:
        # Добуток елементів > 0
        product = 1.0
        count = 0
        for y in y_list:
            if y > EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток елементів > 0")
    
    elif variant == 2:
        # Сума елементів з непарними індексами
        total_odd = 0.0
        count = 0
        for i in range(len(y_list)):
            if i % 2 == 1:
                total_odd += y_list[i]
                count += 1
        return (total_odd, count, "Сума елементів з непарними індексами")
    
    elif variant == 3:
        # Кількість елементів в [0, 5]
        count = 0
        for y in y_list:
            if -EPS <= y <= 5 + EPS:
                count += 1
        return (count, count, "Кількість елементів в інтервалі [0, 5]")
    
    elif variant == 4:
        # Добуток елементів з парними індексами
        product = 1.0
        count = 0
        for i in range(len(y_list)):
            if i % 2 == 0:
                product *= y_list[i]
                count += 1
        return (product, count, "Добуток елементів з парними індексами")
    
    elif variant == 5:
        # Сума від'ємних елементів
        total_neg = 0.0
        count = 0
        for y in y_list:
            if y < -EPS:
                total_neg += y
                count += 1
        return (total_neg, count, "Сума від'ємних елементів")
    
    elif variant == 6:
        # Кількість елементів з |y| < 1
        count = 0
        for y in y_list:
            if abs(y) < 1 - EPS:
                count += 1
        return (count, count, "Кількість елементів з |y| < 1")
    
    elif variant == 7:
        # Сума елементів > середнього
        total_above = 0.0
        count = 0
        for y in y_list:
            if y > average + EPS:
                total_above += y
                count += 1
        return (total_above, count, "Сума елементів > середнього")
    
    elif variant == 8:
        # Добуток елементів в [-2, 2]
        product = 1.0
        count = 0
        for y in y_list:
            if -2 - EPS <= y <= 2 + EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток елементів в інтервалі [-2, 2]")
    
    elif variant == 9:
        # Кількість додатних елементів
        count = 0
        for y in y_list:
            if y > EPS:
                count += 1
        return (count, count, "Кількість додатних елементів")
    
    elif variant == 10:
        # Сума квадратів всіх елементів
        sum_sq = 0.0
        for y in y_list:
            sum_sq += y * y
        return (sum_sq, len(y_list), "Сума квадратів всіх елементів")
    
    elif variant == 11:
        # Добуток від'ємних елементів
        product = 1.0
        count = 0
        for y in y_list:
            if y < -EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток від'ємних елементів")
    
    elif variant == 12:
        # Сума елементів з індексами кратними 3
        total_3 = 0.0
        count = 0
        for i in range(len(y_list)):
            if i % 3 == 0:
                total_3 += y_list[i]
                count += 1
        return (total_3, count, "Сума елементів з індексами кратними 3")
    
    elif variant == 13:
        # Кількість елементів > 0.5
        count = 0
        for y in y_list:
            if y > 0.5 + EPS:
                count += 1
        return (count, count, "Кількість елементів > 0.5")
    
    elif variant == 14:
        # Сума елементів з простими індексами
        total_prime = 0.0
        count = 0
        for i in range(len(y_list)):
            if is_prime(i):
                total_prime += y_list[i]
                count += 1
        return (total_prime, count, "Сума елементів з простими індексами")
    
    elif variant == 15:
        # Добуток елементів в [0, 1]
        product = 1.0
        count = 0
        for y in y_list:
            if -EPS <= y <= 1 + EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток елементів в інтервалі [0, 1]")
    
    elif variant == 16:
        # Кількість елементів < min + 1
        threshold = min_y + 1
        count = 0
        for y in y_list:
            if y < threshold - EPS:
                count += 1
        return (count, count, f"Кількість елементів < min+1 ({threshold:.4f})")
    
    elif variant == 17:
        # Сума перших 5 елементів
        n = min(5, len(y_list))
        total_5 = 0.0
        for i in range(n):
            total_5 += y_list[i]
        return (total_5, n, f"Сума перших {n} елементів")
    
    elif variant == 18:
        # Добуток елементів з непарними індексами
        product = 1.0
        count = 0
        for i in range(len(y_list)):
            if i % 2 == 1:
                product *= y_list[i]
                count += 1
        return (product if count > 0 else 0, count, "Добуток елементів з непарними індексами")
    
    elif variant == 19:
        # Сума елементів близьких до середнього (±1)
        total_near = 0.0
        count = 0
        for y in y_list:
            if abs(y - average) <= 1 + EPS:
                total_near += y
                count += 1
        return (total_near, count, "Сума елементів близьких до середнього (±1)")
    
    elif variant == 20:
        # Кількість елементів ≈ 0
        count = 0
        for y in y_list:
            if abs(y) < EPS:
                count += 1
        return (count, count, "Кількість елементів ≈ 0")
    
    elif variant == 21:
        # Добуток абсолютних значень
        product = 1.0
        for y in y_list:
            product *= abs(y)
        return (product, len(y_list), "Добуток абсолютних значень")
    
    elif variant == 22:
        # Сума останніх 5 елементів
        n = min(5, len(y_list))
        total_5 = 0.0
        for i in range(len(y_list) - n, len(y_list)):
            total_5 += y_list[i]
        return (total_5, n, f"Сума останніх {n} елементів")
    
    elif variant == 23:
        # Сума елементів в [min, average]
        total_interval = 0.0
        count = 0
        for y in y_list:
            if min_y - EPS <= y <= average + EPS:
                total_interval += y
                count += 1
        return (total_interval, count, f"Сума елементів в [{min_y:.4f}, {average:.4f}]")
    
    else:
        return (0, 0, "Невідомий варіант")


def get_function_formula(variant):
    """Return function formula string for given variant."""
    formulas = {
        1: "y = sin(x)/(x²+1) + cos(2x)",
        2: "y = ln(x+3) - e^(-x)",
        3: "y = √|x| · sin(x) + x²",
        4: "y = (e^x - e^(-x))/2 + ln(x²+1)",
        5: "y = cos(x) / √(x²+4)",
        6: "y = tan(x) - 1/(x²+1)",
        7: "y = x · e^(-x²) + sin(πx)",
        8: "y = ln(x²+1) / (cos(x)+2)",
        9: "y = √(x+5) - sin(2x)",
        10: "y = (x³-x) / (e^x+1)",
        11: "y = arctan(x) + 1/(x²+2)",
        12: "y = cos²(x) - sin²(x) + e^(-|x|)",
        13: "y = (sin(x)+cos(x)) / √(x²+1)",
        14: "y = ln(x²+2) · e^(-x)",
        15: "y = x·sin(x) / (x²+3)",
        16: "y = √(x²+1) - ln(x²+2)",
        17: "y = e^(sin(x)) - cos(x²)",
        18: "y = arcsin(0.5x) / (x²+1)",
        19: "y = x² · e^(-x) + sin(2πx)",
        20: "y = cos(x) / (1 + e^(-x))",
        21: "y = ln(e^x+1) - x²/2",
        22: "y = sin(x)·cos(x) + 1/√(x²+5)",
        23: "y = e^(-x²) / √(x²+1) + arctan(x)"
    }
    return formulas.get(variant, "Невідомий варіант")


def get_odz_info(variant):
    """Return ODZ information string for given variant."""
    odz = {
        1: "Функція визначена для всіх x",
        2: "x > -3",
        3: "Функція визначена для всіх x",
        4: "Функція визначена для всіх x",
        5: "Функція визначена для всіх x",
        6: "cos(x) ≠ 0, тобто x ≠ π/2 + πk",
        7: "Функція визначена для всіх x",
        8: "Функція визначена для всіх x",
        9: "x ≥ -5",
        10: "Функція визначена для всіх x",
        11: "Функція визначена для всіх x",
        12: "Функція визначена для всіх x",
        13: "Функція визначена для всіх x",
        14: "Функція визначена для всіх x",
        15: "Функція визначена для всіх x",
        16: "Функція визначена для всіх x",
        17: "Функція визначена для всіх x",
        18: "-2 ≤ x ≤ 2",
        19: "Функція визначена для всіх x",
        20: "Функція визначена для всіх x",
        21: "Функція визначена для всіх x",
        22: "Функція визначена для всіх x",
        23: "Функція визначена для всіх x"
    }
    return odz.get(variant, "Невідомий варіант")


def main():
    """Main program."""
    
    print("=" * 70)
    print("ПРАКТИЧНА РОБОТА №2: ІТЕРАЦІЙНІ ОБЧИСЛЕННЯ")
    print("Комплексний калькулятор для всіх 23 варіантів")
    print("=" * 70)
    
    # Введення номера варіанту
    print("\nДоступні варіанти: 1-23")
    variant = int(input("Введіть номер варіанту: "))
    
    if variant < 1 or variant > 23:
        print("Помилка: варіант має бути від 1 до 23")
        return
    
    # Виведення інформації про варіант
    print(f"\n{'=' * 70}")
    print(f"ВАРІАНТ {variant}")
    print(f"{'=' * 70}")
    print(f"\nФункція: {get_function_formula(variant)}")
    print(f"ОДЗ: {get_odz_info(variant)}")
    print("-" * 70)
    
    # Введення вихідних даних
    print("\n--- ВВЕДЕННЯ ВИХІДНИХ ДАНИХ ---")
    x_start = float(input("Введіть початкове значення x_start: "))
    x_end = float(input("Введіть кінцеве значення x_end: "))
    h = float(input("Введіть крок табуляції h: "))
    
    # Перевірка коректності введення
    if h <= 0:
        print("Помилка: крок має бути додатним")
        return
    
    if x_start > x_end:
        print("Помилка: x_start має бути ≤ x_end")
        return
    
    # ============================================================
    # ТАБУЛЯЦІЯ ФУНКЦІЇ
    # ============================================================
    print(f"\n{'=' * 70}")
    print("ТАБУЛЯЦІЯ ФУНКЦІЇ")
    print(f"{'=' * 70}")
    
    y_list = []
    
    print(f"\n{'№':>5} | {'x':>12} | {'y':>18} | {'Статус':>15}")
    print("-" * 60)
    
    point_number = 0
    x = x_start
    
    while x <= x_end + EPS:
        y, is_valid, error_msg = calculate_function(variant, x)
        
        if is_valid:
            y_list.append(y)
            point_number += 1
            print(f"{point_number:5d} | {x:12.6f} | {y:18.10f} | {'OK':>15}")
        else:
            print(f"{'---':>5} | {x:12.6f} | {'---':>18} | {error_msg:>15}")
        
        x += h
    
    print("-" * 60)
    print(f"Загальна кількість обчислених точок: {len(y_list)}")
    
    # ============================================================
    # ОБРОБКА СПИСКУ
    # ============================================================
    print(f"\n{'=' * 70}")
    print("ОБРОБКА СПИСКУ ЗНАЧЕНЬ")
    print(f"{'=' * 70}")
    
    if len(y_list) > 0:
        # Основна статистика
        max_y = y_list[0]
        min_y = y_list[0]
        total = 0.0
        
        for y in y_list:
            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y
            total += y
        
        average = total / len(y_list)
        
        print(f"\n--- ОСНОВНА СТАТИСТИКА ---")
        print(f"Кількість елементів: {len(y_list)}")
        print(f"Максимальне значення: {max_y:.10f}")
        print(f"Мінімальне значення: {min_y:.10f}")
        print(f"Сума всіх елементів: {total:.10f}")
        print(f"Середнє арифметичне: {average:.10f}")
        
        # Додаткова умова
        result_value, result_count, description = calculate_additional_condition(variant, y_list)
        
        print(f"\n--- ДОДАТКОВА УМОВА ---")
        print(f"Умова: {description}")
        print(f"Кількість елементів, що відповідають умові: {result_count}")
        print(f"Результат: {result_value:.10f}")
        
    else:
        print("\nСписок порожній. Немає даних для обробки.")
        print("Можливо, всі значення x не належать ОДЗ функції.")
    
    # ============================================================
    # ЗАВЕРШЕННЯ
    # ============================================================
    print(f"\n{'=' * 70}")
    print("ПРОГРАМУ ЗАВЕРШЕНО")
    print(f"{'=' * 70}")


# Запуск програми
if __name__ == "__main__":
    main()

