# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here


# Task-1
data_sample = data.sample(n=sample_size, random_state=0)
print(data_sample.head())
print(data_sample.dtypes)

ins_sample_mean = data_sample['installment'].mean()
ins_std = data['installment'].std()

margin_of_error = z_critical*(ins_std/math.sqrt(sample_size))
print('Margin of error =',margin_of_error)

confidence_interval = (ins_sample_mean-margin_of_error, ins_sample_mean+margin_of_error)
print('Confidence Interval =',confidence_interval)

true_mean = data['installment'].mean()
print('True Mean =', true_mean)

if confidence_interval[0] < true_mean < confidence_interval[1]:
    print('Yes True Mean falls in the range of Confidence Interval')
else:
    print('No True Mean does not fall in the range of Confidence Interval') 


# Task-2
fig, axes = plt.subplots(nrows=3, ncols=1) 
sample_size = np.array([20,50,100])

for i in range(len(sample_size)):
    
    means = []
    for j in range(1000):
        sample_data = data.sample(sample_size[i])
        sample_mean = sample_data['installment'].mean() 
       
        means.append(sample_mean)
        
    #Converting the list to series
    mean_series = pd.Series(means) 
    
    #Plotting the histogram for the series
    axes[i].hist(mean_series, bins=1000)

plt.show()


# Task-3 (Small Business Interests)
data['int.rate'] = data['int.rate'].str.rstrip('%').astype('float')

df_1 = data[data['purpose'] == 'small_business']

ir_mean =data['int.rate'].mean()
print('Interest Rate Mean=',ir_mean)

z_statistic_1, p_value_1 = ztest(df_1['int.rate'], value = ir_mean, alternative='larger')
print('z-statistic = ',z_statistic_1)
print('p-value =',p_value_1)
print('-------------------------------')


# Task-4 (Installment vs Loan Defaulting)
df_pb = data[data['paid.back.loan'] == 'Yes']
df_npb = data[data['paid.back.loan'] == 'No']

z_statistic_2, p_value_2 = ztest(x1 = df_npb['installment'], x2 = df_pb['installment'])
print('z-statistic =',z_statistic_2)
print('p-value =',p_value_2)
print('-------------------------------')


# Task-5 (Purpose vs Loan Defaulting)
observed = pd.crosstab(data['purpose'],data['paid.back.loan'])
print(observed)

chi2, p, dof, ex = stats.chi2_contingency(observed)

print('-------------------------------')
print("p-value = ",p)
print("degree of freedom = ",dof)
print("expected frequency = ")
print(ex)
print("Chi-square statistic = ",chi2)
print('critical value =',critical_value)
print('Since chi-squared statistic exceeds the critical value, Null Hypothesis is rejected ')



