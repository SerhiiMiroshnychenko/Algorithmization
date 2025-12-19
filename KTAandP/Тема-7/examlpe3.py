# Читання даних з файлу
with open('measurements.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print('Прочитані дані з measurements.txt:')
    print(content)

with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print('Прочитані дані з example.txt:')
    print(content)