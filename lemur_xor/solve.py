
from PIL import Image, ImageChops

f1 = Image.open(r"flag_7ae18c704272532658c10b5faad06d74.png").convert('RGB')
f2 = Image.open(r"lemur_ed66878c338e662d3473f0d98eedbd0d.png").convert('RGB')
f2 = ImageChops.invert(f2)

ff = ImageChops.difference(f1, f2)
ff = ImageChops.invert(ff)

#ff.save('flag.png') 
ff.show()