import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("fifa_eda.csv")[:200]

df.head()
df.info()
df.shape
df.describe()
df.isna().sum()

categorical = []
numerical = []

for col in df.columns:
  if df[col].dtype == 'object':
    categorical.append(col)
  else:
    numerical.append(col)
    
for col in df.columns:
  print(col,df[col].nunique())
  print(col,df[col].value_counts())
  
correlation = df[['Age','Wage','Value','International Reputation']].corr()
print(correlation)

# height

print('height summary -->')
df['Height'].describe()
q1 = df['Height'].quantile(0.25)
q2 = df['Height'].quantile(0.5)
q3 = df['Height'].quantile(0.75)

iqr = q3 - q1
lowerbound = q1-1.5 * iqr
upperbound = q3 + 1.5 * iqr

print('lowerbound --> ',lowerbound)
print('upperbound --> ',upperbound)

# finding outlier

for height in df['Height']:
  if height < lowerbound or height > upperbound:
    print(height)
    
# Visualization
# player age distribution
sns.histplot(data=df['Age'],kde=True)
plt.title("Age distribution")
plt.show()

# distribution plot for all the numerical columns
for col in numerical:
  if col == 'ID': continue
  plt.figure(figsize=(10,8))
  sns.histplot(data=df[col],kde=True,color='red',bins=20)
  plt.title(f'{col} distribution')
  plt.show()
  
# value vs position
sns.boxplot(x=df['Position'],y=df['Value'])
plt.xticks(rotation=90)
plt.show()

# top 10 clubs with most players
top_clubs = df['Club'].value_counts().head(10)
top_clubs.plot(kind='bar')
plt.show()

# scatter --> age vs value
plt.scatter(x=df['Age'],y=df['Value'])
plt.show()

# pair plot
sns.pairplot(df[numerical[:5]])
plt.show()

# piechart
cols = ['Nationality','Club','Preferred Foot','Position']

for col in cols:
  distribution = df[col].value_counts().head(10)
  distribution.plot(kind='pie',labels=distribution.keys(),autopct="%1.1f%%")
  plt.title(f'{col} distribution')
  plt.show()
  
# heatmap
plt.figure(figsize=(10,8))
corrltn = df[['Age','Value','Wage']].corr()
sns.heatmap(corrltn,annot=True)
plt.show()

# stacked bar chart
nationality_position = pd.crosstab(df['Nationality'],df['Position']).head(10)
nationality_position.plot(kind='bar',stacked=True,colormap='coolwarm')
plt.xticks(rotation=90)
plt.show()