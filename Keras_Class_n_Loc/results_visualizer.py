import numpy as np
import cv2

height = 46*10
width = 30*10

data = np.load('visualize_results.npy')
X1 = (data[:,0]*width).astype(int)
Y1 = (data[:,1]*height).astype(int)
X2 = (data[:,2]*width).astype(int)
Y2 = (data[:,3]*height).astype(int)
X3 = (data[:,4]*width).astype(int)
Y3 = (data[:,5]*height).astype(int)
X4 = (data[:,6]*width).astype(int)
Y4 = (data[:,7]*height).astype(int)

Xc_a = (data[:,8]*width).astype(int)
Yc_a = (data[:,9]*height).astype(int)
W_a = (data[:,10]*width).astype(int)
H_a = (data[:,11]*height).astype(int)
Square_a = data[:,12]

Xc_p = (data[:,13]*width).astype(int)
Yc_p = (data[:,14]*height).astype(int)
W_p = (data[:,15]*width).astype(int)
H_p = (data[:,16]*height).astype(int)
Square_p = data[:,17]

height = 46*10
width = 30*10

red = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

cv2.namedWindow('data',cv2.WINDOW_NORMAL)
cv2.resizeWindow('data',width,height)

vid_title  = 'misleading accuracy.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
VidOutput = cv2.VideoWriter(vid_title,fourcc, 30, (width,height))


vert_radius = 3

for i in np.arange(0,data.shape[0]):
    img = np.zeros((height,width,3),np.uint8)
    img[:,:]=white

    print(i,' of ',data.shape[0])
    cv2.circle(img,(Xc_a[i],Yc_a[i]),vert_radius,red,-1)
    if Square_a[i] >= 1:
        cv2.rectangle(img,(X1[i],Y1[i]),(X4[i],Y4[i]),red,1)

    
    cv2.circle(img,(Xc_p[i],Yc_p[i]),vert_radius*3,green,2)
    cv2.imshow('data',img)
    VidOutput.write(img)

    cv2.waitKey(20)

VidOutput.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
