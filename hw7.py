#!/usr/bin/env python
# coding: utf-8

# In[282]:


print('Erika','Maldonado-Rosado','emaldon1@uncc.edu')
import random
import time
import matplotlib.pyplot as plt
import numpy as np


# In[312]:


class hw7:  
    
    def __init__(self):
        self.size, self.time, self.lst= self.collab()
        
    def rand_samp(self,l):
        numb = random.sample(range(0,100000),l)
        return numb
    
        
    def sort(self, lst):
        start = time.time()
        N = len(lst)
        x = [i for i in range(N)]
        random.shuffle(x)
        x.sort
        end = time.time()
        Tot = end - start
        return len(lst),Tot
                    
    def plot(self):
        x = []
        y = []
        t = np.arange(0., 5., 0.2)
        x.append(self.size)
        y.append(self.time)
        plt.plot(x, y,'.')
        plt.xlabel('List Length')
        plt.ylabel('Time')
        plt.suptitle('Time Complexity & Size of List')
        plt.show()
        
    def collab(self):
        size = []
        clock = []
        numbers = [10,20,50,80,100,150,250,350,450,750,1000,1500,3000,4500,6000]
        for i in numbers:
            rand_lst = self.rand_samp(i)
            x,y = self.sort(rand_lst)
            size.append(x)
            clock.append(y)
        return size,clock,rand_lst
        
        
        #self.plot(self.sort,10,10000,100,10)
        #plt.show()

       # 
       #     rand_lst = generator(i)
       #     x,y = self.sort(rand_lst)
       # self.size.append(x)
       # self.TOT.append(y)
       # return size, TOT, rand_lst


# In[330]:


Visual = hw7()
Visual.plot()
print(Visual)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




