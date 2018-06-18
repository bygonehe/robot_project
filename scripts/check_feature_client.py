#!/usr/bin/env python

import sys
import rospy
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
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = float(sys.argv[2])
        z = float(sys.argv[3])
   
    else:
        print usage()
        sys.exit(1)
    print "Requesting Checking Featrue"
    print "%Object = %s"%(check_feature_client(x, y, z))
