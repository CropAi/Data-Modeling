<h1><strong>Exploratory Data Analysis (EDA Analysis)</strong></h1>

Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.


<h1>EDA explained using sample Data set:</h1>
<h3>Importing libraries</h3>

```
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import missingno
%matplotlib inline
```
<h3>Read data</h3>

```
df=pd.read_csv("file.csv)
```

<h3>Study data</h3>

```
df.info()
df.head()
df.describe()
df.shape()
```

<h3>Visualize data</h3>

```
sns.scatterplot(x='parameter',y='parameter',data=df)
g = sns.relplot(x="parameter", y="parameter", kind="line", data=df)
g.fig.autofmt_xdate()
age_vs_hours_per_week = sns.relplot(x="parameter", y="parameter", kind="line",sort=False, data=df)
sns.catplot(x="parameter",y="parameter",data=df)
```


