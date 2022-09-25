# postme
A project to generate textual images for your social media handles.


Class contains lots of functions, most are crap.


Only useful one is: draw_content



    p = Postme() #creating instance
    ## first you need to draw an empty image, to do so;
    p.draw(size=(1080,1080),color=(22,33,44))
    `size`: a tuple ; describes the size of image, i.e size = (width,height)
    `color`: a tuple of 3 values; describes the background color of the image; i.e color = (red,green,blue)

you have created an empty image, to view it

    p.show()

for adding text on it, I have defined a function with three modes:

- title:

        p.draw_content(type="title",text="this is my title")

- logo:

        p.draw_content(type="logo",text="@mycompany",logo_pos="centre")
        # logo_pos can be  `centre `, `left` or `right`
- content:

        p.draw_content(text="this is very long content")
        # this doesn't require the type parameter as it is default.

----

one more slightly better function is draw_many()

- It will create and save multiple images [with different backgrounds and different logo positons] for you automatically.

        p.draw_many(title="this is title",content="content here",logo="mycompany")