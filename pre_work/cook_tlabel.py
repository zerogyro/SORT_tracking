import cv2
import numpy as np

from read_label import df

#new_img_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/new_data/%010d.png'%i

types = ['Car','Pedestrian','Cyclist']
color_dict = {'Car': (255, 255, 0), 'Pedestrian': (0, 255, 255), 'Cyclist': (255, 0, 255)}

def draw_box(img,box,type):
    top_left = int(box[0]), int(box[1])
    bottom_right = int(box[2]), int(box[3])
    cv2.rectangle(img, top_left, bottom_right, color=color_dict[type],thickness=2)


def draw_label(img,labels,write_path):
    for label in labels:
        draw_box(img,label[1],label[0])
    cv2.imwrite(write_path,img)


if __name__ == '__main__':
    i = 0
    while True:
        print(i)
        img_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/image_02/data/%010d.png'%i
        new_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/new_data/%010d.png'%i
        img = cv2.imread(img_path)
        a = np.array(df[df.frame == i][['bbox_left', 'bbox_top', 'bbox_right', 'bbox_bottom']])
        b = np.array(df[df.frame == i]['type'])
        labels = zip(b, a)
        draw_label(img,labels,write_path=new_path)

        cv2.imshow("img", img)
        cv2.waitKey(100)
        i+=1
        i %=154

