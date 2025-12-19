# Обробка помилок кодування за допомогою параметра errors

# Параметр errors='replace' замінює некоректні символи на знак заміни
with open('text_cp1251.txt', 'r', encoding='utf-8', errors='replace') as file:
    print(f'Некоректне кодування з заміною: {file.read()}')
    