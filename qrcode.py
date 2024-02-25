import pyqrcode 
from pyqrcode import QRCode
# String which represent the QR code 
s = "https://instagram.com/gat_aiml?igshid=ZGUzMzM3NWJiOQ=="
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("qr.svg", scale = 8) 