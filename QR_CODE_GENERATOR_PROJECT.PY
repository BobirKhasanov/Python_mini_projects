import qrcode
url = input("Enter the URL:= "). strip()
img = qrcode.make(url)
img.save("ReadyWithCode_QR.png")
print("QR_code")
