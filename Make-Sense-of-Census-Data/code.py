# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#print(data.shape)

census = np.concatenate((data , new_record), axis=0)
#print(census)
census.shape

#Code starts here

age = census[:,0]

max_age = max(age)
min_age = min(age)
age_mean = age.mean()
age_std = age.std()

# Step - 3

# subsetting Race Array
race_i = census[:,2]

# Simple [for-if] combination does not work here because a new array (eg. race_0) cannot be initialized without a specific size.

# Subsetting Race Array with elements = '0'
race_0 = census[race_i==0]
#print(race_0)

race_1 = census[race_i==1]
#print(race_1)

race_2 = census[race_i==2]
#print(race_2)

race_3 = census[race_i==3]
#print(race_3)

race_4 = census[race_i==4]
#print(race_4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

#print(len_0)
#print(len_1)
#print(len_2)
#print(len_3)
#print(len_4)

minority_race = 3

# Step - 4

senior_citizens = census[age > 60]

working_hours_sum = senior_citizens[:,6].sum()
#print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
#print(senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len
#print(avg_working_hours)

# Step - 5
edu = census[:,1]

high = census[edu > 10]
low = census[edu <= 10]

avg_pay_high = high[:,7].mean()
print(avg_pay_high)

avg_pay_low = low[:,7].mean()
print(avg_pay_low)



