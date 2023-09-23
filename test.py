from PIL import ImageDraw,ImageFont,Image
import numpy as np
image_count=Image.open('img_out\shrimp_0000.jpg')
draw = ImageDraw.Draw(image_count)
font4count= ImageFont.truetype(font='model_data/simhei.ttf', size=np.floor(1e-2 * image_count.size[1] + 20).astype('int32'))

draw.text([20,20], "number of shrimps: " + str(1), fill=(0, 255, 0), font=font4count)