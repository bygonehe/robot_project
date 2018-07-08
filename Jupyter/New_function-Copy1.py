
# coding: utf-8

# These code is for defination, for example :"The human tells the robot "Give me the red ball". The robot can see five objects. Which objects is the red ball?"

# In[7]:


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
object_list = [testobject1 ,testobject2, testobject3,testobject4]
print(object_list)
print(len(object_list))
print(object_list[0][3])
print(object_list[1])


# In[53]:


def robot_know_which_object_human_want(feature_index, feature_value, testobject):
    # For example, when human said give me the red object, robot should know which object(or objects) is(are) red.
    if feature_index == 1 or feature_index == 2: # size and shape index because of 1 element of each index
        threshold_value = 0.05
        x = len(testobject)
        bar = testobject[0:len(testobject),feature_index]
        dif=abs(bar-feature_value)
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
    corr_index = np.array(corr_index)+1 #because the initial index is 0, To represent nth object, add one
    return [thresholded_list,corr_index]


# In[10]:


feature_value = object_list[2][0]
feature_index = 0
print(feature_index)
print(feature_value)
object_feature = robot_know_which_object_human_want2(feature_index, feature_value, object_list)
print(feature_index)
print(feature_value)
print(object_list)
print(object_feature)
print(object_feature[1])


# In[5]:


feature_value = object_list[2][0]
feature_index = 0
print(object_list)
if feature_index == 1 or feature_index == 2: # size and shape index because of 1 element of each index
    threshold_value = 0.1
    x = len(object_list)
    print(len(object_list))
    print(object_list[1][2])
    #print(object_list[0:len(object_list),0])
    bar=[0]*x
    dif=[0]*x
    for i in range (0,x):
        bar[i]=object_list[i][feature_index]
        dif[i]=abs(bar[i]-feature_value)
    print(bar)
    #bar = object_list[0:len(object_list),feature_index]
    #dif=bar-feature_value
    print(dif)
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
    x = len(object_list) 
    bar=[0]*x
    dif=[0]*x
    print(feature_value)
    for i in range (0,x):
        bar[i]=object_list[i][feature_index]
        #dif[i]=abs(bar[i]-np.array(feature_value))
    #dif = dif.tolist()
    print (bar)
    S = 0
    record = 0
    corr_index = [[200]*1 for i in range(x)]
    for i in range(0,x):
        dif=abs(bar[i]-np.array(feature_value))
        print(dif)
        t =  (sum(dif<=threshold_value))
        print(t)
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
        print ('Can not find the object')
print(corr_index)
#thresholded_list = object_list[corr_index[0]]
len2 = len(corr_index)
thresholded_list = [0]*len2
for i in range(0,len2):
    thresholded_list[i] = [object_list[corr_index[i]]]
corr_index = np.array(corr_index)+1 #because the initial index is 0, To represent nth object, add one
fanhuizhi = [thresholded_list,corr_index.tolist()]
print [thresholded_list,corr_index.tolist()]
#print(thresholded_list[1][0][0])
print(fanhuizhi[1])


# In[8]:


def robot_know_which_object_human_want2(feature_index, feature_value, testobject):
    if feature_index == 1 or feature_index == 2: # size and shape index because of 1 element of each index
        threshold_value = 0.1
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
        x = len(object_list) 
        bar=[0]*x
        dif=[0]*x
        print(feature_value)
        for i in range (0,x):
            bar[i]=object_list[i][feature_index]
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
    corr_index = np.array(corr_index)+1 #because the initial index is 0, To represent nth object, add one
    fanhuizhi = [thresholded_list,corr_index.tolist()]
    return [thresholded_list,corr_index.tolist()]
    #print(fanhuizhi[1])


# In[ ]:


import numpy as np
aa = np.array([1,2,3])
print(aa)
bb = [aa,aa]
print(bb)
print(bb-aa)

