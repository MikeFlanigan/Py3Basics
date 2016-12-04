'''
thread joining and merging
testing returning and concatenating threads
'''

import numpy as np
import threading
import time

## --- variable defines ----------------
windows = np.arange(10).astype(np.int)
##windows = np.resize(windows,(1,windows.shape[0]))

results = []
## --- end of; variable defines --------


## ------- function defines -------------------
def array_join_fcn(rows,arr_num):
    global results
    if rows <= 0: rows = 1
    array = np.random.randint(0,5,(rows,1))
    results.append(array)
    if arr_num == 4:
        time.sleep(5)
    return 
## ------- end of; function defines -----------

threads = [] # empty list for threads
thread_names = [] # empty list for thread names

for w in windows:
    thread_names.append('thread_'+str(w))
    threads.append(threading.Thread(name=thread_names[w],target=array_join_fcn, args=[10,w]))
    threads[w].daemon = True
    threads[w].start()

for w in windows: # makes sure all the threads are done
    while threads[w].isAlive():
        print('waiting on thread:',w)
        pass

final_results = np.concatenate((results[:]),0)



    
