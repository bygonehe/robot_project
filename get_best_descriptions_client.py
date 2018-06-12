#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def get_best_descriptions_client(x, y, z):
    rospy.wait_for_service('get_best_descriptions')
    try:
        get_best_descriptions = rospy.ServiceProxy('get_best_descriptions', GetDescriptionsOutput)
        resp1 = get_best_descriptions(x, y, z)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = float(sys.argv[1])
        y = int(sys.argv[2])
        z = float(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting get best descriptions"
    print "Best decsrption = %s"%(add_two_ints_client(x, y, z))
