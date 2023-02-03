import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10, # size of th box where qr code will be displayed
    border = 5 #it is the white part of image--border in all 4 sides with white color
)

data="https://www.youtube.com/watch?v=6qqIGFbiFMU"
#as i have given the path of youtube channel

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")