from pyzbar.pyzbar import decode
from PIL import Image
import datetime

# QR Code Scan
image = Image.open(r'F:\python-project\project-4\Assignments 01\03_advance\attendance_qr.png')
results = decode(image)

# Attendance Record
if results:
    student_info = results[0].data.decode()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Attendance Marked: {student_info} at {timestamp}")
else:
    print("Invalid QR Code!")
