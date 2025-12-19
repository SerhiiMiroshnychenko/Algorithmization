from pathlib import Path

# Зручні методи читання та запису через pathlib
file_path = Path('quick_write.txt')
# print(f"{file_path = }")
# print(f"{file_path.exists() = }")

# content = file_path.read_text(encoding='utf-8')
# print(content)

try:
    content = file_path.read_text(encoding='utf-8')
    print(content)
except (FileNotFoundError, ZeroDivisionError) as error:
    # print(f"{error = }")
    print(f"{str(error) = }")
else:
    print('Спрацював ELSE')
finally:
    print('Спрацювало FINALLY')


# try:
#     print(1/0)
#     content = file_path.read_text(encoding='utf-8')
#     print(content)
# except Exception as exception:
#     print(f"{exception = }")
#     print(f"{str(exception) = }")

print('Подальша логіка')

# if file_path.exists():
#     # Читання тексту
#     content = file_path.read_text(encoding='utf-8')
#     print(content)

