
# coding: utf-8

# After meeting with Tobi, there are some ideas:
# 1.Put the repeated code into functions to reduce computing time.
# 2.Get the probability: 首先计算error probability,然后1-error_probability就是每个feature的概率，然后normilized，就能得到我们想要的概率.
# 3.然后就是去写用最少的feature描述object的代码
# 4.在3之前需要get_possible_descriptions跟get_best_description这两个function（这两个function也太他妈的难了吧根本就没理解。。好鸡儿难受）
# NOTE:有几个网站需要看一下，第一个是statistics multiple features关于spicy的，然后还有维基百科的salience的定义

# In[ ]:


# test single or pair
import numpy as np
#object 1 is red, round, small, position is [0,1,0,2,0.3]
#object 2 is red, square, small, position is [0,1,0,2,0.3]
#object 3 is totally the same as object 1
#object 4 is black, round, large, position is [0,1,0,2,0.3]
#object 5 is black, square, large, position is [0.9 0.9 0.9]
testobject1 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject2 = [[0.5, 0.4, 0.3], 
               0.5, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject3 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.9, 
               [0.1, 0.2, 0.3]]
testobject4 = [[0.1, 0.2, 0.3], 
               0.2, 
               0.9, 
               [0.1, 0.2, 0.3]]
testobject5 = [[0.9, 0.8, 0.7], 
               0.2, 
               0.9, 
               [0.9, 0.9, 0.9]]
testobject6 = [[0.5, 0.4, 0.3], 
               0.5, 
               0.1, 
               [0.1, 0.2, 0.3]]

object_list = [testobject1,testobject2,testobject3,testobject4,testobject5,testobject6]
object_list


# In[ ]:


#TEST 3 combination
import numpy as np
#object 1 is red, round, small, position is [0,1,0,2,0.3]
#object 2 is red, square, small, position is [0,1,0,2,0.3]
#object 3 is totally the same as object 1
#object 4 is black, round, large, position is [0,1,0,2,0.3]
#object 5 is black, square, large, position is [0.9 0.9 0.9]
testobject1 = [[0.5, 0.4, 0.3], 
               0.5, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject2 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject3 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject4 = [[0.8, 0.6, 0.9], 
               0.1, 
               0.4, 
               [0.1, 0.2, 0.3]]
testobject5 = [[0.8, 0.6, 0.9], 
               0.5, 
               0.4, 
               [0.1, 0.2, 0.3]]
testobject6 = [[0.8, 0.6, 0.9], 
               0.5, 
               0.3, 
               [0.1, 0.2, 0.3]]

object_list = [testobject1,testobject2,testobject3,testobject4,testobject5,testobject6]
object_list


# In[1]:


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
        x = len(object_list)
        bar=[0]*x
        dif=[0]*x
        for i in range (0,x):
            bar[i]=object_list[i][feature_index]
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


# In[21]:


def get_best_descriptions(object_list, feature_list, target_object): #feature_list = [0,1,2,3]
    #feature_list = [0,1,2,3]
    NO_OBJECT = ['NO CORRESPONDING OBJECT']
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
            feature_choice[n]=[i]
            n=n+1

    if feature_choice[0]!=200:
        for k in range(0,number_of_feature):
            if feature_choice[k]==200:
                record=record+1
        if record == 0:
            feature_choice = feature_choice
        else:
            feature_choice = feature_choice[:-record]
        print('One feature is used to describe')
        return(feature_choice)

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
        print('TWO features combination are used to describe')
        return(pairs_possible)

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
        print('THREE features combination are used to describe')
        return(triple_possible)
    
    
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
target_object = object_list[1]
testobject = object_list
#output = get_best_descriptions(object_list, feature_list, target_object)
#word_output = change_index_to_feature (output)
#print(output)
feature_index = 1
output=get_probability(feature_index, testobject, target_object)
print(output)


# In[ ]:


object_list.append([[0.8469924710791586, 0.9174721221226261, 0.37918168054353774],
  0.81382982495631908,
  0.0247869124765967,
  [0.7187082208801854, 0.3544713732444361, 0.06469799925197106]])


# In[ ]:


feature_list = [0,1,2,3]
#target_object = np.array([objectfeature()])
target_object = object_list[1]

output = get_best_descriptions(object_list, feature_list, target_object)
#word_output = change_index_to_feature (output)
print(output)




# In[ ]:


feature_list = [0,1,2,3]
target_object = object_list[0]

NO_OBJECT = ['NO CORRESPONDING OBJECT']
number_of_feature = len(feature_list)
number_of_object_list = len(object_list)

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
                print(combination_prob)
                satisied = 0
                for q in range(0,number_of_object_list):
                    if combination_prob[q]>=0.95:
                        satisied=satisied+1
                        print(satisied)
                if satisied == 1:
                    quadra_possible[num]=[t1,t2,t3,t4]
                    num=num+1   
if quadra_possible[0]!=200:
    for k in range(0,random_max_number_choice):
        if quadra_possible[k]==200:
            record=record+1
    quadra_possible = quadra_possible[:-record]
    print('FOUR features combination are used to describe')
    print(quadra_possible)


# In[ ]:


# 测试概率能不能用
target_object = object_list[5]
print(object_list)
feature_index = 2
if feature_index == 0 or feature_index == 3: # color have 3 elements: R,G,B, norm1 # position have 3 elements: X,Y and Z, in the case of calculating distance error, norm2
    x = len(object_list)
    bar=[0]*x
    dif=[0]*x
    for i in range (0,x):
        bar[i]=object_list[i][feature_index]
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
print(corr_prob)


# In[34]:


#TEST single or pairs or 4
import numpy as np
#object 1 is red, round, small, position is [0,1,0,2,0.3]
#object 2 is red, square, small, position is [0,1,0,2,0.3]
#object 3 is totally the same as object 1
#object 4 is black, round, large, position is [0,1,0,2,0.3]
#object 5 is black, square, large, position is [0.9 0.9 0.9]
testobject1 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject2 = [[0.5, 0.4, 0.3], 
               0.5, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject3 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.9, 
               [0.1, 0.2, 0.3]]
testobject4 = [[0.1, 0.2, 0.3], 
               0.2, 
               0.9, 
               [0.1, 0.2, 0.3]]
testobject5 = [[0.9, 0.8, 0.7], 
               0.2, 
               0.9, 
               [0.9, 0.9, 0.9]]
testobject6 = [[0.5, 0.4, 0.3], 
               0.5, 
               0.9, 
               [0.1, 0.2, 0.3]]

object_list = [testobject1,testobject2,testobject3,testobject4,testobject5,testobject6]
object_list
feature_list = [0,1,2,3]
target_object = object_list[1]
output = get_best_descriptions(object_list, feature_list, target_object)
print(output)
for l in range (0,len(output)):
    for m in range(0,len(output[0])):
        if output[l][m]==0:
            output[l][m]='COLOR'
        if output[l][m]==1:
            output[l][m]='SIZE'  
        if output[l][m]==2:
            output[l][m]='SHAPE'
        if output[l][m]==3:
            output[l][m]='POSITION'
print(output)
    


# In[31]:


print(len(output[0]))


# In[11]:


object_list


# In[35]:


# TEST 3 features combination
#TEST 3 combination
import numpy as np
#object 1 is red, round, small, position is [0,1,0,2,0.3]
#object 2 is red, square, small, position is [0,1,0,2,0.3]
#object 3 is totally the same as object 1
#object 4 is black, round, large, position is [0,1,0,2,0.3]
#object 5 is black, square, large, position is [0.9 0.9 0.9]
testobject1 = [[0.5, 0.4, 0.3], 
               0.5, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject2 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject3 = [[0.5, 0.4, 0.3], 
               0.2, 
               0.1, 
               [0.1, 0.2, 0.3]]
testobject4 = [[0.8, 0.6, 0.9], 
               0.1, 
               0.4, 
               [0.1, 0.2, 0.3]]
testobject5 = [[0.8, 0.6, 0.9], 
               0.5, 
               0.4, 
               [0.1, 0.2, 0.3]]
testobject6 = [[0.8, 0.6, 0.9], 
               0.5, 
               0.3, 
               [0.1, 0.2, 0.3]]

object_list = [testobject1,testobject2,testobject3,testobject4,testobject5,testobject6]
object_list

feature_list = [0,1,2,3]
target_object = object_list[4]
output = get_best_descriptions(object_list, feature_list, target_object)
print(output)
for l in range (0,len(output)):
    for m in range(0,len(output[0])):
        if output[l][m]==0:
            output[l][m]='COLOR'
        if output[l][m]==1:
            output[l][m]='SIZE'  
        if output[l][m]==2:
            output[l][m]='SHAPE'
        if output[l][m]==3:
            output[l][m]='POSITION'
print(output)

