#!/usr/bin/env python

import sys
import rospy
import random
import numpy as np
from beginner_tutorials.msg import *
from beginner_tutorials.srv import *

def check_feature_client(x, y, z):
    rospy.wait_for_service('check_feature')
    try:
        check_feature = rospy.ServiceProxy('check_feature', CheckFeatureOutput)
        resp1 = check_feature(x, y, z)
        return resp1.outputobject
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":


    y1 = Feature()
    y1.feature_val = [0.2, 0.3, 0.5]
    y2 = Feature()
    y2.feature_val = [0.1]
    y = [y1,y2]
    print(y)

    z1 = Object()
    z1.name = 'Banana'
    z1.color = [0.2, 0.3, 0.5] #YELLOW
    z1.shape = 0.21    
    z1.size = 0.6              #MEDIUM
    z1.position = [0.8, 0, 0]
    z1_feature_list = [z1.color, z1.size, z1.shape, z1.position]


    z2 = Object()
    z2.name = 'Apple'
    z2.color = [0.7, 0.9, 0.5] #RED
    z2.shape = 0.87
    z2.size = 0.1              #small
    z2.position = [0.6, 0.5, 0.1]
    z2_feature_list = [z2.color, z2.size, z2.shape, z2.position]


    z3 = Object()
    z3.name = 'Orange'
    z3.color = [0.2, 0.3, 0.5] #YELLOW
    z3.shape = 0.87
    z3.size = 0.1              #small
    z3.position = [0.6, 0.5, 0.1]
    z3_feature_list = [z3.color, z3.size, z3.shape, z3.position]
    z = [z1,z2,z3]



    print(len(z))
    z_feature_list = [0]*len(z)
    ztotal=[0]*len(z)
    for i in range(0,len(z)):
        ztotal[i]=[z[i].color,z[i].size,z[i].shape,z[i].position]
    print(y1.feature_val)
    print(z)
    #Output = OutputObject()
    Output=check_feature_client([0,1], y, z)
    print(Output)
 
    print "Requesting Checking Featrue"
    #print (Output)
    #print "%Object = %s"%(feature_output.output_object)
