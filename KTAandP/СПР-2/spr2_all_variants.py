"""
Практична робота №2: Ітераційні обчислення
Автоматичне обчислення всіх 23 варіантів

Програма послідовно обчислює завдання для всіх варіантів
з фіксованими параметрами табуляції.
"""

import math

# Константа точності
EPS = 1e-9

# Параметри табуляції за замовчуванням
DEFAULT_X_START = -2.0
DEFAULT_X_END = 2.0
DEFAULT_STEP = 0.5


def calculate_function(variant, x):
    """
    Calculate function value for given variant and x.
    Returns (y, is_valid, error_message)
    """
    
    if variant == 1:
        y = math.sin(x) / (x * x + 1) + math.cos(2 * x)
        return (y, True, "")
    
    elif variant == 2:
        if x + 3 > EPS:
            y = math.log(x + 3) - math.exp(-x)
            return (y, True, "")
        else:
            return (0, False, "x + 3 ≤ 0")
    
    elif variant == 3:
        y = math.sqrt(abs(x)) * math.sin(x) + x * x
        return (y, True, "")
    
    elif variant == 4:
        y = (math.exp(x) - math.exp(-x)) / 2 + math.log(x * x + 1)
        return (y, True, "")
    
    elif variant == 5:
        y = math.cos(x) / math.sqrt(x * x + 4)
        return (y, True, "")
    
    elif variant == 6:
        if abs(math.cos(x)) > EPS:
            y = math.tan(x) - 1 / (x * x + 1)
            return (y, True, "")
        else:
            return (0, False, "cos(x) = 0")
    
    elif variant == 7:
        y = x * math.exp(-x * x) + math.sin(math.pi * x)
        return (y, True, "")
    
    elif variant == 8:
        y = math.log(x * x + 1) / (math.cos(x) + 2)
        return (y, True, "")
    
    elif variant == 9:
        if x + 5 >= -EPS:
            y = math.sqrt(max(0, x + 5)) - math.sin(2 * x)
            return (y, True, "")
        else:
            return (0, False, "x + 5 < 0")
    
    elif variant == 10:
        y = (x ** 3 - x) / (math.exp(x) + 1)
        return (y, True, "")
    
    elif variant == 11:
        y = math.atan(x) + 1 / (x * x + 2)
        return (y, True, "")
    
    elif variant == 12:
        y = math.cos(x) ** 2 - math.sin(x) ** 2 + math.exp(-abs(x))
        return (y, True, "")
    
    elif variant == 13:
        y = (math.sin(x) + math.cos(x)) / math.sqrt(x * x + 1)
        return (y, True, "")
    
    elif variant == 14:
        y = math.log(x * x + 2) * math.exp(-x)
        return (y, True, "")
    
    elif variant == 15:
        y = x * math.sin(x) / (x * x + 3)
        return (y, True, "")
    
    elif variant == 16:
        y = math.sqrt(x * x + 1) - math.log(x * x + 2)
        return (y, True, "")
    
    elif variant == 17:
        y = math.exp(math.sin(x)) - math.cos(x * x)
        return (y, True, "")
    
    elif variant == 18:
        if abs(0.5 * x) <= 1 + EPS:
            arg = max(-1, min(1, 0.5 * x))
            y = math.asin(arg) / (x * x + 1)
            return (y, True, "")
        else:
            return (0, False, "|0.5x| > 1")
    
    elif variant == 19:
        y = x * x * math.exp(-x) + math.sin(2 * math.pi * x)
        return (y, True, "")
    
    elif variant == 20:
        y = math.cos(x) / (1 + math.exp(-x))
        return (y, True, "")
    
    elif variant == 21:
        y = math.log(math.exp(x) + 1) - x * x / 2
        return (y, True, "")
    
    elif variant == 22:
        y = math.sin(x) * math.cos(x) + 1 / math.sqrt(x * x + 5)
        return (y, True, "")
    
    elif variant == 23:
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
    """Calculate additional condition for given variant."""
    
    if len(y_list) == 0:
        return (0, 0, "Список порожній")
    
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
        product = 1.0
        count = 0
        for y in y_list:
            if y > EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток елементів > 0")
    
    elif variant == 2:
        total_odd = 0.0
        count = 0
        for i in range(len(y_list)):
            if i % 2 == 1:
                total_odd += y_list[i]
                count += 1
        return (total_odd, count, "Сума елементів з непарними індексами")
    
    elif variant == 3:
        count = 0
        for y in y_list:
            if -EPS <= y <= 5 + EPS:
                count += 1
        return (count, count, "Кількість елементів в [0, 5]")
    
    elif variant == 4:
        product = 1.0
        count = 0
        for i in range(len(y_list)):
            if i % 2 == 0:
                product *= y_list[i]
                count += 1
        return (product, count, "Добуток елементів з парними індексами")
    
    elif variant == 5:
        total_neg = 0.0
        count = 0
        for y in y_list:
            if y < -EPS:
                total_neg += y
                count += 1
        return (total_neg, count, "Сума від'ємних елементів")
    
    elif variant == 6:
        count = 0
        for y in y_list:
            if abs(y) < 1 - EPS:
                count += 1
        return (count, count, "Кількість елементів з |y| < 1")
    
    elif variant == 7:
        total_above = 0.0
        count = 0
        for y in y_list:
            if y > average + EPS:
                total_above += y
                count += 1
        return (total_above, count, "Сума елементів > середнього")
    
    elif variant == 8:
        product = 1.0
        count = 0
        for y in y_list:
            if -2 - EPS <= y <= 2 + EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток елементів в [-2, 2]")
    
    elif variant == 9:
        count = 0
        for y in y_list:
            if y > EPS:
                count += 1
        return (count, count, "Кількість додатних елементів")
    
    elif variant == 10:
        sum_sq = 0.0
        for y in y_list:
            sum_sq += y * y
        return (sum_sq, len(y_list), "Сума квадратів")
    
    elif variant == 11:
        product = 1.0
        count = 0
        for y in y_list:
            if y < -EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток від'ємних")
    
    elif variant == 12:
        total_3 = 0.0
        count = 0
        for i in range(len(y_list)):
            if i % 3 == 0:
                total_3 += y_list[i]
                count += 1
        return (total_3, count, "Сума з індексами кратними 3")
    
    elif variant == 13:
        count = 0
        for y in y_list:
            if y > 0.5 + EPS:
                count += 1
        return (count, count, "Кількість елементів > 0.5")
    
    elif variant == 14:
        total_prime = 0.0
        count = 0
        for i in range(len(y_list)):
            if is_prime(i):
                total_prime += y_list[i]
                count += 1
        return (total_prime, count, "Сума з простими індексами")
    
    elif variant == 15:
        product = 1.0
        count = 0
        for y in y_list:
            if -EPS <= y <= 1 + EPS:
                product *= y
                count += 1
        return (product if count > 0 else 0, count, "Добуток елементів в [0, 1]")
    
    elif variant == 16:
        threshold = min_y + 1
        count = 0
        for y in y_list:
            if y < threshold - EPS:
                count += 1
        return (count, count, f"Кількість < min+1")
    
    elif variant == 17:
        n = min(5, len(y_list))
        total_5 = 0.0
        for i in range(n):
            total_5 += y_list[i]
        return (total_5, n, f"Сума перших {n}")
    
    elif variant == 18:
        product = 1.0
        count = 0
        for i in range(len(y_list)):
            if i % 2 == 1:
                product *= y_list[i]
                count += 1
        return (product if count > 0 else 0, count, "Добуток з непарними індексами")
    
    elif variant == 19:
        total_near = 0.0
        count = 0
        for y in y_list:
            if abs(y - average) <= 1 + EPS:
                total_near += y
                count += 1
        return (total_near, count, "Сума близьких до середнього")
    
    elif variant == 20:
        count = 0
        for y in y_list:
            if abs(y) < EPS:
                count += 1
        return (count, count, "Кількість ≈ 0")
    
    elif variant == 21:
        product = 1.0
        for y in y_list:
            product *= abs(y)
        return (product, len(y_list), "Добуток |y|")
    
    elif variant == 22:
        n = min(5, len(y_list))
        total_5 = 0.0
        for i in range(len(y_list) - n, len(y_list)):
            total_5 += y_list[i]
        return (total_5, n, f"Сума останніх {n}")
    
    elif variant == 23:
        total_interval = 0.0
        count = 0
        for y in y_list:
            if min_y - EPS <= y <= average + EPS:
                total_interval += y
                count += 1
        return (total_interval, count, "Сума в [min, avg]")
    
    else:
        return (0, 0, "Невідомий варіант")


def get_function_formula(variant):
    """Return function formula string for given variant."""
    formulas = {
        1: "y = sin(x)/(x²+1) + cos(2x)",
        2: "y = ln(x+3) - e^(-x)",
        3: "y = √|x|·sin(x) + x²",
        4: "y = sinh(x) + ln(x²+1)",
        5: "y = cos(x)/√(x²+4)",
        6: "y = tan(x) - 1/(x²+1)",
        7: "y = x·e^(-x²) + sin(πx)",
        8: "y = ln(x²+1)/(cos(x)+2)",
        9: "y = √(x+5) - sin(2x)",
        10: "y = (x³-x)/(e^x+1)",
        11: "y = arctan(x) + 1/(x²+2)",
        12: "y = cos²(x)-sin²(x)+e^(-|x|)",
        13: "y = (sin(x)+cos(x))/√(x²+1)",
        14: "y = ln(x²+2)·e^(-x)",
        15: "y = x·sin(x)/(x²+3)",
        16: "y = √(x²+1) - ln(x²+2)",
        17: "y = e^(sin(x)) - cos(x²)",
        18: "y = arcsin(0.5x)/(x²+1)",
        19: "y = x²·e^(-x) + sin(2πx)",
        20: "y = cos(x)/(1+e^(-x))",
        21: "y = ln(e^x+1) - x²/2",
        22: "y = sin(x)cos(x)+1/√(x²+5)",
        23: "y = e^(-x²)/√(x²+1)+arctan(x)"
    }
    return formulas.get(variant, "?")


def process_variant(variant, x_start, x_end, h, verbose=True):
    """Process single variant and return results."""
    
    y_list = []
    x = x_start
    
    while x <= x_end + EPS:
        y, is_valid, _ = calculate_function(variant, x)
        if is_valid:
            y_list.append(y)
        x += h
    
    if len(y_list) == 0:
        return None
    
    # Basic statistics
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
    
    # Additional condition
    add_result, add_count, add_desc = calculate_additional_condition(variant, y_list)
    
    return {
        'count': len(y_list),
        'max': max_y,
        'min': min_y,
        'sum': total,
        'avg': average,
        'add_result': add_result,
        'add_count': add_count,
        'add_desc': add_desc
    }


def main():
    """Main program - process all 23 variants."""
    
    print("=" * 90)
    print("ПРАКТИЧНА РОБОТА №2: ІТЕРАЦІЙНІ ОБЧИСЛЕННЯ")
    print("Автоматичне обчислення всіх 23 варіантів")
    print("=" * 90)
    
    print(f"\nПараметри табуляції:")
    print(f"  x_start = {DEFAULT_X_START}")
    print(f"  x_end   = {DEFAULT_X_END}")
    print(f"  h       = {DEFAULT_STEP}")
    
    print("\n" + "=" * 90)
    print(f"{'Вар':>3} | {'Функція':<32} | {'N':>3} | {'Max':>10} | {'Min':>10} | {'Avg':>10} | {'Дод. умова':<25} | {'Результат':>12}")
    print("=" * 90)
    
    for variant in range(1, 24):
        formula = get_function_formula(variant)
        result = process_variant(variant, DEFAULT_X_START, DEFAULT_X_END, DEFAULT_STEP)
        
        if result:
            print(f"{variant:3d} | {formula:<32} | {result['count']:3d} | {result['max']:10.4f} | {result['min']:10.4f} | {result['avg']:10.4f} | {result['add_desc']:<25} | {result['add_result']:12.4f}")
        else:
            print(f"{variant:3d} | {formula:<32} | {'---':>3} | {'---':>10} | {'---':>10} | {'---':>10} | {'Немає даних':<25} | {'---':>12}")
    
    print("=" * 90)
    
    # Detailed output for each variant
    print("\n\n")
    print("#" * 90)
    print("ДЕТАЛЬНІ РЕЗУЛЬТАТИ ДЛЯ КОЖНОГО ВАРІАНТУ")
    print("#" * 90)
    
    for variant in range(1, 24):
        print(f"\n{'─' * 90}")
        print(f"ВАРІАНТ {variant}: {get_function_formula(variant)}")
        print(f"{'─' * 90}")
        
        y_list = []
        x = DEFAULT_X_START
        
        print(f"\n{'№':>4} | {'x':>10} | {'y':>15}")
        print("-" * 35)
        
        point_num = 0
        while x <= DEFAULT_X_END + EPS:
            y, is_valid, error = calculate_function(variant, x)
            if is_valid:
                y_list.append(y)
                point_num += 1
                print(f"{point_num:4d} | {x:10.4f} | {y:15.8f}")
            else:
                print(f"{'---':>4} | {x:10.4f} | {error:>15}")
            x += DEFAULT_STEP
        
        print("-" * 35)
        
        if len(y_list) > 0:
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
            
            print(f"\nСтатистика:")
            print(f"  Кількість точок: {len(y_list)}")
            print(f"  Максимум: {max_y:.8f}")
            print(f"  Мінімум: {min_y:.8f}")
            print(f"  Сума: {total:.8f}")
            print(f"  Середнє: {average:.8f}")
            
            add_result, add_count, add_desc = calculate_additional_condition(variant, y_list)
            print(f"\nДодаткова умова: {add_desc}")
            print(f"  Кількість елементів: {add_count}")
            print(f"  Результат: {add_result:.8f}")
        else:
            print("\nНемає даних для обробки.")
    
    print("\n" + "=" * 90)
    print("ОБЧИСЛЕННЯ ЗАВЕРШЕНО")
    print("=" * 90)


if __name__ == "__main__":
    main()

