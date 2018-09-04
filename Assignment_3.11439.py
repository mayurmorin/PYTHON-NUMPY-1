
# coding: utf-8

# Task 1.1 Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[1]:


def myDivision(num1,num2):
    try:
        x = num1 / num2
    except ZeroDivisionError:    #When num2 value is zero, this exception will be raised.
        print("Error dividing by zero!!!")
    except:                      #Any other exceptions will be raised here.
        print("Any Other Exception has been handled")
    else:                        #If no exception and Division gives valid output, then we can print the value using else
        print("Output Value : ", x)
    finally:                     #It is optional, but is intended to define clean-up actions which must be executed 
        print("Finally Always Executed and Used For Cleaning Up")
    
myDivision(5,0)               #Function returns Error Dividing by Zero
print("--------------")
myDivision(4,2)               #Function returns correct output with division   
print("--------------")
myDivision((1,1),(1,1))       #Function return other exception by passing wrong values as parameters


# Task 1.2.Implement a Python program to generate all sentences where subject is in ["Americans ",
# "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[2]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
#By Using list comprehension along with formatting for the output values as specified output can be achieved.
print(''.join([ sub + ' ' + verb + ' ' + obj + '.\n' for sub in subjects for verb in verbs for obj in objects]))


# Task 2.1. Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
# Theophile Vandermonde.

# In[3]:


import numpy as np
def myVander(lst,columns,boolean):
    x = np.array(lst)  #x : array_like 1-D input array.
    N = columns        #N : int, optional, Number of columns in the output.
    increase = boolean #Order of the powers of the columns.  
                       #If True, the powers increase from left to right, if False (the default) they are reversed.
    return np.vander(x,N,increase)

print('When increasing is False : \n', myVander([1,2,3,4,5],6,False))
print('-------------------------')
print('When increasing is True : \n', myVander([1,2,3,4,5],5, True))

