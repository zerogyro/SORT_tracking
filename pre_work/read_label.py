import pandas as pd
import os

COLUMN_NAMES = ['frame', 'track id', 'type', 'truncated', 'occluded', 'alpha', 'bbox_left', 'bbox_top', 'bbox_right',
                'bbox_bottom', 'height', 'width', 'length', 'pos_x', 'pos_y', 'pos_z', 'rotation_y']
path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/0000.txt'
dir_path = '/home/jerry/data_jerry/2011_09_26/2011_09_26_drive_0005_sync/image_02/data'
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
# df_boxes = df[['frame','bbox_left', 'bbox_top', 'bbox_right', 'bbox_bottom']]
# print(df_boxes)


