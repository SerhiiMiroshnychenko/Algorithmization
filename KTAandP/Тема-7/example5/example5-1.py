# Демонстрація роботи з кодуваннями

text_ukr = 'Привіт, світе! Це текст українською мовою.'

# Запис у форматі UTF-8
with open('text_utf8.txt', 'w', encoding='utf-8') as file:
    print(f"{file = }")
    file.write(text_ukr)
