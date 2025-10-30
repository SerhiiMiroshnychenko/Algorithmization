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

    # Зчитування номера варіанту
    variant_input = input("Введіть номер варіанту (1-19): ")

    # Перевірка, чи введено ціле число
    is_valid_variant = True
    if not variant_input:
        is_valid_variant = False
    else:
        for char in variant_input:
            if not char.isdigit():
                is_valid_variant = False
                break

    if not is_valid_variant:
        print("Помилка: номер варіанту має бути цілим числом")
        print("Програма завершена")
    else:
        variant = int(variant_input)

        if variant < 1 or variant > 19:
            print(f"Помилка: невірний номер варіанту {variant}")
            print("Програма завершена")
        else:
            # Обчислення критеріїв сортування для кожного рядка
            criteria = []

            for line in lines:
                match variant:
                    case 1 | 2:
                        # Лексикографічне сортування - використовуємо сам рядок як критерій
                        criteria.append(line)

                    case 3 | 4:
                        # Кількість слів
                        words = line.split()
                        criteria.append(len(words))

                    case 5 | 6:
                        # Довжина першого слова
                        words = line.split()
                        if len(words) > 0:
                            criteria.append(len(words[0]))
                        else:
                            criteria.append(0)

                    case 7 | 8:
                        # Кількість цифр
                        count = 0
                        for ch in line:
                            if ch.isdigit():
                                count += 1
                        criteria.append(count)

                    case 9 | 10:
                        # Кількість малих літер
                        count = 0
                        for ch in line:
                            if ch.islower():
                                count += 1
                        criteria.append(count)

                    case 11 | 12:
                        # Кількість великих літер
                        count = 0
                        for ch in line:
                            if ch.isupper():
                                count += 1
                        criteria.append(count)

                    case 13 | 14:
                        # Кількість пунктуації
                        count = 0
                        for ch in line:
                            if ch in PUNCTUATION:
                                count += 1
                        criteria.append(count)

                    case 15 | 16:
                        # Кількість літер
                        count = 0
                        for ch in line:
                            if ch.isalpha():
                                count += 1
                        criteria.append(count)

                    case 17 | 18:
                        # Довжина другого слова
                        words = line.split()
                        if len(words) > 1:
                            criteria.append(len(words[1]))
                        else:
                            criteria.append(0)

                    case 19:
                        # Кількість недрукованих символів
                        count = 0
                        line = line.encode().decode('unicode_escape')
                        for ch in line:
                            if not ch.isprintable():
                                count += 1
                        criteria.append(count)

            # Визначення напряму сортування
            # Варіанти зі спаданням
            if variant in (2, 4, 5, 8, 9, 11, 13, 15, 17):
                ascending = False
            else:
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