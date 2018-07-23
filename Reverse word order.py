# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:31:48 2018

@author: ankitsh3
"""

#print the reverse words in a string

str = "Hello World!"
print(str[::-1])   #!dlroW olleH


str1 = 'My name is Ankita'
reverse_list = str1.split()[::-1]
print(' '.join(reverse_list))     #Ankita is name My

reversed_list = str1.split()
reverse_list.reverse()
print(' '.join(reverse_list)) 


#Program to remove the duplicates
a = [1,2,3,1,3,4]
del_dup = list(set(a))
print(del_dup)       # [1,2,3,4] 
#set is an unordered collection datatype which is iterable, mutable and has no duplicate elements
#Frozenset has immutable objects ie. can't add or remove elements from it as below

normal_set = set(a)
frozen_set = frozenset(a)
normal_set.add(5)
#frozen_set.add(6)   #gives error 'frozenset' object has no attribute 'add'
print(normal_set)    # {1,2,3,4,5}

