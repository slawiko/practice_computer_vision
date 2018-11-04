import numpy as np
import cv2

original = cv2.imread('media/task2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original', original)

pos1 = np.float32([
    [135, 215],
    [476, 114],
    [358, 569],
    [742, 413]
])

pos2 = np.float32([
    [0, 0],
    [500, 0],
    [0, 700],
    [500, 700],
])

M = cv2.getPerspectiveTransform(pos1, pos2)

transformed = cv2.warpPerspective(original, M, (838, 670))

cv2.imshow('Transformed', transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
