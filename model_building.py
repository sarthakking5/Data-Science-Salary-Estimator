# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:35:56 2023

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('eda1_data.csv')
#df1=pd.read_csv('eda_data.csv')
#choose relevant columns
df.columns

# #df_model=df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','competitors_cnt','hourly','emp_provided',
#            #'job_state','same_state','age','python','spark','aws','job_simp','seniority','sql','excel','rstudio']]

# df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','num_comp','hourly','employer_provided',
#              'job_state','same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]
# #get dummy data
# df_dum=pd.get_dummies(df_model)

# # train test split 
# from sklearn.model_selection import train_test_split

# X = df_dum.drop('avg_salary', axis =1)
# y = df_dum.avg_salary.values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # multiple linear regression 
# import statsmodels.api as sm

# X_sm = X = sm.add_constant(X)
# model = sm.OLS(y.astype(float),X_sm.astype(float))
# model.fit().summary()

df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','num_comp','hourly','employer_provided',
             'job_state','same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]

# get dummy data 
df_dum = pd.get_dummies(df_model)

# train test split 
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis =1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression 
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y.astype(float),X_sm.astype(float))
model.fit().summary()



#lasso regression
#random forest
#tune models using GridsearchCV