"""
Програма для сортування рядків за різними критеріями
Підтримує варіанти 1-19
Використовує тільки базові конструкції: цикли, умовні оператори, списки
"""

# Символи ASCII-пунктуації
PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Зчитування кількості рядків
n_input = input("Введіть кількість рядків: ")

# Перевірка, чи введено ціле число
is_valid = True
if not n_input:
    is_valid = False
else:
    for char in n_input:
        if not char.isdigit():
            is_valid = False
            break

if not is_valid:
    print("Помилка: кількість має бути цілим числом")
    print("Програма завершена")
else:
    n = int(n_input)

    # Зчитування рядків
    print(f"Введіть {n} рядків:")
    lines = []
    for i in range(n):
        line = input(f"Рядок {i+1}: ")
        lines.append(line)

    variant = 19

    criteria = []

    for line in lines:
        count = 0
        line = line.encode().decode('unicode_escape')
        for ch in line:
            if not ch.isprintable():
                count += 1
        criteria.append(count)

    ascending = True

    # Бульбашкове сортування
    for i in range(len(lines) - 1):
        for j in range(len(lines) - 1 - i):
            # Порівняння criteria[j] з criteria[j+1]
            should_swap = False

            if ascending:
                # Для зростання міняємо, якщо поточний > наступного
                should_swap = criteria[j] > criteria[j + 1]
            else:
                # Для спадання міняємо, якщо поточний < наступного
                should_swap = criteria[j] < criteria[j + 1]

            if should_swap:
                # Обмін рядків
                lines[j], lines[j + 1] = lines[j + 1], lines[j]
                # Обмін критеріїв
                criteria[j], criteria[j + 1] = criteria[j + 1], criteria[j]

    # Виведення результатів
    print(f"\nВідсортовані рядки (варіант {variant}):")
    for i in range(len(lines)):
        # Виведення значення критерію для наочності
        if variant == 1 or variant == 2:
            print(f"{i+1}. {lines[i]}")
        else:
            print(f"{i+1}. [{criteria[i]}] {lines[i]}")
