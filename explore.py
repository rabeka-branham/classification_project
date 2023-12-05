import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def pie_churn(train,target):
    values  = [train[target].mean(),(1-(train[target].mean()))]
    labels = ['Churned','Active'] 
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%.2f%%', colors=['lightsalmon','lightseagreen'])
    plt.title('The "Churn vs Active" Rate of Customers')
    plt.show()
    
def bar_tenure(train):
    values = [train.tenure[(train.churn == True)].mean(),train.tenure[(train.churn == False)].mean()]
    labels = ['Churned','Active']
    plt.figure(figsize=(6, 6))
    plt.bar(height=values, x=labels, color=['lightsalmon','lightseagreen'])
    plt.title('Comparing Avg Tenure of Churn vs Active')
    plt.show()

def bar_monthly_charges(train):
    values = [train.monthly_charges[(train.churn == True)].mean(),train.monthly_charges[(train.churn == False)].mean()]
    labels = ['Churned','Active']
    plt.figure(figsize=(6, 6))
    plt.bar(height=values, x=labels, color=['lightsalmon','lightseagreen'])
    plt.title('Comparing Avg Monthly Charges of Churn vs Active')
    plt.show()
    
def pie_churn_by_contract_type(train):
    fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(18,6))
    labels = ['Churned', 'Active'] 

    values = [len(train.churn[(train.contract_type == 'Month-to-month') & (train.churn == True)]),
            len(train.churn[(train.contract_type == 'Month-to-month') & (train.churn == False)])]
    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['lightsalmon','lightseagreen'])
    ax1.title.set_text('Month-to-month')

    values = [len(train.churn[(train.contract_type == 'One year') & (train.churn == True)]),
            len(train.churn[(train.contract_type == 'One year') & (train.churn == False)])]
    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['lightsalmon','lightseagreen'])
    ax2.title.set_text('One year')

    values = [len(train.churn[(train.contract_type == 'Two year') & (train.churn == True)]),
            len(train.churn[(train.contract_type == 'Two year') & (train.churn == False)])]
    ax3.pie(values, labels=labels, autopct='%.0f%%', colors=['lightsalmon','lightseagreen'])
    ax3.title.set_text('Two year')
    
    plt.title('Churn vs Active by Contract Type')
    plt.tight_layout
    plt.show()
    
def chi_squared_contract_type(train):
    observed = pd.crosstab(train.contract_type,train.churn)
    α = .05
    chi2, p, dof, expected = stats.chi2_contingency(observed)

    if p < α:
        print('There IS a relationship between contract_type & churn rate!')
    else:
        print('There is NO relationship between contract_type & churn rate!')
        
def mann_whitney_tenure(train):
    churned = train[train.churn == 1]
    active = train[train.churn == 0]
    t,p = stats.mannwhitneyu(churned.tenure, active.tenure)
    α = 0.05

    if p < α:
        print('There IS a relationship between tenure & churn rate!')
    else:
        print('There is NO relationship between tenure & churn rate!')
        
def mann_whitney_monthly_charges(train):
    churned = train[train.churn == 1]
    active = train[train.churn == 0]
    t,p = stats.mannwhitneyu(churned.monthly_charges, active.monthly_charges)
    α = 0.05

    if p < α:
        print('There IS a relationship between monthly_charges & churn rate!')
    else:
        print('There is NO relationship between monthly_charges & churn rate!')