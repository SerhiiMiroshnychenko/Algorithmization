# Коректне читання файлу UTF-8
with open('text_utf8.txt', 'r', encoding='utf-8') as file:
    print(f'UTF-8: {file.read()}')
    