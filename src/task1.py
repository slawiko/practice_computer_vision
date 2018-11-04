import cv2
import numpy

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size = 3

def convolution(image, kernel, kernel_size):
  kernel_half = kernel_size // 2
  image_height, image_width, = image.shape
  for x in range(kernel_half, image_width - kernel_half):
    for y in range(kernel_half, image_height - kernel_half):
      mult(image[x][y], kernel_half, kernel_size)

def mult(center, half, kernel):
  pass # TODO

# for col in numpy.nditer(image):
#   for row in numpy.nditer(col):
#     print(row)

# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
