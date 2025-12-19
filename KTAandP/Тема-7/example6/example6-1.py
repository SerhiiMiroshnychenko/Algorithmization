from pathlib import Path

# Створення об'єкта шляху
file_path = Path(r'D:\PROJECTs\MY\Algorithmization\KTAandP\Тема-7\example4\measurement_log.txt')

# Перевірка існування файлу
if file_path.exists():
    print(f'Файл {file_path.name} існує')
    print(f'Абсолютний шлях: {file_path.absolute()}')
    print(f'Розширення: {file_path.suffix}')
    print(f'Розмір: {file_path.stat().st_size} байт')
else:
    print('Файл не знайдено')
