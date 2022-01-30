#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("hello world")


# In[4]:


s = 3
t = 9
s*t


# In[7]:


import numpy
import pandas
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pylab as plt


# In[7]:


plt.plot([3,2,5],[1,2,3])


# In[8]:


plt.scatter([3,2,5],[1,2,3])


# In[12]:


plt.plot([3,2,5,7,2,3,4,5,2,1,8,9,2,3,1,8],[3,2,5,1,2,3,4,8,9,2,1,3,2,5,3,2])


# # header test
# This is just a test using markdown for inserting text.

# In[5]:


a = .05
b = 27
c = 156
d = 12

((b*c)/1)**d


# # Short Cuts

# Command Mode (press Esc to enable)
# F : find and replace
# ↩ : enter edit mode
# ⌘⇧F : open the command palette
# ⌘⇧P : open the command palette
# P : open the command palette
# ⇧↩ : run cell, select below
# ⌃↩ : run selected cells
# ⌘↩ : run selected cells
# ⌥↩ : run cell and insert below
# Y : change cell to code
# M : change cell to markdown
# R : change cell to raw
# 1 : change cell to heading 1
# 2 : change cell to heading 2
# 3 : change cell to heading 3
# 4 : change cell to heading 4
# 5 : change cell to heading 5
# 6 : change cell to heading 6
# K : select cell above
# ↑ : select cell above
# ↓ : select cell below
# J : select cell below
# ⇧K : extend selected cells above
# ⇧↑ : extend selected cells above
# ⇧↓ : extend selected cells below
# ⇧J : extend selected cells below
# ⌘A : select all cells
# A : insert cell above
# B : insert cell below
# X : cut selected cells
# C : copy selected cells
# ⇧V : paste cells above
# V : paste cells below
# Z : undo cell deletion
# D,D : delete selected cells
# ⇧M : merge selected cells, or current cell with cell below if only one cell is selected
# ⌘S : Save and Checkpoint
# S : Save and Checkpoint
# L : toggle line numbers
# O : toggle output of selected cells
# ⇧O : toggle output scrolling of selected cells
# H : show keyboard shortcuts
# I,I : interrupt the kernel
# 0,0 : restart the kernel (with dialog)
# ⌘V : Dialog for paste from syst

# In[13]:


import numpy as np


# In[14]:


arr = np.array([1,2,3,4,5])


# In[18]:


high_values = ['High','High','High','High','High']
low_values = ['Low','Low','Low','Low','Low']


# In[19]:


arr > 3


# In[20]:


np.where(arr > 3, ['High','High','High','High','High'],['Low','Low','Low','Low','Low'])


# In[25]:


import pandas as pd


# In[26]:



data = np.array([['','Col1','Col2','Col3','Col4','Col5'],
                ['Row1',1,2,3,4,5],
                ['Row2',6,7,8,9,10]])
                
print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))


# In[28]:


i = 0
while i<100:
    print("intinite loop")


# In[ ]:




