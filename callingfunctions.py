# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:19:26 2023

@author: Snehal
"""

class vehicle():
    def drive(self, speed):
        #print('speed is:', speed)
        print('hi')
        return speed

class car(vehicle):
    def drive(self, speed):
        super().drive(speed)
        #print("Driving my Car at", speed)
        print('bye')
        return speed

# calling function from class
vehicle().drive(30)
car().drive(10)

