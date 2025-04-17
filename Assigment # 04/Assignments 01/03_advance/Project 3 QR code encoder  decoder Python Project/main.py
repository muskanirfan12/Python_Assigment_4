import qrcode


data = """Don't forget to subscribe"""
qr = qrcode.QRCode(version = 1 , box_size=10 , border = 5)

qr.add_data(data)

qr.make(fit = True)
image = qr.make_image(fill_color = 'red' , back_color = "white")

image.save(r'F:\python-project\project-4\Assignments 01\03_advance\muqrcode.png')
