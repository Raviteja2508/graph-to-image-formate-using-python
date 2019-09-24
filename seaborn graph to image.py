# -*- coding: utf-8 -*-
"""


@author: raviteja
"""
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# Example 1 
df = sns.load_dataset('iris')
df
sns.plot = sns.pairplot(df, hue='species', size = 2.5)
sns.plot.savefig("C:\\Users\\ravi\\Desktop\\INDRAS ACADEMY\\phyton programming\\output4.png")


# Example 2 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


train = pd.read_csv("C:\\Users\\ravi\Desktop\\INDRAS ACADEMY\\phyton programming\\titanic_train.csv")
train.head()

sns.set_style('whitegrid')
df=sns.countplot(x='Survived',data=train,palette='RdBu_r')

fig = df.get_figure()
fig.savefig("C:\\Users\\ravi\\Desktop\\INDRAS ACADEMY\\phyton programming\\output6.png")
