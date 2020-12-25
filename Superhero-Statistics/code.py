# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
print(data.head())

# Code starts here
# Step-1
data['Gender'].replace({'-':'Agender'}, inplace=True)
data['Gender'].value_counts()

data['Gender'].value_counts().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Step-2
data['Alignment'].value_counts().plot(kind='bar')
plt.xlabel('Alignment')
plt.ylabel('Count')
plt.show()

# Step-3
data['Combat'].plot(kind='kde')
data['Strength'].plot(kind='kde')
data['Intelligence'].plot(kind='kde')
plt.legend()

newdf1 = data[['Combat', 'Intelligence']]
newdf2 = data[['Combat', 'Strength']]

# Pearson Correlation

covariance = newdf2.cov().loc['Combat', 'Strength']
std_Combat = newdf2['Combat'].std()
std_Strength = newdf2['Strength'].std()
pearson2 = covariance/(std_Combat*std_Strength)
print('Pearson Correlation between Combat and Strength:',pearson2)

covariance = newdf1.cov().loc['Combat', 'Intelligence']
std_Combat1 = newdf1['Combat'].std()
std_Intelligence = newdf1['Intelligence'].std()
pearson1 = covariance/(std_Combat1*std_Strength)
print('Pearson Correlation between Combat and Intelligence:',pearson1)

# Step-4
total = data['Total'].quantile(q=0.99)
print('Quantile Value for q=0.99:',total)

superhero = data[data['Total'] > 554.05]
super_best_names = superhero['Name'].tolist()
print(super_best_names)



