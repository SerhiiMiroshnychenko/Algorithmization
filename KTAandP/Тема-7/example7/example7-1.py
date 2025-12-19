# Приклад виникнення винятку без обробки
# (цей код призведе до помилки)

# Спроба відкрити неіснуючий файл
try:
    with open('nonexistent_file.txt', 'r') as file:
            content = file.read()
except FileNotFoundError as error:
    print(f"{error.__class__ = }")
    print(f"{str(error) = }")


# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'

print('Закоментований код демонструє помилку FileNotFoundError')
