from keras.models import Sequential
from keras.layers import Dense, Dropout
import keras
import numpy as np
import matplotlib.pyplot as plt

# fix random seed for reproducible testing
##seed = 17
##np.random.seed(seed)

# load data
X = np.load('Sq_Data.npy')
Y = np.load('Sq_labels.npy')

# scale normalize X
for i in np.arange(X.shape[1]):
    X[:,i] = X[:,i]/X[:,i].max()
    print('Max val in feature',i,X[:,i].max())

# shuffling data
indx = np.arange(X.shape[0]) 
np.random.shuffle(indx)
X = X[indx]
Y = Y[indx]

# Splitting data into train, validation, and test sets
eightyP = int(np.floor(X.shape[0]*.8))
sixtyP = int(np.floor(X.shape[0]*.6))
twentyP = int(np.floor(X.shape[0]*.2))

X_train = X[0:sixtyP,:]
Y_train = Y[0:sixtyP,:]

X_val = X[sixtyP:sixtyP+twentyP,:]
Y_val = Y[sixtyP:sixtyP+twentyP,:]

X_test = X[eightyP:X.shape[0],:]
Y_test = Y[eightyP:X.shape[0],:]

print('Training set shape:',X_train.shape)
print('Testing set shape:',X_test.shape)
print('Validation set shape:',X_val.shape)


# custom evaluation function for increased clarity/insight into model performance
def custom_eval(dec_thresh,predictions,labels):
        # classification evaluation
        true_pos = len(np.where((predictions[:,4] > dec_thresh) & (labels[:,4] >= 1))[0])
        false_pos = len(np.where((predictions[:,4] > dec_thresh) & (labels[:,4] == 0))[0])
        true_neg = len(np.where((predictions[:,4] < dec_thresh) & (labels[:,4] == 0))[0])
        false_neg = len(np.where((predictions[:,4] < dec_thresh) & (labels[:,4] >= 1))[0])

        if (true_pos+false_pos)>0:
                precision = true_pos/(true_pos+false_pos)
        else:
                precision = 0
        if (true_pos+false_neg) > 0:
                recall = true_pos/(true_pos+false_neg)
        else:
                recall = 0
        if (precision+recall)>0:
                F1score = 2*precision*recall/(precision+recall)
        else:
                F1score = 0
                
        class_results = [F1score,precision,recall,true_pos,false_pos,true_neg,false_neg]
        
        # localization evaluation
        Xc_acc = sum(predictions[:,0])/sum(labels[:,0])
        Yc_acc = sum(predictions[:,1])/sum(labels[:,1])
        W_acc = sum(predictions[:,2])/sum(labels[:,2])
        H_acc = sum(predictions[:,3])/sum(labels[:,3])
        tot_acc = (Xc_acc + Yc_acc + W_acc + H_acc)/4
        
        loc_results = [Xc_acc,Yc_acc,W_acc,H_acc,tot_acc]
        return class_results,loc_results
    


# make a custom callback since regular tends to prints bloat notes
class cust_callback(keras.callbacks.Callback):
        def __init__(self):
                self.train_loss = []
                self.val_loss = []
        def on_epoch_end(self,epoch,logs={}):
                print('epoch:',epoch,' loss:',logs.get('loss'),' validation loss:',logs.get('val_loss'))
                self.val_loss.append(logs.get('val_loss'))
                self.train_loss.append(logs.get('loss'))
                return
        def on_batch_end(self,batch,logs={}):

                return
history = cust_callback()

# define model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dropout(0.2))
##model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(5, init='uniform', activation='relu'))

# Compile model
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

# Fit the model
model.fit(X_train,Y_train,validation_data=(X_val,Y_val),batch_size=16,nb_epoch=150, verbose = 0, callbacks=[history])

plt.ion()
plt.plot(history.train_loss, 'b',label='train loss')
plt.plot(history.val_loss, 'r',label='val loss')
plt.legend()
plt.show()

# evaluate the model
dec_thresh = 0.5
print('TRAINING SET RESULTS:')
predictions = model.predict(X_train) # make predicitions
class_results,loc_results = custom_eval(dec_thresh,predictions,Y_train)
F1score,precision,recall,true_pos,false_pos,true_neg,false_neg = class_results
print('True Pos:',true_pos,'False Pos:',false_pos,'True Neg:',true_neg,'False Neg:',false_neg)
print('F1score:',F1score)
Xc_acc,Yc_acc,W_acc,H_acc,tot_acc = loc_results
print('Xc acc:',Xc_acc,'Yc acc:',Yc_acc,'W acc:',W_acc,'H acc:',H_acc)
print('Total Loc acc:',tot_acc)

print('VALIDATION SET RESULTS:')
predictions = model.predict(X_val) # make predicitions
class_results,loc_results = custom_eval(dec_thresh,predictions,Y_val)
F1score,precision,recall,true_pos,false_pos,true_neg,false_neg = class_results
print('True Pos:',true_pos,'False Pos:',false_pos,'True Neg:',true_neg,'False Neg:',false_neg)
print('F1score:',F1score)
Xc_acc,Yc_acc,W_acc,H_acc,tot_acc = loc_results
print('Xc acc:',Xc_acc,'Yc acc:',Yc_acc,'W acc:',W_acc,'H acc:',H_acc)
print('Total Loc acc:',tot_acc)

print('TEST SET RESULTS:')
predictions = model.predict(X_test) # make predicitions
class_results,loc_results = custom_eval(dec_thresh,predictions,Y_test)
F1score,precision,recall,true_pos,false_pos,true_neg,false_neg = class_results
print('True Pos:',true_pos,'False Pos:',false_pos,'True Neg:',true_neg,'False Neg:',false_neg)
print('F1score:',F1score)
Xc_acc,Yc_acc,W_acc,H_acc,tot_acc = loc_results
print('Xc acc:',Xc_acc,'Yc acc:',Yc_acc,'W acc:',W_acc,'H acc:',H_acc)
print('Total Loc acc:',tot_acc)

comparisons = np.concatenate((X_test,Y_test,predictions),1)
print(comparisons.shape)
np.save('visualize_results.npy',comparisons)
