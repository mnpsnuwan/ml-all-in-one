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
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


# In[3]:


G = nx.random_tree(100)
nx.draw(G, node_size = 40,node_color = 'red')


# In[4]:


G = nx.balanced_tree(r=3, h=4)
nx.draw(G, node_size = 40,node_color = 'green')


# In[5]:


G = nx.barbell_graph(5, 2)
nx.draw(G, node_size = 40,node_color = 'blue')


# In[6]:


G = nx.complete_graph(30)
nx.draw(G, node_size = 40,node_color = 'orange')


# In[7]:


G = nx.complete_multipartite_graph(50)
nx.draw(G, node_size = 40,node_color = 'yellow')


# In[8]:


G = nx.circular_ladder_graph(50)
nx.draw(G, node_size = 40,node_color = 'violet')


# In[9]:


G = nx.circulant_graph(1000,[10,50])
nx.draw(G, node_size = 10,node_color = 'limegreen')


# In[10]:


G = nx.cycle_graph(50)
nx.draw(G, node_size = 40,node_color = 'darkorange')


# In[11]:


G = nx.dorogovtsev_goltsev_mendes_graph(7)
nx.draw(G, node_size = 40,node_color = 'gold')


# In[12]:


G = nx.lollipop_graph(5,3)
nx.draw(G, node_size = 40,node_color = 'pink')


# In[13]:


G = nx.star_graph(100)
nx.draw(G, node_size = 40,node_color = 'lightblue')


# In[15]:


G = nx.wheel_graph(100)
nx.draw(G, node_size = 40,node_color = 'lightgreen')


# In[ ]:




