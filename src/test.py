from email import header
from turtle import xcor
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
        self.positions = {
            
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

    def draw_content(self,text="",type='content'):
        if type == 'title':
            x_corr = 305
            y_corr = 70
            tits_f_size = 45
            tits_font = self.fonts_['Roboto-Medium']
            tits_font = self.select_font(tits_font,tits_f_size)
            self.wr.text((x_corr,y_corr),text,font=tits_font)
        elif type == 'logo':
            x_corr = 895
            y_corr = 1000
            logo_f_size = 25
            logo_font = self.fonts_['LibreFranklin-SemiBold']
            logo_font = self.select_font(logo_font,logo_f_size)
            self.wr.text((x_corr,y_corr),text,font=logo_font)
        else:
            title = """
                This is a very long process. It takes alot of 
                effort to achieve.

                I have no idea what I am writting. I think this is 
                enough to see the results
                but not that good for usl.
            """
            x_corr = 10
            y_corr = 150
            print(x_corr)
            tits_f_size = 30
            tits_font = self.fonts_['NotoSansGeorgian-SemiBold']
            tits_font = self.select_font(tits_font,tits_f_size)
            self.wr.text((x_corr,y_corr),text,font=tits_font)
    




def main():
    logo_pos = ()
    title_pos = ()
    content_pos = ()

    p = post()
    # mode = p.choose_mode()
    mode = (1080,1080)

    # logo_font = p.choose_font()
    # position_ = p.choose_pos()
    # background_color = p.choose_color()
    cont = """
    We all have read or heard that computers use binary number system. But why? Why not decimal?

First of all, computers use billions of transistors for storing the bits. Transistor made-up of a semi-conductor material, meaning it can act as an insulator as well as an conductor; depending on the voltage applied. When it is acting as an insulator, i.e. current is absent, it is considered a 0 bit. Similarly, when it is acting as a conductor, it is considered a 1 bit.

So clearly, there are only two possibilities for a single transistor to work on. So, binary.

 But still decimals can be used with it, but we always use binary. Let's see the advantages of using binary over decimal.

      suppose I want to add two numbers 5 and 32 using in computer. Now, using decimal system; I will first turn on 5 transistors in a sequence to represent 5 and other 22 transistors to represents the number 32. Here I had to use 27 transistors.
   
     1.1.1.1.1 + 1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1
     
     Let's redo this same activity using binary. In binary, 5 means 101. So I will make a sequence of 3 transistors and turn on the first and the last one of the sequence. Now 22 is 10110 in binary. So I will make another sequence of 5 transistors and turn on the first, third and the forth ones. Here, I used only 8 transistors.

     1.0.1 + 1.0.1.1.0

You can see the difference in the number of transistors used. 27 is way more than 8. That's why we use binary.
    """
    words = cont.split(" ")
    for i in range(1,len(words)+1):
        if i%10==0:
            words[i] += "\n"
    cont_ = ""
    for i in range(len(words)):
        cont_ += words[i]+" "
    background_color = (63, 70, 159)
    p.draw(size=mode,color=background_color)
    p.draw_content(text="@geekbind",type='logo')
    p.draw_content(text="Why do computers use binary?",type='title')
    p.draw_content(text=cont_)
    # logo_f_size = p.choose_font_size()
    # logo_font = p.select_font(logo_font,logo_f_size)
    # p.draw_wm(text="@shittypage69",position=position_,font_=logo_font)
    # # p.draw_wm(text="@crap",font_=None)
    # print('logo end -- header')
    # header_font = p.choose_font()
    # header_f_size = p.choose_font_size()
    # header_font = p.select_font(header_font,header_f_size)
    # position_ = p.choose_pos()
    # p.draw_wm(text="How do computer read 0 and 1?",font_=header_font,position=position_)
    p.show()
    # print('header end -- content')
    # cont_font = p.choose_font()
    # cont_f_size = p.choose_font_size()
    # position_ = p.choose_pos()
    # cont_font = p.select_font(cont_font,cont_f_size)
    # p.draw_wm(text="This is a long process which is carried out by different method and is very good and shitty at the same time, haha watever but. fuck shit crap piss blah blah whatever",position=position_,font_=cont_font,)
    # p.show()
    p.save("ddd.png")


if __name__ == "__main__":
    main()
