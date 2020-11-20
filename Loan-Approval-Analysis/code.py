# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#Code starts here

# Step - 1

categorical_var = bank_data.select_dtypes(include='object')
print(categorical_var.head())
print(categorical_var.shape)

numerical_var = bank_data.select_dtypes(include='number')
print(numerical_var.head())
print(numerical_var.shape) 

# Step - 2

banks = bank_data.drop(columns = ['Loan_ID'])
null_values = banks.isnull().sum()
print(null_values)

bank_mode = banks.mode()
print(bank_mode)

values = {"Gender":'Male', 'Married':'Yes', 'Dependents':0, 'Self_Employed':'No', 'LoanAmount': 120.0, 'Loan_Amount_Term':360.0, 'Credit_History':1.0}

# method 2 ----------->
#for column in banks.columns:
#    banks[column].fillna(banks[column].mode()[0], inplace=True)

# Remove below statement for method 2
banks = banks.fillna(value = values)
print(banks.isnull().sum())

# Step - 3

avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount')
# By Default --> aggfunc='mean' inside pivot_table
print(avg_loan_amount)

# Step - 4

loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)

Loan_Status = 614

percentage_se = (loan_approved_se/Loan_Status)*100
print(percentage_se)

percentage_nse = (loan_approved_nse/Loan_Status)*100
print(percentage_nse)

# Step - 5

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = loan_term >= 25
print(big_loan_term.sum())
# .sum() is used for counting the True values in a column

# Step - 6

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()
print(mean_values)



