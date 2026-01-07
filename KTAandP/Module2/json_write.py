import json
data = {'name': 'Іван', 'age': 25, 'isStudent': True}

# Запис у файл
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4) # indent для зручного читання

# Читання з файлу
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(f"{loaded_data = }")
