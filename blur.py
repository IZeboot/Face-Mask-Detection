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
    dst = cv2.GaussianBlur(img,(1,1),cv2.BORDER_DEFAULT)
    cv2.imwrite('blur{}.png'.format(index), dst)