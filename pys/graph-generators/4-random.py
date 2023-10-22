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


G = nx.fast_gnp_random_graph(100,0.1)
nx.draw(G, node_size = 40,node_color = 'red')


# In[4]:


G = nx.gnp_random_graph(100,0.1)
nx.draw(G, node_size = 40,node_color = 'green')


# In[5]:


G = nx.dense_gnm_random_graph(100,100)
nx.draw(G, node_size = 40,node_color = 'orange')


# In[6]:


G = nx.binomial_graph(100, 0.1)
nx.draw(G, node_size = 40,node_color = 'salmon')


# In[7]:


G = nx.barabasi_albert_graph(20,10)
nx.draw(G, node_size = 40,node_color = 'cyan')


# In[9]:


G = nx.random_powerlaw_tree(30, gamma=3, seed=None, tries=100)
nx.draw(G, node_size = 40,node_color = 'gold')


# In[10]:


G = nx.powerlaw_cluster_graph(100,8,0.1)
nx.draw(G, node_size = 40,node_color = 'purple')


# In[ ]:




