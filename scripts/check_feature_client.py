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
    y.feature_val = np.array([0.2, 0.3, 0.5])
    #y.feature_val = 0.21


    z1 = Object()
    z1.name = 'Banana'
    #z1_color = Feature()
    z1.color.feature_val = np.array([0.2, 0.3, 0.5])
    #z1_shape = Feature()
    z1.shape.feature_val = 0.21
    #z1_size = Feature()
    z1.size.feature_val = 0.6
    #z1_position = Feature()
    z1.position.feature_val = np.array([0.8, 0, 0])
    z1.feature_list = [z1.color.feature_val, z1.shape.feature_val, z1.size.feature_val, z1.position.feature_val]


    z2 = Object()
    z2.name = 'Apple'
    #z1_color = Feature()
    z2.color.feature_val = np.array([0.8, 0.6, 0.59])
    #z1_shape = Feature()
    z2.shape.feature_val = 0.87
    #z1_size = Feature()
    z2.size.feature_val = 0.1
    #z1_position = Feature()
    z2.position.feature_val = np.array([0.6, 0.5, 0.1])
    z2.feature_list = [z2.color.feature_val, z2.shape.feature_val, z2.size.feature_val, z2.position.feature_val]

    z = np.array([z1.feature_list,z2.feature_list])
    print(z)
    print(y.feature_val)
    print(z[0][0])
    feature_output=check_feature_client(0, y.feature_val, z)
 
    print "Requesting Checking Featrue"
    #feature_output=check_feature_client(x, y, z)
    print "%Object = %s"%(feature_output[1])
    #print "%Object = %s"%(feature_output.output_object)
