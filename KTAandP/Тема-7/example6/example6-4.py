from pathlib import Path

# Зручні методи читання та запису через pathlib
file_path = Path('quick_write.txt')

# Видалення файлу
file_path.unlink()
print('\nФайл видалено')
