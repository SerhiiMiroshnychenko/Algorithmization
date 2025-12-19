from pathlib import Path

# Зручні методи читання та запису через pathlib
file_path = Path('quick_write.txt')

# Запис тексту
file_path.write_text('Швидкий запис через pathlib\nДругий рядок', encoding='utf-8')
