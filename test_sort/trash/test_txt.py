import numpy as np


seq_dets_fn = '/home/jerry/utokyo/Fall2021/sort/data/train/KITTI-13/det/det.txt'
seq_dets = np.loadtxt(seq_dets_fn, delimiter=',')


#int(seq_dets[:,0].max())
# print(seq_dets[:,0])
# frame += 1 #detection and frame numbers begin at 1
#         dets = seq_dets[seq_dets[:, 0]==frame, 2:7]
for frame in range(int(seq_dets[:,0].max())):
    print(frame)