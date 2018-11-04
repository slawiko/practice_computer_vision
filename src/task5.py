import numpy as np
import cv2

original = cv2.imread('media/task5.png')
image = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

_, big_circles = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
_, dots = cv2.threshold(image, 97, 255, cv2.THRESH_BINARY)

green_big_circles = cv2.cvtColor(big_circles, cv2.COLOR_GRAY2RGB)
green_big_circles[big_circles == 255] = [0, 255, 0]

kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(green_big_circles, kernel, iterations=1)
kernel = np.ones((10, 10), np.uint8)
closed = cv2.morphologyEx(eroded, cv2.MORPH_CLOSE, kernel)
kernel = np.ones((3, 3), np.uint8)
double_eroded = cv2.erode(closed, kernel, iterations=1)

kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(double_eroded, kernel, iterations=1)
kernel = np.ones((10, 10), np.uint8)
opened = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
kernel = np.ones((5, 5), np.uint8)
double_dilated = cv2.dilate(opened, kernel, iterations=1)

dots_rgb = cv2.cvtColor(dots, cv2.COLOR_GRAY2RGB)
green_dots = dots_rgb | double_dilated

new = green_dots & original

result = np.concatenate((original, new), axis=1)
cv2.imshow('original -> greed_dots', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
