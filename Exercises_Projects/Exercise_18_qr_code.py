import qrcode
from PIL import Image

# VERSION 1
# img = qrcode.make("https://github.com/leventeblanar")
# img.save("levente_blanar_GH.png")

qr = qrcode.QRCode(version=1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size= 40, border = 10 )
qr.add_data("https://github.com/leventeblanar")
qr.make(fit=True)
img=qr.make_image(fill_color = "lightgreen", back_color="purple")
img.save("levente_blanarGH2.png")