
# coding: utf-8

# In[1]:


# Task - 2


# In[2]:


# WRITE A PYTHON PROGRAM TO PRINT ALL POSITIVE NUMBERS IN A RANGE.


# In[3]:


#1
list1= []
n=int(input("Enter the size: "))
for i in range(0,n):
    s=int(input("Enter the elements: "))
    list1.append(s)
    
print("Positive no:s are: ")

for i in list1:
    if i>=0:
        print(i, end=" ")


# In[6]:


#2
list2=[]
n=int(input("Enter the size: "))
for i in range(0,n):
    s=int(input("Enter the elements: "))
    list2.append(s)
    
print("Positive no:s are: ")

positive_number=[num for num in list2 if num>=0]

print(positive_number)

