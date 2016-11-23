import numpy as np


window = (30,46)
strideY = 10
strideX = 10


img = np.random.randint(0,255,(640,480))
##print(img.shape)

indx = np.arange(0,img.shape[0]-window[1],strideY)[:,None]+np.arange(window[1])
##print(indx.shape)

vertical_windows = img[indx]

##print(vertical_windows.shape)

##print('visual confirmation:')
##print('img first 10x10 vals')
##print(img[0:10,0:10])
##print('window 1, first 10x10 vals')
##print(vertical_windows[0,0:10,0:10])

##print('the above is a window 46 pixels tall and the full width of the img',
##      'moving vertically')


new_img = vertical_windows[0,:,:]
##print(new_img.shape)

new_imgt = new_img.copy()

new_imgt = np.transpose(new_imgt)
##print(new_imgt.shape)

indx = np.arange(0,new_img.shape[1]-window[0],strideX)[:,None]+np.arange(window[0])
##print(indx.shape)


horizontal_windows = new_imgt[indx]
##print(horizontal_windows.shape)
horizontal_windows = np.transpose(horizontal_windows,(0,2,1))
##print(horizontal_windows.shape)

##print('visual confirmation:')
##print('new_img first 10x10 vals')
##print(new_img[0:10,0:10])
##print('window 1, first 10x10 vals')
##print(horizontal_windows[0,0:10,0:10])

##print('the above should be a window height window sliding horizontally across the whole image')


print('now to vectorize the whole thing')
print(vertical_windows.shape)
vertical_windows = np.transpose(vertical_windows,(0,2,1))
print(vertical_windows.shape)                     
indx = np.arange(0,vertical_windows.shape[1]-window[0],strideX)[:,None]+np.arange(window[0])
print(indx.shape)
indx2 = np.arange(vertical_windows.shape[0])
all_windows = vertical_windows[0:vertical_windows.shape[0],indx]
print(all_windows.shape)

all_windows = np.transpose(all_windows,(1,0,3,2))
print(all_windows.shape)

rows = all_windows.shape[0]*all_windows.shape[1]
cols = all_windows.shape[2]*all_windows.shape[3]
all_windows = np.resize(all_windows,(rows,cols))
print('all_windows is now a flattened matrix with rows falling in vertical sliding windows and then horizontal windows')
print(all_windows.shape)


