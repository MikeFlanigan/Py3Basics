import numpy as np

base_shape = (46,30) # rows, cols

number_positives = 2000
number_negatives = 2000

for i in np.arange(number_positives):
    Xc = np.random.uniform(.25,.75)
    Yc = np.random.uniform(.25,.75)
    W = np.random.uniform(.25,.75)
    H = np.random.uniform(.25,.75)
    Square = 10 # positive label

    # threshold width and height on image boarders
    if Xc - W/2 < 0:
        W = Xc
    elif Xc + W/2 > 1:
        W = 1-Xc
    if Yc - H/2 < 0:
        H = Yc
    elif Yc + H/2 >1:
        H = 1-Yc

    example_labels = np.resize(np.array([Xc, Yc, W, H, Square]),(1,5))

    # vertices are in order: Top left, Top right, Bottom left, Bottom right
    # vertices are the pixel positions in opencv coordinate sys
    X1 = X3 = (Xc - W/2)*base_shape[1] 
    Y1 = Y2 = (Yc - H/2)*base_shape[0]
    X2 = X4 = (Xc + W/2)*base_shape[1] 
    Y3 = Y4 = (Yc + H/2)*base_shape[0]

    example_features = np.resize(np.array([X1,Y1,X2,Y2,X3,Y3,X4,Y4]),(1,8))

    try:
        Data = np.concatenate((Data,example_features),0)
        Data_labels = np.concatenate((Data_labels,example_labels),0)
    except NameError:
        Data = example_features
        Data_labels = example_labels


print('Data shape:',Data.shape,'Labels shape:',Data_labels.shape)

for i in np.arange(number_negatives):

    Xc = Yc = W = H = .5
    Square = 0 # negative label

    example_labels = np.resize(np.array([Xc, Yc, W, H, Square]),(1,5))


    X1 = np.random.random(1)*base_shape[1] 
    Y1 = np.random.random(1)*base_shape[0]
    X2 = np.random.random(1)*base_shape[1] 
    Y2 = np.random.random(1)*base_shape[0]
    X3 = np.random.random(1)*base_shape[1] 
    Y3 = np.random.random(1)*base_shape[0]
    X4 = np.random.random(1)*base_shape[1] 
    Y4 = np.random.random(1)*base_shape[0]

    example_features = np.resize(np.array([X1,Y1,X2,Y2,X3,Y3,X4,Y4]),(1,8))

    Data = np.concatenate((Data,example_features),0)
    Data_labels = np.concatenate((Data_labels,example_labels),0)

print('Data shape:',Data.shape,'Labels shape:',Data_labels.shape)

# shuffle
indx = np.arange(Data.shape[0])
np.random.shuffle(indx)
Data = Data[indx]
Data_labels = Data_labels[indx]


# save
np.save('Sq_Data.npy',Data)
np.save('Sq_labels.npy',Data_labels)
