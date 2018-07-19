#!/usr/bin/env python

from beginner_tutorials.msg import *
from beginner_tutorials.srv import *
import numpy as np
import rospy

def robot_know_which_object_human_want(req):
    feature_index = req.Feature_Index
    feature_value = req.Feature_Value
    Testobject = req.Object_List
    testobject = [0]*len(Testobject)
    if len(feature_value) == 1:
        feature_value = feature_value[0]
    for i in range(0,len(Testobject)):
        testobject[i]=[Testobject[i].color,Testobject[i].shape,Testobject[i].size,Testobject[i].position]

    # The code below works well in Jupter Notebook
    if feature_index == 1 or feature_index == 2: # size and shape index because of 1 element of each index
        threshold_value = 0.05
        x = len(testobject)
        bar=[0]*x
        dif=[0]*x
        for i in range (0,x):
            bar[i]=testobject[i][feature_index]
            dif[i]=abs(bar[i]-feature_value)
        dif = np.array(dif)
        S = (sum(dif<=threshold_value))

        corr_index = [[0]*1 for i in range(S)]
        corr_value = [[0]*1 for i in range(S)]
        i=0
        m=0
    
        while (i<S):
            if dif.min()<=threshold_value:
                corr_index[m] = (np.argmin(dif, axis=0))
                corr_value[m] = dif.min()
                temp_para = corr_index[i];
                m=m+1
                dif[temp_para]=256
            i=i+1
    if feature_index == 0 or feature_index == 3: # color and position index have 3 elements
        threshold_value = 0.05
        x = len(testobject) 
        bar=[0]*x
        dif=[0]*x
        print(feature_value)
        for i in range (0,x):
            bar[i]=testobject[i][feature_index]
        S = 0
        record = 0
        corr_index = [[200]*1 for i in range(x)]
        for i in range(0,x):
            dif=abs(bar[i]-np.array(feature_value))
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
    len2 = len(corr_index)
    thresholded_list = [0]*len2
    for i in range(0,len2):
        thresholded_list[i] = [testobject[corr_index[i]]]
    corr_index = np.array(corr_index) #because the initial index is 0, To represent nth object, add one
    fanhuizhi = [thresholded_list,corr_index.tolist()]
    print((fanhuizhi[1]))
    for i in range(0,len(fanhuizhi[1])):
        fanhuizhi[1][i]=Testobject[i].name
    return [fanhuizhi[1]]


def check_feature_server():
    rospy.init_node('check_feature_server')
    s = rospy.Service('check_feature', CheckFeatureOutput, robot_know_which_object_human_want)
    print "Ready to check feature"
    rospy.spin()

if __name__ == "__main__":
    check_feature_server()


