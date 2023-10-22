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


G = nx.grid_2d_graph(10,10)
nx.draw(G, node_size = 40,node_color = 'grey')


# In[4]:


G = nx.grid_graph([5,5], periodic = True)
nx.draw(G, node_size = 40,node_color = 'brown') 


# In[5]:


G = nx.hexagonal_lattice_graph(6,6)
nx.draw(G, node_size = 40,node_color = 'purple')


# In[6]:


G = nx.hypercube_graph(4)
nx.draw(G, node_size = 40,node_color = 'cyan')


# In[7]:


G = nx.triangular_lattice_graph(10,10)
nx.draw(G, node_size = 40,node_color = 'salmon')


# In[ ]:




