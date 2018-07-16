
# coding: utf-8

# After meeting with Tobi, there are some ideas:
# 1.Put the repeated code into functions to reduce computing time.
# 2.Get the probability: 首先计算error probability,然后1-error_probability就是每个feature的概率，然后normilized，就能得到我们想要的概率.
# 3.然后就是去写用最少的feature描述object的代码
# 4.在3之前需要get_possible_descriptions跟get_best_description这两个function（这两个function也太他妈的难了吧根本就没理解。。好鸡儿难受）
# NOTE:有几个网站需要看一下，第一个是statistics multiple features关于spicy的，然后还有维基百科的salience的定义

# In[ ]:


# Some definition of parameters:
COLOR_FEATURE_IDX = 0
SIZE_FEATURE_IDX = 1
SHAPE_FEATURE_IDX = 2
POSITION_FEATURE_IDX = 3

SIZE_DESCRIPTION_SMALL = 0.1
SIZE_DESCRIPTION_MIDDLE = 0.5
SIZE_DESCRIPION_LARGE = 0.85

SHAPE_DESCRIPTION_SQUARE = 0.4
SHAPE_DESCRIPTION_ROUND = 0.85


# In[1]:


# The function of produce the object
# The function of produce the object
import numpy as np
import random
def objectfeature ():
    #red = random.randint(1,256)
    #green = random.randint(1,256)
    #blue = random.randint(1,256)
    #color = random.randint(1,256)
    color = [random.random(), random.random(), random.random()]
    size = random.random() 
    shape = random.random()
    position = [random.random(), random.random(), random.random()]
    
    #a = ([red,green,blue,size,shape,position])
    a = [color,size,shape,position]
    return a
testobject1 = objectfeature()   #produce the first object
testobject2 = objectfeature()   #produce the second object
testobject3 = objectfeature()   #produce the third object
testobject4 = objectfeature()
object_list = [testobject1 ,testobject2]
object_list = [testobject1 ,testobject2, testobject3,testobject4]
print(object_list)
print(len(object_list))
print(object_list[0][3])
print(object_list[1])


# In[ ]:


# To produce target_object
target_object = objectfeature() # Produce an object
print(target_object)
print(len(target_object))
print(target_object[0][1])
#print(target_object[feature_index])


# # only for testing my own code, IGNORE IT!!!
# bar = object_list[0:len(object_list),0]
# threshold_value = 0.1
# print(bar)
# print(target_object[0])
# tot=0
# cor_index = [[200]*1 for i in range(3)]
# for i in range (0,3):
#     d = (abs((bar[i])-target_object[0]))
#     t =  (sum(d<=threshold_value))
#     if t == 2 or t == 3:
#         cor_index[tot]=i
#         tot = tot+1
#     print(d)
#     print(t)
# record = 0
# for i in range(0,3):
#     if cor_index[i]==[200]:
#         record=record+1
# cor_index = cor_index[:-record]
# print(cor_index)
# 
# 
# 
# #d=abs(bar-target_object[0])

# #First step: Put the repeated code into functions to reduce computing time and define the get_prob function
# def check_feature(feature_index, threshold_value, testobject, target_object):
#     if feature_index == 1 or feature_index == 2: # size and shape index because of 1 element of each index
#         x = len(testobject)
#         bar = testobject[0:len(testobject),feature_index]
#         dif=abs(bar-target_object[0][feature_index])
#         S = (sum(dif<=threshold_value))
# 
#         corr_index = [[0]*1 for i in range(S)]
#         corr_value = [[0]*1 for i in range(S)]
#         i=0
#         m=0
#     
#         while (i<x):
#             if dif.min()<=threshold_value:
#                 corr_index[m] = (np.argmin(dif, axis=0))
#                 corr_value[m] = dif.min()
#                 temp_para = corr_index[i];
#                 m=m+1
#                 dif[temp_para]=256
#             i=i+1
#     if feature_index == 0 or feature_index == 3: # color and position index have 3 elements
#         x = len(testobject)
#         bar = testobject[0:len(testobject),feature_index]
#         S = 0
#         record = 0
#         corr_index = [[200]*1 for i in range(x)]
#         for i in range(0,x):
#             dif = (abs((bar[i])-target_object[0][feature_index]))
#             t =  (sum(dif<=threshold_value))
#             if t == 2 or t == 3:
#                 corr_index[S]=i
#                 S = S+1  
#         for i in range(0,x):
#             if corr_index[i]==[200]:
#                 record = record+1
#         corr_index = corr_index[:-record]
#         if S == 0:
#             print('Can not find the object')  
#     thresholded_list = testobject[corr_index]
#     return thresholded_list

# In[2]:


#Get the probability function, firstly we need to get the error probability and then the probability
def get_probability(feature_index, testobject, target_object):
    if feature_index == 1 or feature_index == 2: # size and shape only has one element
        x = len(testobject)
        print(x)
        bar=[0]*x
        dif=[0]*x
        for i in range (0,x):
            bar[i]=testobject[i][feature_index]
            dif[i]=abs(bar[i]-target_object[feature_index])
        dif = np.array(dif)
        if sum(dif)==0:
            return('The probability is 100% and is uniqle')
        norm_error_prob = dif/(sum(dif))
        corr_prob = (1-norm_error_prob)
    if feature_index == 0 or feature_index == 3: # color have 3 elements: R,G,B, norm1 # position have 3 elements: X,Y and Z, in the case of calculating distance error, norm2
        x = len(testobject)
        bar=[0]*x
        dif=[0]*x
        for i in range (0,x):
            bar[i]=object_list[i][feature_index]
        if feature_index == 0: # color probability: norm1
            for i in range(0,x):
                temp_dif=abs(bar[i]-np.array(target_object[feature_index]))
                dif[i] = sum(temp_dif)
            if sum(dif)==0:
                return('The probability is 100% and is uniqle')
            norm_error_prob = dif/sum(dif)  
        if feature_index == 3: # position probability: norm2
            for i in range(0,x):
                temp_dif=abs(bar[i]-np.array(target_object[feature_index])) 
                dif[i] = np.sqrt(temp_dif[0]**2+temp_dif[1]**2+temp_dif[2]**2)
            if sum(dif)==0:
                return('The probability is 100% and is uniqle')
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

# In[5]:


def get_best_descriptions(object_list, feature_list, target_object): #feature_list = [0,1,2,3]
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
        print()
        max_prob = max(prob)
        print(max_prob)
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
            t1 = feature_list[i]
            t2 = feature_list[m]
            prob1 = get_probability(t1, object_list, target_object)
            prob2 = get_probability(t2, object_list, target_object)
            combination_prob = (prob1*prob2)
            #norm_prob = combination_prob/sum(combination_prob)
            if max(combination_prob)>=0.6:
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
                #norm_prob = combination_prob/sum(combination_prob)
                if max(combination_prob)>=0.6:
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
                    #norm_prob = combination_prob/sum(combination_prob)
                    if max(combination_prob)>=0.6:
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


# In[ ]:


def change_index_to_feature (feature):
    length_of_feature_descriptions = len(feature[1][0])
    for i in range (0,length_of_feature_descriptions):
        if feature[1][0][i] == 0:
            feature[1][0][i] = 'color'
        if feature[1][0][i] == 1:
            feature[1][0][i] = 'size'
        if feature[1][0][i] == 2:
            feature[1][0][i] = 'shape'
        if feature[1][0][i] == 4:
            feature[1][0][i] = 'position'
            


# In[ ]:


feature_list = [0,1,2,3]
#target_object = np.array([objectfeature()])
target_object = object_list[0]
testobject = object_list
#output = get_best_descriptions(object_list, feature_list, target_object)
#word_output = change_index_to_feature (output)
#print(output)
feature_index = 3
output=get_probability(feature_index, testobject, target_object)
print(output)


# In[6]:


feature_list = [0,1,2,3]
#target_object = np.array([objectfeature()])
target_object = object_list[1]

print(target_object)
output = get_best_descriptions(object_list, feature_list, target_object)
#word_output = change_index_to_feature (output)
print(output)




# # TEST ONLY
# feature_list = [0,1,2,3]
# #target_object = np.array([objectfeature()])
# target_object = [object_list[1]]
# number_of_feature = len(feature_list)
# number_of_object_list = len(object_list)
# feature_choice = [[200]*1 for i in range(number_of_feature)]
# record=0
# 
# # check whether one feature can describe
# for i in range (0,number_of_feature): 
#     feature = feature_list[i]
#     prob = get_probability(feature, object_list, target_object)
#     print(prob)
#         #if prob == 'The probability is 100% and is uniqle':
#             #return ('feature_list')
#     max_prob = max(prob)
#     if max_prob >= 0.4:
#         feature_choice[i]=feature
#     else:
#         if number_of_feature == 1:
#             print(NO_OBJECT)
# print(feature_choice)
# record=0
# if feature_choice[0]!=[200]:
#     for k in range(0,number_of_feature):
#         if feature_choice[k]==[200]:
#             record=record+1
#             print(record)
#     print(feature_choice)
#     if record == 0:
#         feature_choice = feature_choice
#     else:
#         feature_choice = feature_choice[:-record]
#     print(feature_choice)
#     print('One feature is used to describe',feature_choice)
# 

# # TEST PROBABILITY
# x = len(object_list)
# target_object = [object_list[1]]
# feature_index = 1
# bar = object_list[0:len(object_list),feature_index]
# print(bar)
# print(target_object[0][feature_index])
# dif=abs(bar-target_object[0][feature_index])
# print(dif)
# if sum(dif)==0:
#     print('The probability is 100% and is uniqle')
# norm_error_prob = dif/(sum(dif))
# print(norm_error_prob)
# corr_prob = (1-norm_error_prob)
# norm_prob = corr_prob/(sum(corr_prob))
# print(norm_prob)

# # FOR CODE TEST IGNORE IT
# 1. 
# feature_list = [0,1,2,3]
# number_of_feature = len(feature_list)
# number_of_object_list = len(object_list)
# #pairs_possible = [[200]*1 for i in range(0,2)]
# random_max_number_choice=10
# Choice = [200*1 for i in range(0,random_max_number_choice)]
# p=0
# for i in range (0,number_of_feature): # check whether two feature can describe
#     for m in range (i+1,number_of_feature):
#         for n in range (m+1,number_of_feature):
#             for r in range (n+1,number_of_feature):
#                 t1 = i
#                 t2 = m
#                 t3 = n
#                 t4 = r
#                 Choice[p]=[t1,t2,t3,t4]
#                 p=p+1
#             #print(Choice[p])
#             
# print((Choice))
# record = 0
# if Choice[0]!=200:
#     for k in range(0,random_max_number_choice):
#         if Choice[k]==200:
#             record=record+1
#     Choice = Choice[:-record]
#     print(record)
#     print(Choice)
# print (Choice[0])
# 
# 2. 
# feature_choice = [[200]*1 for i in range(3)]
# print(min(feature_choice))
# a = [200]
# if a == min(feature_choice):
#     print('good')
#     
# 3. 
# import numpy as np
# a = np.array([1.,2.,3.])
# print(a)
# b = np.array([4.,5.,6.])
# c = np.array([10.,11.,12.])
# d=0
# print(c)
# d=a*b*c
# print(d)
# NO_FE = ('NO CORRESPONDING OBJECT')
# print(NO_FE)
# 
# 4.
# feature_list = [0,1,2,3]
# number_of_feature = 4
# number_of_object_list = 3
# a = [[200]*1 for i in range(0,2)]
# result = [[200]*1 for i in range(0,10)]
# p=0
# for i in range (0,4): 
#     for m in range (i+1,4):
#             t1 = i
#             t2 = m
#             result[p]=[t1,t2]
#             print(a)
#             print(result[p])
#             p=p+1
# print(result)

# # IGNORE THIS PART, JUST FOR TESTING
# x = len(object_list)
# feature_index = 3
# bar = object_list[0:len(object_list),feature_index]
# print(bar)
# print(target_object[feature_index])
# for i in range(0,x):
#     temp_dif = (abs((bar[i])-target_object[feature_index]))
#     print(temp_dif)
#     dif[i] = np.sqrt(temp_dif[0]**2+temp_dif[1]**2+temp_dif[2]**2)
# print(dif)
# 
# 
