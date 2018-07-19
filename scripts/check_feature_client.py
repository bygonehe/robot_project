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

    print Feature.COLOR

    #y = Feature()
    y = [0.2, 0.3, 0.5]
    #y.feature_val = 0.21


    z1 = Object()
    z1.name = 'Banana'
    z1.color = [0.2, 0.3, 0.5]
    z1.shape = 0.21
    z1.size = 0.6
    z1.position = [0.8, 0, 0]
    z1_feature_list = [z1.color, z1.shape, z1.size, z1.position]


    z2 = Object()
    z2.name = 'Apple'
    z2.color = [0.7, 0.9, 0.5]
    z2.shape = 0.87
    z2.size = 0.1
    z2.position = [0.6, 0.5, 0.1]
    z2_feature_list = [z2.color, z2.shape, z2.size, z2.position]


    z3 = Object()
    z3.name = 'Orange'
    z3.color = [0.2, 0.3, 0.5]
    z3.shape = 0.87
    z3.size = 0.1
    z3.position = [0.6, 0.5, 0.1]
    z3_feature_list = [z3.color, z3.shape, z3.size, z3.position]
    z = [z1,z2,z3]

    print(len(z))
    z_feature_list = [0]*len(z)
    ztotal=[0]*len(z)
    for i in range(0,len(z)):
        ztotal[i]=[z[i].color,z[i].shape,z[i].size,z[i].position]
    print(y)
    print(z)
    #Output = OutputObject()
    Output=check_feature_client(0, y, z)
    output=list(Output)
 
    print "Requesting Checking Featrue"
    print (output)
    #print "%Object = %s"%(feature_output.output_object)
