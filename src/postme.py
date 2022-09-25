from PIL import Image, ImageDraw, ImageFont
import os


class postme:
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
        self.positions = {
            
        }
        self.font_size = {
            'watermark':20,
            'heading':40,
            'content': 30
        }
        self.mode = (1080,1080)
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
        print(size)
    def choose_pos(self):
        x_cor = int(input("enter the x cordinate"))
        y_cor = int(input("enter the y-cordinate"))
        return (x_cor,y_cor)
    def draw_wm(self,text="your water mark",position=(0,0),fill_=(255,255,255),font_=None):
        self.wr.text(position,text,fill=fill_,font=font_)
    def draw_header(self):
        self.wr.text((512,20),"your sweet heading",fill=(255,255,255),font=self.font)
    def draw_content(self):
        self.wr.text((20,200),"They just .. ladfjl",fill=(255,255,255))
    def show(self):
        self.jii.show()
    def save(self,file_name):
        self.jii.save(file_name)
    def draw_logo(self):
        x_corr = 895
        y_corr = 1000
        logo_f_size = 25
        logo_font = self.fonts_['LibreFranklin-SemiBold']
        logo_font = self.select_font(logo_font,logo_f_size)
        self.wr.text((x_corr,y_corr),"@geekbind",font=logo_font)
    
    def draw_title(self):
        title = "How do computers read binary?"
        x_corr = 305
        y_corr = 70
        print(x_corr)
        tits_f_size = 45
        tits_font = self.fonts_['Roboto-Medium']
        tits_font = self.select_font(tits_font,tits_f_size)
        self.wr.text((x_corr,y_corr),title,font=tits_font)

    def add_line_breaks(self,text):
        words = text.split(" ")
        for i in range(1,len(words)+1):
            if i%10==0:
                words[i] += "\n"
        cont_ = ""
        for i in range(len(words)):
            cont_ += words[i]+" "
        return cont_

    def draw_content(self,logo_pos=None,text="",type='content'):
        if type == 'title':
            x_corr = 305
            y_corr = 70
            tits_f_size = 45
            tits_font = self.fonts_['Roboto-Medium']
            tits_font = self.select_font(tits_font,tits_f_size)
            self.wr.text((x_corr,y_corr),text,font=tits_font)
        elif type == 'logo':
            # x_corr = 895 #for right
            # x_corr = 50 # for left
            if logo_pos == "left":
                logo_pos = 30
            elif logo_pos == "centre":
                logo_pos = 470
            elif logo_pos == "right":
                logo_pos = 895
            x_corr = logo_pos #for center
            y_corr = 1000
            logo_f_size = 25
            logo_font = self.fonts_['LibreFranklin-SemiBold']
            logo_font = self.select_font(logo_font,logo_f_size)
            self.wr.text((x_corr,y_corr),text,font=logo_font)
        else:
            x_corr = 10
            y_corr = 150
            tits_f_size = 30
            tits_font = self.fonts_['NotoSansGeorgian-SemiBold']
            tits_font = self.select_font(tits_font,tits_f_size)
            text = self.add_line_breaks(text)
            self.wr.text((x_corr,y_corr),text,font=tits_font)

    def draw_many(self,title,content,logo):
        background_color = [
            (63, 70, 159),
            (140,110,201),
            (110,201,189),
            (89,215,57),
            (215,168,57),
            (215,73,57)
        ]
        logo_x_corr = [895,50,470]
        for i in range(len(background_color)):
            for j in range(len(logo_x_corr)):
                self.draw(size=self.mode,color=background_color[i])
                self.draw_content(text=logo,type='logo',logo_pos=logo_x_corr[j])
                self.draw_content(text=title,type='title')
                self.draw_content(text=content)
                self.save(f"postme{i}{j}.png")

def main():
    p = postme()
    mode = (1080,1080)
    tt = "How do computers read binary digits?"
    pp = "content"
    ll = "@geekbind"
    cont = """
    We all have read or heard that computers use binary number system. But why? Why not decimal?

First of all, computers use billions of transistors for storing the bits. Transistor made-up of a semi-conductor material, meaning it can act as an insulator as well as an conductor; depending on the voltage applied. When it is acting as an insulator, i.e. current is absent, it is considered a 0 bit. Similarly, when it is acting as a conductor, it is considered a 1 bit.

So clearly, there are only two possibilities for a single transistor to work on. So, binary
You can see the difference in the number of transistors used. 27 is way more than 8. That's why we use binary.
    """

    background_color = [
        (63, 70, 159),
        (140,110,201),
        (110,201,189),
        (89,215,57),
        (215,168,57),
        (215,73,57)
    ]
    logo_x_corr = [895,50,470]
    p.draw(size=mode,color=background_color[3])
    p.draw_many(title="utsab is genius",content="wow really",logo="saferige")


if __name__ == "__main__":
    main()
