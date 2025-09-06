import pyqrcode
from PIL import Image

link = input("Enter anything to generate QR : ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=10)
Image.open("QRCode.png")
