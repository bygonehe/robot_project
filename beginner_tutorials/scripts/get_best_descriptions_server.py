#!/usr/bin/env python

from beginner_tutorials.msg import *
from beginner_tutorials.srv import *
import numpy as np
import rospy


#Get the probability function, firstly we need to get the error probability and then the probability
def get_probability(feature_index, testobject, target_object):
    if feature_index == 1 or feature_index == 2: # size and shape only has one element
        x = len(testobject)
        bar=[0]*x
        dif=[0]*x
        for i in range (0,x):
            bar[i]=testobject[i][feature_index]
            dif[i]=abs(bar[i]-target_object[feature_index])
        dif = np.array(dif)
        if sum(dif)==0:
            norm_error_prob = np.array(dif)
        else:
            norm_error_prob = dif/(sum(dif))
        corr_prob = (1-norm_error_prob)
    if feature_index == 0 or feature_index == 3: # color have 3 elements: R,G,B, norm1 # position have 3 elements: X,Y and Z, in the case of calculating distance error, norm2
        x = len(testobject)
        bar=[0]*x
        dif=[0]*x
        for i in range (0,x):
            bar[i]=testobject[i][feature_index]
        if feature_index == 0: # color probability: norm1
            for i in range(0,x):
                temp_dif=abs(bar[i]-np.array(target_object[feature_index]))
                dif[i] = sum(temp_dif)
            if sum(dif)==0:
                norm_error_prob = np.array(dif)
            else:
                norm_error_prob = dif/sum(dif)  
        if feature_index == 3: # position probability: norm2
            for i in range(0,x):
                temp_dif=abs(bar[i]-np.array(target_object[feature_index])) 
                dif[i] = np.sqrt(temp_dif[0]**2+temp_dif[1]**2+temp_dif[2]**2)
            if sum(dif)==0:
                norm_error_prob = np.array(dif)
            else:
                norm_error_prob = dif/sum(dif)
        corr_prob = (1-norm_error_prob)
    return (corr_prob)

# get_possible_descriptions:
# Given a list of objects and a target object (which is probably contained within the list of objects), you should find
# possible variations of describing the target object using as few features as possible. If one feature is enough to 
# sufficiently describe the target object (so that it can't get confused with any of the other objects), then return 
# this feature (e.g. shape). But there are some variations of this case: It might be that both the shape and the colour 
# are distinctive. Then you should return two possible descriptions. On the other hand, one single feature might not 
# be sufficient to describe the object. Then you should return (all possible) pairs of features which can distinctively 
# describe the target object and so forth.
def handle_get_best_descriptions(req):
    Object_list = req.Object_LIST
    object_list = [0]*len(Object_list)
    for i in range(0,len(Object_list)):
        object_list[i]=[Object_list[i].color,Object_list[i].size,Object_list[i].shape,Object_list[i].position]


    target_Object = req.Target_object
    target_object=[target_Object.color,target_Object.size,target_Object.shape,target_Object.position]

    feature_list = req.Feature_list


 #feature_list = [0,1,2,3]
    #feature_list = [0,1,2,3] represents color, size, shape, position individually
    number_of_feature = len(feature_list)
    number_of_object_list = len(object_list)
    loop = 1
    feature_choice = [200*1 for i in range(number_of_feature)]
    record=0
    n=0
# check whether one feature can describe
    for i in range (0,number_of_feature): 
        feature = feature_list[i]
        prob = get_probability(feature, object_list, target_object)
        satisied = 0
        for m in range(0,number_of_object_list):
            if prob[m]>=0.9:
                satisied = satisied + 1
        if satisied == 1:
            feature_choice[n]=i
            n=n+1

    if feature_choice[0]!=200:
        for k in range(0,number_of_feature):
            if feature_choice[k]==200:
                record=record+1
        if record == 0:
            feature_choice = feature_choice
        else:
            feature_choice = feature_choice[:-record]
        for i in range (0,len(feature_choice)):
            if feature_choice[i] == 0:
                feature_choice[i] = 'COLOR'
            if feature_choice[i] == 1:
                feature_choice[i] = 'SIZE'
            if feature_choice[i] == 2:
                feature_choice[i] = 'SHAPE'
            if feature_choice[i] == 3:
                feature_choice[i] = 'POSITION'
        print('One feature is used to describe')
        return([feature_choice])

# check whether two features can describe
    record=0
    num=0
    random_max_number_choice = 10
    pairs_possible = [200*1 for i in range(0,random_max_number_choice)]
    satisied = 0
    for i in range (0,number_of_feature): 
        for m in range (i+1,number_of_feature):
            t1 = feature_list[i]
            t2 = feature_list[m]
            prob1 = get_probability(t1, object_list, target_object)
            prob2 = get_probability(t2, object_list, target_object)
            combination_prob = (prob1*prob2)
            satisied = 0
            for n in range(0,number_of_object_list):
                if combination_prob[n]>=0.9:
                    satisied=satisied+1
            if satisied == 1:
                pairs_possible[num]=[t1,t2]
                num=num+1

    if pairs_possible[0]!=200:
        for k in range(0,random_max_number_choice):
            if pairs_possible[k]==200:
                record=record+1
        pairs_possible = pairs_possible[:-record]
        pairs_possible_return = ['1']*len(pairs_possible)
        for i in range (0,len(pairs_possible)):
            for m in range(0,len(pairs_possible[0])):
                if pairs_possible[i][m] == 0:
                    pairs_possible[i][m] = 'COLOR'
		if pairs_possible[i][m] == 1:
		    pairs_possible[i][m] = 'SIZE'
		if pairs_possible[i][m] == 2:
		    pairs_possible[i][m] = 'SHAPE'
		if pairs_possible[i][m] == 3:
		    pairs_possible[i][m] = 'POSITION'
            pairs_possible_return[i] = pairs_possible[i][m-1]+' and '+pairs_possible[i][m]
        print('TWO features combination are used to describe')
        return([pairs_possible_return])

    # check whether three features can describe
    combination_prob=0
    random_max_number_choice = 10
    triple_possible = [200*1 for i in range(0,random_max_number_choice)]
    num = 0
    record = 0
    for i in range (0,number_of_feature): 
        for m in range (i+1,number_of_feature):
            for n in range (m+1,number_of_feature):
                t1 = feature_list[i]
                t2 = feature_list[m]
                t3 = feature_list[n]
                prob1 = get_probability(t1, object_list, target_object)
                prob2 = get_probability(t2, object_list, target_object)
                prob3 = get_probability(t3, object_list, target_object)
                combination_prob = prob1*prob2*prob3
                satisied = 0
                for q in range(0,number_of_object_list):
                    if combination_prob[q]>=0.95:
                        satisied=satisied+1
                if satisied == 1:
                    triple_possible[num]=[t1,t2,t3]
                    num=num+1
    if triple_possible[0]!=200:
        for k in range(0,random_max_number_choice):
            if triple_possible[k]==200:
                record=record+1
        triple_possible = triple_possible[:-record]
        triple_possible_return = ['1']*len(triple_possible)
        for i in range (0,len(triple_possible)):
            for m in range(0,len(triple_possible[0])):
                if triple_possible[i][m] == 0:
                    triple_possible[i][m] = 'COLOR'
		if triple_possible[i][m] == 1:
		    triple_possible[i][m] = 'SIZE'
		if triple_possible[i][m] == 2:
		    triple_possible[i][m] = 'SHAPE'
		if triple_possible[i][m] == 3:
		    triple_possible[i][m] = 'POSITION'
            triple_possible_return[i] = pairs_possible[i][m-2]+' and '+pairs_possible[i][m-1]+' and '+pairs_possible[i][m]
        
        print('THREE features combination are used to describe')
        return([triple_possible_return])
    
    
# check whether four features can describe   
    combination_prob=0
    quadra_possible = [200*1 for i in range(0,random_max_number_choice)]
    q=0
    record = 0
    num=0
    for i in range (0,number_of_feature): 
        for m in range (i+1,number_of_feature):
            for n in range (m+1,number_of_feature):
                for r in range (n+1,number_of_feature):
                    t1 = feature_list[i]
                    t2 = feature_list[m]
                    t3 = feature_list[n]
                    t4 = feature_list[r]
                    prob1 = get_probability(t1, object_list, target_object)
                    prob2 = get_probability(t2, object_list, target_object)
                    prob3 = get_probability(t3, object_list, target_object)
                    prob4 = get_probability(t4, object_list, target_object)
                    combination_prob = prob1*prob2*prob3*prob4
                    satisied = 0
                    for q in range(0,number_of_object_list):
                        if combination_prob[q]>=0.95:
                            satisied=satisied+1
                    if satisied == 1:
                        quadra_possible[num]=[t1,t2,t3,t4]
                        num=num+1   
    if quadra_possible[0]!=200:
        for k in range(0,random_max_number_choice):
            if quadra_possible[k]==200:
                record=record+1
        quadra_possible = quadra_possible[:-record]
        quadra_possible_return = ['1']*len(quadra_possible)
        for i in range (0,len(quadra_possible)):
            for m in range(0,len(quadra_possible[0])):
                if quadra_possible[i][m] == 0:
                    quadra_possible[i][m] = 'COLOR'
		if quadra_possible[i][m] == 1:
		    quadra_possible[i][m] = 'SIZE'
		if quadra_possible[i][m] == 2:
		    quadra_possible[i][m] = 'SHAPE'
		if quadra_possible[i][m] == 3:
		    quadra_possible[i][m] = 'POSITION'
            quadra_possible_return[i] = quadra_possible[i][m-3]+' and '+quadra_possible[i][m-2]+' and '+quadra_possible[i][m-1]+' and '+quadra_possible[i][m]
        print('FOUR features combination are used to describe')
        return([quadra_possible_return])


def get_best_descriptions_server():
    rospy.init_node('get_best_descriptions_server')
    s = rospy.Service('get_best_descriptions', GetDescriptionsOutput, handle_get_best_descriptions)
    print "Ready to get best descriptions"
    rospy.spin()

if __name__ == "__main__":
    get_best_descriptions_server()


