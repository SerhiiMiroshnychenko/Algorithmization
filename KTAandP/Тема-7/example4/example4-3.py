# Порядковий перебір файлу через цикл for (найефективніший для великих файлів)

print('Обробка файлу рядок за рядком:')
with open('measurement_log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Видаляємо символи переносу рядка
        clean_line = line.strip()
        print(f'  → {clean_line}')
