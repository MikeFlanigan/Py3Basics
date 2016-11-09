'''
# modules are basically just other python scripts
# can go see that in lib the statistics module has all the code visible
'''

import statistics as s # as s allows for short hand referencing
from statistics import variance # allows for direct reference of function in the module
from statistics import * # astrix imports everything from the module


example_list = [2, 3, 4]

x = s.median(example_list)
print('median= ',x)


v = variance(example_list)
print('variance = ',v)



