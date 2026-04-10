from PIL import Image, ImageDraw

def create_smiley(path='smiley.png'):
    size = (256, 256)
    background = (255, 255, 255)
    face = (255, 223, 0)
    eye = (0, 0, 0)
    mouth = (255, 102, 0)

    img = Image.new('RGB', size, background)
    draw = ImageDraw.Draw(img)
    draw.ellipse((32, 32, 224, 224), fill=face, outline=(0,0,0), width=4)
    draw.ellipse((80, 96, 120, 136), fill=eye)
    draw.ellipse((136, 96, 176, 136), fill=eye)
    draw.arc((80, 110, 176, 200), start=20, end=160, fill=mouth, width=6)
    img.save(path)

if __name__ == '__main__':
    create_smiley()
