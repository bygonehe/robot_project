#!/usr/bin/env python

import sys
import rospy
import random
import numpy as np
from beginner_tutorials.msg import *
from beginner_tutorials.srv import *

def get_best_descriptions_client(x, y, z):
    rospy.wait_for_service('get_best_descriptions')
    try:
        get_best_descriptions = rospy.ServiceProxy('get_best_descriptions', GetDescriptionsOutput)
        resp1 = get_best_descriptions(x, y, z)
        return resp1.Outputfeature
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":


    z1 = Object()
    z1.name = 'Banana'
    z1.color = [0.2, 0.3, 0.5]
    z1.size = 0.21
    z1.shape = 0.6
    z1.position = [0.8, 0, 0]
    z1_feature_list = [z1.color, z1.size, z1.shape, z1.position]


    z2 = Object()
    z2.name = 'Apple'
    z2.color = [0.7, 0.9, 0.5]
    z2.size = 0.51
    z2.shape = 0.1
    z2.position = [0.6, 0.5, 0.1]
    z2_feature_list = [z2.color, z2.size, z2.shape, z2.position]

    z3 = Object()
    z3.name = 'Orange'
    z3.color = [0.2, 0.3, 0.5]
    z3.size = 0.21
    z3.shape = 0.1
    z3.position = [0.8, 0, 0]
    z3_feature_list = [z3.color, z3.size, z3.shape, z3.position]

    z4 = Object()
    z4.name = 'berry'
    z4.color = [0.2, 0.3, 0.5]
    z4.size = 0.51
    z4.shape = 0.1
    z4.position = [0.8, 0, 0]
    z4_feature_list = [z4.color, z4.size, z4.shape, z4.position]
    z = [z1,z2,z3,z4]


    print(len(z))
    z_feature_list = [0]*len(z)
    ztotal=[0]*len(z)
    for i in range(0,len(z)):
        ztotal[i]=[z[i].color,z[i].size,z[i].shape,z[i].position]
    print(z)
    #Output = OutputObject()
    x = [0,1,2,3]
    #print(type(x))
    #print(z[0])

    #for i in range(0,len(z)):
    #    m[i]=[z[i].color,z[i].shape,z[i].size,z[i].position]
    #print(m)


    Output=get_best_descriptions_client(z,x, z[3])
    #output=list(Output)


    
    print "Requesting get best descriptions"
    print([1]*5)
    print (Output)
