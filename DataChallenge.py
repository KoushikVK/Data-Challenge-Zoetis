# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:58:47 2022

@author: Koushik V
"""


# =============================================================================
#Cleaning the data for analysis  
#**Getting the data ready for analysis
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()




campaign = pd.read_excel("CUSTOMER_CAMPAIGN.xlsx")


##Concatinating two columns into one

campaign['CUSTOMER_NAME'] = campaign['CUSTOMER_FIRST_NAME'] + " " +campaign['CUSTOMER_LAST_NAME']


#removing first name and last name as it is not needed 


campaign.drop(['CUSTOMER_FIRST_NAME','CUSTOMER_LAST_NAME'],axis=1,inplace=True)


# =============================================================================
# Data cleaning sales data 
# =============================================================================


sales = pd.read_excel("CUSTOMER_SALES.xlsx")

#copying the data 

dfs = sales.copy()


#importing regex module

import re


##lowering the characters fro customer name column

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].str.lower()


##Checking for NA values of if any 


dfs.isna().sum()

campaign.isna().sum()



# removing the null terminating char at the end
dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].apply(lambda x : x[:-1])


#Checking if the column has any special characters

from string import printable

if set(dfs['CUSTOMER_NAME']).difference(printable):
    print('Text has special characters.')
else:
    print("Text hasn't special characters.")

##Copying for convenient purposes
dfscopy = dfs.copy()


##removing prefix 

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].replace(['dr\. ','fr\. ','ms\. ','mr\. ','prof\. ','miss','m.d','master'],'', regex=True)



#dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].replace(['mr','mrs\. ',' ph ','3r ',' b ',' i ','b.a','sir\. ',' ii ',' 2n ',' es ',' lord ',' davi ',],'', regex=True)


dfs= pd.read_excel("cleaned.xlsx")
dfscopy = dfs.copy()

#Remocing extra column that was created
dfs.drop('Unnamed: 0',axis=1,inplace=True)


dfs= pd.read_excel("cleaned.xlsx")  
    
##trimming white spaces in dataframe


def trim_all_columns(df):
    
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

    
trim_all_columns(dfs)    


##remove everything after '('

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].str.split('(').str[0]



##remove characters inside double quotes and single quotes

dfscopy=dfs.copy()    

##removes characters in double quotes
dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in [i for i in x.split(' ') if not i.startswith('"')] if not i.endswith('"')]) )

##single quotes
dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in [i for i in x.split(' ') if not i.startswith("'")] if not i.endswith("'")]) )


dfscopy=dfs.copy()    

dfs= dfscopy.copy()
##removing initials of customers


dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i.endswith('.')]) )


dfs.to_excel('cleaned.xlsx')


dfs= pd.read_excel("cleaned.xlsx")



##replace 0 as 'o' in few names 

dfs.drop('Unnamed: 0',axis=1,inplace=True)
dfs['CUSTOMER_NAME'].replace(to_replace = '0', value = 'o',inplace=True)

#dfs['CUSTOMER_NAME'].replace(to_replace = '$', value = 's',inplace=True)


dfs= pd.read_excel("cleaned.xlsx")


dfscopy=dfs.copy()  

##removing all other unwanted characters like   

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].replace([' 3r ','ph ',' es ','b\.eng ',],'', regex=True)

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'ph']) )

  
dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == '3r']) )

  
dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'es']) )

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'es']) )


dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == '2n']) )


dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'b']) )

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'ii']) )

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'snr']) )


dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'esq']) )

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'wals']) )

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'mr']) )

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'bs']) )

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'jn']) )


dfscopy=dfs.copy()  



dfs = pd.read_excel('cleaned.xlsx')


df= campaign.copy()

##trimming customer_name

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].apply(lambda x: x.strip())


df = pd.merge(campaign,dfs,how='inner',on='CUSTOMER_NAME')

dfs.to_excel('cleaned.xlsx')

dfscopy=dfs.copy()  


result = [i.split(' ') for i in dfs['CUSTOMER_NAME'] if len(i)]




dfs = pd.read_excel('cleaned.xlsx')

##After removing '.' from initials , initials were still present so removing them 

dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ') if not len(i) == 1]) )


##removing special characters  and other characters 


dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'jnr']) )


dfs['CUSTOMER_NAME'] = dfs['CUSTOMER_NAME'].map(lambda x: ' '.join([i for i in x.split(' ')  if not i == 'davi']) )

dfscopy=dfs.copy()  

dfs= dfscopy.copy()



#removing comma
dfs['CUSTOMER_NAME']= dfs['CUSTOMER_NAME'].replace(",",' ')




##sorting the columns based upon customer name

dfs.sort_values(by='CUSTOMER_NAME', inplace=True, ascending=True)

dfs.drop('Unnamed: 0',axis=1,inplace=True)

##replacing names of few customers
dfs['CUSTOMER_NAME']= dfs['CUSTOMER_NAME'].replace("yuleetuck",'yule etuck')

dfs['CUSTOMER_NAME']= dfs['CUSTOMER_NAME'].replace("wilfred ah",'wilfrid ahmed')


dfs['CUSTOMER_NAME']= dfs['CUSTOMER_NAME'].replace('elva janse nee gubne','elva janse')


dfs.to_excel('cleaned.xlsx')

campaign['CUSTOMER_NAME'] = campaign['CUSTOMER_NAME'].str.lower()


# =============================================================================
# Here i am sorting the datasets by customer names so that they match the same in the next column and 
#outer join them so that i can compare them 
# =============================================================================


#campaign.sort_values(by='CUSTOMER_NAME_CAMPAIGN', inplace=True, ascending=True)

##join both datasets
#df = pd.merge(campaign,dfs,how='outer',left_on='CUSTOMER_NAME_CAMPAIGN',right_on='CUSTOMER_NAME')

df =pd.read_excel('cleaned.xlsx')


##after sorting the customer_name_campaign column in campaign dataset 

df_campaign_name_only = campaign['CUSTOMER_NAME']

##changing the name of the dataset column to some other name
df_campaign_name_only.rename({'CUSTOMER_NAME':'CUSTOMER_NAME_CAMPAIGN'},axis=1,inplace =True)
pd.DataFrame(df_campaign_name_only)


# =============================================================================
# Now i have successfully cleaned the dataset now lets compare the names of both the customer names 
# =============================================================================

##using np.where see if the name is present in campaign name else replace it with 
#the name as in campaign name

# ==========================================================================================================
# like if the name is crist ronaldo in sales and if it is cristiano ronaldo in campaign then replace it with cristiano ronaldo
# ================================================================================================

df1= df.copy()

##
#df.sort_values(by='CUSTOMER_NAME', inplace=True, ascending=True)



##to eliminate misspelling of names we are doing this
df['CUSTOMER_NAME'] = np.where(df['CUSTOMER_NAME'] == df['CUSTOMER_NAME_CAMPAIGN'],df['CUSTOMER_NAME'],df['CUSTOMER_NAME_CAMPAIGN'] )

##checking fro null values in the dataframe
df.isnull().sum()

# =============================================================================
# Out[78]: 
# =============================================================================
# CUSTOMER_NAME_CAMPAIGN                0
# CUSTOMER_NAME                         0
# SALES_SCHEME_CODE                     0
# SALES_STRATEGY_TYPE                   0
# MARITAL_STATUS                        0
# DAYS_SINCE_CUSTOMER_ENGAGEMENT        0
# REG_DATE                              0
# START_DATE                            0
# OCC_CODE                              0
# TOTAL_HOUSEHOLD_ANNUAL_EXPENDITURE    0
# GROCERY_WEEKLY_SPENDING               0
# TOTAL_EXPENDATURE_TO_DATE             0
# NO_ITEMS_PURCHASED                    0
# WEEKLY_FUEL_EXPENDATURE               0
# SALES_CALL_STATUS                     0
# STORES_VISITED                        0
# LOYALTY_CARD_STATUS                   0
# LOYALTY_GIFT_SENT                     0
# dtype: int64
# =============================================================================
# =============================================================================

df.to_excel('cleaned.xlsx')

#now that we cleaned the data lets join campaign and sales


df1= pd.merge(campaign,df,how='inner',on='CUSTOMER_NAME')


df1.isnull().sum()

# =============================================================================
# Out[98]:There are no null values thankfully
# =============================================================================
# CUSTOMER_NUMBER_x                     0
# DATE_OF_BIRTH_x                       0
# GENDER_x                              0
# STREET_ADDRESS_x                      0
# COUNTRY_x                             0
# SALE_x                                0
# CUSTOMER_NAME                         0
# CUSTOMER_NAME_CAMPAIGN                0
# SALES_SCHEME_CODE                     0
# SALES_STRATEGY_TYPE                   0
# MARITAL_STATUS                        0
# DAYS_SINCE_CUSTOMER_ENGAGEMENT        0
# REG_DATE                              0
# START_DATE                            0
# OCC_CODE                              0
# TOTAL_HOUSEHOLD_ANNUAL_EXPENDITURE    0
# GROCERY_WEEKLY_SPENDING               0
# TOTAL_EXPENDATURE_TO_DATE             0
# NO_ITEMS_PURCHASED                    0
# WEEKLY_FUEL_EXPENDATURE               0
# SALES_CALL_STATUS                     0
# STORES_VISITED                        0
# LOYALTY_CARD_STATUS                   0
# LOYALTY_GIFT_SENT                     0
# CUSTOMER_NUMBER_y                     0
# DATE_OF_BIRTH_y                       0
# GENDER_y                              0
# STREET_ADDRESS_y                      0
# COUNTRY_y                             0
# SALE_y                                0
# dtype: int64
# =============================================================================
# =============================================================================



df= df1.copy()
#see if there are any duplicates 

df[df['CUSTOMER_NAME'].duplicated() == True]



# =============================================================================
# Out[102]: 
#Empty DataFrame
# =============================================================================

#There are no duplicates in our data set and its perfectly cleaned for analysis


# =============================================================================
# I choose to eliminate one customer name column
# =============================================================================


df.drop('CUSTOMER_NAME_CAMPAIGN',axis=1,inplace=True)


##Final dataset 


df.to_excel('finaldata.xlsx')






