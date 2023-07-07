from PIL import Image, ImageEnhance, ImageFilter
import os


path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    factor = 1.1
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    save_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")

    edit.save(save_path)