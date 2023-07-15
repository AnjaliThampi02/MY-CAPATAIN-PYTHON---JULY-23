
# coding: utf-8

# In[1]:


#Task -1 


# 1. WRITE A PYTHON CODE TO CREATE A FUNCTION CALLED most_frequent THAT TAKES A STRING AND PRINTS THE LETTERS IN DECREASING ORDER OF FREQUENCY. USE DICTIONARIES.

# In[2]:


def most_frequent(string):
    d=dict()
    for i in string:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    return d
            


# In[3]:


most_frequent('Mississippi')


# In[5]:


# to find decreasing frequency


# In[22]:


def most_frequent(string):
    string=string.replace(" "," ")
    d={}
    for i in string:
        d[i]=d.get(i,0) + 1
        
    new=[]
    
    for i, j in d.items():
        new=new + [(j,i)]
    new.sort(reverse=True)
    
    for j, i in new:
        print(i,j)


# In[23]:


most_frequent('Mississippi')

