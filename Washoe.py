#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[32]:


# Load data to dataframes
df_stops = pd.read_csv('stops.txt')
df_trips = pd.read_csv('trips.txt')
df_stoptimes = pd.read_csv('stop_times.txt')
df_routes = pd.read_csv('routes.txt')


# In[42]:


# Join stoptimes to trips to get route id
df_trip_stops =  df_stoptimes.join(df_trips.set_index('trip_id'), 
                                   on = 'trip_id', 
                                   how = 'left')[['trip_id','arrival_time','departure_time','stop_id','stop_sequence','route_id']]


# In[43]:


# Join df to routes to obtain route short name
df_trip_stops = df_trip_stops.merge(df_routes, 
                                    on = 'route_id', 
                                    how = 'left')[['trip_id','arrival_time','departure_time','stop_id','stop_sequence','route_id','route_short_name']]


# In[45]:


# Create a dummy value with next stop sequence id
df_trip_stops['next_stop_seq'] = df_trip_stops['stop_sequence']+1


# In[62]:


# Join again to stoptimes to get the next stop id
df_trip_stops['next_stop_id'] = df_trip_stops.merge(df_stoptimes, 
                         left_on  = ['trip_id','next_stop_seq'], 
                         right_on = ['trip_id','stop_sequence'], 
                         how = 'left')[['stop_id_y']]


# In[64]:


# present only relevant columns 
df_format = df_trip_stops[['trip_id','route_id','route_short_name','stop_id','next_stop_id','departure_time','arrival_time']]


# In[65]:


# print output
df_format

