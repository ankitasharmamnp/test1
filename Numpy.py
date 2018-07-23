# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:36:54 2018

@author: ankitsh3
"""

import numpy as np

list1 = [1,2,3,4]   #1-d array
print(np.array(list1))
np.arange(0,21,3)
np.zeros(4)
np.ones(5)

matrix1 = [[1,2],[3,4],[5,6]]   #2-d array
print(np.array(matrix1))
print(np.array(matrix1).shape)  #(3,2)  3 columns and 2 rows (cols,rows)
