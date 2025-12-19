# Параметр errors='ignore' пропускає некоректні символи
with open('text_cp1251.txt', 'r', encoding='utf-8', errors='ignore') as file:
    print(f'Некоректне кодування з пропуском: {file.read()}')
