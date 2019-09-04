
# coding: utf-8

# In[56]:


import pandas as pd


# In[57]:


H6 = pd.read_csv("C:/Users/erika/Desktop/HW6.txt",delimiter="\t")


# In[59]:


print (H6)


# In[64]:


SubH6 = H6.loc[0:,'HG00096':]


# In[65]:


print (SubH6)


# In[69]:


#Q1
H6Avg = SubH6.mean(axis=1)


# In[70]:


print (H6Avg)


# In[81]:


#Here I found the max average and it told me it was 1403.61
Q1A = print (H6Avg.max())


# In[85]:


#Here I asked it to locate where the max is at
H6Avg.idxmax()


# In[90]:


#Q1A: Here I asked for it to search for the gene name based off of the row number I got.
H6.iloc[47] [0]


# In[91]:


#Q2
H6HG = SubH6['HG00096']


# In[100]:


H6HGAVG = H6HG.min()


# In[102]:


print (H6HGAVG)


# In[103]:


H6HG.idxmin()


# In[106]:


H6.iloc[51]['Gene_Symbol']


# In[125]:


#Q3
AllAVG = SubH6.mean(axis = 0)


# In[126]:


print(AllAVG)

