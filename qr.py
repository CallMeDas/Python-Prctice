import qrcode

qr= qrcode.make("https://github.com/CallMeDas/House-Price-Prediction/blob/main/House-Price-Prediction.ipynb")
qr.save("qr.jpg")