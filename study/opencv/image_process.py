import sys
import numpy as np
import cv2

## 밝기 조절 코드 - 흑백
# src = cv2.imread('/home/soomin/dev_ws/opencv/data/lenna.bmp', cv2.IMREAD_GRAYSCALE)
# if src is None:
#     print('Image load failed!')
#     sys.exit()

# dst1 = cv2.add(src, 100)
# dst2 = np.clip(src + 100., 0, 255).astype(np.uint8)

# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# ## 밝기 조절 코드 - 칼라
# src = cv2.imread('/home/soomin/dev_ws/opencv/data/lenna.bmp')
# if src is None:
#     print('Image load failed!')
#     sys.exit()

# dst1 = cv2.add(src, (100, 100, 100, 0))
# dst2 = np.clip(src + 100., 0, 255).astype(np.uint8)

# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2 ', dst2)

# cv2.waitKey()
# cv2.destroyAllWindows()

## 명암비 조절 코드
# import sys
# import numpy as np
# import cv2
# src = cv2.imread('/home/soomin/dev_ws/opencv/data/lenna.bmp', cv2.IMREAD_GRAYSCALE)

# if src is None:
#     print('Image load failed!')
#     sys.exit()
# alpha = 1.0
# dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

## 정규화 코드

# import sys
# import numpy as np
# import cv2

# src = cv2.imread('/home/soomin/dev_ws/opencv/data/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

# if src is None:
#     print("image load failed")
#     sys.exit()

# dst = cv2.normalize(src, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

# cv2.destroyAllWindows()

## YCbCr 색공간 

# import sys
# import numpy as np
# import cv2

# src = cv2.imread('/home/soomin/dev_ws/opencv/data/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

# if src is None:
#     print('image load failed')
#     sys.exit()

# dst = cv2.equalizeHist(src)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

# cv2.destroyAllWindows()

## 컬러 영상의 히스토그램 평활화
# src = cv2.imread('/home/soomin/dev_ws/opencv/data/field.bmp')
# if src is None:
#     print('Image load failed!')
#     sys.exit()
# src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# y, cr, cb = cv2.split(src_ycrcb)

# ## 밝기 성분에 대해서만 히스토그램 평활화 수행
# ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])
# dst_ycrcb = cv2.merge((y, cr, cb))
# dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

## inrange 
import sys
import numpy as np
import cv2

src = cv2.imread('/home/soomin/dev_ws/opencv/data/candies.png')
#src = cv2.imread('candies2.png')
if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()