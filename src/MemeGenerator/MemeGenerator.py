import re
from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    """Class to create a Meme object.
    
    Args:
        outpath (str): Path to folder where MEMEs should be stored.
    """
    def __init__(self, outpath):
        self.out_path = outpath         #./static
        self.file_cnt = 0               # helper variable to increment the filename

    def make_meme(self, img_path, text, author, width = 500) -> str:
        # load picture
        img = Image.open(img_path)
        # get filename. Needed to create outputpath.
        filename = img_path.split('/')[-1]
        self.file_cnt = self.file_cnt + 1
        filename = re.sub('\d', str(self.file_cnt), filename)

        # resize
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img_s = img.resize((width, height), Image.NEAREST)
        
        # get a drawing context
        draw = ImageDraw.Draw(img_s)

        # get a font
        fnt = ImageFont.truetype('./MemeGenerator/fonts/LilitaOne-Regular.ttf', 35) 

        # Add text and author
        draw.multiline_text((50, 10), text, font=fnt, fill=(100, 123, 200), stroke_width=4, stroke_fill='black')
        draw.multiline_text((60, 60), 'from: ' + author, font=fnt, fill=(200, 23, 100), stroke_width=4, stroke_fill='black')

        # save at ./temp
        path_to_img = self.out_path + '/' + filename
        img_s.save(path_to_img)
        print(path_to_img)

        #return self.out_path
        return path_to_img