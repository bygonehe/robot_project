# These code is for defination, for example :"The human tells the robot "Give me the red ball". The robot can see five objects. Which objects is the red ball?"
# The function of produce the object
import numpy as np
import random
def objectfeature ():
    #red = random.randint(1,256)
    #green = random.randint(1,256)
    #blue = random.randint(1,256)
    #color = random.randint(1,256)
    color = np.array([random.random(), random.random(), random.random()])
    size = random.random() 
    shape = random.random()
    position = np.array([random.random(), random.random(), random.random()])
    a = np.array([color,size,shape,position])
    return a
testobject1 = objectfeature()   #produce the first object
testobject2 = objectfeature()   #produce the second object
testobject3 = objectfeature()   #produce the third object

def robot_know_which_object_human_want(feature_index, feature_value, object_list):
    # For example, when human said give me the red object, robot should know which object(or objects) is(are) red.
    # feature_index = 0 means COLOR, =1 means SIZE, =2 means SHAPE, =3 means POSITION
    if feature_index == 1 or feature_index == 2: # size and shape index because of only 1 element of each index
        threshold_value = 0.1  # Set a threshold value
        x = len(object_list)  # The number of objects
        bar = object_list[0:len(object_list),feature_index]  # Extract feature value of corresponding feature index for all objects
        dif=abs(bar-feature_value) 
        S = (sum(dif<=threshold_value)) # Calculate how many objects satisfy the condition

        corr_index = [[0]*1 for i in range(S)]
        corr_value = [[0]*1 for i in range(S)]
        i=0
        m=0
    
        while (i<S):
            if dif.min()<=object_list:
                corr_index[m] = (np.argmin(dif, axis=0)) # Get the index of the minimum difference
                corr_value[m] = dif.min() # Get the value of the minimum difference
                temp_para = corr_index[i];
                m=m+1
                dif[temp_para]=256 # Delete this minimum value by replacing this small value by a large value
            i=i+1
    if feature_index == 0 or feature_index == 3: # color and position index have 3 elements, COLOR has RGB, position has xyz
        threshold_value = 0.1
        x = len(object_list) # number of objects
        bar = object_list[0:len(object_list),feature_index] # Extract feature value of corresponding feature index for all objects
        S = 0
        record = 0
        corr_index = [[200]*1 for i in range(x)] # Initially, define corr_index a long array
        for i in range(0,x):
            dif = (abs((bar[i])-feature_value)) 
            t =  (sum(dif<=threshold_value)) # determine number of elements for each object, which satisfy the condition
            if t == 2 or t == 3: # If the 2 of 3 or 3 of 3 elements satisfy the condition: enter this 'if' condition
                corr_index[S]=i # Recording the object_index
                S = S+1  
        # The code below is just for delete [200] initialy set.
        for i in range(0,x): 
            if corr_index[i]==[200]:
                record = record+1
        if record == 0:
            corr_index = corr_index
        else:
            corr_index = corr_index[:-record]
            
        ##    
        if S == 0:
            return ('Can not find the object')  
    thresholded_list = object_list[corr_index]
    corr_index = np.array(corr_index)+1 #because the initial index is 0, To represent nth object, add 1
    return [thresholded_list,corr_index]

# The code below is just for the testing
feature_value = object_list[1][2] # object_list[1] means the second object, object_list[1][2] means the shape value of the second object
print(feature_value)
feature_index = 2
object_feature = robot_know_which_object_human_want(feature_index, feature_value, object_list)
print(object_feature[1])


