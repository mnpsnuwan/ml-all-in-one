#!/usr/bin/env python
# coding: utf-8

# ### Linear and Polynomial Regression for Pumpkin Pricing
# 
# Load up required libraries and dataset. Convert the data to a dataframe containing a subset of the data:
# 
# - Only get pumpkins priced by the bushel
# - Convert the date to a month
# - Calculate the price to be an average of high and low prices
# - Convert the price to reflect the pricing by bushel quantity

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

pumpkins = pd.read_csv('../../../data/pumpkins.csv')

pumpkins.head()


# In[2]:


pumpkins = pumpkins[pumpkins['Package'].str.contains('bushel', case=True, regex=True)]

new_columns = ['Package', 'Variety', 'City Name', 'Month', 'Low Price', 'High Price', 'Date']
pumpkins = pumpkins.drop([c for c in pumpkins.columns if c not in new_columns], axis=1)

price = (pumpkins['Low Price'] + pumpkins['High Price']) / 2

month = pd.DatetimeIndex(pumpkins['Date']).month
day_of_year = pd.to_datetime(pumpkins['Date']).apply(lambda dt: (dt-datetime(dt.year,1,1)).days)

new_pumpkins = pd.DataFrame(
    {'Month': month,
     'DayOfYear' : day_of_year,
     'Variety': pumpkins['Variety'],
     'City': pumpkins['City Name'],
     'Package': pumpkins['Package'],
     'Low Price': pumpkins['Low Price'],
     'High Price': pumpkins['High Price'],
     'Price': price})

new_pumpkins.loc[new_pumpkins['Package'].str.contains('1 1/9'), 'Price'] = price/1.1
new_pumpkins.loc[new_pumpkins['Package'].str.contains('1/2'), 'Price'] = price*2

new_pumpkins.head()


# A scatterplot reminds us that we only have month data from August through December. We probably need more data to be able to draw conclusions in a linear fashion.

# In[3]:


new_pumpkins.plot.scatter('Month','Price')


# In[4]:


new_pumpkins.plot.scatter('DayOfYear','Price')


# Let's see if there is correlation:

# In[5]:


print(new_pumpkins['Month'].corr(new_pumpkins['Price']))
print(new_pumpkins['DayOfYear'].corr(new_pumpkins['Price']))


# Looks like correlation is pretty small, but there is some other more important relationship - because price points in the plot above seem to have several distinct clusters. Let's make a plot that will show different pumpkin varieties:

# In[6]:


ax=None
colors = ['red','blue','green','yellow']
for i,var in enumerate(new_pumpkins['Variety'].unique()):
    ax = new_pumpkins[new_pumpkins['Variety']==var].plot.scatter('DayOfYear','Price',ax=ax,c=colors[i],label=var)


# In[7]:


new_pumpkins.groupby('Variety')['Price'].mean().plot(kind='bar')


# For the time being, let's concentrate only on one variety - **pie type**.

# In[8]:


pie_pumpkins = new_pumpkins[new_pumpkins['Variety']=='PIE TYPE']
print(pie_pumpkins['DayOfYear'].corr(pie_pumpkins['Price']))
pie_pumpkins.plot.scatter('DayOfYear','Price')


# ### Linear Regression
# 
# We will use Scikit Learn to train linear regression model:

# In[9]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split


# In[10]:


X = pie_pumpkins['DayOfYear'].to_numpy().reshape(-1,1)
y = pie_pumpkins['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)

pred = lin_reg.predict(X_test)

mse = np.sqrt(mean_squared_error(y_test,pred))
print(f'Mean error: {mse:3.3} ({mse/np.mean(pred)*100:3.3}%)')


# In[11]:


plt.scatter(X_test,y_test)
plt.plot(X_test,pred)


# The slope of the line can be determined from linear regression coefficients:

# In[12]:


lin_reg.coef_, lin_reg.intercept_


# We can use the trained model to predict price:

# In[13]:


# Pumpkin price on programmer's day

lin_reg.predict([[256]])


# ### Polynomial Regression
# 
# Sometimes the relationship between features and the results is inherently non-linear. For example, pumpkin prices might be high in winter (months=1,2), then drop over summer (months=5-7), and then rise again. Linear regression is unable to fin this relationship accurately.
# 
# In this case, we may consider adding extra features. Simple way is to use polynomials from input features, which would result in **polynomial regression**. In Scikit Learn, we can automatically pre-compute polynomial features using pipelines:

# In[14]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

pipeline = make_pipeline(PolynomialFeatures(2), LinearRegression())

pipeline.fit(X_train,y_train)

pred = pipeline.predict(X_test)

mse = np.sqrt(mean_squared_error(y_test,pred))
print(f'Mean error: {mse:3.3} ({mse/np.mean(pred)*100:3.3}%)')

score = pipeline.score(X_train,y_train)
print('Model determination: ', score)

plt.scatter(X_test,y_test)
plt.plot(sorted(X_test),pipeline.predict(sorted(X_test)))


# ### Encoding varieties
# 
# In the ideal world, we want to be able to predict prices for different pumpkin varieties using the same model. To take variety into account, we first need to convert it to numeric form, or **encode**. There are several way we can do it:
# 
# * Simple numeric encoding that will build a table of different varieties, and then replace variety name by an index in that table. This is not the best idea for linear regression, because linear regression takes the numeric value of the index into account, and the numeric value is likely not to correlate numerically with the price.
# * One-hot encoding, which will replace `Variety` column by 4 different columns, one for each variety, that will contain 1 if the corresponding row is of given variety, and 0 otherwise.
# The code below shows how we can can one-hot encode a variety:

# In[15]:


pd.get_dummies(new_pumpkins['Variety'])


# ### Linear Regression on Variety
# 
# We will now use the same code as above, but instead of `DayOfYear` we will use our one-hot-encoded variety as input:

# In[16]:


X = pd.get_dummies(new_pumpkins['Variety'])
y = new_pumpkins['Price']


# In[17]:


def run_linear_regression(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    lin_reg = LinearRegression()
    lin_reg.fit(X_train,y_train)

    pred = lin_reg.predict(X_test)

    mse = np.sqrt(mean_squared_error(y_test,pred))
    print(f'Mean error: {mse:3.3} ({mse/np.mean(pred)*100:3.3}%)')

    score = lin_reg.score(X_train,y_train)
    print('Model determination: ', score)

run_linear_regression(X,y)


# We can also try using other features in the same manner, and combining them with numerical features, such as `Month` or `DayOfYear`:

# In[18]:


X = pd.get_dummies(new_pumpkins['Variety']) \
        .join(new_pumpkins['Month']) \
        .join(pd.get_dummies(new_pumpkins['City'])) \
        .join(pd.get_dummies(new_pumpkins['Package']))
y = new_pumpkins['Price']

run_linear_regression(X,y)


# ### Polynomial Regression
# 
# Polynomial regression can also be used with categorical features that are one-hot-encoded. The code to train polynomial regression would essentially be the same as we have seen above.

# In[19]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

pipeline = make_pipeline(PolynomialFeatures(2), LinearRegression())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

pipeline.fit(X_train,y_train)

pred = pipeline.predict(X_test)

mse = np.sqrt(mean_squared_error(y_test,pred))
print(f'Mean error: {mse:3.3} ({mse/np.mean(pred)*100:3.3}%)')

score = pipeline.score(X_train,y_train)
print('Model determination: ', score)

