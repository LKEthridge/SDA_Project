#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid green 2px; padding: 20px"> <h1 style="color:green; margin-bottom:20px">Reviewer's comment v1</h1>
# 
# Hello Lydia, my name is Dmitrii. I'm going to review your project! Nice to meet you! 🙌
# 
# You can find my comments under the heading **«Review»**. I will categorize my comments in green, blue or red boxes like this:
# 
# <div class="alert alert-success">
#     <b>Success:</b> if everything is done successfully
# </div>
# <div class="alert alert-warning">
#     <b>Remarks:</b> if I can give some recommendations or ways to improve the project
# </div>
# <div class="alert alert-danger">
#     <b>Needs fixing:</b> if the block requires some corrections. Work can't be accepted with the red comments
# </div>
# 
# Please don't remove my comments :) If you have any questions don't hesitate to respond to my comments in a different section. 
# <div class="alert alert-info"> <b>Student comments: </div>    
# 

# <div style="border:solid green 2px; padding: 20px">
# <b>Reviewer's comment v1</b>
#     
# <b>Overall Feedback</b> 
#     
# Overall, well done! I can see that a lot of effort has been put in. Your project already looks really good, and you've achieved impressive results.
# 
# However, there are some comments/areas left to fix that will help you to make your project even better (in red boxes with the title - `Reviewer's comment v1`). 
#     
# And of course, if you have any questions along the way, remember that you can always reach out to your tutor for clarification.
# </div>

# <div style="border:solid green 2px; padding: 20px">
# <b>Reviewer's comment v2:</b>
#     
# <b>Overall Feedback</b> 
#     
# Thank you for going an extra mile and enhancing your project. There are no issues left, so your project has been accepted. I wish you engaging projects in the upcoming sprints! ☘️
#     
# PS: As a final note, I can recommend cool lectures on stat analysis here: https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo  
#     
# Another great self-paced course that covers basic concepts in probability and statistics - Probability and Statistics by Stanford Online or you could check this one [An Introduction to Statistical Learning with Applications in R](https://www.r-bloggers.com/2014/09/in-depth-introduction-to-machine-learning-in-15-hours-of-expert-videos/) 🙌
# 
# </div>

# # Which one is a better plan?
# 
# You work as an analyst for the telecom operator Megaline. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget.
# 
# You are going to carry out a preliminary analysis of the plans based on a relatively small client selection. You'll have the data on 500 Megaline clients: who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent in 2018. Your job is to analyze the clients' behavior and determine which prepaid plan brings in more revenue.

# <span style="font-weight: bold; font-style: italic; color: blue">Megaline offers two prepaid plans, Surf and Ultimate.  This project will determine which plan generates more revenue to help the commercial department adjust their advertising budget.  These conclusions are tentative as they reflect the data of a small data set: however, they are a starting point in determining which plan generates more revenue.</span>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment v1</b>
#  
# Great that you added additional information about the project goal and tasks.

# ## Initialization

# <span style="font-weight: bold; font-style: italic; color: blue">This project will use pandas, numpy, pyplot, factorial, and stats.</span>

# In[1]:


# Loading all the libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import math as math
from math import factorial
import scipy as spy
from scipy import stats as st


# ## Load data

# <span style="font-weight: bold; font-style: italic; color: blue">This project draws on 5 data sets: call data, internet usage, message data, plan information, and user information.</span>

# In[2]:


# Load the data files into different DataFrames
try:
    calls = pd.read_csv('/datasets/megaline_calls.csv')
    internet = pd.read_csv('/datasets/megaline_internet.csv')
    messages = pd.read_csv('/datasets/megaline_messages.csv')
    plans = pd.read_csv('/datasets/megaline_plans.csv')
    users = pd.read_csv('/datasets/megaline_users.csv')
except FileNotFoundError:
    print('File was not found.')


# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment v1</b>
#  
# You could also apply `try/except` structure with different paths so it will work with both local and remote data paths. 
#     
# You could check additional information here: https://www.w3schools.com/python/python_try_except.asp
#     
# Here's a simple example of how you can apply a try/except structure to handle both local and remote data paths:
# 
# ```
# try:
#     orders = pd.read_csv(local_path['orders'], sep=';')
# 
# except FileNotFoundError:
#     orders = pd.read_csv(server_path['orders'], sep=';')
# ```

# <div class="alert alert-info"> <b>Student comments:</b> That's a helpful thing to incorporate!  I wasn't sure the server_path to use in this case, but I added one of the examples from the link you sent.</div> 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment v2</b>
#  
# Looks great! Thank for incorporating that. 

# ## Prepare the data

# <span style="font-weight: bold; font-style: italic; color: blue">Having loaded the data, general information can be printed, fixed, and the data can be enriched as needed for each data frame.</span>

# ## Plans

# In[3]:


# Print the general/summary information about the plans' DataFrame
plans.info()


# In[4]:


# Print a sample of data for plans
plans.head()


# <span style="font-weight: bold; font-style: italic; color: blue">This is a small data frame containing 2 entries with no null values.  Data appears to be fairly standard and clean.  I will maintain usd_per_message and usd_per_minute as float64 data type to avoid loss of data.</span>

# ## Fix data

# <span style="font-weight: bold; font-style: italic; color: blue">There is no need to fix the data.</span>

# ## Enrich data

# <span style="font-weight: bold; font-style: italic; color: blue">No additional factors are necessary.</span>

# ## Users

# In[5]:


# Print the general/summary information about the users' DataFrame

users.info()


# In[6]:


# Print a sample of data for users

users.sample(5, random_state=500)


# <span style="font-weight: bold; font-style: italic; color: blue">The data set contains information for 500 users, including 34 former users (as evidenced by the 34 non-null values in churn_date.  All data are accounted for and need only one minor adjustments: user_id would be better represented in object data type as the numbers have no mathematical significance.</span>

# ### Fix Data

# [Fix obvious issues with the data given the initial observations.]

# In[7]:


users['user_id'] = users['user_id'].astype(object)
users.info()


# ### Enrich Data

# <span style="font-weight: bold; font-style: italic; color: blue">No additional factors are necessary.</span>

# ## Calls

# In[8]:


# Print the general/summary information about the calls' DataFrame
calls.info()


# In[9]:


# Print a sample of data for calls
calls.sample(15, random_state=137735)


# <span style="font-weight: bold; font-style: italic; color: blue">The data set is complete with no null values.  User_id will be converted to the object data type for the same reason noted above.  Call date will be converted to a date-time object for greater analysis options.  I will add a secondary column for duration that uses an integer data type as Megaline rounds call length up to the next full minute for billing purposes, so partial duration is most likely unneccessary.  However, it is prudent to maintain the data and simply create a second column: 'billed_duration'.  I will also group by user_id.
# It is unclear why some calls are marked as being 0.00 minutes long... is this missing data?  Calls that were immediately cancelled?  It is impossible to draw a conclusion at this point.</span>

# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment v1</b>
#  
# - Please note that the telecom operator rounds up all minutes and traffic values.
# 
# `Note: Megaline rounds seconds up to minutes, and megabytes to gigabytes. For calls, each individual call is rounded up: even if the call lasted just one second, it will be counted as one minute. For web traffic, individual web sessions are not rounded up. Instead, the total for the month is rounded up. If someone uses 1025 megabytes this month, they will be charged for 2 gigabytes.`
# 
# Can you please add data rounding?

# <div class="alert alert-info"> <b>Student comments:</b> I did this below on 2.8.2, and it was marked as correct.  I did not do it at this stage because my understanding was this section was just for printing info and a sample to get a preview of the data and plan changes needed.  So, I am unsure if you're wanting me to address it here instead?  Since it's addressed below, I didn't make any adjustments here.  Please clarify what changes are needed at this stage of the project.</div> 

# <div class="alert alert-success">
# <b>Reviewer's comment v2:</b>
# 
# Got it. I guess there was some confusion on my part that's why I left this comment.
# 
# Your code in 2.8.2 is fully correct and happens before data aggregation, so please disregard the comment above.

# ### Fix data

# In[10]:


calls['user_id'] = calls['user_id'].astype(object)
calls['call_date'] = pd.to_datetime(calls['call_date'])
calls.info()
calls.sample(15, random_state=137735)


# In[11]:


calls.groupby('user_id')
calls.head(15)


# <span style="font-weight: bold; font-style: italic; color: blue">Data types have been converted and no data has been compromised based on referencing the sample.  Additionally, I grouped by user_id and printed the head to ensure everything worked as intended.</span>

# ### Enrich data

# In[12]:


calls['billed_duration'] = calls['duration'].apply(lambda x: math.ceil(x))

calls.head()


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment v1</b>
#  
# Everything is correct here! 
# 
# As a second approach you could also use `np.ceil` function from the numpy library:
#     
# https://numpy.org/doc/stable/reference/generated/numpy.ceil.html

# <span style="font-weight: bold; font-style: italic; color: blue">This should provide more flexibility for analysis!</span>

# ## Messages

# In[13]:


# Print the general/summary information about the messages' DataFrame

messages.info()


# In[14]:


# Print a sample of data for messages

messages.sample(10, random_state=76051)


# <span style="font-weight: bold; font-style: italic; color: blue">This data frame contains information about id and message date.  I will convert user_id to an object data type and message_date to date-time format for consistency across data frames.  I will also group by user_id.</span>

#  

# ### Fix data

# In[15]:


messages['user_id'] = messages['user_id'].astype(object)
messages['message_date'] = pd.to_datetime(messages['message_date'])
messages.info()


# <span style="font-weight: bold; font-style: italic; color: blue">Data converted for consistency and greater possibilities for analysis.</span>

# ### Enrich data

# In[16]:


messages.groupby('user_id')
messages.head(10)


# ## Internet

# In[17]:


# Print the general/summary information about the internet DataFrame
internet.info()


# In[18]:


# Print a sample of data for the internet traffic
internet.sample(10, random_state=104825)


# <span style="font-weight: bold; font-style: italic; color: blue">Based on a first look at the data, user_id should be converted to object data type and session_date should be converted to datetime.</span>

# ### Fix data

# In[19]:


internet['user_id'] = internet['user_id'].astype(object)
internet['session_date'] = pd.to_datetime(internet['session_date'])
internet.info()


# <span style="font-weight: bold; font-style: italic; color: blue">Changed data types accordingly.</span>

# ### Enrich data

# <span style="font-weight: bold; font-style: italic; color: blue">No enrichment is needed.</span>

# ## Study plan conditions

# In[20]:


# Print out the plan conditions and make sure they are clear for you

plans.head()


# <span style="font-weight: bold; font-style: italic; color: blue">The Surf plan includes 500 minutes, 50 messages, and 15360 mb/month of data for 20/month.  If Surf users exceed those limits, they pay 0.03/minute, 0.03/message, and 10/gb.  The Ultimate plan includes 3000 minutes, 1000 messages, and 30720 mb/month of data for 70/month.  If Ultimate users exceed those limits, they pay 0.01/minute, 0.01/message, and 7/gb.</span>

# <div class="alert alert-success" role="alert">
# <b>Reviewer's comment v1:</b>
#     
# Everything is correct here. 

# ## Aggregate data per user
# 
# <span style="font-weight: bold; font-style: italic; color: blue">Now that the data is clean, I will aggregate the data by user and per period to simplify further analysis.</span>

# In[21]:


# Calculate the number of calls made by each user per month. Save the result.
calls['month'] = calls['call_date'].dt.month
calls_upm = calls.groupby(['user_id', 'month']).agg(total_calls=('id', 'count')).reset_index()
calls_upm


# <div class="alert alert-warning">
# <b>Reviewer's comment v1:</b>
#     
# Everything is correct here but usually, it is always helpful to double-check whether we indeed have data within one year/time period. If not then selecting and aggregating data by the month number will cause an issue. So here it is safer to use datetime64[M] which provides a complete date. 
# 
# Also you could achieve the same using the following code `calls['call_date'].dt.to_period('M')`
#   

# <div class="alert alert-info"> <b>Student comments:</b> Makes sense!  I think I had previously noticed everything was in 2018, but this is a great strategy to know!  I ran the code that way to give it a try but changed it back since the different data type was making later merge operations more complicated.</div> 

# In[22]:


# Calculate the amount of minutes spent by each user per month. Save the result.
calls_mpu = calls.groupby(['user_id','month']).agg({'billed_duration' : ('sum')}).reset_index()
calls_mpu


# <div class="alert alert-danger">
# <b>Reviewer's comment v1:</b>
#     
# Here you need to use rounded before `billed_duration` column. 

# <div class="alert alert-success">
# <b>Reviewer's comment v2:</b>
# 
# Everything is correct now.

# <div class="alert alert-warning" role="alert">
# <b>Reviewer's comment v1:</b>
#     
# In pivot_table or groupby it is possible to pass multiple arguments, so here, you can create an aggregated table in one go like this:
# 
# 
# ```
# data_calls.groupby(['user_id','month']).agg({'duration' : ('count','sum')}).reset_index()
# ```
# 
# or 
# 
# ```
# data_calls.pivot_table(index = ('user_id','month'), values = 'duration', aggfunc = ('count','sum')).reset_index()
# ```

# <div class="alert alert-info"> <b>Student comments:</b> I believe that fixed it!</div>

# In[23]:


# Calculate the number of messages sent by each user per month. Save the result.
messages['month'] = messages['message_date'].dt.month
msg_upm = messages.groupby(['user_id', 'month']).agg(total_msgs=('id', 'count')).reset_index()
msg_upm


# In[24]:


# Calculate the volume of internet traffic used by each user per month. Save the result.
internet['month'] = internet['session_date'].dt.month

def round_to_gb(mb):
    return np.ceil(mb/1024)
internet['gb_billed'] = internet['mb_used'].apply(round_to_gb)
internet_upm = internet.groupby(['user_id', 'month']).agg({'gb_billed':('sum')}).reset_index()
internet_upm


# <span style="font-weight: bold; font-style: italic; color: blue">Now that I have calculated totals per month, I will merge all of these dataframes into one for further analysis.</span>

# In[25]:


# Merge the data for calls, minutes, messages, internet based on user_id and month
usage = calls_upm.merge(calls_mpu, how='outer', on=['user_id', 'month'])
usage = usage.merge(msg_upm, how='outer', on=['user_id', 'month'])
usage = usage.merge(internet_upm, how='outer', on=['user_id', 'month'])
usage


# <div class="alert alert-danger">
# <b>Reviewer's comment v1:</b>
# 
# Here you need to use another way of joining tables (change the how parameter). Now, if users made calls, but did not send messages, it will not be tracked in the new table (the same with the Internet). This will happen because with the left method we take all the keys from the left table and look for their matches in the right table. If there are unique values in the right table, we will ignore them. For this task, we need to take all the records from the right and left tables. You can see about connections here https://www.freecodecamp.org/news/sql-join-types-inner-join-vs-outer-join-example/#:~:text=The biggest difference between an,table in the resulting table.

# <div class="alert alert-info"> <b>Student comments:</b> I believe that fixed it!</div>

# <div class="alert alert-success">
# <b>Reviewer's comment v2:</b>
# 
# Indeed `how=outer` is a correct way of keeping all data. 

# In[50]:


# Add the plan information
usage = usage.merge(users[['user_id', 'plan']], how='outer', on='user_id')
usage = usage.fillna(0)
usage


# In[27]:


usage_plan_limits = usage.merge(plans, left_on='plan', right_on='plan_name', how='left')
usage_plan_limits


# <span style="font-weight: bold; font-style: italic; color: blue">Now that there is a merged table with usage and plan information for all of the users in the sample, monthly revenue can be calculated.</span>

# In[28]:


# Calculate the monthly revenue for each user
def monthly_rev(row, plans):
    
    revenue = 0
    
    plan = row['plan']
    total_mins = row['billed_duration']
    total_msgs = row['total_msgs']
    total_internet = row['gb_billed']
    
    plan_data = plans[plans['plan_name'] == plan].iloc[0]
    
    calls_diff = max(0, total_mins - plan_data['minutes_included'])
    msgs_diff = max(0, total_msgs - plan_data['messages_included'])
    internet_diff = max(0, total_internet - (plan_data['mb_per_month_included']/1024))
    
    revenue += calls_diff * plan_data['usd_per_minute']
    revenue += msgs_diff * plan_data['usd_per_message']
    revenue += internet_diff * plan_data['usd_per_gb']
    revenue += plan_data['usd_monthly_pay']
    
    return revenue

usage_plan_limits['monthly_revenue'] = usage_plan_limits.apply(monthly_rev, axis=1, args=(plans,)).round(2)
usage_plan_limits


# <div class="alert alert-danger">
# <b>Reviewer's comment v1:</b>
# 
# Results will be different due to missing rounding for calls and internet; however overall logic is correct. 

# <div class="alert alert-info"> <b>Student comments:</b> I believe that fixed it!</div>

# <div class="alert alert-success" role="alert">
# <b>Reviewer's comment v2:</b>
# 
# Everything is correct now. 
# 
# Btw it is also possible to make the calculation of revenue a little bit shorter / easier using np.where - https://numpy.org/doc/stable/reference/generated/numpy.where.html
#     
# ```
# np.where ('condition: if exceeding the package limit', 'multiply the difference by the price of additional services', '0')
# ```
# 
#     
# Great thing about python is that there are so many libraries and ready-to-use functions. For example, this task can also be solved using `.clip()` (a useful method in many tasks). You can read it here: https://www.pythonpool.com/numpy-clip/

# <span style="font-weight: bold; font-style: italic; color: blue">We now have calculations for the total revenue earned per month from each customer.</span>

# ## Study user behaviour

# ### Calls

# In[29]:


# Compare average duration of calls per each plan per each distinct month. Plot a bar plat to visualize it.
calls_dur_mandp = usage.groupby(['plan', 'month'])['billed_duration'].mean('billed_duration').reset_index()
calls_dur_mandp_pivot = calls_dur_mandp.pivot(index='month', columns='plan', values='billed_duration')
calls_dur_mandp_pivot.plot(kind='bar',
                     title='Average Monthly Billed Call Duration per Plan', 
                     xlabel='Month', 
                     ylabel='Average Billed Call Duration (Minutes)', figsize=[12, 5])
plt.legend(['Surf', 'Ultimate'])
plt.show()


# In[30]:


calls_dur_mandp_pivot


# In[31]:


# Compare the number of minutes users of each plan require each month. Plot a histogram.
calls_dur_mandp_pivot['surf'].plot(kind='hist', 
                                   bins=12, 
                                   title='Average Number of Minutes per Plan', 
                                   alpha=0.5)
calls_dur_mandp_pivot['ultimate'].plot(kind='hist', 
                                       bins=12, 
                                       alpha=0.5)
plt.xlabel('Minutes')
plt.ylabel('Number of Months')
plt.legend()
plt.show()


# In[32]:


# Calculate the mean and the variance of the monthly call duration
surf_calls_dur_avg = calls_dur_mandp_pivot['surf'].mean()
ultm_calls_dur_avg = calls_dur_mandp_pivot['ultimate'].mean()
surf_calls_dur_var = np.var(calls_dur_mandp_pivot['surf'])
ultm_calls_dur_var = np.var(calls_dur_mandp_pivot['ultimate'])
print(f'The mean for Surf plans is {surf_calls_dur_avg}.')
print(f'The mean for Ultimate plans is {ultm_calls_dur_avg}.')
print(f'The variance for Surf plans is {surf_calls_dur_var}.')
print(f'The variance for Ultimate plans is {ultm_calls_dur_var}.')


# In[33]:


# Plot a boxplot to visualize the distribution of the monthly call duration
calls_dur_mandp['billed_duration'].plot(kind='box')
plt.title('Distribution of Monthly Billed Call Duration')
plt.ylabel('Minutes')
plt.show()


# <span style="font-weight: bold; font-style: italic; color: blue">Overall, users of both plans have similar call activity.  Ultimate plan users' call duration varies more greatly than Surf plan users; this makes sense, given Ultimate plan users receive 3000 minutes as part of their plan.  However, users of both plans average around 385 minutes per month, which is within the limits of the lower-cost Surf plan.</span>

# <div class="alert alert-warning">
# <b>Reviewer's comment v1:</b>
#     
# To avoid repetitive code you could utilize functions. 

# <div class="alert alert-info"> <b>Student comments:</b> For sure!  I honestly just found for this small of an operation, it was quicker to copy and paste.  :)</div>

# ### Messages

# In[34]:


# Compare the number of messages users of each plan tend to send each month
msgs_sent_mandp = usage.groupby(['plan', 'month'])['total_msgs'].mean('total_msgs').reset_index()
msgs_sent_mandp_pivot = msgs_sent_mandp.pivot(index='month', columns='plan', values='total_msgs')
msgs_sent_mandp_pivot.plot(kind='bar', 
                           title='Average Messages Sent per Plan', 
                           xlabel='Month', 
                           ylabel='Average Messages', 
                           figsize=[12, 5])
plt.legend(['Surf', 'Ultimate'])
plt.show()


# In[35]:


msgs_sent_mandp_pivot


# In[36]:


#Calculating mean and variance for each plan
surf_msgs_sent_avg = msgs_sent_mandp_pivot['surf'].mean()
ultm_msgs_sent_avg = msgs_sent_mandp_pivot['ultimate'].mean()
surf_msgs_sent_var = np.var(msgs_sent_mandp_pivot['surf'])
ultm_msgs_sent_var = np.var(msgs_sent_mandp_pivot['ultimate'])
print(f'The mean for Surf plans is {surf_msgs_sent_avg}.')
print(f'The mean for Ultimate plans is {ultm_msgs_sent_avg}.')
print(f'The variance for Surf plans is {surf_msgs_sent_var}.')
print(f'The variance for Ultimate plans is {ultm_msgs_sent_avg}.')


# <span style="font-weight: bold; font-style: italic; color: blue">On average, Ultimate plan users send only slightly more messages per month than Surf plan users, despite being allotted significantly more messages per month.  Although Surf plan users average fewer texts per month, the number of messages they send varies more dramatically from month to month, while Ultimate plan users are more consistent in their average number of messages sent.  This indicates that some Surf users are regularly incurring overage fees for sending text messages above their plan's limit of 50 messages per month.</span>

# ### Internet

# In[37]:


# Compare the amount of internet traffic consumed by users per plan
web_use_mandp = usage.groupby(['plan', 'month'])['gb_billed'].mean('gb_billed').reset_index()
web_use_mandp_pivot = web_use_mandp.pivot(index='month', columns='plan', values='gb_billed')
web_use_mandp_pivot.plot(kind='bar', 
                         title='Average Internet Use (GB) Billed per Month', 
                         xlabel='Month', 
                         ylabel='Average Usage Bulled (in GB)', 
                         figsize=[12,5])
plt.legend(['Surf', 'Ultimate'])
plt.show()


# In[38]:


web_use_mandp_pivot


# In[39]:


#Calculating mean and variance for each plan
surf_web_use_avg = web_use_mandp_pivot['surf'].mean()
ultm_web_use_avg = web_use_mandp_pivot['ultimate'].mean()
surf_web_use_var = np.var(web_use_mandp_pivot['surf'])
ultm_web_use_var = np.var(web_use_mandp_pivot['ultimate'])
print(f'The mean for Surf plans is {surf_web_use_avg}.')
print(f'The mean for Ultimate plans is {ultm_web_use_avg}.')
print(f'The variance for Surf plans is {surf_web_use_var}.')
print(f'The variance for Ultimate plans is {ultm_web_use_var}.')


# <span style="font-weight: bold; font-style: italic; color: blue">On average, Ultimate plan users use more MB of internet than Surf users.  However, Ultimate plan users, in general, stay well within the limits of their plan's internet allotment (30,720mb).  Surf plan users use fewer MB of internet, but their average annual usage is within the limits of their plan (15,360mb).  However, for 7 out of 12 months, the average usage of Surf plan users exceeded that limit, generating additional revenue for Megaline.</span>

# ## Revenue

# In[40]:


plan_revenue = usage_plan_limits.groupby(['plan', 'month'])['monthly_revenue'].mean('monthly_revenue').reset_index()
plan_revenue_pivot = plan_revenue.pivot(index='month', columns='plan', values='monthly_revenue')
plan_revenue_pivot.plot(kind='bar', 
                        title='Monthly Revenue per Plan', 
                        xlabel='Month', 
                        ylabel='Revenue (USD)', 
                        figsize=[12, 5])
plt.legend(['Surf', 'Ultimate'])
plt.show()


# In[41]:


plan_revenue_pivot['extra_rev_surf'] = plan_revenue_pivot['surf'] - 20
plan_revenue_pivot['extra_rev_ultm'] = plan_revenue_pivot['ultimate'] - 70
plan_revenue_pivot


# In[42]:


plan_revenue_pivot[['extra_rev_surf', 'extra_rev_ultm']].plot(kind='bar', 
                                              title='Extra Monthly Revenue per Plan', 
                                              xlabel='Month', 
                                              ylabel='Revenue (USD)', 
                                              figsize=[12, 5])
plt.legend(['Surf', 'Ultimate'])
plt.show()


# In[43]:


surf_plan_revenue_avg = plan_revenue_pivot['surf'].mean()
xtra_surf_rev_avg = plan_revenue_pivot['extra_rev_surf'].mean()
ultm_plan_revenue_avg = plan_revenue_pivot['ultimate'].mean()
xtra_ultm_rev_avg = plan_revenue_pivot['extra_rev_ultm'].mean()

surf_plan_revenue_var = np.var(plan_revenue_pivot['surf'])
xtra_surf_rev_var = np.var(plan_revenue_pivot['extra_rev_surf'])
ultm_plan_revenue_var = np.var(plan_revenue_pivot['ultimate'])
xtra_ultm_rev_var = np.var(plan_revenue_pivot['extra_rev_ultm'])

print(f'The mean for Surf plans is {surf_plan_revenue_avg}, and the mean for extra revenue is {xtra_surf_rev_avg}. The mean for Ultimate plans is {ultm_plan_revenue_avg}, and the mean for extra revenue is {xtra_ultm_rev_avg}.')
print(f'The variance for Surf plans is {surf_plan_revenue_var}, and the variance for extra revenue is {xtra_surf_rev_var}. The variance for Ultimate plans is {ultm_plan_revenue_var}, and the variance for extra revenue is {xtra_ultm_rev_var}.')


# <span style="font-weight: bold; font-style: italic; color: blue">Overall, Surf plan users generate more revenue for the company: on average, 237.92 per month.  They frequently incur overage fees: the average amount of extra fees collected above their plan cost is 217.92 per month and the variance is high, suggesting that some customers incur many more fees while others incur far fewer.  On average, Ultimate plan users generate less revenue (157.80) and a smaller amount of extra fees (87.80) per month.  The variance is fairly low, so users typically stay close to the average.</span>

# <div class="alert alert-success">
# <b>Reviewer's comment v1:</b>
#     
# - I will write overall thoughts about the data analysis section:
# - Very nice visualisation of the data. Great that you combined both plans on one graph for the comparison and also used different graph types to check available data.
# -  If you have time and willing to practice, you can display two charts (histogram and a boxplot) using a two-column subplot.
# 
# ```
#     # Create one row with 2 columns
# 	  fig, axes = plt.subplots(1, 2, figsize=(16, 5))
# 
# 	  # Create a histogram for the surf plan
# 	  sns.distplot(... ax=axes[0])
# 	  # Create a histogram for the second plan
# 	  sns.distplot(... ax=axes[0])
# 	
# 	  # Create a boxplot for both plans
# 	  sns.boxplot(... ax=axes[1])
# ```

#  

# ## Test statistical hypotheses

# <span style="font-weight: bold; font-style: italic; color: blue">This project will determine which plan generates more revenue to help the commercial department adjust their advertising budget.  Does the average revenue of users of these calling plans differ?</span>

# <span style="font-weight: bold; font-style: italic; color: blue">The null hypothesis is that the plans generate the same or a very similar amount of revenue.  The alternative hypothesis is that one plan generates more revenue than the other plan.  Having already calculated average revenue, a ttest can be performed to compare the means of each group.  The alpha value will be 0.05 to ensure any differences are significant enough to justify recommending that the commercial department adjust their budget.</span>

# In[44]:


# Test the hypotheses
alpha = 0.05
results_all = st.ttest_ind(plan_revenue_pivot['surf'], plan_revenue_pivot['ultimate'])
print(f'p-value: {results_all.pvalue}')
if results_all.pvalue < alpha:
    print('We reject the null hypothesis.')
else:
    print('We cannot reject the null hypothesis.')


# <span style="font-weight: bold; font-style: italic; color: blue">Given revenue may vary between regions and advertisements may only need to be adjusted in specific areas, a test of the NY-NJ area--as a primarily urban area--in comparison to other regions may reveal if there are differences in regional usage that should be accounted for.</span>

# <span style="font-weight: bold; font-style: italic; color: blue">The null hypothesis is that NY-NJ users generate the same or a very similar amount of revenue to users in other parts of the country.  The alternative hypothesis is that NY-NJ users generate a significantly different amount of revenue.  Having already calculated average revenue, a ttest can be performed to compare the means of each group.  The alpha value will be 0.05 to ensure any differences are significant enough to justify recommending that the commercial department adjust their budget.</span>

# In[45]:


users_nynj = usage_plan_limits.merge(users[users['city'].str.contains('NY-NJ')], how='inner', on='user_id')
notnynj = ~users['city'].str.contains('NY-NJ')
users_other = usage_plan_limits.merge(users[notnynj], how='inner', on='user_id')
users_other


# In[46]:


users_nynj_rev_avg = users_nynj['monthly_revenue'].mean()
users_other_rev_avg = users_other['monthly_revenue'].mean()
print(f'The average monthly revenue from customers in NY-NJ is {users_nynj_rev_avg}.')
print(f'The average monthly revenue from customers in other areas is {users_other_rev_avg}.')


# In[47]:


# Test the hypotheses
alpha = 0.05
results_nynj = st.ttest_ind(users_nynj['monthly_revenue'], users_other['monthly_revenue'])
print(f'p-value: {results_nynj.pvalue}')
if results_all.pvalue < alpha:
    print('We reject the null hypothesis.')
else:
    print('We cannot reject the null hypothesis.')


# <span style="font-weight: bold; font-style: italic; color: blue">This preliminary inquiry indicates that there are regional differences that should be accounted for in determining the marketing budget.</span>

# <div class="alert alert-success">
# <b>Reviewer's comment v1:</b>
#     
# - Everything is correct. Hypotheses have been formulated correctly, however, by default the alternative hypothesis states only a difference between two groups, as we don't know at this point which one is bigger or smaller. 
#     
# - Your conclusions based on the results are also correct. 
#    
# - Additionally, you can compare the variances of the samples before testing hypotheses to understand which equal_var parameter to use with the t-test_ind test method (by default, True). Here, you can manually calculate variances or use Levene's statistic test (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html) or Bartlett's test (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bartlett.html).   

# <div class="alert alert-info"> <b>Student comments:</b> Thanks for the resources and the correction on writing alternative hypotheses... still getting the hang of that!</div>

# <div class="alert alert-success" role="alert">
# <b>Reviewer's comment v2:</b>
#     
# No problem at all! Glad that smth was useful.

# ## General conclusion
# <span style="font-weight: bold; font-style: italic; color: blue">This project set out to determine whether the Surf or the Ultimate plan earned more revenue for Megaline so that the commercial budget could be adjusted.  As noted previously, these conclusions are a starting point in determining which plan generates more revenue.</span>

# <span style="font-weight: bold; font-style: italic; color: blue">This project relied on several Python libraries including pandas, numpy, pyplot, factorial, and stats to analyze data from five different datasets: call data, internet usage, message data, plan information, and user information. After loading and preprocessing the data, including handling data types, fixing inconsistencies, I aggregated the information to simplify further analysis.  There was no need to enrich the data to draw the conclusions needed for this project.</span>

# <span style="font-weight: bold; font-style: italic; color: blue">On average, users of both plans exhibited similar call activity, with Ultimate plan users showing more variation in call duration due to their higher plan limits. However, Ultimate plan users sent only slightly more messages per month despite having a significantly higher message allowance, while some Surf plan users regularly exceeded their message limit, incurring overage fees.  Additionally, I found that Ultimate plan users generally stayed well within their internet usage limit, while Surf plan users often exceeded their data allotment, resulting in additional revenue for the company.</span>

# <span style="font-weight: bold; font-style: italic; color: blue">In terms of revenue, Surf plan users generate more revenue on average due to the overage fees they regularly incur.  Therefore, the advertising department should focus commercials on the Surf plan as it generates the most revenue due to these overage fees.  As for regional differences, I compared the average revenue of users in the NY-NJ area to those in other regions. The results indicated significant regional variations, suggesting the need for further analysis to determine where adjustments in the marketing budget should be made to account for these differences.</span>

# <div class="alert alert-success" role="alert">
# <b>Reviewer's comment v1:</b>
#     
# - Overall you conducted great research with correct interim findings, clean code and nice visualisation.
# - I also like your overall conclusions. It is very structured and provides insights about what you accomplished and recommendations to the business.
#     

# <div class="alert alert-info"> <b>Student comments:</b> Thank you for reviewing my project!  I think I corrected everything, but please let me know if any further changes are needed.  :)</div>

# <div class="alert alert-success" role="alert">
# <b>Reviewer's comment v2:</b>
#     
#  👏
