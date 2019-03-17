import cv2  # then,in python ,just pil is ok

print(cv2.__version__)
from PIL import Image
from PIL import ImageDraw


def draw_rectangle(file_name):
    im = Image.open(file_name)
    im_draw = ImageDraw.Draw(im);
    cor = [100, 100, 400, 500]
    im_draw.rectangle(cor, width=10)
    im.show()

file_name ="/Users/yongli/Pictures/flower.jpeg"
draw_rectangle(file_name)
