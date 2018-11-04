import numpy as np
import cv2

original = cv2.imread('media/task4.jpg')
output = original.copy()

blured = cv2.GaussianBlur(original, (5, 5), 0)
edges = cv2.Canny(blured, 50, 80)

lines = cv2.HoughLinesP(edges, 1, np.pi / 16, 10, minLineLength=15, maxLineGap=2)
for x in range(0, len(lines)):
    for x1, y1, x2, y2 in lines[x]:
        cv2.line(output, (x1, y1), (x2, y2), (0, 0, 255), 2)

result = np.concatenate((original, output), axis=1)
cv2.imshow('Output', result)

cv2.waitKey(0)
cv2.destroyAllWindows()