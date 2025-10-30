"""
Тестування шаблону розв'язку для всіх варіантів ІЗ2
Автоматично перевіряє роботу сортування для варіантів 1-19
"""

# Символи ASCII-пунктуації
PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Тестові дані з різними характеристиками
test_lines = [
    "Hello World",           # 2 слова, 10 літер, 1 велика, 9 малих, 0 цифр, 0 пунктуації, 0 недрукованих
    "Python3.11",            # 1 слово, 6 літер, 1 велика, 5 малих, 3 цифри, 1 пунктуація, 0 недрукованих
    "test string here",      # 3 слова, 14 літер, 0 великих, 14 малих, 0 цифр, 0 пунктуації, 0 недрукованих
    "ABC 123",               # 2 слова, 3 літери, 3 великих, 0 малих, 3 цифри, 0 пунктуації, 0 недрукованих
    "Hi!!!",                 # 1 слово, 2 літери, 1 велика, 1 мала, 0 цифр, 3 пунктуації, 0 недрукованих
    "a",                     # 1 слово, 1 літера, 0 великих, 1 мала, 0 цифр, 0 пунктуації, 0 недрукованих
    "Programming in Python", # 3 слова, 17 літер, 2 великих, 15 малих, 0 цифр, 0 пунктуації, 0 недрукованих
    "2024 year",             # 2 слова, 4 літери, 0 великих, 4 малих, 4 цифри, 0 пунктуації, 0 недрукованих
    "Test\n\nLine",          # 2 слова, 8 літер, 1 велика, 7 малих, 0 цифр, 0 пунктуації, 2 недрукованих (\n\n)
    "Tab\t\there",           # 2 слова, 7 літер, 1 велика, 6 малих, 0 цифр, 0 пунктуації, 2 недрукованих (\t\t)
]

# Опис варіантів
variant_descriptions = {
    1: "Лексикографічно (зростання)",
    2: "Лексикографічно (спадання)",
    3: "За кількістю слів (зростання)",
    4: "За кількістю слів (спадання)",
    5: "За довжиною першого слова (спадання)",
    6: "За довжиною першого слова (зростання)",
    7: "За кількістю цифр (зростання)",
    8: "За кількістю цифр (спадання)",
    9: "За кількістю малих літер (спадання)",
    10: "За кількістю малих літер (зростання)",
    11: "За кількістю великих літер (спадання)",
    12: "За кількістю великих літер (зростання)",
    13: "За кількістю пунктуації (спадання)",
    14: "За кількістю пунктуації (зростання)",
    15: "За кількістю літер (зростання)",
    16: "За кількістю літер (спадання)",
    17: "За довжиною другого слова (спадання)",
    18: "За довжиною другого слова (зростання)",
    19: "За кількістю недрукованих символів (зростання)",
}

def test_variant(variant):
    """
    Тестування одного варіанту
    """
    # Копіюємо тестові дані
    lines = test_lines.copy()

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
                for ch in line:
                    if not ch.isprintable():
                        count += 1
                criteria.append(count)

    # Визначення напряму сортування
    if variant in (2, 4, 5, 8, 9, 11, 13, 16, 17):
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
    print(f"\n{'='*80}")
    print(f"ВАРІАНТ {variant}: {variant_descriptions[variant]}")
    print(f"{'='*80}")
    
    for i in range(len(lines)):
        # Виведення значення критерію для наочності
        if variant == 1 or variant == 2:
            print(f"{i+1}. {lines[i]}")
        else:
            print(f"{i+1}. [{criteria[i]}] {lines[i]}")

# Основна програма
if __name__ == "__main__":
    print("ТЕСТУВАННЯ ШАБЛОНУ РОЗВ'ЯЗКУ ДЛЯ ВСІХ ВАРІАНТІВ ІЗ2")
    print(f"{'='*80}")
    print("Тестові дані:")
    for i, line in enumerate(test_lines, 1):
        print(f"  {i}. {line}")
    
    # Тестування всіх варіантів
    for variant in range(1, 20):
        test_variant(variant)
    
    print(f"\n{'='*80}")
    print("ТЕСТУВАННЯ ЗАВЕРШЕНО")
    print(f"{'='*80}")

