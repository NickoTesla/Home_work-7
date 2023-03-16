import os
import shutil
import sys
import unicodedata

# список розширень файлів для кожної категорії
EXTENSIONS = {
    'images': ('JPEG', 'JPG', 'PNG', 'SVG'),
    'videos': ('AVI', 'MP4', 'MOV', 'MKV'),
    'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
    'music': ('MP3', 'OGG', 'WAV', 'AMR'),
    'archives': ('ZIP', 'GZ', 'TAR'),
    'unknown': set()
}


def normalize(filename):
    """
    Проводить транслітерацію кирилічного алфавіту на латинський.
    Замінює всі символи крім латинських літер, цифр на '_'.
    """
    filename = unicodedata.normalize('NFD', filename)
    filename = filename.encode('ascii', 'ignore').decode('ascii')
    filename = ''.join(c if c.isalnum() else '_' for c in filename)
    return filename


def sort_files(path):
    """
    Обробляє папку та всі її вкладені папки, сортує файли по категоріях
    та перейменовує їх.
    """
    for root, dirs, files in os.walk(path):
        for filename in files:
            # Отримуємо розширення файлу
            ext = filename.split('.')[-1].upper()
            # Перевіряємо, до якої категорії відноситься файл
            for category, extensions in EXTENSIONS.items():
                if ext in extensions:
                    # Копіюємо файл в відповідну папку
                    src = os.path.join(root, filename)
                    dst_dir = os.path.join(path, category)
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)
                    dst = os.path.join(dst_dir, normalize(filename))
                    shutil.copy2(src, dst)
                    # Додаємо розширення файлу до відомих розширень
                    EXTENSIONS[category] = EXTENSIONS[category] + (ext,)
                    break
            else:
                # Якщо розширення невідоме, додаємо його до списку невідомих розширень
                EXTENSIONS['unknown'].add(ext)

    # Виводимо результати
    print('Відомі розширення: ', end='')
    print(', '.join(sorted(set(e for extensions in EXTENSIONS.values()
          for e in extensions))))
    print('Розширення, які невідомі програмі: ', end='')
    print(', '.join(sorted(EXTENSIONS['unknown'])))
    for category in EXTENSIONS:
        if category == 'unknown':
            continue
        print(f'Файли у категорії "{category}":')
        for ext in EXTENSIONS[category]:
            print(f'  {ext}')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python3 sort_files.py path")
        sys.exit(1)

    path = sys.argv[1]
    sort_files(path)
