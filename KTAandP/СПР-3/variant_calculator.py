"""
Комплексний скрипт для табуляції кусково-заданих функцій
Практична робота №3
Варіанти 1-23
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


def tabulate_function(variant_func, x_start, x_end, step, variant_num):
    """Tabulate piecewise function"""
    print(f"\n{'=' * 70}")
    print(f"{'x':>15} | {'y':>20} | {'Формула':>25}")
    print(f"{'=' * 70}")
    
    x = x_start
    count = 0
    
    while x <= x_end + EPS:
        try:
            y, formula = variant_func(x)
            print(f"{x:15.6f} | {y:20.10f} | {formula:>25}")
            count += 1
        except (ValueError, ZeroDivisionError) as e:
            print(f"{x:15.6f} | {'Помилка обчислення':>20} | {'---':>25}")
        
        x += step
    
    print(f"{'=' * 70}")
    print(f"Всього обчислено точок: {count}")


def get_input_parameters():
    """Get tabulation parameters from user"""
    print("\nВведіть параметри табуляції:")
    
    while True:
        try:
            x_start = float(input("Початкове значення x_start: "))
            x_end = float(input("Кінцеве значення x_end: "))
            
            if x_end <= x_start:
                print("Помилка! x_end має бути більшим за x_start.")
                continue
            
            step = float(input("Крок табуляції h: "))
            
            if step <= 0:
                print("Помилка! Крок має бути додатним числом.")
                continue
            
            if step > (x_end - x_start):
                print("Попередження! Крок більший за діапазон. Продовжити? (y/n): ", end="")
                response = input().lower()
                if response != 'y':
                    continue
            
            return x_start, x_end, step
        except ValueError:
            print("Помилка! Введіть дійсне число.")


def main():
    """Main program"""
    print("=" * 70)
    print("ТАБУЛЯЦІЯ КУСКОВО-ЗАДАНИХ ФУНКЦІЙ")
    print("Практична робота №3")
    print("=" * 70)
    
    # Введення номера варіанту
    while True:
        try:
            variant_num = int(input("\nВведіть номер варіанту (1-23): "))
            if 1 <= variant_num <= 23:
                break
            else:
                print("Помилка! Номер варіанту має бути від 1 до 23.")
        except ValueError:
            print("Помилка! Введіть ціле число.")
    
    # Виведення опису варіанту
    print(f"\nВаріант {variant_num}:")
    print(get_variant_description(variant_num))
    
    # Введення параметрів табуляції
    x_start, x_end, step = get_input_parameters()
    
    # Отримання функції для обраного варіанту
    variant_func = VARIANTS[variant_num]
    
    # Табуляція функції
    tabulate_function(variant_func, x_start, x_end, step, variant_num)
    
    # Пропозиція повторити обчислення
    print("\nБажаєте виконати обчислення для іншого варіанту? (y/n): ", end="")
    response = input().lower()
    
    if response == 'y':
        print("\n" + "=" * 70 + "\n")
        main()
    else:
        print("\n" + "=" * 70)
        print("Дякуємо за використання програми!")
        print("=" * 70)


if __name__ == "__main__":
    main()


