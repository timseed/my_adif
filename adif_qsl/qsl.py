#Actually from pillow
from PIL import Image, ImageDraw, ImageFont
import sys

class qsl(object):

    def __init__(self):
        junk=1

    def qsl(self):
        im = Image.open("adif_qsl.jpg")
        draw = ImageDraw.Draw(im)
        draw.line((0, 0) + im.size, fill=128)
        draw.line((0, im.size[1], im.size[0], 0), fill=128)


        # get a font

        #Fonts generated by
        #mkdir fonts && cd fonts
        #fondu /System/Library/Fonts/Helvetica.dfont
        #cp * /Users/tim/pe35/lib/python3.5/site-packages

        fnt = ImageFont.truetype('Courier', 300)

        # draw text, half opacity
        draw.text((100, 300), "Hello", font=fnt, fill=(255, 255, 255, 128))
        # draw text, full opacity
        draw.text((100, 1300), "World", font=fnt, fill=(255, 255, 255, 255))

        del draw

        # write to stdout
        im.save("new.jpg", "jpeg")



if __name__ == "__main__":
    q = qsl()
    q.qsl()