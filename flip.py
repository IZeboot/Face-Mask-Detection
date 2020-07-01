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

    img_flip_lr = cv2.flip(img, 1)
    cv2.imwrite('fill{}.png'.format(index), img_flip_lr)

    plt.imshow(cv2.cvtColor(img_flip_lr, cv2.COLOR_BGRA2RGBA))
    plt.show()
    key = cv2.waitKey(1000)
    if key == 27:
        cv2.destroyAllWindows()
        break