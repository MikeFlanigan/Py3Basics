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
print('start of more applicable example')
print('start of more applicable example')
## more applicable to sliding window example below
# given a 360x480 matrix (img) create a vector of sliding window slices that cover it

img = np.random.randint(0,10,(5,5)) # the image to be sliced
img_ht = img.shape[0]
img_wd = img.shape[1]

win_ht = 2  # the first step is to slice the image into rows of this height
win_stride = 1 # how much to step over on each window

idx = np.arange(0,img_ht-win_ht+1,win_stride)[:,None]+np.arange(win_ht)
row_windows = img[idx]

##print('shape: ',np.shape(np.arange(0,img.shape[0]-win_slice.shape[0]+1,window_step)[:,None]))
##print('shape2: ',np.shape(np.arange(win_slice.shape[0])))
##print(idxa)
##print('idx ',idxa.shape)
##print('number of windows in the vertical slide: ',idxa.shape[0],' height of window: ',idxa.shape[1],' width: Full')
##print('vector of row windows shape: ',vect_o_windows.shape)

small_img = np.transpose(row_windows[0,:,:])
idx2_j = np.reshape(np.arange(0,4,1),(4,1,1))
idx2_k = np.reshape(np.arange(win_ht),(win_ht,1))
idx2 = idx2_j + idx2_k
all_windows = small_img[idx2]

print('img shape: ',img.shape)
print('img: ',img)
print('row_windows shape: ',row_windows.shape)
print('row_windows: ',row_windows)
print('small_img shape: ',small_img.shape)
print('small_img: ',small_img)
print('all windows shape: ',all_windows.shape)
print('all_windows: ',all_windows)
print('one random window:')
print(all_windows[np.random.randint(0,all_windows.shape[0],(1,1))])


# F it, instead of sliding horizontally going to transpose the windows previously created so can slide vertically again
print('now we slide a window horizontally across the first of those full width windows')
####small_img = np.transpose(vect_o_windows)
##small_img = vect_o_windows[0,:,:]
##print('small img: ',small_img)
####win_slice = np.zeros((30,45))
##win_slice = np.zeros((2,2))
##idx = np.arange(0,small_img.shape[0]-win_slice.shape[0]+1,window_step)[:,None]+np.resize(np.arange(win_slice.shape[0]),(1,2))
##print('shape: ',np.shape(np.arange(0,small_img.shape[0]-win_slice.shape[0]+1,window_step)[:,None]+np.resize(np.arange(win_slice.shape[0]),(1,2))))
##print('idx ',idx.shape)
##print(idx)
####idx = np.transpose(idx)
##print(np.transpose(idxa))
##windows = small_img[idxa]
####vect_o_horz_windows[0:10,0,:]
##print('vector of horizontal windows shape: ',windows.shape)




## once confirmed correct
# resize resize
# till mxn dimensions to feed to predicter





