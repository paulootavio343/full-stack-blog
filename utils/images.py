from django.conf import settings
from PIL import Image
import os


def resize_image(img_path, new_width, new_height):
    img_path = os.path.join(settings.MEDIA_ROOT, img_path)
    img = Image.open(img_path)
    width, height = img.size
    height_to_resize = round((new_width * height) / width)

    if width <= new_width:
        img.close()
        return

    crop_size_top = (height_to_resize - new_height) / 2
    crop_size_bottom = height_to_resize - crop_size_top

    new_img = img.resize((new_width, height_to_resize), Image.ANTIALIAS)
    new_img = new_img.crop((0, crop_size_top, new_width, crop_size_bottom))
    new_img.save(
        img_path,
        optimize=True,
        quality=80
    )
    new_img.close()
