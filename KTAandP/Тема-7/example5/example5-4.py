# Коректне читання файлу Windows-1251
with open('text_cp1251.txt', 'r', encoding='cp1251') as file:
    print(f'CP1251: {file.read()}')
