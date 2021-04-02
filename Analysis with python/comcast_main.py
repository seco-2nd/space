#!/usr/bin/env python
# coding: utf-8

# # - Import data into Python environment.

# In[83]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"Z:\simp\PYTHON\comcast\Comcast_telecom_complaints_data.csv")
df.head()


# # - Provide the trend chart for the number of complaints at monthly and daily granularity levels.

# Monthly

# In[84]:


df["date_index"] = df["Date_month_year"] + " " + df["Time"]
df["date_index"] = pd.to_datetime(df["date_index"])
df["Date_month_year"] = pd.to_datetime(df["Date_month_year"])
df = df.set_index(df["date_index"])
df.groupby(pd.Grouper(freq="M")).size().plot()


# Daily

# In[85]:


df["Date_month_year"].value_counts().plot()


# # - Provide a table with the frequency of complaint types.

# In[121]:


import re 
Internet=sum(df['Customer Complaint'].str.count("internet", re.I))
Network=sum(df['Customer Complaint'].str.count("network", re.I))
Billing=sum(df['Customer Complaint'].str.count("bill", re.I))
Email=sum(df['Customer Complaint'].str.count("email", re.I))
Charges=sum(df['Customer Complaint'].str.count("charge", re.I))
Other=len(df)-dfn1['Charges issues']-dfn1['Email issues']-dfn1['Billing issues']-dfn1['Internet issues']
issues = {'Complaint types': ['Internet','Network','Billing','Email','Charges','Other'],
        'Count': [Internet,Network,Billing,Email,Charges,Other]
        }
dfd = pd.DataFrame(issues, columns = ['Complaint types','Count'])
dfd


# # Which complaint types are maximum i.e., around internet, network issues, or across any other domains.

# In[122]:


dfd.sort_values(by='Count',ascending=False).head(2).tail(1)


# # - Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed & Solved is to be categorized as Closed.

# In[124]:


df["newStatus"] = ["Open" if Status=="Open" or Status=="Pending" else "Closed" for Status in df["Status"]]
dfx = df.groupby(['State', 'newStatus'])['State'].count().reset_index(name='Value')
dfx.head()


# # - Provide state wise status of complaints in a stacked bar chart. Use the categorized variable from Q3.

# In[89]:


pivot_df = dfx.pivot(index='State', columns='newStatus', values='Value')
pivot_df.loc[:,['Closed','Open']].plot.bar(stacked=True,figsize=(16,8))


# # Which state has the maximum complaints

# In[90]:


df.groupby(["State"]).size().sort_values(ascending=False).to_frame().reset_index().rename({0: "Count"}, axis=1).head(1)


# # Which state has the highest percentage of unresolved complaints

# In[91]:


open=dfx[dfx['newStatus']=='Open']
closed=dfx[dfx['newStatus']=='Closed']
open=open.rename(columns={'Value':'Open'})
closed=closed.rename(columns={'Value':'Closed'})
total=pd.merge(open,closed,on='State')
total['Count']=total['Open']+total['Closed']
total=total.sort_values(by='Count',ascending=False)
total['Percentage of unresolved']=(total['Open']/total['Count'])*100
total.sort_values(by='Percentage of unresolved',ascending=False).head(1)


# # - Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls.

# In[126]:


complaints= df.groupby(['Received Via', 'newStatus'])['State'].count().reset_index(name='Value')
complaints_open=complaints[complaints['newStatus']=='Open']
complaints_closed=complaints[complaints['newStatus']=='Closed']
complaints_total=pd.merge(complaints_closed,complaints_open,on='Received Via')
complaints_total=complaints_total.rename(columns={'Value_x':'Closed','Value_y':'Open'})
complaints_total['Total_count']=complaints_total['Closed']+complaints_total['Open']
complaints_total.head()
complaints_total['Resolved %']=(complaints_total['Closed']/complaints_total['Total_count'])*100
complaints_total.head()

