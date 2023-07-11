
# coding: utf-8

# ASSIGNMENT - 1 

# 1. Write a python program which accepts the radius of a circle from the user and computes area.

# In[12]:


import math


# In[13]:


r=float(input("Radius of the circle is: "))
area=float(math.pi*r**2)
print(area)


# 2. Write a python program to accept a filename from the user and print the extension of that.

# In[16]:


file_name=input("Enter the filename: ")
file_extension=file_name.split(".")
print("Extension of file is: " + (file_extension[-1]))

