import cv2
import numpy as np
import pandas as pd
colours = np.random.rand(32, 3)*256
COLUMN_NAMES = ['frame', 'track id', 'x1','y1','x2','y2','a','b','c','d']
path = '/home/jerry/utokyo/Fall2021/test_sort/output/05in.txt.txt'

def read_label(csv_path):
    df = pd.read_csv(csv_path, header=None)
    df.columns = COLUMN_NAMES
    return df

def draw_box(img,box,type):
    top_left = int(box[0]), int(box[1])
    bottom_right = int(box[2]), int(box[3])
    cv2.rectangle(img, top_left, bottom_right, color=colours[type%32],thickness=2)
    cv2.putText(img,'ID:'+str(type),top_left,cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255))


def draw_label(img,labels,write_path):
    for label in labels:
        draw_box(img,label[1],label[0])
    cv2.imwrite(write_path,img)

df = read_label(path)
print(df)
if __name__ == '__main__':
    frame  = 1
    while True:
        print(frame)
        img_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/image_02/data/%010d.png' % frame
        new_path = '/new_data/%010d.png' %frame
        img = cv2.imread(img_path)
        a = np.array(df[df.frame == frame][['x1', 'y1', 'x2', 'y2']])
        b = np.array(df[df.frame == frame]['track id'])
        labels = zip(b,a)
        draw_label(img,labels,write_path=new_path)

        cv2.imshow('img',img)
        cv2.waitKey(100)
        frame+=1
        frame %=154




