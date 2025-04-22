import matplotlib.pyplot as plt
import seaborn as sns
data = [[10,20,30],[40,60,21],[54,62,79]]
sns.heatmap(data,annot=True)
plt.title("heatmap")
plt.show()


# Stem Plot
import matplotlib.pyplot as plt 
import seaborn as sns

plt.stem([10,20,30],[40,60,21])
plt.title("stem plot")
plt.show()

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[7,8,9,10])
plt.title("line plot")
plt.show()

import matplotlib.pyplot as plt
data = [10,20,30,40]
beta = ['a','b','c','d']
plt.pie(data,labels=beta)
plt.title("pie plot")
plt.show()

import matplotlib.pyplot as plt
data =  [10,20,30,40,60,21,54,62,79,80]
plt.boxplot(data)
plt.title("boxplot")
plt.show()

import matplotlib.pyplot as plt
plt.bar(['A','B','C','D'],[7,8,9,10])
plt.title("bar plot")
plt.show()