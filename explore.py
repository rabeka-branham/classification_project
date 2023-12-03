import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

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
    quant_cols = df.columns[df.nunique() >= 10].drop(['customer_id','tenure']).tolist()
    
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