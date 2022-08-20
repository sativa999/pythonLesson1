print('тезис 1. пайтон - интерпретируемый язык')
print('тезис 2. pycharm для каждого проекта создаёт локальное виртуальное окружение (venv).\n'
      + '\tглобально же (из любой папки в винде) среда пайтона будет недоступна.')

# любая библиотека делится на две части: внутренняя и внешняя (API).

# from 'lib name' import 'module name'. https://docs.python.org/3/reference/import.html

from PIL import Image, ImageFilter
from colorsys import rgb_to_hsv, hsv_to_rgb

def washout(r, g, b):
    h, s, v = rgb_to_hsv(r, g, b)
    if 0.3 < h < 0.7:
        print('saturation between 0.3 and 0.7 for pixel')
        s = 0
    # v = 0.6
    return hsv_to_rgb(h, s, v)


im = Image.open('images.jpg')
im = im.filter(ImageFilter.Color3DLUT.generate(17, washout))
im.save('images_processed.jpg')


