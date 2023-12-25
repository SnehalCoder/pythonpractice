# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 19:41:55 2023

@author: Snehal
"""
def testList(list):
    for item in list[1:]:
        if item != list[0]:
            return False
    return True
print(testList([1,1,1,1,8]))

