import qrcode
import telebot

data = input('> ')

qr = qrcode.QRCode(version=1, box_size=10, border=4)

qr.add_data(data)
qr.make(fit=10)

qr_img = qr.make_image(fill_color='black',  back_color='white')

qr_img.save('qrcode.png')