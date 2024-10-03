from PIL import Image
import math

def drawCircle(matrx,r): # Draws a circle with radius of r at the center of the picture
    cx = 255 // 2
    cy = 255 // 2
    for a in range(0,36100):
        px = int(round(cx + r * math.cos(math.radians(a/100))))
        py = int(round(cy + r * math.sin(math.radians(a/100))))
        i = py*256+px
        matrx[i] = (255,px,py,255)

    return matrx
def drawMesh(matrx): # Draws a mesh over the picture by painting the even values of the matrix
    for i,value in enumerate(matrx):
        if (i%256 + i//256)%2==0: 
            matrx[i] = (255,i%256,i//256,255)  
        
    return matrx
        
# Directory of the Matrix
dir = ".\\"
matrix = []
# Read the the matrix which is only for black&white 
with open(dir+"a.txt","r") as openfileobject:
    for line in openfileobject:
        words = [int(x) for x in line.split()]
        for i, value in enumerate(words):
            # Give the value of the pixel to all RGB so that its an spectrum of grey 
            words[i] = (value, value ,value,255)
            matrix.append(words[i])
            
# Open an image file to create and save the new built image (Output)
img = Image.open(dir+'img.jpg')

# # image 1: Editing the existing image (Superman)
list_of_pixels = list(img.getdata())
list_of_pixels = drawMesh(list_of_pixels)
list_of_pixels = drawCircle(list_of_pixels,110)
im1 = Image.new(img.mode, img.size) # Copying image size and mode from the existing image
im1.putdata(list_of_pixels)
im1.show()

# # image 2: Creating an image based on the read matrix (Charlie Chaplin)
# for i in range(70,128,2):
#     list_of_pixels = drawCircle(matrix,i)
# im2 = Image.new(img.mode, img.size)
# im2.putdata(matrix)
# im2.show()

# # save image:
# im2 = im2.save(dir+"newImg.png")

