from PIL import Image, ImageEnhance, ImageFilter
import os


path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    clean_name = os.path.splitext(filename)[0]

    save_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")

    edit.save(save_path)