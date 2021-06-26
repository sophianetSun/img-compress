import time
from PIL import Image

start_ts = time.perf_counter()

img_path = "IMG_1576.PNG"
with open(img_path, 'rb') as img_f:
    im = Image.open(img_f)
    print(im.format, im.size, im.mode)
    new_img = Image.new("RGB", im.size, (255, 255, 255))
    new_img.paste(im, im)
    new_img.save('output.jpg', quality=85)
    # im.save('output.jpg', compression='JPEG', quality=85)

end_ts = time.perf_counter()
print(f"elasped: {end_ts-start_ts}")