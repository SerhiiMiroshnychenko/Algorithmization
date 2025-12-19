# Демонстрація роботи з кодуваннями

text_ukr = 'Привіт, світе! Це текст українською мовою.'

# Запис
with open('text.txt', 'w') as file:
    print(f"{file = }")
    file.write(text_ukr)
