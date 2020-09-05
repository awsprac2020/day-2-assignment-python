#!/usr/bin/env python
# coding: utf-8

# # List and its default functions

# In[4]:


lst=["x","10","12.5","Ranit"]


# In[5]:


lst


# In[6]:


lst.append("y")


# In[10]:


lst


# In[32]:


lst.index('10')


# In[33]:


lst[1]


# In[34]:


lst.remove('x')


# In[35]:


lst


# In[48]:


lst.count('10')


# # Dictionary and its default functions

# In[50]:


dit={"name":"Ranit","age":"x","roll":"y","school":"z"}


# In[51]:


dit


# In[56]:


dit.get('age')


# In[58]:


dit.keys()


# In[59]:


dit.items()


# In[62]:


dit["class"] = "a"


# In[63]:


dit


# In[64]:


dit.pop('age')


# In[65]:


dit


# # Sets and its default functions

# In[3]:


st={"Ranit","day 2",1,2,3,4,4,4,6,5,5}


# In[38]:


st


# In[41]:


st1={1,2}


# In[42]:


st1.issubset(st)


# In[40]:


st1.intersection()


# In[33]:


st.add(7)


# In[34]:


st


# In[46]:


st1.isdisjoint(st)


# # Tuple and explore default methods

# In[73]:


tuple=("@","#","!")


# In[74]:


tuple


# In[98]:


tuple.count("#")


# In[95]:


tuple.index("@")


# # Strings and explore default methods

# In[99]:


str=["ranit","ram","shyam"]


# In[100]:


str


# In[101]:


str.append("virat")


# In[102]:


str


# In[104]:


str.count("ram")


# In[106]:


str.index("virat")


# In[107]:


str.remove("shyam")


# In[108]:


str


# In[111]:


str.reverse()


# In[112]:


str


# In[ ]:




