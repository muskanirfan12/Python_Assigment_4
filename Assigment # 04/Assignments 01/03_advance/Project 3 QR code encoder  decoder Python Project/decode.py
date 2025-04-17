from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open(r'F:\python-project\project-4\Assignments 01\03_advance\muqrcode.png')

result = decode(image)


print(result)