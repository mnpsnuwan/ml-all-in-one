#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="matplotlib")


# In[3]:


G = nx.karate_club_graph()
nx.draw(G, node_size = 40,node_color = 'indigo')


# In[4]:


G = nx.davis_southern_women_graph()
nx.draw(G, node_size = 40,node_color = 'maroon')


# In[5]:


G = nx.florentine_families_graph()
nx.draw(G, node_size = 40,node_color = 'blue')


# In[ ]:




