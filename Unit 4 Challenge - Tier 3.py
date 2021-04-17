#!/usr/bin/env python
# coding: utf-8

# # Springboard Data Science Career Track Unit 4 Challenge - Tier 3 Complete
# 
# ## Objectives
# Hey! Great job getting through those challenging DataCamp courses. You're learning a lot in a short span of time. 
# 
# In this notebook, you're going to apply the skills you've been learning, bridging the gap between the controlled environment of DataCamp and the *slightly* messier work that data scientists do with actual datasets!
# 
# Here’s the mystery we’re going to solve: ***which boroughs of London have seen the greatest increase in housing prices, on average, over the last two decades?***
# 
# 
# A borough is just a fancy word for district. You may be familiar with the five boroughs of New York… well, there are 32 boroughs within Greater London [(here's some info for the curious)](https://en.wikipedia.org/wiki/London_boroughs). Some of them are more desirable areas to live in, and the data will reflect that with a greater rise in housing prices.
# 
# ***This is the Tier 3 notebook, which means it's not filled in at all: we'll just give you the skeleton of a project, the brief and the data. It's up to you to play around with it and see what you can find out! Good luck! If you struggle, feel free to look at easier tiers for help; but try to dip in and out of them, as the more independent work you do, the better it is for your learning!***
# 
# This challenge will make use of only what you learned in the following DataCamp courses: 
# - Prework courses (Introduction to Python for Data Science, Intermediate Python for Data Science)
# - Data Types for Data Science
# - Python Data Science Toolbox (Part One) 
# - pandas Foundations
# - Manipulating DataFrames with pandas
# - Merging DataFrames with pandas
# 
# Of the tools, techniques and concepts in the above DataCamp courses, this challenge should require the application of the following: 
# - **pandas**
#     - **data ingestion and inspection** (pandas Foundations, Module One) 
#     - **exploratory data analysis** (pandas Foundations, Module Two)
#     - **tidying and cleaning** (Manipulating DataFrames with pandas, Module Three) 
#     - **transforming DataFrames** (Manipulating DataFrames with pandas, Module One)
#     - **subsetting DataFrames with lists** (Manipulating DataFrames with pandas, Module One) 
#     - **filtering DataFrames** (Manipulating DataFrames with pandas, Module One) 
#     - **grouping data** (Manipulating DataFrames with pandas, Module Four) 
#     - **melting data** (Manipulating DataFrames with pandas, Module Three) 
#     - **advanced indexing** (Manipulating DataFrames with pandas, Module Four) 
# - **matplotlib** (Intermediate Python for Data Science, Module One)
# - **fundamental data types** (Data Types for Data Science, Module One) 
# - **dictionaries** (Intermediate Python for Data Science, Module Two)
# - **handling dates and times** (Data Types for Data Science, Module Four)
# - **function definition** (Python Data Science Toolbox - Part One, Module One)
# - **default arguments, variable length, and scope** (Python Data Science Toolbox - Part One, Module Two) 
# - **lambda functions and error handling** (Python Data Science Toolbox - Part One, Module Four) 

# ## The Data Science Pipeline
# 
# This is Tier Three, so we'll get you started. But after that, it's all in your hands! When you feel done with your investigations, look back over what you've accomplished, and prepare a quick presentation of your findings for the next mentor meeting. 
# 
# Data Science is magical. In this case study, you'll get to apply some complex machine learning algorithms. But as  [David Spiegelhalter](https://www.youtube.com/watch?v=oUs1uvsz0Ok) reminds us, there is no substitute for simply **taking a really, really good look at the data.** Sometimes, this is all we need to answer our question.
# 
# Data Science projects generally adhere to the four stages of Data Science Pipeline:
# 1. Sourcing and loading 
# 2. Cleaning, transforming, and visualizing 
# 3. Modeling 
# 4. Evaluating and concluding 
# 

# ### 1. Sourcing and Loading 
# 
# Any Data Science project kicks off by importing  ***pandas***. The documentation of this wonderful library can be found [here](https://pandas.pydata.org/). As you've seen, pandas is conveniently connected to the [Numpy](http://www.numpy.org/) and [Matplotlib](https://matplotlib.org/) libraries. 
# 
# ***Hint:*** This part of the data science pipeline will test those skills you acquired in the pandas Foundations course, Module One. 

# #### 1.1. Importing Libraries

# In[1]:


# Let's import the pandas, numpy libraries as pd, and np respectively. 
import pandas as pd
import numpy as np

# Load the pyplot collection of functions from matplotlib, as plt 
import matplotlib.pyplot as plt 


# #### 1.2.  Loading the data
# Your data comes from the [London Datastore](https://data.london.gov.uk/): a free, open-source data-sharing portal for London-oriented datasets. 

# In[2]:


# First, make a variable called url_LondonHousePrices, and assign it the following link, enclosed in quotation-marks as a string:
# https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls

url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

# The dataset we're interested in contains the Average prices of the houses, and is actually on a particular sheet of the Excel file. 
# As a result, we need to specify the sheet name in the read_excel() method.
# Put this data into a variable called properties.  
properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None)


# ### 2. Cleaning, transforming, and visualizing
# This second stage is arguably the most important part of any Data Science project. The first thing to do is take a proper look at the data. Cleaning forms the majority of this stage, and can be done both before or after Transformation.
# 
# The end goal of data cleaning is to have tidy data. When data is tidy: 
# 
# 1. Each variable has a column.
# 2. Each observation forms a row.
# 
# Keep the end goal in mind as you move through this process, every step will take you closer. 
# 
# 
# 
# ***Hint:*** This part of the data science pipeline should test those skills you acquired in: 
# - Intermediate Python for data science, all modules.
# - pandas Foundations, all modules. 
# - Manipulating DataFrames with pandas, all modules.
# - Data Types for Data Science, Module Four.
# - Python Data Science Toolbox - Part One, all modules

# **2.1. Exploring your data** 
# 
# Think about your pandas functions for checking out a dataframe. 

# In[3]:


properties.head()
properties.shape
properties.describe()


# **2.2. Cleaning the data**
# 
# You might find you need to transpose your dataframe, check out what its row indexes are, and reset the index. You  also might find you need to assign the values of the first row to your column headings  . (Hint: recall the .columns feature of DataFrames, as well as the iloc[] method).
# 
# Don't be afraid to use StackOverflow for help  with this.

# In[4]:


prop_T=properties.transpose()
prop_T.head()


# **2.3. Cleaning the data (part 2)**
# 
# You might we have to **rename** a couple columns. How do you do this? The clue's pretty bold...

# In[5]:


#Reset Index
prop_T=prop_T.reset_index()

#Make Row 0 headers
prop_T.columns = prop_T.iloc[0]


# In[6]:


#Rename Columns one and two
prop_T = prop_T.rename(columns = {'Unnamed: 0':'London_Borough', pd.NaT: 'ID'})


# In[7]:


#Remove headers in the first row
prop_T.drop(index=0,inplace=True,axis=0)
prop_T.head()


# **2.4.Transforming the data**
# 
# Remember what Wes McKinney said about tidy data? 
# 
# You might need to **melt** your DataFrame here. 

# In[8]:


prop_melt = pd.melt(prop_T, id_vars= ['London_Borough','ID'])


# # Remember to make sure your column data types are all correct. Average prices, for example, should be floating point numbers... 

# In[9]:


#rename columns in prop_melt
prop_melt=prop_melt.rename(columns = {0: 'Month', 'value': 'Average_price'})
prop_melt.dtypes


# In[10]:


#change Average_price to float
prop_melt['Average_price'] = pd.to_numeric(prop_melt['Average_price'])
prop_melt.dtypes


# **2.5. Cleaning the data (part 3)**
# 
# Do we have an equal number of observations in the ID, Average Price, Month, and London Borough columns? Remember that there are only 32 London Boroughs. How many entries do you have in that column? 
# 
# Check out the contents of the London Borough column, and if you find null values, get rid of them however you see fit. 

# In[11]:


#view number of unique elements in London_Borough
len(prop_melt['London_Borough'].unique())


# In[12]:


prop_melt['London_Borough'].unique()


# In[13]:


nonBoroughs = ['City of London','Inner London', 'Outer London', 
               'NORTH EAST', 'NORTH WEST', 'YORKS & THE HUMBER', 
               'EAST MIDLANDS', 'WEST MIDLANDS',
              'EAST OF ENGLAND', 'LONDON', 'SOUTH EAST', 
              'SOUTH WEST', 'England','Unnamed: 34',
       'Unnamed: 37', 'Unnamed: 47']

df=prop_melt[~prop_melt.London_Borough.isin(nonBoroughs)]


# In[14]:


df.shape
df['London_Borough'].unique()


# **2.6. Visualizing the data**
# 
# To visualize the data, why not subset on a particular London Borough? Maybe do a line plot of Month against Average Price?

# In[15]:


brent_prices=df[df['London_Borough']=='Brent']

plot1=brent_prices.plot(kind='line',x='Month',y='Average_price')


# To limit the number of data points you have, you might want to extract the year from every month value your *Month* column. 
# 
# To this end, you *could* apply a ***lambda function***. Your logic could work as follows:
# 1. look through the `Month` column
# 2. extract the year from each individual value in that column 
# 3. store that corresponding year as separate column. 
# 
# Whether you go ahead with this is up to you. Just so long as you answer our initial brief: which boroughs of London have seen the greatest house price increase, on average, over the past two decades? 

# In[16]:


#Extract Year from DateTime and store in new column
df['Year'] = df['Month'].apply(lambda t: t.year)
df.tail()


# **3. Modeling**
# 
# Consider creating a function that will calculate a ratio of house prices, comparing the price of a house in 2018 to the price in 1998.
# 
# Consider calling this function create_price_ratio.
# 
# You'd want this function to:
# 1. Take a filter of dfg, specifically where this filter constrains the London_Borough, as an argument. For example, one admissible argument should be: dfg[dfg['London_Borough']=='Camden'].
# 2. Get the Average Price for that Borough, for the years 1998 and 2018.
# 4. Calculate the ratio of the Average Price for 1998 divided by the Average Price for 2018.
# 5. Return that ratio.
# 
# Once you've written this function, you ultimately want to use it to iterate through all the unique London_Boroughs and work out the ratio capturing the difference of house prices between 1998 and 2018.
# 
# Bear in mind: you don't have to write a function like this if you don't want to. If you can solve the brief otherwise, then great! 
# 
# ***Hint***: This section should test the skills you acquired in:
# - Python Data Science Toolbox - Part One, all modules

# In[17]:


# Using the function 'groupby' will help you to calculate the mean for each year and for each Borough. 
## As you can see, the variables Borough and Year are now indices
dfg =df.groupby(by=['London_Borough', 'Year']).mean()
dfg.sample(10)
# Let's reset the index for our new DataFrame dfg, and call the head() method on it. 
dfg = dfg.reset_index()
dfg.head()


# In[18]:


# Here's where you should write your function:
def create_price_ratio(d):
    y1998 = float(d['Average_price'][d['Year']==1998])
    y2018 = float(d['Average_price'][d['Year']==2018])
    ratio = [y2018/y1998]
    return ratio


# In[19]:


#  Test out the function by calling it with the following argument:
# dfg[dfg['London_Borough']=='Barking & Dagenham']
create_price_ratio(dfg[dfg['London_Borough']=='Harrow'])


# In[20]:


# We want to do this for all of the London Boroughs. 
# First, let's make an empty dictionary, called final, where we'll store our ratios for each unique London_Borough.
final = {}


# In[21]:


# Now let's declare a for loop that will iterate through each of the unique elements of the 'London_Borough' column of our DataFrame dfg.
# Call the iterator variable 'b'. 
for b in dfg['London_Borough'].unique():
    # Let's make our parameter to our create_price_ratio function: i.e., we subset dfg on 'London_Borough' == b. 
    borough = dfg[dfg['London_Borough'] == b]
    # Make a new entry in the final dictionary whose value's the result of calling create_price_ratio with the argument: borough
    final[b] = create_price_ratio(borough)
# We use the function and incorporate that into a new key of the dictionary 
print(final) 


# In[22]:


# Make a variable called df_ratios, and assign it the result of calling the DataFrame method on the dictionary final. 
df_ratios = pd.DataFrame(final)


# In[23]:


# Call the head() method on this variable to check it out. 
df_ratios.head()


# In[24]:


# All we need to do now is transpose it, and reset the index! 
df_ratios_T = df_ratios.T
df_ratios = df_ratios_T.reset_index()
df_ratios.head()


# In[25]:


# Let's just rename the 'index' column as 'London_Borough', and the '0' column to '2018'.
df_ratios.rename(columns={'index':'Borough', 0:'2018'}, inplace=True)
df_ratios.head()


# In[26]:


# Let's sort in descending order and select the top 15 boroughs.
# Make a variable called top15, and assign it the result of calling sort_values() on df_ratios. 
top15 = df_ratios.sort_values(by='2018',ascending=False).head(15)
print(top15)


# In[29]:


# Let's sort in descending order and select the bottom 15 boroughs.

bot15 = df_ratios.sort_values(by='2018',ascending=True).head(15)
print(bot15)
type(bot15)


# In[27]:


# Let's plot the boroughs that have seen the greatest changes in price.
# Make a variable called ax. Assign it the result of filtering top15 on 'Borough' and '2018', then calling plot(), with
# the parameter kind = 'bar'. 
ax = top15[['Borough','2018']].plot(kind='bar')

ax.set_xticklabels(top15.Borough)


# In[30]:


ax_bot = bot15[['Borough','2018']].plot(kind='bar')

ax.set_xticklabels(bot15.Borough)


# In[33]:


all_borough = df_ratios.sort_values(by='2018',ascending=True)
all_borough = all_borough[['Borough','2018']].plot(kind='bar')

all_borough.set_xticklabels(all_borough.Borough)


# ### 4. Conclusion
# What can you conclude? Type out your conclusion below. 
# 
# Look back at your notebook. Think about how you might summarize what you have done, and prepare a quick presentation on it to your mentor at your next meeting. 
# 
# We hope you enjoyed this practical project. It should have consolidated your data hygiene and pandas skills by looking at a real-world problem involving just the kind of dataset you might encounter as a budding data scientist. Congratulations, and looking forward to seeing you at the next step in the course! 

# In[ ]:




