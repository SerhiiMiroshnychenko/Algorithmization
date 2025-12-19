# Метод readlines() — отримання списку рядків

with open('measurement_log.txt', 'r', encoding='utf-8') as file:
    print(f"{file = }")
    print(f"{type(file) = }")
    lines = file.readlines()
    print(f"{lines = }")
    print(f'Кількість рядків: {len(lines)}')
    for num, line in enumerate(lines, start=1):
        print(f'Рядок {num}: {line.strip()}')
