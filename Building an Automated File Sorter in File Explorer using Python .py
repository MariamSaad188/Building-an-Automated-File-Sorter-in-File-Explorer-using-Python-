#!/usr/bin/env python
# coding: utf-8

# In[67]:


import os, shutil


# In[68]:


path = r'C:/Users/cleopa/OneDrive/Desktop/data projects/'


# In[69]:


file_names=os.listdir(path)


# In[70]:


folder_names=['csv files','image files','txt files']

for loop in range(0,3):
    if not os.path.exists(path+folder_names[loop]):
        print(path+folder_names[loop])
        os.makedirs(path+folder_names[loop])
    


# In[72]:


for file in file_names:
    if '.xlsx'in file and not os.path.exists(path+'csv files/'+file):
        shutil.move(path+file,path+'csv files/'+file)
        
    elif '.jpg'in file and not os.path.exists(path+'image files/'+file):
             shutil.move(path+file,path+'image files/'+file) 
            
    elif '.sql'in file and not os.path.exists(path+'txt files/'+file):
        shutil.move(path+file,path+'txt files/'+file)
    
    else:
        print('not there')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




