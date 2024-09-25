"pip Install qrcode"
import qrcode as qr
a = input("Enter your qr detail: ")
img = qr.make(a)
img.save("qrcode.png")
