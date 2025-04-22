import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fifa_eda.csv')[:200]

#EDA
print(df.head())

print(df.info())

print(df.shape)

print(df.describe())

print(df.isna().sum)

#correlation
correlation = df[['Age','Wage','Value','International Reputation']].corr()

print(correlation)
