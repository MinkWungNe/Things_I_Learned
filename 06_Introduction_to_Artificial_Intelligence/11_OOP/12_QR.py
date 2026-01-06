'''
Open CMD and enter 2 codes:
pip install qrcode
pip install Pillow
'''

import qrcode
from PIL import Image

data = input('Insert anything you want to make QR code')

qr = qrcode.QRCode(version=3, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="Black", back_color = "Peru")

image.save('QR_Code.png')
Image.open('QR_Code.png')