#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def mapping(string):
    speech = ['100']*len(string)
    feature_index = ['100']*len(string)
    print (len(string))
    enter = 0
    record = 0

    if ('RED' in string) == True:
        speech[enter] = [0.7,0.9,0.5]
        feature_index[enter] = 0
        enter = enter+1
    if ('YELLOW' in string) == True:
        speech[enter] = [0.2,0.3,0.5]
        feature_index[enter] = 0
        enter = enter+1
    if ('SMALL' in string) == True:
        speech[enter] = [0.1]
        feature_index[enter] = 1
        enter = enter+1
    if ('MEDIUM' in string) == True:
        speech[enter] = [0.6]
        feature_index[enter] = 1
        enter = enter+1
    if ('ROUND' in string) == True:
        speech[enter] = [0.1]
        feature_index[enter] = 2
        enter = enter+1
    if ('RECTANGULAR' in string) == True:
        speech[enter] = [0.6]
        feature_index[enter] =2
        enter = enter+1
    if speech[0]!= '100':
        for i in range (0,len(speech)):
            if speech[i]=='100':
                record = record + 1
    speech = speech[:-record]
    feature_index = feature_index[:-record]
    
    return (speech,feature_index)

    

if __name__ == '__main__':
    try:
        mapping()
    except rospy.ROSInterruptException:
        pass
