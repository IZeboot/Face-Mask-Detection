import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

folder = "images"
for root, dirs, files in os.walk("images"):
    for index in range(len(files)):
        if files[index].endswith(".png"):
            path = os.path.dirname(os.path.join(root, files[index]))+ "/rotate30"
            path1 = os.path.dirname(os.path.join(root, files[index]))+ "/rotate-30"
            if not os.path.exists(path):
                print("create directory: "+ path)
                os.mkdir(path)
            if not os.path.exists(path1):
                print("create directory: "+ path1)
                os.mkdir(path1)
            
            print(os.path.join(root, files[index]))
            img = cv2.imread(os.path.join(root, files[index]))

            if img is None:
                print('errr')
                continue


            height, width = (img.shape[0] , img.shape[1])
            size = (width, height)
            center = (width/2,height/2)


            # ------------

            #create 3 separate BGRA images as our "layers"
            layer1 = np.zeros((width, height, 4))
            layer2 = np.zeros((width, height, 4))
            layer3 = np.zeros((width, height, 4))
            res = layer1[:] #copy the first layer into the resulting image

            #copy only the pixels we were drawing on from the 2nd and 3rd layers
            #(if you don't do this, the black background will also be copied)
            cnd = layer2[:, :, 3] > 0
            res[cnd] = layer2[cnd]
            cnd = layer3[:, :, 3] > 0
            res[cnd] = layer3[cnd]
            #draw a red circle on the first "layer",
            #a green rectangle on the second "layer",
            #a blue line on the third "layer"

            res = layer1[:] #copy the first layer into the resulting image

            #copy only the pixels we were drawing on from the 2nd and 3rd layers
            #(if you don't do this, the black background will also be copied)
            cnd = layer2[:, :, 3] > 0
            res[cnd] = layer2[cnd]
            cnd = layer3[:, :, 3] > 0
            res[cnd] = layer3[cnd]

            cv2.imwrite("out.png", res)

            # ------

            dst_mat = np.zeros((height, width, 4), np.uint8)

            angle = -30.0

            scale = 1

            rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

            img_dst = cv2.imread("out.png", -1)
            # cv2.imshow("Output", img_dst)
            if img_dst is None:
                print('errr')
                continue

            img_out = cv2.warpAffine(img, rotation_matrix, size, img_dst,
                                    flags=cv2.INTER_NEAREST,
                                    borderMode=cv2.BORDER_TRANSPARENT)

            # dst = cv2.addWeighted(img, 0.5, img_dst, 0.5, 0.0)
            file_save = os.path.join(path , "{}rotate{}.png".format(index, -(angle)))
            print("save file"+ file_save)
            cv2.imwrite(file_save, img_out)
            # 111111111
            # 111111111
            angle = 30.0

            scale = 1

            rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

            img_dst = cv2.imread("out.png", -1)
            # cv2.imshow("Output", img_dst)
            if img_dst is None:
                print('errr')
                continue

            img_out = cv2.warpAffine(img, rotation_matrix, size, img_dst,
                                    flags=cv2.INTER_NEAREST,
                                    borderMode=cv2.BORDER_TRANSPARENT)

            # dst = cv2.addWeighted(img, 0.5, img_dst, 0.5, 0.0)

            cv2.imwrite(os.path.join(path1 , "{}rotate{}.png".format(index, -(angle))), img_out)
            cv2.imshow("Output", img_out)
            key = cv2.waitKey(100)
            if key == 27:
                cv2.destroyAllWindows()
                break