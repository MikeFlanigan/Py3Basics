'''
speed comparisons
'''

import numpy as np
import timeit
import cv2




start_time = timeit.default_timer() # begin timer

blank_image = np.zeros((1920,1080,3), np.uint8)
img = cv2.cvtColor(blank_image,cv2.COLOR_BGR2GRAY)
print('img:',img.shape)

##img = np.random.randint(0,255,(1920,1080))  ## ~ 1/100th of a second 

elapsed = timeit.default_timer() - start_time # end timer 
print('array creation: ',elapsed)




start_time = timeit.default_timer() # begin timer
## ----------------------------------------------------

win_h = 100
win_w = 68
strideX = int(win_w*1/6)
strideY = int(win_h*1/6)
data_patch_size = (30,46)

## -------- sliding window vectorization steps --------------------------
num_vert_windows = len(np.arange(0,img.shape[0]-win_h,strideY)) # number of vertical windows that will be created
indx = np.arange(0,img.shape[0]-win_h,strideY)[:,None]+np.arange(win_h) # index that will be broadcasted across image
vertical_windows = img[indx] # array of windows win_h tall and the full width of the image

vertical_windows = np.transpose(vertical_windows,(0,2,1)) # transpose to prep for broadcasting
num_horz_windows = len(np.arange(0,vertical_windows.shape[1]-win_w,strideX)) # number of horizontal windows that will be created
indx = np.arange(0,vertical_windows.shape[1]-win_w,strideX)[:,None]+np.arange(win_w) # index for broadcasting across vertical windows
all_windows = vertical_windows[0:vertical_windows.shape[0],indx] # array of all the windows
## -------- end of, sliding window vectorization ------------------------

## ------- prep for passing to the predicter ---------------------------
total_windows = num_vert_windows*num_horz_windows

all_windows = np.transpose(all_windows,(3,2,1,0)) # rearrange for resizing and intuitive indexing

start_time2 = timeit.default_timer() # begin timer
all_windows = np.resize(all_windows,(win_h,win_w,total_windows))
elapsed2 = timeit.default_timer() - start_time2 # end timer 
print('reshaping windows: ',elapsed2)

# shrinking all the windows down to the size needed for object detect predictions
## ---- resizeing seems to have a max size value of ~ 6.95 million, this works around that limit
try:
    del small_windows # resets small windows for each frame after the first frame
except NameError:
    pass

start_time2 = timeit.default_timer() # begin timer
if all_windows.shape[0]*all_windows.shape[1]*all_windows.shape[2] >= 600000:
    max_num_windows = int(np.floor(600000/(all_windows.shape[0]*all_windows.shape[1])))

    for i in range(int(np.floor(all_windows.shape[2]/max_num_windows))+1):
        start_time3 = timeit.default_timer() # begin timer
        if max_num_windows*(i+1) >= all_windows.shape[2]:
            small_windows_part = cv2.resize(all_windows[:,:,max_num_windows*i:all_windows.shape[2]],data_patch_size,0,0,cv2.INTER_AREA)
        else:
            small_windows_part = cv2.resize(all_windows[:,:,max_num_windows*i:max_num_windows*(i+1)],data_patch_size,0,0,cv2.INTER_AREA)
        try:
            small_windows = np.concatenate((small_windows,small_windows_part),2)
        except NameError:
            small_windows = small_windows_part
        elapsed3 = timeit.default_timer() - start_time3 # end timer 
##        print('loop time: ',elapsed3)
else:
    small_windows = cv2.resize(all_windows[:,:,0:all_windows.shape[2]],data_patch_size,0,0,cv2.INTER_AREA)
elapsed2 = timeit.default_timer() - start_time2 # end timer 
print('for loop for cv resizing: ',elapsed2)
##  small_windows = scipy.misc.imresize(all_windows[:,:,0:all_windows.shape[2]],data_patch_size,interp = 'bilinear',mode = None) ## interp mode should be researched!!
## ---- end of resizing work around -----------

start_time2 = timeit.default_timer() # begin timer
# flattening and rearranging the window data so that the pixels are in columns and each window is a row
flat_windows = np.resize(small_windows,(data_patch_size[0]*data_patch_size[1],total_windows))
flat_windows = np.transpose(flat_windows)
## ------- end of, prep for passing to the predicter ----------------------
elapsed2 = timeit.default_timer() - start_time2 # end timer 
print('flattening and transposing (uses resize): ',elapsed2)

## ----------------------------------------------------
elapsed = timeit.default_timer() - start_time # end timer 
print('total elapsed time: ',elapsed)
