from PIL import Image, ImageDraw

def create_smiley(path='smiley.png'):
    """
    Generates a 256x256 cool smiley face image with sunglasses.
    """
    size = (256, 256)
    background = (255, 255, 255)
    face = (255, 223, 0)
    sunglasses = (0, 0, 0)
    mouth = (255, 102, 0)

    img = Image.new('RGB', size, background)
    draw = ImageDraw.Draw(img)
    
    # Face
    draw.ellipse((32, 32, 224, 224), fill=face, outline=(0,0,0), width=4)
    
    # Sunglasses
    draw.polygon([(60, 90), (120, 90), (120, 130), (60, 130)], fill=sunglasses) # Left lens
    draw.polygon([(136, 90), (196, 90), (196, 130), (136, 130)], fill=sunglasses) # Right lens
    draw.line((120, 100, 136, 100), fill=sunglasses, width=8) # Bridge
    draw.line((32, 105, 60, 100), fill=sunglasses, width=4) # Left arm
    draw.line((196, 100, 224, 105), fill=sunglasses, width=4) # Right arm
    
    # Mouth (cool smirk)
    draw.arc((100, 150, 180, 190), start=0, end=140, fill=mouth, width=6)
    
    img.save(path)

if __name__ == '__main__':
    create_smiley()
