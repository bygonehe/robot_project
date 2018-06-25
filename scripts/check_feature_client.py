#!/usr/bin/env python

import sys
import rospy
import random
import numpy as np
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
    #if len(sys.argv) == 4:
    #    x = int(sys.argv[1])
    #    y = float(sys.argv[2])
    #    z = float(sys.argv[3])
   
    #else:
    #    print usage()
    #    sys.exit(1)
    color = np.array([random.random(), random.random(), random.random()])
    size = random.random() 
    shape = random.random()
    position = np.array([random.random(), random.random(), random.random()])
    testobject1 = np.array([color,size,shape,position])
    
    color = np.array([random.random(), random.random(), random.random()])
    size = random.random() 
    shape = random.random()
    position = np.array([random.random(), random.random(), random.random()])
    testobject2 = np.array([color,size,shape,position])
    
    color = np.array([random.random(), random.random(), random.random()])
    size = random.random() 
    shape = random.random()
    position = np.array([random.random(), random.random(), random.random()])
    testobject3 = np.array([color,size,shape,position])
    
    z = np.array([testobject1 ,testobject2, testobject3])
    x = 2
    y = z[1][2]
    print "Requesting Checking Featrue"
    feature_output=check_feature_client(x, y, z)
    print "%Object = %s"%(feature_output[1])
