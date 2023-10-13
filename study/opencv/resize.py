import sys
import numpy as np
import cv2

src = cv2.imread('./data/airplane.bmp')

if src is None:
    print('image load failed')
    sys.exit()

dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920,1280), interpolation = cv2.INTER_LINEAR)
dst3=  cv2.resize(src, (1920, 1280), interpolation = cv2.INTER_CUBIC)   ## w, h
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

dst5 = cv2.pyrDown(src)

dst6 = cv2.flip(src, -1)

cv2.imshow('src', src)
cv2.imshow('dst', dst6)  ## h, w 
cv2.waitKey()
cv2.destoryAllWindows()
