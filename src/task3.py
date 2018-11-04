import cv2
import numpy as np

image = cv2.imread('media/task3.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

transformed = np.fft.fft2(image)
shifted = np.fft.fftshift(transformed)

mask = np.ones((rows, cols), np.uint8)
mask[crow - 15:crow + 15, ccol - 70:ccol + 70] = 0
filtered = shifted * mask

ishifted = np.fft.ifftshift(filtered)
output = np.fft.ifft2(ishifted)

output = np.abs(output)
output = np.asarray(output, np.uint8)
cv2.imshow('Compare', np.concatenate((image, output), axis=1))

cv2.waitKey(0)
cv2.destroyAllWindows()
