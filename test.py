from PIL import Image
#watermark function
def watermark_with_transparency(input_image_path,watermark_image_path,position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save("NEW.png")

#read the image
im = Image.open("11.png")
if im.width > im.height:
    #rotate image
    angle = 270
    out = im.rotate(angle, expand=True)
    im = out.resize((2480,3507))
im = im.resize((2480,3507))
im.show()
im.save('rotate-output.png')
#call watermark function 
watermark_with_transparency('rotate-output.png','./test-photo/req-logo.png', position=(0,0))