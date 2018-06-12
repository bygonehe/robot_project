#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

#Get the probability function, firstly we need to get the error probability and then the probability
def get_probability(feature_index, object_list, target_object):
    if feature_index == 1 or feature_index == 2: # size and shape only has one element
        x = len(object_list)
        bar = object_list[0:len(object_list),feature_index]
        dif=abs(bar-target_object[0][feature_index])
        if sum(dif)==0:
            return('The probability is 100% and is uniqle')
        norm_error_prob = dif/(sum(dif))
        corr_prob = (1-norm_error_prob)
        norm_prob = corr_prob/(sum(corr_prob))
    if feature_index == 0 or feature_index == 3: # color have 3 elements: R,G,B, norm1 # position have 3 elements: X,Y and Z, in the case of calculating distance error, norm2
        x = len(object_list)
        bar = object_list[0:len(object_list),feature_index]
        dif = [[0]*1 for i in range(x)]
        if feature_index == 0: # color probability: norm1
            for i in range(0,x):
                temp_dif = (abs((bar[i])-target_object[0][feature_index]))
                dif[i] = sum(temp_dif)
            if sum(dif)==0:
                return('The probability is 100% and is uniqle')
            norm_error_prob = dif/sum(dif)  
        if feature_index == 3: # position probability: norm2
            for i in range(0,x):
                temp_dif = (abs((bar[i])-target_object[0][feature_index])) 
                dif[i] = np.sqrt(temp_dif[0]**2+temp_dif[1]**2+temp_dif[2]**2)
            if sum(dif)==0:
                return('The probability is 100% and is uniqle')
            norm_error_prob = dif/sum(dif)
        corr_prob = (1-norm_error_prob)
        norm_prob = corr_prob/(sum(corr_prob))            
    return (norm_prob)



def handle_get_best_descriptions(object_list, feature_list, target_object): #feature_list = [0,1,2,3]
    #feature_list = [0,1,2,3]
    NO_OBJECT = ('NO CORRESPONDING OBJECT')
    number_of_feature = len(feature_list)
    number_of_object_list = len(object_list)
    loop = 1
    feature_choice = [[200]*1 for i in range(number_of_feature)]
    record=0

# check whether one feature can describe
    for i in range (0,number_of_feature): 
        feature = feature_list[i]
        prob = get_probability(feature, object_list, target_object)
        #if prob == 'The probability is 100% and is uniqle':
            #return ('feature_list')
        max_prob = max(prob)
        if max_prob >= 0.48:
            feature_choice[i]=feature
        else:
            if number_of_feature == 1:
                return(NO_OBJECT)
    if feature_choice[0]!=[200]:
        for k in range(0,number_of_feature):
            if feature_choice[k]==[200]:
                record=record+1
        if record == 0:
            feature_choice = feature_choice
        else:
            feature_choice = feature_choice[:-record]
        print('One feature is used to describe')
        return(feature_choice)

# check whether two features can describe
    random_max_number_choice = 10
    pairs_possible = [[200]*1 for i in range(0,random_max_number_choice)]
    q=0
    for i in range (0,number_of_feature): 
        for m in range (i+1,number_of_feature):
            #pairs_possible[0] = feature_list[i]
            #pairs_possible[1] = feature_list[m]
            t1 = feature_list[i]
            t2 = feature_list[m]
            prob1 = get_probability(t1, object_list, target_object)
            prob2 = get_probability(t2, object_list, target_object)
            combination_prob = (prob1*prob2)
            norm_prob = combination_prob/sum(combination_prob)
            if max(norm_prob)>=0.6:
                pairs_possible[q] = [t1,t2]
                q=q+1
            else:
                if number_of_feature == 2:
                    return(NO_OBJECT) 
    if pairs_possible[0]!=[200]:
        for k in range(0,random_max_number_choice):
            if pairs_possible[k]==[200]:
                record=record+1
        pairs_possible = pairs_possible[:-record]
        print('TWO features combination are used to describe')
        return(pairs_possible)

# check whether three features can describe
    combination_prob=0
    triple_possible = [[200]*1 for i in range(0,random_max_number_choice)]
    q=0
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
                norm_prob = combination_prob/sum(combination_prob)
                if max(norm_prob)>=0.6:
                    triple_possible[q] = [t1,t2,t3]
                    q=q+1
                else:
                    if number_of_feature == 3:
                        return(NO_OBJECT)   
    if triple_possible[0]!=[200]:
        for k in range(0,random_max_number_choice):
            if triple_possible[k]==[200]:
                record=record+1
        triple_possible = triple_possible[:-record]
        print('THREE features combination are used to describe')
        return(triple_possible)
    
    
# check whether four features can describe   
    combination_prob=0
    quadra_possible = [[200]*1 for i in range(0,random_max_number_choice)]
    q=0
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
                    norm_prob = combination_prob/sum(combination_prob)
                    if max(norm_prob)>=0.6:
                        quadra_possible[q] = [t1,t2,t3,t4]
                        q=q+1
                    else:
                        if number_of_feature == 3:
                            return(NO_OBJECT)   
    if quadra_possible[0]!=[200]:
        for k in range(0,random_max_number_choice):
            if quadra_possible[k]==[200]:
                record=record+1
        quadra_possible = quadra_possible[:-record]
        print('FOUR features combination are used to describe')
        return(quadra_possible)



def get_best_descriptions_server():
    rospy.init_node('get_best_descriptions_server')
    s = rospy.Service('get_best_descriptions', GetDescriptionsOutput, handle_get_best_descriptions)
    print "Ready to get best descriptions"
    rospy.spin()

if __name__ == "__main__":
    get_best_descriptions_server()


