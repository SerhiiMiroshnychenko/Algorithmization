"""
Автоматичний розрахунок всіх варіантів кусково-заданих функцій
Практична робота №3
Варіанти 1-23 (без запитів до користувача)
"""

import math

# Константа точності
EPS = 1e-9


def variant_1(x):
    """Variant 1: y = {2x+1, x², √x}"""
    if x < -1 - EPS:
        return 2 * x + 1, "2x + 1"
    elif -1 - EPS <= x < 2 - EPS:
        return x ** 2, "x²"
    else:  # x >= 2
        return math.sqrt(x), "√x"


def variant_2(x):
    """Variant 2: y = {x³, cos(x), e^x}"""
    if x < 0 - EPS:
        return x ** 3, "x³"
    elif 0 - EPS <= x < math.pi - EPS:
        return math.cos(x), "cos(x)"
    else:  # x >= π
        return math.exp(x), "e^x"


def variant_3(x):
    """Variant 3: y = {|x|, x²-4, 1/x}"""
    if x < -2 - EPS:
        return abs(x), "|x|"
    elif -2 - EPS <= x < 2 - EPS:
        return x ** 2 - 4, "x² - 4"
    else:  # x >= 2
        return 1 / x, "1/x"


def variant_4(x):
    """Variant 4: y = {sin(x), 2x, x²+x+1}"""
    if x < 0 - EPS:
        return math.sin(x), "sin(x)"
    elif 0 - EPS <= x < 1 - EPS:
        return 2 * x, "2x"
    else:  # x >= 1
        return x ** 2 + x + 1, "x² + x + 1"


def variant_5(x):
    """Variant 5: y = {x²+2x, √(x+1), ln(x)}"""
    if x < -1 - EPS:
        return x ** 2 + 2 * x, "x² + 2x"
    elif -1 - EPS <= x < 3 - EPS:
        return math.sqrt(x + 1), "√(x + 1)"
    else:  # x >= 3
        return math.log(x), "ln(x)"


def variant_6(x):
    """Variant 6: y = {3-x, x³-x, 2^x}"""
    if x < 0 - EPS:
        return 3 - x, "3 - x"
    elif 0 - EPS <= x < 2 - EPS:
        return x ** 3 - x, "x³ - x"
    else:  # x >= 2
        return 2 ** x, "2^x"


def variant_7(x):
    """Variant 7: y = {e^(-x), x²-1, tan(x)}"""
    if x < -1 - EPS:
        return math.exp(-x), "e^(-x)"
    elif -1 - EPS <= x < 1 - EPS:
        return x ** 2 - 1, "x² - 1"
    else:  # x >= 1
        return math.tan(x), "tan(x)"


def variant_8(x):
    """Variant 8: y = {x+5, √(4-x²), x-5}"""
    if x < -2 - EPS:
        return x + 5, "x + 5"
    elif -2 - EPS <= x < 2 - EPS:
        return math.sqrt(4 - x ** 2), "√(4 - x²)"
    else:  # x >= 2
        return x - 5, "x - 5"


def variant_9(x):
    """Variant 9: y = {1/(x+2), x²+3x, sin(πx)}"""
    if x < -3 - EPS:
        return 1 / (x + 2), "1/(x + 2)"
    elif -3 - EPS <= x < 0 - EPS:
        return x ** 2 + 3 * x, "x² + 3x"
    else:  # x >= 0
        return math.sin(math.pi * x), "sin(πx)"


def variant_10(x):
    """Variant 10: y = {√(-x), x², ln(x-2)}"""
    if x < 0 - EPS:
        return math.sqrt(-x), "√(-x)"
    elif 0 - EPS <= x < 3 - EPS:
        return x ** 2, "x²"
    else:  # x >= 3
        return math.log(x - 2), "ln(x - 2)"


def variant_11(x):
    """Variant 11: y = {cos(πx), 2x+1, e^(-x)}"""
    if x < 0 - EPS:
        return math.cos(math.pi * x), "cos(πx)"
    elif 0 - EPS <= x < 2 - EPS:
        return 2 * x + 1, "2x + 1"
    else:  # x >= 2
        return math.exp(-x), "e^(-x)"


def variant_12(x):
    """Variant 12: y = {x³-x, √(1-x²), x³+x}"""
    if x < -1 - EPS:
        return x ** 3 - x, "x³ - x"
    elif -1 - EPS <= x < 1 - EPS:
        return math.sqrt(1 - x ** 2), "√(1 - x²)"
    else:  # x >= 1
        return x ** 3 + x, "x³ + x"


def variant_13(x):
    """Variant 13: y = {|x-1|, x²+2, 1/(x-1)}"""
    if x < 0 - EPS:
        return abs(x - 1), "|x - 1|"
    elif 0 - EPS <= x < 2 - EPS:
        return x ** 2 + 2, "x² + 2"
    else:  # x >= 2
        return 1 / (x - 1), "1/(x - 1)"


def variant_14(x):
    """Variant 14: y = {e^x, x, ln(x)}"""
    if x < -1 - EPS:
        return math.exp(x), "e^x"
    elif -1 - EPS <= x < 1 - EPS:
        return x, "x"
    else:  # x >= 1
        return math.log(x), "ln(x)"


def variant_15(x):
    """Variant 15: y = {x²-5, cos(x), √(x-1)}"""
    if x < -2 - EPS:
        return x ** 2 - 5, "x² - 5"
    elif -2 - EPS <= x < 2 - EPS:
        return math.cos(x), "cos(x)"
    else:  # x >= 2
        return math.sqrt(x - 1), "√(x - 1)"


def variant_16(x):
    """Variant 16: y = {2^(-x), x³, sin(πx)}"""
    if x < 0 - EPS:
        return 2 ** (-x), "2^(-x)"
    elif 0 - EPS <= x < 1 - EPS:
        return x ** 3, "x³"
    else:  # x >= 1
        return math.sin(math.pi * x), "sin(πx)"


def variant_17(x):
    """Variant 17: y = {√(x+3), x²-x, 1/(x-2)}"""
    if x < 0 - EPS:
        return math.sqrt(x + 3), "√(x + 3)"
    elif 0 - EPS <= x < 3 - EPS:
        return x ** 2 - x, "x² - x"
    else:  # x >= 3
        return 1 / (x - 2), "1/(x - 2)"


def variant_18(x):
    """Variant 18: y = {tan(x), x²+x, e^x}"""
    if x < -math.pi / 4 - EPS:
        return math.tan(x), "tan(x)"
    elif -math.pi / 4 - EPS <= x < 1 - EPS:
        return x ** 2 + x, "x² + x"
    else:  # x >= 1
        return math.exp(x), "e^x"


def variant_19(x):
    """Variant 19: y = {|x+2|, 2x²-1, ln(x+1)}"""
    if x < -1 - EPS:
        return abs(x + 2), "|x + 2|"
    elif -1 - EPS <= x < 1 - EPS:
        return 2 * x ** 2 - 1, "2x² - 1"
    else:  # x >= 1
        return math.log(x + 1), "ln(x + 1)"


def variant_20(x):
    """Variant 20: y = {sin(x), √x, x-2}"""
    if x < 0 - EPS:
        return math.sin(x), "sin(x)"
    elif 0 - EPS <= x < 4 - EPS:
        return math.sqrt(x), "√x"
    else:  # x >= 4
        return x - 2, "x - 2"


def variant_21(x):
    """Variant 21: y = {x²+1, cos(πx), e^(-x)}"""
    if x < -1 - EPS:
        return x ** 2 + 1, "x² + 1"
    elif -1 - EPS <= x < 1 - EPS:
        return math.cos(math.pi * x), "cos(πx)"
    else:  # x >= 1
        return math.exp(-x), "e^(-x)"


def variant_22(x):
    """Variant 22: y = {1/(x+1), x³-2x, √(x+1)}"""
    if x < -2 - EPS:
        return 1 / (x + 1), "1/(x + 1)"
    elif -2 - EPS <= x < 1 - EPS:
        return x ** 3 - 2 * x, "x³ - 2x"
    else:  # x >= 1
        return math.sqrt(x + 1), "√(x + 1)"


def variant_23(x):
    """Variant 23: y = {cos(x), x²-2x+1, ln(x+3)}"""
    if x < -math.pi / 2 - EPS:
        return math.cos(x), "cos(x)"
    elif -math.pi / 2 - EPS <= x < 2 - EPS:
        return x ** 2 - 2 * x + 1, "x² - 2x + 1"
    else:  # x >= 2
        return math.log(x + 3), "ln(x + 3)"


# Словник варіантів
VARIANTS = {
    1: variant_1,
    2: variant_2,
    3: variant_3,
    4: variant_4,
    5: variant_5,
    6: variant_6,
    7: variant_7,
    8: variant_8,
    9: variant_9,
    10: variant_10,
    11: variant_11,
    12: variant_12,
    13: variant_13,
    14: variant_14,
    15: variant_15,
    16: variant_16,
    17: variant_17,
    18: variant_18,
    19: variant_19,
    20: variant_20,
    21: variant_21,
    22: variant_22,
    23: variant_23,
}


# Предефіновані параметри для кожного варіанту
VARIANT_PARAMETERS = {
    1: {"x_start": -2, "x_end": 3, "step": 0.5},
    2: {"x_start": -1, "x_end": 4, "step": 0.5},
    3: {"x_start": -3, "x_end": 3, "step": 0.5},
    4: {"x_start": -1, "x_end": 2, "step": 0.25},
    5: {"x_start": -2, "x_end": 4, "step": 0.5},
    6: {"x_start": -1, "x_end": 3, "step": 0.5},
    7: {"x_start": -2, "x_end": 2, "step": 0.5},
    8: {"x_start": -3, "x_end": 3, "step": 0.5},
    9: {"x_start": -4, "x_end": 2, "step": 0.5},
    10: {"x_start": -1, "x_end": 4, "step": 0.5},
    11: {"x_start": -1, "x_end": 3, "step": 0.5},
    12: {"x_start": -2, "x_end": 2, "step": 0.5},
    13: {"x_start": -1, "x_end": 3, "step": 0.5},
    14: {"x_start": -2, "x_end": 2, "step": 0.5},
    15: {"x_start": -3, "x_end": 3, "step": 0.5},
    16: {"x_start": -1, "x_end": 2, "step": 0.5},
    17: {"x_start": -2, "x_end": 4, "step": 0.5},
    18: {"x_start": -1, "x_end": 2, "step": 0.5},
    19: {"x_start": -2, "x_end": 2, "step": 0.5},
    20: {"x_start": -1, "x_end": 5, "step": 0.5},
    21: {"x_start": -2, "x_end": 2, "step": 0.5},
    22: {"x_start": -3, "x_end": 2, "step": 0.5},
    23: {"x_start": -3, "x_end": 3, "step": 0.5},
}


def get_variant_description(variant_num):
    """Get description of variant function"""
    descriptions = {
        1: "y = {2x+1 (x<-1), x² (-1≤x<2), √x (x≥2)}",
        2: "y = {x³ (x<0), cos(x) (0≤x<π), e^x (x≥π)}",
        3: "y = {|x| (x<-2), x²-4 (-2≤x<2), 1/x (x≥2)}",
        4: "y = {sin(x) (x<0), 2x (0≤x<1), x²+x+1 (x≥1)}",
        5: "y = {x²+2x (x<-1), √(x+1) (-1≤x<3), ln(x) (x≥3)}",
        6: "y = {3-x (x<0), x³-x (0≤x<2), 2^x (x≥2)}",
        7: "y = {e^(-x) (x<-1), x²-1 (-1≤x<1), tan(x) (x≥1)}",
        8: "y = {x+5 (x<-2), √(4-x²) (-2≤x<2), x-5 (x≥2)}",
        9: "y = {1/(x+2) (x<-3), x²+3x (-3≤x<0), sin(πx) (x≥0)}",
        10: "y = {√(-x) (x<0), x² (0≤x<3), ln(x-2) (x≥3)}",
        11: "y = {cos(πx) (x<0), 2x+1 (0≤x<2), e^(-x) (x≥2)}",
        12: "y = {x³-x (x<-1), √(1-x²) (-1≤x<1), x³+x (x≥1)}",
        13: "y = {|x-1| (x<0), x²+2 (0≤x<2), 1/(x-1) (x≥2)}",
        14: "y = {e^x (x<-1), x (-1≤x<1), ln(x) (x≥1)}",
        15: "y = {x²-5 (x<-2), cos(x) (-2≤x<2), √(x-1) (x≥2)}",
        16: "y = {2^(-x) (x<0), x³ (0≤x<1), sin(πx) (x≥1)}",
        17: "y = {√(x+3) (x<0), x²-x (0≤x<3), 1/(x-2) (x≥3)}",
        18: "y = {tan(x) (x<-π/4), x²+x (-π/4≤x<1), e^x (x≥1)}",
        19: "y = {|x+2| (x<-1), 2x²-1 (-1≤x<1), ln(x+1) (x≥1)}",
        20: "y = {sin(x) (x<0), √x (0≤x<4), x-2 (x≥4)}",
        21: "y = {x²+1 (x<-1), cos(πx) (-1≤x<1), e^(-x) (x≥1)}",
        22: "y = {1/(x+1) (x<-2), x³-2x (-2≤x<1), √(x+1) (x≥1)}",
        23: "y = {cos(x) (x<-π/2), x²-2x+1 (-π/2≤x<2), ln(x+3) (x≥2)}",
    }
    return descriptions.get(variant_num, "Невідомий варіант")


def tabulate_variant(variant_num, variant_func, x_start, x_end, step, verbose=True):
    """Tabulate single variant"""
    if verbose:
        print(f"\n{'=' * 70}")
        print(f"ВАРІАНТ {variant_num}")
        print(f"{get_variant_description(variant_num)}")
        print(f"Діапазон: [{x_start}, {x_end}], крок: {step}")
        print(f"{'=' * 70}")
        print(f"{'x':>12} | {'y':>18} | {'Формула':>25}")
        print(f"{'-' * 70}")
    
    x = x_start
    count = 0
    errors = 0
    
    while x <= x_end + EPS:
        try:
            y, formula = variant_func(x)
            if verbose:
                print(f"{x:12.6f} | {y:18.10f} | {formula:>25}")
            count += 1
        except (ValueError, ZeroDivisionError) as e:
            if verbose:
                print(f"{x:12.6f} | {'ПОМИЛКА':>18} | {'---':>25}")
            errors += 1
        
        x += step
    
    if verbose:
        print(f"{'-' * 70}")
        print(f"Обчислено точок: {count}, Помилок: {errors}")
        print(f"{'=' * 70}")
    
    return count, errors


def calculate_all_variants(verbose=True):
    """Calculate all 23 variants"""
    total_points = 0
    total_errors = 0
    
    if verbose:
        print("=" * 70)
        print("АВТОМАТИЧНИЙ РОЗРАХУНОК УСІХ ВАРІАНТІВ")
        print("Практична робота №3")
        print("Табуляція кусково-заданих функцій")
        print("=" * 70)
    
    for variant_num in range(1, 24):
        variant_func = VARIANTS[variant_num]
        params = VARIANT_PARAMETERS[variant_num]
        
        count, errors = tabulate_variant(
            variant_num,
            variant_func,
            params["x_start"],
            params["x_end"],
            params["step"],
            verbose
        )
        
        total_points += count
        total_errors += errors
    
    if verbose:
        print("\n" + "=" * 70)
        print("ПІДСУМОК")
        print("=" * 70)
        print(f"Всього варіантів оброблено: 23")
        print(f"Всього точок обчислено: {total_points}")
        print(f"Всього помилок: {total_errors}")
        print("=" * 70)
    
    return total_points, total_errors


def calculate_specific_variants(variant_list, verbose=True):
    """Calculate specific variants from list"""
    if verbose:
        print("=" * 70)
        print(f"РОЗРАХУНОК ВАРІАНТІВ: {variant_list}")
        print("=" * 70)
    
    total_points = 0
    total_errors = 0
    
    for variant_num in variant_list:
        if variant_num not in VARIANTS:
            print(f"ПОМИЛКА: Варіант {variant_num} не існує!")
            continue
        
        variant_func = VARIANTS[variant_num]
        params = VARIANT_PARAMETERS[variant_num]
        
        count, errors = tabulate_variant(
            variant_num,
            variant_func,
            params["x_start"],
            params["x_end"],
            params["step"],
            verbose
        )
        
        total_points += count
        total_errors += errors
    
    if verbose:
        print("\n" + "=" * 70)
        print(f"Оброблено варіантів: {len(variant_list)}")
        print(f"Обчислено точок: {total_points}")
        print(f"Помилок: {total_errors}")
        print("=" * 70)
    
    return total_points, total_errors


def main():
    """Main program"""
    # Розрахувати ВСІ варіанти
    calculate_all_variants(verbose=True)
    
    # Або розрахувати тільки конкретні варіанти (розкоментуйте потрібне):
    # calculate_specific_variants([1, 4, 6, 8, 23], verbose=True)
    
    # Або тихий режим (тільки підсумок):
    # total_points, total_errors = calculate_all_variants(verbose=False)
    # print(f"Обчислено {total_points} точок, помилок: {total_errors}")


if __name__ == "__main__":
    main()


