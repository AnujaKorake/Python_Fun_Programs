import cv2
image = cv2.imread('MSDhoni.jpeg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255-grayImage
blur = cv2.GaussianBlur(inverted, (21,21), 0)
invertedblur = 255-blur
sketch = cv2.divide(grayImage, invertedblur, scale=256.0)
cv2.imwrite("skech_image.png", sketch)
cv2.imshow("Image", sketch)
