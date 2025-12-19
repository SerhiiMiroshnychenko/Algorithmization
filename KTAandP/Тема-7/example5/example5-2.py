text_ukr = 'Привіт, світе! Це текст українською мовою.'

# Запис у форматі Windows-1251
with open('text_cp1251.txt', 'w', encoding='cp1251') as file:
    file.write(text_ukr)
