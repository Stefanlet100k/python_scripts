import os
from unidecode import unidecode
from PIL import Image

dirfrom = 'photos/'
dirto = 'photos_new/'

files = [f for f in os.listdir(dirfrom)]

for file in files:
    old_name = file
    new_name = unidecode(file.replace(',', '_'))

    with Image.open(dirfrom + old_name) as im:
        if im.height + im.width > 1080+1920:
            im.thumbnail((1920, 1080))
        name = new_name.split('.')[0]
        print(name)
        im.save(dirto + name + '.jpg')
