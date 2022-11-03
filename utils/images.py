from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import os


def resize_image(image, new_width, new_height):
    memory_img = BytesIO(image.read())
    img = Image.open(memory_img)
    width, height = img.size
    height_to_resize = round((new_width * height) / width)
    img_format = os.path.splitext(image.name)[1][1:].upper()
    img_format = 'JPEG' if img_format == 'JPG' else img_format

    if width <= new_width:
        img.close()
        return image

    crop_size_top = (height_to_resize - new_height) / 2
    crop_size_bottom = height_to_resize - crop_size_top

    img = img.resize((new_width, height_to_resize), Image.ANTIALIAS)
    img = img.crop((0, crop_size_top, new_width, crop_size_bottom))
    buffer = BytesIO()
    img.save(buffer, format=img_format)
    new_img = ContentFile(buffer.getvalue())
    img.close()
    return InMemoryUploadedFile(new_img, 'ImageField', image.name, img_format, None, None)
