import pandas as pd
import cv2
import numpy as np
COLUMN_NAMES = ['frame', 'track id', 'type', 'truncated', 'occluded', 'alpha', 'bbox_left', 'bbox_top', 'bbox_right',
                'bbox_bottom', 'height', 'width', 'length', 'pos_x', 'pos_y', 'pos_z', 'rotation_y']
path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/0000.txt'

def read_label_txt(csv_path):
    # read raw csv
    df = pd.read_csv(csv_path, header=None, sep=' ')
    # name columns
    df.columns = COLUMN_NAMES
    # combine car categories
    df.loc[df.type.isin(['Truck', 'Van', 'Tram']), 'type'] = 'Car'
    # get rid of other categories
    df = df[df.type.isin(['Car', 'Pedestrian', 'Cyclist'])]
    return df


df = read_label_txt(csv_path=path)
df_boxes = df[['frame','bbox_left', 'bbox_top', 'bbox_right', 'bbox_bottom']]

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
def draw_only_box(img,box):
    top_left = int(box[0]), int(box[1])
    bottom_right = int(box[2]), int(box[3])
    cv2.rectangle(img, top_left, bottom_right, color=(0, 255, 255), thickness=2)

if __name__ == '__main__':
    i = 0
    in_file = '/home/jerry/utokyo/Fall2021/test_sort/05in.txt'
    with open(in_file,'w') as in_file:
        for i in range(154):
            a = np.array(df_boxes[df.frame == i])
            for d in a:
                print(d,d[1],d[2],d[3],d[4])
                print(type(d[1]))
                print('%d,1,%.2f,%.2f,%.2f,%.2f,1,-1,-1,-1' % (i+1, d[1], d[2], d[3] , d[4]),file=in_file)
            i+=1
    # img_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/image_02/data/%010d.png' % i
    # #new_path = '/new_data/%010d.png'%i
    # img = cv2.imread(img_path)
    # a = np.array(df[df.frame == i][['bbox_left', 'bbox_top', 'bbox_right', 'bbox_bottom']])
    # b = np.array(df[df.frame == i]['type'])
    # #draw_only_box(img,a)
    # for box in a:
    #     draw_only_box(img, box)
    # print(a)
    # cv2.imshow("img", img)
    # cv2.waitKey(1000)





    # for i in range(154):
    #     img_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/image_02/data/%010d.png'%i
    #     new_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/new_data/%010d.png'%i
    #     img = cv2.imread(img_path)
    #     a = np.array(df[df.frame == i][['bbox_left', 'bbox_top', 'bbox_right', 'bbox_bottom']])
    #     b = np.array(df[df.frame == i]['type'])
    #     labels = zip(b, a)
    #     draw_label(img,labels,write_path=new_path)
    #
    #     cv2.imshow("img", img)
    #     cv2.waitKey(100)
    #     i+=1
