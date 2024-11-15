import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/Jameel/Downloads/WHO-COVID-19-global-data.csv') #we have to put .csv at last
print(df.head(10))

print("\nRemoving Country_code column from data set :\n")
df2=df.drop(['Country_code'],axis=1) #axis=1 means its column and inplace = true means make changes in orginal dataset
print(df2.head(10))  #if we dont use inplace=true then write df=df.drop...

print("\nRemoving WHO_region column from data set :\n")
df2.drop(['WHO_region'],axis=1,inplace=True)
print(df2.head(10)) 
countries=df2['Country'].unique()
print("\nThe description of total data is :\n")
print(df2.describe())

print(f"\nThe Total Number of countries in the data set are :",len(countries))


print("\nThe graphs of whole World is :\n ")
df3 = df2.groupby('Date_reported', as_index=False)[['New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']].sum()
c=df3
plt.scatter(np.arange(0,len(c)),c['New_cases'],color='blue',label='New_cases',s=1) #s is used to decrease thickness of graph lines
plt.scatter(np.arange(0,len(c)),c['New_deaths'],color='red',label='New_deaths',s=1)
plt.scatter(np.arange(0,len(c)),c['Cumulative_deaths'],color='yellow',label='Cumulative_deaths',s=1)
plt.scatter(np.arange(0,len(c)),c['Cumulative_cases'],color='green',label='Cumulative_cases',s=1)
plt.title("World data ")
plt.xlabel("No of days")
plt.ylabel("No of cases")
plt.legend()
plt.show()

print("\nThe graphs of all countries are :\n")
for i in range(0,len(countries)):
    c=df2[df2['Country']==countries[i]].reset_index()
    plt.scatter(np.arange(0,len(c)),c['New_cases'],color='blue',label='New_cases',s=1) #s is used to decrease thickness of graph lines
    plt.scatter(np.arange(0,len(c)),c['New_deaths'],color='red',label='New_deaths',s=1)
    plt.scatter(np.arange(0,len(c)),c['Cumulative_deaths'],color='yellow',label='Cumulative_deaths',s=1)
    plt.scatter(np.arange(0,len(c)),c['Cumulative_cases'],color='green',label='Cumulative_cases',s=1)
    plt.title(countries[i])
    plt.xlabel("No of days")
    plt.ylabel("No of cases")
    plt.legend()
    plt.show()

