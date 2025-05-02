import qrcode
qr = qrcode.make(input("Enter Link , Text , URL , profile URL or something else :  "))

qr.save(" QR code.png")

print("QR code saved the file name is QR code.png ")