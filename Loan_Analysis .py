#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
loan = pd.read_csv('Loan_dataset.csv')


# In[5]:


loan.head(10)


# 1.What is the average current loan amount for 
# each loan status?

# In[6]:


average_loan_amount_by_status = loan.groupby('Loan Status')['Current Loan Amount'].mean()
print(average_loan_amount_by_status)


# 2.How does the credit score vary with the annual 
# income?

# In[7]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Annual Income', y='Credit Score', data=loan)
plt.title('Credit Score vs. Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Credit Score')
plt.show()


# In[8]:


plt.figure(figsize=(10, 6))
sns.regplot(x='Annual Income', y='Credit Score', data=loan, line_kws={"color": "red"})
plt.title('Credit Score vs. Annual Income with Regression Line')
plt.xlabel('Annual Income')
plt.ylabel('Credit Score')
plt.show()


# In[9]:


correlation = loan['Annual Income'].corr(loan['Credit Score'])
print(f'Correlation coefficient between annual income and credit score: {correlation:.2f}')


# 3.Is there a correlation between the number of 
# open accounts and the current credit balance?

# In[12]:


correlation_open_accounts_credit_balance = loan['Number of Open Accounts'].corr(loan['Current Credit Balance'])
print(f'Correlation between number of open accounts and current credit balance: {correlation_open_accounts_credit_balance:.2f}')


# 4.What is the distribution of credit scores across 
# different home ownership types?

# In[13]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Home Ownership', y='Credit Score', data=loan)
plt.title('Distribution of Credit Scores across Home Ownership Types')
plt.xlabel('Home Ownership')
plt.ylabel('Credit Score')
plt.show()


# In[15]:


data=loan #keeping loan file dataset in data for no confusion


# 5. How does the annual income differ for different purposes of loans?

# In[16]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Purpose', y='Annual Income', data=data)
plt.title('Annual Income for Different Loan Purposes')
plt.xlabel('Purpose')
plt.ylabel('Annual Income')
plt.xticks(rotation=90)
plt.show()


# 6. What is the average monthly debt for each term (short-term vs. long-term)?

# In[17]:


avg_monthly_debt_by_term = data.groupby('Term')['Monthly Debt'].mean()
print("Average monthly debt for each term:")
print(avg_monthly_debt_by_term)


# 7. Is there a correlation between years of credit history and the current credit balance?

# In[18]:


correlation_credit_history_credit_balance = data['Years of Credit History'].corr(data['Current Credit Balance'])
print(f'Correlation between years of credit history and current credit balance: {correlation_credit_history_credit_balance:.2f}')


# 8. How does the credit score vary with the years in the current job?

# In[19]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years in current job', y='Credit Score', data=data)
plt.title('Credit Score vs. Years in Current Job')
plt.xlabel('Years in Current Job')
plt.ylabel('Credit Score')
plt.show()


# 9. What is the relationship between the number of credit problems and the number of open accounts?

# In[20]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Number of Credit Problems', y='Number of Open Accounts', data=data)
plt.title('Number of Credit Problems vs. Number of Open Accounts')
plt.xlabel('Number of Credit Problems')
plt.ylabel('Number of Open Accounts')
plt.show()


# 10. What is the distribution of annual income across different loan statuses?

# In[21]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Loan Status', y='Annual Income', data=data)
plt.title('Annual Income across Loan Statuses')
plt.xlabel('Loan Status')
plt.ylabel('Annual Income')
plt.show()


# 11. Is there a correlation between the current loan amount and the number of open accounts?

# In[22]:


correlation_loan_amount_open_accounts = data['Current Loan Amount'].corr(data['Number of Open Accounts'])
print(f'Correlation between current loan amount and number of open accounts: {correlation_loan_amount_open_accounts:.2f}')


# 12. How does the monthly debt vary with the years of credit history?

# In[23]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years of Credit History', y='Monthly Debt', data=data)
plt.title('Monthly Debt vs. Years of Credit History')
plt.xlabel('Years of Credit History')
plt.ylabel('Monthly Debt')
plt.show()


# 13. What is the average annual income for each purpose of loan?

# In[24]:


avg_annual_income_by_purpose = data.groupby('Purpose')['Annual Income'].mean()
print("Average annual income for each purpose of loan:")
print(avg_annual_income_by_purpose)


# 14. How does the credit score vary with the number of credit problems?

# In[25]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Number of Credit Problems', y='Credit Score', data=data)
plt.title('Credit Score vs. Number of Credit Problems')
plt.xlabel('Number of Credit Problems')
plt.ylabel('Credit Score')
plt.show()


# 15. Is there a correlation between the number of credit problems and the current credit balance?

# In[26]:


correlation_credit_problems_credit_balance = data['Number of Credit Problems'].corr(data['Current Credit Balance'])
print(f'Correlation between number of credit problems and current credit balance: {correlation_credit_problems_credit_balance:.2f}')


# 16. What is the distribution of current loan amounts across different home ownership types?

# In[27]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Home Ownership', y='Current Loan Amount', data=data)
plt.title('Distribution of Current Loan Amounts across Home Ownership Types')
plt.xlabel('Home Ownership')
plt.ylabel('Current Loan Amount')
plt.show()


# 17. How does the annual income vary with the years in the current job?

# In[28]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years in current job', y='Annual Income', data=data)
plt.title('Annual Income vs. Years in Current Job')
plt.xlabel('Years in Current Job')
plt.ylabel('Annual Income')
plt.show()


# 18. Is there a correlation between the current loan amount and the monthly debt?

# In[29]:


correlation_loan_amount_monthly_debt = data['Current Loan Amount'].corr(data['Monthly Debt'])
print(f'Correlation between current loan amount and monthly debt: {correlation_loan_amount_monthly_debt:.2f}')


# 19. What is the average monthly debt for each home ownership type?

# In[30]:


avg_monthly_debt_by_home_ownership = data.groupby('Home Ownership')['Monthly Debt'].mean()
print("Average monthly debt for each home ownership type:")
print(avg_monthly_debt_by_home_ownership)


# 20. How does the credit score vary with the number of open accounts?

# In[31]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Number of Open Accounts', y='Credit Score', data=data)
plt.title('Credit Score vs. Number of Open Accounts')
plt.xlabel('Number of Open Accounts')
plt.ylabel('Credit Score')
plt.show()


# 21. What is the distribution of credit scores across different loan statuses?

# In[32]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Loan Status', y='Credit Score', data=data)
plt.title('Distribution of Credit Scores across Loan Statuses')
plt.xlabel('Loan Status')
plt.ylabel('Credit Score')
plt.show()


# 22. Is there a correlation between the current loan amount and the years of credit history?

# In[33]:


correlation_loan_amount_credit_history = data['Current Loan Amount'].corr(data['Years of Credit History'])
print(f'Correlation between current loan amount and years of credit history: {correlation_loan_amount_credit_history:.2f}')


# 23. How does the monthly debt vary with the number of credit problems?

# In[35]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Number of Credit Problems', y='Monthly Debt', data=data)
plt.title('Monthly Debt vs. Number of Credit Problems')
plt.xlabel('Number of Credit Problems')
plt.ylabel('Monthly Debt')
plt.show()


# 24. What is the average current loan amount for each purpose of loan?

# In[36]:


avg_loan_amount_by_purpose = data.groupby('Purpose')['Current Loan Amount'].mean()
print("Average current loan amount for each purpose of loan:")
print(avg_loan_amount_by_purpose)


# 25. How does the credit score vary with the current credit balance?

# In[37]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Current Credit Balance', y='Credit Score', data=data)
plt.title('Credit Score vs. Current Credit Balance')
plt.xlabel('Current Credit Balance')
plt.ylabel('Credit Score')
plt.show()


# 26. Is there a correlation between the annual income and the current credit balance?

# In[38]:


correlation_income_credit_balance = data['Annual Income'].corr(data['Current Credit Balance'])
print(f'Correlation between annual income and current credit balance: {correlation_income_credit_balance:.2f}')


# 27. What is the distribution of annual income across different terms (short-term vs. long-term)?

# In[39]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Term', y='Annual Income', data=data)
plt.title('Annual Income across Terms')
plt.xlabel('Term')
plt.ylabel('Annual Income')
plt.show()


# 28. How does the credit score vary with the number of credit problems?

# In[40]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Number of Credit Problems', y='Credit Score', data=data)
plt.title('Credit Score vs. Number of Credit Problems')
plt.xlabel('Number of Credit Problems')
plt.ylabel('Credit Score')
plt.show()


# 29. Is there a correlation between the current loan amount and the number of credit problems?

# In[41]:


correlation_loan_amount_credit_problems = data['Current Loan Amount'].corr(data['Number of Credit Problems'])
print(f'Correlation between current loan amount and number of credit problems: {correlation_loan_amount_credit_problems:.2f}')


# 30. What is the relationship between the number of open accounts and the years of credit history?

# In[42]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years of Credit History', y='Number of Open Accounts', data=data)
plt.title('Number of Open Accounts vs. Years of Credit History')
plt.xlabel('Years of Credit History')
plt.ylabel('Number of Open Accounts')
plt.show()

