import os
import cv2
import sys

mypath = sys.argv[1]

dirs = os.listdir(mypath)
files = []

for i in dirs:
    if '.mp4' in i:
        files.append(i)

for name in files:
    vid = cv2.VideoCapture(mypath+name)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    if ( width == 1920 and height == 1080 ):
        print ('OK ' + name)
    else:
        print ('NOT OK ' + name)
