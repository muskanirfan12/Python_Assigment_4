import qrcode

# Unique Data (Employee ID / Student Roll Number)
data = "Student: Areeba Yaseen | Roll No: 12345"

# QR Code Generate
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Image Save
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save(r'F:\python-project\project-4\Assignments 01\03_advance\attendance_qr.png')

print("QR Code generated for:", data)
