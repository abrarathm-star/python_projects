import qrcode

# Sajda Song

img = qrcode.make("https://www.youtube.com/watch?v=Vl2zhN_CfW0")
img.save("qr youtube.png")

