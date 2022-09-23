from PIL import Image, ImageDraw, ImageFont
import os


class post:
    def __init__(self):
        self.photo_mode = {
            'facebook':{
            'landscape':(630,1200),
            'potrait':(1200,630),
            'stories':(1920,1080),
            'square':(1080,1080)
                },
            'instagram':{
                'landscape':(566,1080),
                'potrait':(1350,1080),
                'stories':(1920,1080),
                'square':(1080,1080)
                }
        }
        self.font_size = {
            'watermark':20,
            'heading':40,
            'content': 30
        }
        ### scanning the fonts
        all_fonts = os.listdir('./src/fonts')
        self.fonts_ = {}
        for i in all_fonts:
            name = i.split(".")[0]
            self.fonts_[name] = f"./src/fonts/{i}"
        self.all_fonts = self.fonts_.keys()

    def load_fonts(self):
        all_fonts = os.listdir('./src/fonts')
        self.fonts_ = {}
        for i in all_fonts:
            name = i.split(".")[0]
            self.fonts_[name] = f"./src/fonts/{i}"
        return self.fonts_

    def choose_font(self):
        print("choose a font. [press enter to use the default one.]")
        fon = input(f'[available: {self.all_fonts}]: ')
        for i in self.all_fonts:
            if fon in i:
                self.font = self.fonts_[i]

    def choose_font_size(self):
        siz = int(input("enter the font size: "))
        self.font_size = siz

    def choose_mode(self):
        inp = input(f"enter social site [options: {self.photo_modes.keys()}] :")
        for i in self.photo_modes.keys():
            if inp in i:
                new_ip = input(f"choose mode [options: {self.photo_modes[i].keys()}] :")
                for j in self.photo_modes[i].keys():
                    if new_ip in j:
                        self.size = self.photo_modes[i][j]
        return self.size
    
    def draw(self):
        jii = Image.new('RGB',(1024,700),color=(5,5,5))
        font = ImageFont.truetype(self.font,self.font_size)
        wr = ImageDraw.Draw(jii)
        wr.text((512,500),"we rock",fill=(255,255,255),font=font)
        jii.save('file.png')

        jii.show()

