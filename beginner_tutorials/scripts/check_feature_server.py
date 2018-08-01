#!/usr/bin/env python

from beginner_tutorials.msg import *
from beginner_tutorials.srv import *
import numpy as np
import rospy

def robot_know_which_object_human_want(req):
    feature_index = req.Feature_Index
    feature_Value = req.Feature_Value
    #print(feature_Value)
    Testobject = req.Object_List
    testobject = [0]*len(Testobject)
    feature_value = [0]*len(feature_Value)
    for i in range(0,len(Testobject)):
        testobject[i]=[Testobject[i].color,Testobject[i].size,Testobject[i].shape,Testobject[i].position]
    if len(feature_index) == 1:
    	for i in range(0,len(feature_value)):
            #print(feature_Value[i].feature_val)
            feature_value[i] = feature_Value[i].feature_val
        #print(feature_value)
    else:
        for i in range(0,len(feature_value)):
            print(feature_Value[i].feature_val)
            feature_value[i] = [feature_Value[i].feature_val]
        print(feature_value)
    # The code below works well in Jupter Notebook
    if (len(feature_index))==1:
        if feature_index[0] == 1 or feature_index[0] == 2: # size and shape index because of 1 element of each index
            threshold_value = 0.1
            x = len(testobject)
            bar=[0]*x
            dif=[0]*x
            for i in range (0,x):
                bar[i]=testobject[i][feature_index[0]]
                print('enter')
                print(feature_value[0][0])
                dif[i]=abs(bar[i]-feature_value[0][0])
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
        if feature_index[0] == 0 or feature_index[0] == 3: # color and position index have 3 elements
            threshold_value = 0.05
            x = len(testobject) 
            bar=[0]*x
            dif=[0]*x
            print(feature_value)
            for i in range (0,x):
                bar[i]=testobject[i][feature_index[0]]
            S = 0
            record = 0
            corr_index = [[200]*1 for i in range(x)]
            for i in range(0,x):
                dif=abs(bar[i]-np.array(feature_value[0]))
                print(dif)
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
        return_value = ['0']*len(fanhuizhi[1])
        for i in range(0,len(fanhuizhi[1])):
            temp = fanhuizhi[1][i]
            return_value[i]=Testobject[temp].name
            #print(Testobject[temp].name)
        print(return_value)
        return([return_value])

    if (len(feature_index))>1:
        for l in range (0,len(feature_index)):
            if feature_index[l] == 1 or feature_index[l] == 2: # size and shape index because of 1 element of each index
                threshold_value = 0.1
                x = len(testobject)
                bar=[0]*x
                dif=[0]*x
                for i in range (0,x):
                    bar[i]=testobject[i][feature_index[l]]
		    #print(bar)
                    #print(feature_value[l][0][0])
                    dif[i]=abs(bar[i]-feature_value[l][0][0])
                #print(dif)
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
            if feature_index[l] == 0 or feature_index[l] == 3: # color and position index have 3 elements
                threshold_value = 0.05
                x = len(testobject) 
                bar=[0]*x
                dif=[0]*x
                #print(feature_value[l])
                for i in range (0,x):
                    bar[i]=testobject[i][feature_index[l]]
                S = 0
                record = 0
                corr_index = [[200]*1 for i in range(x)]
                for i in range(0,x):
                    #print(i)
                    dif=abs(bar[i]-np.array(feature_value[l]))
                    dif = dif[0]
                    #print(dif)
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
            corr_index = np.array(corr_index) 
            fanhuizhi = [thresholded_list,corr_index.tolist()]
            #print(l)
            #print(fanhuizhi[1])
            if l>=1:
                return_value = set(fanhuizhi[1])&set(return_value)
            else:
                return_value = fanhuizhi[1]
            #print(list(return_value))
        return_value = list(return_value)
        for i in range(0,len(return_value)):
            temp = return_value[i]
            print(temp)
            return_value[i]=Testobject[temp].name
            print(Testobject[temp].name)          
        return([list(return_value)])



def check_feature_server():
    rospy.init_node('check_feature_server')
    s = rospy.Service('check_feature', CheckFeatureOutput, robot_know_which_object_human_want)
    print "Ready to check feature"
    rospy.spin()

if __name__ == "__main__":
    check_feature_server()


