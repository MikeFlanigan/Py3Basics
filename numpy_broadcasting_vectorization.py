import numpy as np


## working example from stack overflow to play with and understand
# they wanted to mult arr_1 and arr_2 with arr_1 sliding over arr_2
# OP used a for loop, question was how to vectorize
arr_1 = np.random.randint(0,10,(3,2)) 
arr_2 = np.random.randint(0,10,(5,2))

Window = arr_1.shape[0] # = window size in direction of slide 
idx = np.arange(arr_2.shape[0]-Window+1)[:,None]+np.arange(Window)
# np.arange(arr_2.shape[0]-Window+1) ,size of path in direction of slide - window size + 1 since size v index
# [:,None] turns it into a column since this example is a vertical slider
# [None,:] would be a row for horizontal slider  wrong?
# note, at this point np.arange(arr_2.shape[0]-Window+1)[:,None] is of dimension 3x1
# when +np.arange(Window) is applied it broadcasts (qsuedo stretch) the 3x1 across the 1x3 creating a 3x3

print(idx)
print(arr_2[idx])
# now when arr_2, dim 5x2, is indexed by the 3x3 matrix each row of the indexing matrix is broadcasted across
# the main matrix, arr_2, creating window sliced slices of those values

print(arr_1*arr_2[idx])

print('start of more applicable example')
## more applicable to sliding window example below
# given a 360x480 matrix (img) create a vector of sliding window slices that cover it

img = np.random.randint(0,10,(360,420))
win_slice = np.zeros((45,420))
img = np.random.randint(0,10,(5,5))
win_slice = np.zeros((2,2))
window_step = 1

print('the below gives a slider of the full image width sliding in the vertical direction')
idx = np.arange(0,img.shape[0]-win_slice.shape[0]+1,window_step)[:,None]+np.arange(win_slice.shape[0])
print(idx)
print('idx ',idx.shape)
print('number of windows in the vertical slide: ',idx.shape[0],' height of window: ',idx.shape[1],' width: Full')

vect_o_windows = img[idx]
print('vector of row windows shape: ',vect_o_windows.shape)

# F it, instead of sliding horizontally going to transpose the windows previously created so can slide vertically again
print('now we slide a window horizontally across the first of those full width windows')
small_img = np.transpose(vect_o_windows)
win_slice = np.zeros((30,45))
win_slice = np.zeros((2,2))
idx = np.arange(0,small_img.shape[0]-win_slice.shape[0]+1,window_step)[:,None]+np.arange(win_slice.shape[0])
print('idx ',idx.shape)
print(idx)
##idx = np.transpose(idx)
windows = small_img[idx]
##vect_o_horz_windows[0:10,0,:]
print('vector of horizontal windows shape: ',windows.shape)

## once confirmed correct
# resize resize
# till mxn dimensions to feed to predicter





