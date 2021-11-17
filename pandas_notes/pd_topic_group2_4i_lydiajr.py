# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Topic Title](#Topic-Title) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide. 

#!/usr/bin/env python
# coding: utf-8

# + [Timedeltas: Representing changes in time](#Topic-Title)
# *Lydia Rogers*, lydiajr@umich.edu
# 
# Reference for timedeltas can be found [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html)

# ## Intro to Timedeltas
# * In addition to the datetime functionality that works well with pandas, there are occasions where we will want to analyze changes in time rather than dates.
# * We can represent these changes in time as timedeltas using the `datetime` module in addition to pandas.

# In[1]:


# Load required modules
import pandas as pd
import datetime

# Initializing timedeltas
# Can initialize using pd.Timedelta...
t1 = pd.Timedelta("2 days")
t2 = pd.Timedelta(2, unit = "d")
print(t1 == t2)

# null = NaT
t3 = pd.Timedelta("nan")
t4 = pd.Timedelta("nat")
print(t3, t4)

# negative times also supported
t5 = pd.Timedelta("-1us")
t6 = pd.Timedelta("-3hr")
print(t5, t6)


# ... or from a time string using to_timedelta
t7 = pd.to_timedelta("1 days 06:05:01.00003")
t8 = pd.to_timedelta("247ms")
print(t7, t8)


# ## Operations using timedeltas
# * Timedeltas can be used in arithmetic operations such as addition and subtraction with other timedeltas or datetimes, as well as in scalar multiplication. 
# * Other operations supported include minimum and maximum calculations, and absolute values. 
# * We can convert timedeltas to different scales (hours, minutes, seconds) by dividing one timedelta object by another. 

# In[2]:


# Create example dataframe
sundays = pd.Series(pd.date_range("2021-10-24", periods=6, freq="W"))
td = pd.Series([pd.Timedelta(days=i*7) for i in range(6)])
df = pd.DataFrame({"dates": sundays, "days": td})

# Timedelta arithmetic
df["new_date"] = df["dates"] + 2 * df["days"]
df["new_timedelta"] = df["dates"] - df["new_date"]
df["scaled_timedelta"] = df["new_timedelta"] * 0.4
df["seconds_timedelta"] = df["scaled_timedelta"] / pd.Timedelta(1, "s")
print(df)

# Additional operations
print("min:", df["new_date"].min())
print("max:", df["new_date"].max())
print(abs(df["new_timedelta"]))


# ## Summarizing Timedeltas
# * Timedeltas and datetimes are also supported by most reduction operations such as mean, median, quantile, and sum. 
# * These reduction operations, implemented in pandas, offer easy ways to summarize changes in time. 

# In[3]:


print("mean timedelta:", df["seconds_timedelta"].mean())
print("mean date:", df["new_date"].mean())

print("median timedelta:", df["seconds_timedelta"].median())
print("median date:", df["new_date"].median())

print("timedelta 75th quantile:", df["seconds_timedelta"].quantile(0.75))
print("date 75th quantile:", df["new_date"].quantile(0.75))

print("timedelta sum:", df["seconds_timedelta"].sum())

