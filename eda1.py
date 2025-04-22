import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fifa_eda.csv')[:200]

#EDA
df.head()

df.info()

df.shape

df.describe()

df.isna().sum

#correlation
correlation = df[['Age','Wage','Value','International Reputation']].corr()

print(correlation)