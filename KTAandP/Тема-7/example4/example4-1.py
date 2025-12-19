# Метод read() — зчитування всього вмісту

with open('measurement_log.txt', 'r', encoding='utf-8') as file:
    full_content = file.read()
    print('Повний вміст файлу:')
    print(full_content)
