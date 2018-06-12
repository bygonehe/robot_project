#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def robot_know_which_object_human_want(feature_index, feature_value, testobject):
    # For example, when human said give me the red object, robot should know which object(or objects) is(are) red.
    if feature_index == 1 or feature_index == 2: # size and shape index because of 1 element of each index
        threshold_value = 0.1
        x = len(testobject)
        bar = testobject[0:len(testobject),feature_index]
        dif=abs(bar-feature_value)
        S = (sum(dif<=threshold_value))

        corr_index = [[0]*1 for i in range(S)]
        corr_value = [[0]*1 for i in range(S)]
        i=0
        m=0
    
        while (i<x):
            if dif.min()<=threshold_value:
                corr_index[m] = (np.argmin(dif, axis=0))
                corr_value[m] = dif.min()
                temp_para = corr_index[i];
                m=m+1
                dif[temp_para]=256
            i=i+1
    if feature_index == 0 or feature_index == 3: # color and position index have 3 elements
        threshold_value = 0.1
        x = len(testobject)
        bar = testobject[0:len(testobject),feature_index]
        S = 0
        record = 0
        corr_index = [[200]*1 for i in range(x)]
        for i in range(0,x):
            dif = (abs((bar[i])-feature_value))
            t =  (sum(dif<=threshold_value))
            if t == 2 or t == 3:
                corr_index[S]=i
                S = S+1  
        for i in range(0,x):
            if corr_index[i]==[200]:
                record = record+1
        if record == 0:
            corr_index = corr_index
        else:
            corr_index = corr_index[:-record]
        if S == 0:
            return ('Can not find the object')  
    thresholded_list = testobject[corr_index]
    corr_index = np.array(corr_index)+1 
    #because the initial index is 0, To represent nth object, add one
    return [thresholded_list,corr_index]

def robot_know_which_object_human_want_server():
    rospy.init_node('robot_know_which_object_human_want_server')
    s = rospy.Service('check_feature', ChechFeatureOutput, robot_know_which_object_human_want)
    print "Ready to check feature"
    rospy.spin()

if __name__ == "__main__":
    robot_know_which_object_human_want_server()


