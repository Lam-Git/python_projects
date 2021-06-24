import qrcode

data = " Don't forget to Subscribe "

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")

# img.save(C:/ THIS IS DIFFERENT FOR EVERYONE WITH THE SAME FORMATE)
img.save("C:/Desktop/python_projects/new/qrcode1.png")
