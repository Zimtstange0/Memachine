from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    """Class to create a Meme object.
    
    Args:
        outpath (str): Path to folder where MEMEs should be stored.
    """
    def __init__(self, outpath):
        self.out_path = outpath         #./static

    def make_meme(self, img_path, text, author, width = 500) -> str:
        # load picture
        img = Image.open(img_path)
        # get filename. Needed to create outputpath
        filename = img_path.split('\\')[-1]
        # resize
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img_s = img.resize((width, height), Image.NEAREST)
        
        # get a drawing context
        draw = ImageDraw.Draw(img_s)

        # get a font
        fnt = ImageFont.truetype(r"C:\MT\00_Scripts\repos\udacity_course\Memachine\src\MemeGenerator\fonts\LilitaOne-Regular.ttf", 20) 

        # Add text and author
        draw.multiline_text((50, 430), text, font=fnt, fill=(0, 0, 0))
        draw.multiline_text((50, 450), author, font=fnt, fill=(0, 0, 100))

        # save at ./temp
        path_to_img = self.out_path + '/' + filename
        img_s.save(path_to_img)
        print(path_to_img)

        #return self.out_path
        return path_to_img