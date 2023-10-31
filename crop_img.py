from PIL import Image
import os

# Путь до папки с изображениями
path_to_images = "./data_files/"

# Итерация по всем файлам в папке
for filename in os.listdir(path_to_images):
    # Проверка на соответствие формату PNG
    if filename.endswith(".png"):
        # Переименование оригинального файла
        full_filename = os.path.join(path_to_images, filename.replace('.png', '_full.png'))
        os.rename(os.path.join(path_to_images, filename), full_filename)

        # Открытие изображения
        with Image.open(full_filename) as img:
            # Изменение размера изображения
            # Можно изменить параметр (300, 300) на желаемый размер
            img.thumbnail((300, 300))
            
            # Сохранение сжатого изображения с оригинальным именем
            img.save(os.path.join(path_to_images, filename))

print("Изображения сжаты и оригиналы переименованы.")
