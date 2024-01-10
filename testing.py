# import required libraries
import cv2
import numpy as np

# load the input images
img1 = cv2.imread('images\giant1.png')
img2 = cv2.imread('images\giant1.png')

# convert the images to grayscale
# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)

cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
