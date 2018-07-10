from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('westbrook.jpg')
pix = img.load()
width = img.size[0]
print(width)
height = img.size[1]
print(height)
for x in range(width):
    for y in range(height):
        r,g,b=pix[x, y]
        pix[x,y]=int(r/2),int(g/2),int(b/2)
plt.figure("westbrook")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()