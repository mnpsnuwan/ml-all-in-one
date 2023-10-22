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


# In[6]:


G = nx.bull_graph()
nx.draw(G, node_size = 40,node_color = 'maroon')


# In[9]:


G = nx.chvatal_graph()
nx.draw(G, node_size = 40,node_color = 'coral')


# In[12]:


G = nx.cubical_graph()
nx.draw(G, node_size = 40,node_color = 'silver')


# In[13]:


G = nx.desargues_graph()
nx.draw(G, node_size = 40,node_color = 'darkgreen')


# In[15]:


G = nx.diamond_graph()
nx.draw(G, node_size = 40,node_color = 'darkgrey')


# In[16]:


G = nx.dodecahedral_graph()
nx.draw(G, node_size = 40,node_color = 'darkblue')


# In[18]:


G = nx.frucht_graph()
nx.draw(G, node_size = 40,node_color = 'darkred')


# In[19]:


G = nx.heawood_graph()
nx.draw(G, node_size = 40,node_color = 'magenta')


# In[20]:


G = nx.hoffman_singleton_graph()
nx.draw(G, node_size = 40,node_color = 'indigo')


# In[21]:


G = nx.house_graph()
nx.draw(G, node_size = 40,node_color = 'teal')


# In[22]:


G = nx.house_x_graph()
nx.draw(G, node_size = 40,node_color = 'crimson')


# In[23]:


G = nx.icosahedral_graph()
nx.draw(G, node_size = 40,node_color = 'khaki')


# In[24]:


G = nx.krackhardt_kite_graph()
nx.draw(G, node_size = 40,node_color = 'beige')


# In[25]:


G = nx.moebius_kantor_graph()
nx.draw(G, node_size = 40,node_color = 'plum')


# In[26]:


G = nx.octahedral_graph()
nx.draw(G, node_size = 40,node_color = 'skyblue')


# In[28]:


G = nx.pappus_graph()
nx.draw(G, node_size = 40,node_color = 'limegreen')


# In[29]:


G = nx.petersen_graph()
nx.draw(G, node_size = 40,node_color = 'lavender')


# In[30]:


G = nx.sedgewick_maze_graph()
nx.draw(G, node_size = 40,node_color = 'olive')


# In[31]:


G = nx.tutte_graph()
nx.draw(G, node_size = 40,node_color = 'blue')


# In[ ]:




