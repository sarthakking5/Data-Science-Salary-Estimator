import pandas as pd

df=pd.read_csv('glassdoor_jobs.csv')

df1=df[df['Salary Estimate']!='-1']
df1
print(df.shape)
#Cleaning Salary Estimate
salary=df1['Salary Estimate'].apply(lambda x: x.split('(')[0])
rd_sign=salary.apply(lambda x: x.replace('$','').replace('K',''))

df1['hourly']=df1['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

df1['emp_provided']=df1['Salary Estimate'].apply(lambda x:1 if 'employer provided salary' in x.lower() else 0)
min_hr_sal=rd_sign.apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))

df1['min_salary']=min_hr_sal.apply(lambda x : int(x.split('-')[0]))
df1['max_salary']=min_hr_sal.apply(lambda x : int(x.split('-')[1]))

df1['avg_salary']=(df1.min_salary+df1.max_salary)/2
#Company Name
df1['company_txt']=df1.apply(lambda x: x['Company Name']if x['Rating']<0 else x['Company Name'][:-3],axis=1)
#State Name

df1['job_state']=df1['Location'].apply(lambda x:x.split(',')[1])
state_count2=df1.job_state.value_counts()

#if job is at the headquaters
df1['same_state']=df1.apply(lambda x: 1 if x.Location == x.Headquarters else 0,axis=1)
df1['age']=df1.Founded.apply(lambda x: x if x<1 else 2023 - x)

#parsing the job description
df1['python']=df1['Job Description'].apply(lambda x:1 if 'python'in x.lower() else 0)

df1['sql']=df1['Job Description'].apply(lambda x:1 if 'sql'in x.lower() else 0)

df1['excel']=df1['Job Description'].apply(lambda x:1 if 'excel'in x.lower() else 0)

df1['spark']=df1['Job Description'].apply(lambda x:1 if 'spark'in x.lower() else 0)

df1['rstudio']=df1['Job Description'].apply(lambda x:1 if 'r-studio'or 'r studio' in x.lower() else 0)

df1['aws']=df1['Job Description'].apply(lambda x:1 if 'aws'in x.lower() else 0)

df_out=df1.drop(['Unnamed: 0'],axis=1)

df_out.to_csv('salary_data_cleaned.csv',index=False)

df2=pd.read_csv('salary_data_cleaned.csv')