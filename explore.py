import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def pie_churn(train,target):
    values  = [train[target].mean(),(1-(train[target].mean()))]
    labels = ['Churned','Active'] 
    plt.pie(values, labels=labels, autopct='%.2f%%', colors=['lightsalmon','lightseagreen'])
    plt.title('The "Churn vs Active" Rate of Customers')
    plt.show()
    
def bar_tenure(train):
    values = [train.tenure[(train.churn == True)].mean(),train.tenure[(train.churn == False)].mean()]
    labels = ['Churn','Active']
    plt.figure(figsize=(4, 4))
    plt.bar(height=values, x=labels, color=['lightsalmon','lightseagreen'])
    plt.title('Comparing Avg Tenure of Churn vs Active')
    plt.show()

def bar_monthly_charges(train):
    values = [train.monthly_charges[(train.churn == True)].mean(),train.monthly_charges[(train.churn == False)].mean()]
    labels = ['Churn','Active']
    plt.figure(figsize=(4, 4))
    plt.bar(height=values, x=labels, color=['lightsalmon','lightseagreen'])
    plt.title('Comparing Avg Monthly Charges of Churn vs Active')
    plt.show()
    
def pie_churn_by_contract_type(train):
    fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,5))
    labels = ['Churn', 'Active'] 

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
        
def top_three_cols(d_rel_cols):
    values = []
    for value in d_rel_cols.values():
        values.append(value)
    values.sort()
    
    top_three_pvalues = values[:3]
    
    top_three_cols = []
    for key in d_rel_cols.keys():
        if d_rel_cols[key] in top_three_pvalues:
            top_three_cols.append(key)
            
    return top_three_cols

def top_three_rel_columns(df, target):
    cat_cols = df.columns[df.nunique() < 10].drop(target).tolist()
    quant_cols = df.columns[df.nunique() >= 10].drop(['customer_id']).tolist()
    
    churned = df[df[target] == 'Yes']
    active = df[df[target] == 'No']
    
    rel_keys = []
    rel_values = []
    
    no_rel_keys = []
    no_rel_values = []

    for col in cat_cols:
        observed = pd.crosstab(df[col],df.churn)
        α = .05
        chi2, p, dof, expected = stats.chi2_contingency(observed)

        if p < α:
            rel_keys.append(col)
            rel_values.append(p)
        else:
            no_rel_keys.append(col)
            no_rel_values.append(p)
        
    for col in quant_cols:
        t,p = stats.mannwhitneyu(churned[col], active[col])
        α = .05

        if p < α:
            rel_keys.append(col)
            rel_values.append(p)
        else:
            no_rel_keys.append(col)
            no_rel_values.append(p)
            
    d_rel_cols = dict(zip(rel_keys, rel_values))
    d_no_rel_cols = dict(zip(no_rel_keys, no_rel_values))
    
    top_three = top_three_cols(d_rel_cols)
    
    return top_three