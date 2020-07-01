import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

folder = "images"

onlyfiles = [f for f in os.listdir(
    folder) if os.path.isfile(os.path.join(folder, f))]
for index in range(len(onlyfiles)):
        
    img = cv2.imread(folder + "/" + onlyfiles[index], -1)

    if img is None:
        print('errr')
        sys.exit()


    height, width = (img.shape[0] , img.shape[1])
    size = (width, height)
    center = (width/2,height/2)

    dst_mat = np.zeros((height, width, 4), np.uint8)

    angle = -30.0

    scale = 1

    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    img_dst = cv2.warpAffine(img, rotation_matrix, size, dst_mat,
                            flags=cv2.INTER_LINEAR,
                            borderMode=cv2.BORDER_TRANSPARENT)

    cv2.imwrite("dst.png", img_dst)

    plt.imshow(cv2.cvtColor(img_dst, cv2.COLOR_BGRA2RGBA))
    plt.show()
    key = cv2.waitKey(1000)
    if key == 27:
        cv2.destroyAllWindows()
        break