import numpy as np
import cv2


def Predict(flattened_patches):
    # taking the mean of the flattened windows and then returning the
    # index of the row (window) with the highest mean, a predicter would have the same syntax
    results = flattened_patches.mean(1) 
    max_index = results.argmax() 
    return results, max_index

## -------- image and sliding window setup -------------------------
AR = 1.45 # choose an aspect ratio to maintain throughout scaling steps
win_h = 200 # window height
win_w = int(win_h/AR) # window width
window = (win_w,win_h)# window dimensions
strideY = 100
strideX = 100

data_patch_size = (30,46) # size the windows will be shrunk to for object detection

img = cv2.imread('vectorizationDemoPic.png') # load an image to slide over

cv2.namedWindow('image',cv2.WINDOW_NORMAL) 
cv2.resizeWindow("image",int(img.shape[1]/2),int(img.shape[0]/2)) # shrink the image viewing window if you have large images

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
## -------- end of, image and sliding window setup --------------------

## -------- sliding window vectorization steps --------------------------
num_vert_windows = len(np.arange(0,img.shape[0]-window[1],strideY)) # number of vertical windows that will be created
indx = np.arange(0,img.shape[0]-window[1],strideY)[:,None]+np.arange(window[1]) # index that will be broadcasted across image
vertical_windows = img[indx] # array of windows win_h tall and the full width of the image

vertical_windows = np.transpose(vertical_windows,(0,2,1)) # transpose to prep for broadcasting
num_horz_windows = len(np.arange(0,vertical_windows.shape[1]-window[0],strideX)) # number of horizontal windows that will be created
indx = np.arange(0,vertical_windows.shape[1]-window[0],strideX)[:,None]+np.arange(window[0]) # index for broadcasting across vertical windows
all_windows = vertical_windows[0:vertical_windows.shape[0],indx] # array of all the windows
## -------- end of, sliding window vectorization ------------------------

## ------- The below code rearranges and flattens the windows into a single matrix of pixels in columns and each window
## ------- in a row which makes evaluating a function over every window in a vectorized manner easier

total_windows = num_vert_windows*num_horz_windows

all_windows = np.transpose(all_windows,(3,2,1,0)) # rearrange for resizing and intuitive indexing

print('all_windows shape as stored in 2d matrix:', all_windows.shape)
for i in range(all_windows.shape[2]): # display windows for visual confirmation
    for j in range(all_windows.shape[3]):
        cv2.imshow('image',all_windows[:,:,i,j])
        cv2.waitKey(100)

all_windows = np.resize(all_windows,(win_h,win_w,total_windows))
print('all_windows shape after folding into 1d vector:', all_windows.shape)
for i in range(all_windows.shape[2]): # display windows for visual confirmation
    cv2.imshow('image',all_windows[:,:,i])
    cv2.waitKey(100)

# shrinking all the windows down to the size needed for object detect predictions
small_windows = cv2.resize(all_windows[:,:,0:all_windows.shape[2]],data_patch_size,0,0,cv2.INTER_AREA)
print('all_windows shape after shrinking to evaluation size:',small_windows.shape)
for i in range(small_windows.shape[2]): # display windows for vis. conf.
    cv2.imshow('image',small_windows[:,:,i])
    cv2.waitKey(100)

# flattening and rearranging the window data so that the pixels are in columns and each window is a row
flat_windows = np.resize(small_windows,(data_patch_size[0]*data_patch_size[1],total_windows))
flat_windows = np.transpose(flat_windows)
print('shape of the window data to send to the predicter:',np.shape(flat_windows))

results, max_index = Predict(flat_windows) # get predictions on all the windows 
