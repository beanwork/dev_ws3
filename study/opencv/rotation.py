import sys
import numpy as np
import cv2

src = cv2.imread('./data/airplane.bmp')

if src is None:
    print('image is none')
    sys.exit()

rad = 20 * np.pi /180
aff = np.array([[np.cos(rad), np.sin(rad), 0],
                [-np.sin(rad), np.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destoryAllWindows()