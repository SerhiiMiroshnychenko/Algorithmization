# Запис у файл
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Привіт, файл!\n")
# Файл закрито автоматично

# Читання з файлу
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read() # Читає весь вміст файлу як один рядок
    print(f"{content = }")
