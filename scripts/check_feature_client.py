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
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":

    print Feature.COLOR

    y = Feature()
    y.feature_val = [0.2, 0.3, 0.5]
    #y.feature_val = 0.21


    z1 = Object()
    z1.name = 'Banana'
    #z1_color = Feature()
    z1.color.feature_val = [0.2, 0.3, 0.5]
    #z1_shape = Feature()
    z1.shape.feature_valu = 0.21
    #z1_size = Feature()
    z1.size.feature_valu = 0.6
    #z1_position = Feature()
    z1.position.feature_val = [0.8, 0, 0]
    z1.feature_list = [z1.color.feature_val, z1.shape.feature_valu, z1.size.feature_valu, z1.position.feature_val]


    z2 = Object()
    z2.name = 'Apple'
    #z1_color = Feature()
    z2.color.feature_val = [0.8, 0.6, 0.59]
    #z1_shape = Feature()
    z2.shape.feature_valu = 0.87
    #z1_size = Feature()
    z2.size.feature_valu = 0.1
    #z1_position = Feature()
    z2.position.feature_val = [0.6, 0.5, 0.1]
    z2.feature_list = [z2.color.feature_val, z2.shape.feature_valu, z2.size.feature_valu, z2.position.feature_val]

    #z = [z1.feature_list,z2.feature_list]
    z = [z1,z2]
    print(z)
    #print(len(z))
    ztotal = [0]*len(z)
    print(len(y.feature_val))
    for i in range(0,len(z)):
        print(z[i].feature_list)
        ztotal[i]=z[i].feature_list
    print(ztotal)
    #print(y.feature_val)
    #print(z[0][0])
    object_output=check_feature_client(0, y, z)
 
    print "Requesting Checking Featrue"
    #feature_output=check_feature_client(x, y, z)
    print "%Object = %s"%(object_output[1])
    #print "%Object = %s"%(feature_output.output_object)
