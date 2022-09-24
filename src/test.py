from PIL import Image, ImageDraw, ImageFont
import os


class post:
    def __init__(self):
        self.photo_modes = {
            'facebook':{
            'landscape':(1200,630),
            'potrait':(630,1200),
            'stories':(1080,1920),
            'square':(1080,1080)
                },
            'instagram':{
                'landscape':(1080,566),
                'potrait':(1080,1350),
                'stories':(1080,1920),
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
        print(f"fonts available: {self.fonts_.keys()}")
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
        return self.font

    def choose_font_size(self):
        siz = int(input("enter the font size: "))
        self.font_size = siz
        return self.font_size

    def choose_mode(self):
        inp = input(f"enter social site [options: {self.photo_modes.keys()}] :")
        for i in self.photo_modes.keys():
            if inp in i:
                new_ip = input(f"choose mode [options: {self.photo_modes[i].keys()}] :")
                for j in self.photo_modes[i].keys():
                    if new_ip in j:
                        self.size = self.photo_modes[i][j]
        return self.size
    
    def choose_color(self):
        r = int(input("enter red value [max:255]"))
        g = int(input("enter green value [max:255]"))
        b = int(input("enter blue value [max: 255]"))
        self.bg_color = (r,g,b)
        return self.bg_color

    def select_font(self,name=None,size=None):
        self.font = ImageFont.truetype(name,size)
        return self.font

    def draw(self,size=(1024,720),color=(0,0,0),):
        self.jii = Image.new('RGB',size,color=color)
        self.wr = ImageDraw.Draw(self.jii)

    
    def draw_wm(self,text="your water mark",position=(0,0),fill=(255,255,255),font=None):
        self.wr.text(position,text,fill=fill,font=font)
    def draw_header(self):
        self.wr.text((512,20),"your sweet heading",fill=(255,255,255),font=self.font)

    def draw_content(self):
        self.wr.text((20,200),"They just do it brah. fucking do it.",fill=(255,255,255))
    def show(self):
        self.jii.show()
    def save(self,file_name):
        self.jii.save(file_name)

def main():
    p = post()
    logo_font = p.choose_font()
    print(logo_font)
    # header_font = p.choose_font()
    # content_font = p.choose_font()
    logo_f_size = p.choose_font_size()
    logo_font = p.select_font(logo_font,logo_f_size)
    # header_f_size = p.choose_font_size()
    # content_f_size = p.choose_font_size()
    mode = p.choose_mode()
    background_color = p.choose_color()
    p.draw(size=mode,color=background_color)
    p.draw_wm(text="holy fucking",position=(200,200),font=logo_font)
    p.draw_wm(text="holy happy",position=(100,200),font=logo_font)
    p.show()
    p.save('crap.png')


if __name__ == "__main__":
    main()
