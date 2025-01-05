import os
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=RrWDf1eeb2g&list=RDRrWDf1eeb2g&start_radio=1&ab_channel=RANDOM%27MUSIC%27BYMASSATO1") #link of the https you want to make your qr
img.save("qr.png", "PNG") #saves a file as a qr with the name in the brackets
os.system("eog qr.png")    # Use xdg-open to open the image on Linux
