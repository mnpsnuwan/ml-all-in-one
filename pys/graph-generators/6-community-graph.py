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


G = nx.caveman_graph(4,5)
nx.draw(G, node_size = 40,node_color = 'green')


# In[4]:


G = nx.connected_caveman_graph(20,5)
nx.draw(G, node_size = 40,node_color = 'violet')


# In[5]:


G = nx.relaxed_caveman_graph(20,10,0.1)
nx.draw(G, node_size = 40,node_color = 'crimson')


# In[6]:


G = nx.random_partition_graph([20,10,30],0.1,0.1)
nx.draw(G, node_size = 40,node_color = 'blue')


# In[7]:


G = nx.ring_of_cliques(20,5)
nx.draw(G, node_size = 40,node_color = 'yellow')


# In[8]:


G = nx.windmill_graph(20,10)
nx.draw(G, node_size = 40,node_color = 'orange')


# In[ ]:




