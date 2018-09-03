
# coding: utf-8

# Task 1.1 Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[1]:


def myDivision(num1,num2):
    try:
        x = num1 / num2
    except:
        return "Error dividing by zero"
    else:
        return x
print(myDivision(5,0))
print(myDivision(4,2))


# Task 1.2.Implement a Python program to generate all sentences where subject is in ["Americans",
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


subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
print(''.join([i+' '+j+' '+k+'.\n' for i in subjects for j in verbs for k in objects]))


# Task 2.1. Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
# Theophile Vandermonde.

# In[3]:


def myVander(lst,boolean):
    import numpy as np
    x = np.array(lst)
    return np.vander(x,increasing=boolean)
print('When increasing is False : \n', myVander([1,2,3,4,5],False))
print('When increasing is True : \n', myVander([1,2,3,4,5],True))

