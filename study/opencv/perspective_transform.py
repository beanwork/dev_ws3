import sys
import cv2
import numpy as np

src = cv2.imread('./data/pinkwink_namecard.jpeg')

if src is None:
    print('image load failed')
    sys.exit()

w, h = 720, 400

srcQuad = np.array([[360,345], [879, 404], [895, 664], [254, 573]], dtype=np.float32)
dstQuad = np.array([[0,0], [w, 0], [w, h], [0, h]], dtype=np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)  ## set matrix
dst = cv2.warpPerspective(src, pers, (w, h))  ## rotate img for matrix

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destoryAllWindows()

