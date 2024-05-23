import cv2 
img=cv2.imread('image.jpeg')
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('grey.jpg',gry)
cv2.imwrite('rgb.jpg',rgb)