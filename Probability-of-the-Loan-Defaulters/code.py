# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)
print(df.head())

#Code starts here

#Task-1 => Check if events are independent
# p(A)
p_a = len(df[df['fico']>700])/len(df)
print('probability p(A) that fico score > 700:',p_a)

# p(B)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)
print('probability p(B) that purpose is debt consolidation:',p_b)

# p(A intersection B)
p_a_intersection_b = len(df[(df['purpose'] == 'debt_consolidation')&(df['fico']>700)])/len(df)

# p(A|B)
p_a_b = p_a_intersection_b/p_b
print('probability of A given B:',p_a_b)

if (p_a_b == p_a):
    result = True
else:
    result = False
print(result)


#Task-2
# p(A)
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)
print('probability p(A) that loan is paid back:',prob_lp)

# p(B)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)
print('probability p(B) that credit policy is Yes:',prob_cs)

c = np.array(df['credit.policy'])
p = np.array(df['paid.back.loan'])
table = pd.crosstab(c,p)
print(table)

# p(A intersection B)
prob_pd_intersection_cs = table.iloc[1,1]/len(df)

# p(B|A)
prob_pd_cs = prob_pd_intersection_cs/prob_lp
print('probability of B given A:',prob_pd_cs)

# p(A|B)=(p(B|A)*p(A))/p(B)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print('Bayes:',bayes)

# the codes below gives the same value, so both can be used
# print(table.iloc[1,1])
# print(len(df[(df['paid.back.loan'] == 'Yes')&(df['credit.policy']=='Yes')]))


#Task-3
df['purpose'].value_counts().plot(kind='bar')
plt.show()

df1 = df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts().plot(kind='bar')
plt.show()


#Task-4
inst_median = df['installment'].median()
print('Installment Median:',inst_median)

inst_mean = df['installment'].mean()
print('Installment Mean:',inst_mean)

df['installment'].plot(kind='hist')
plt.xlabel('Installment')
plt.show()

df['log.annual.inc'].plot(kind='hist')
plt.xlabel('Log Annual Income')
plt.show()



