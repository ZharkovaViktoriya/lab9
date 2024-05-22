import os
import csv
from PIL import Image
from PIL import ImageFilter
def z1():
    old_dir="old"
    new_dir="new"
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    for filename in os.listdir(old_dir):
        image=os.path.join(old_dir, filename)
        img = Image.open(image)
        img = img.filter(ImageFilter.EMBOSS)
        img.save(f'new/{filename}')
def z2():
    old_dir = "old"
    new_dir = "new"
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    for filename in os.listdir(old_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = os.path.join(old_dir, filename)
            img = Image.open(image)
            img = img.filter(ImageFilter.EMBOSS)
            img.save(f'new/{filename}')

def z3():
    with open('spisok.csv',encoding='utf-8') as f:
        reader= csv.reader(f)
        next(reader)
        s=0
        print("Нужно купить:")
        for row in reader:
            print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
            s+=int(row[1])*int(row[2])
        print(f'Итоговая сумма: {s} руб.')

z1()
z2()
z3()