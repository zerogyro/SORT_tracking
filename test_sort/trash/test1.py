import cv2
import numpy as np


# 4,-1,748.744,152.562,32.441,55.121,0.672558,-1,-1,-1
x = [748.744,152.562,32.441,55.121]
# y = [748.744 152.562 781.185 207.683]
print(x)
def convert_x_to_bbox(x, score=None):
    """
  Takes a bounding box in the centre form [x,y,s,r] and returns it in the form
    [x1,y1,x2,y2] where x1,y1 is the top left and x2,y2 is the bottom right
  """
    w = np.sqrt(x[2] * x[3])
    h = x[2] / w
    if score == None:
        return np.array([x[0] - w / 2., x[1] - h / 2., x[0] + w / 2., x[1] + h / 2.]).reshape((1, 4))
    else:
        return np.array([x[0] - w / 2., x[1] - h / 2., x[0] + w / 2., x[1] + h / 2., score]).reshape((1, 5))


img_path = '/home/jerry/kitti/tracking/2011_09_26_drive_0013_sync/2011_09_26/2011_09_26_drive_0013_sync/image_02/data/%010d.png' % 0

img = cv2.imread(img_path)
top_left = int(748), int(152)
bottom_right = int(781), int(207)


# a = convert_x_to_bbox(x)
# print(a)
# cv2.rectangle(img, top_left, bottom_right, color=(255, 0, 255), thickness=2)
# cv2.imshow('img', img)
# cv2.waitKey(1000000)
