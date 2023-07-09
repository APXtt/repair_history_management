import qrcode

for i in range(1, 101):
    img = qrcode.make('http://127.0.0.1:8000/machine/{}/short'.format(i))
    img.save('scripts/ImageQR/{}.png'.format(i))