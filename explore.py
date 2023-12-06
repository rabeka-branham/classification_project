import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def pie_churn(df):
    """
    Generate a pie chart to visualize the churn rate of customers.

    Parameters:
    - df (pd.DataFrame): A Pandas DataFrame containing a 'churn' column with binary values (0 or 1).

    Returns:
    None
    """
    # Calculate the mean of the 'churn' column to get the churn rate
    churn_rate = df.churn.mean()

    # Calculate the percentage of churned and active customers
    values = [churn_rate, 1 - churn_rate]

    # Define labels for the pie chart
    labels = ['Churned', 'Active']

    # Create a pie chart with custom colors and display percentages
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%.2f%%', colors=['lightsalmon', 'lightseagreen'])

    # Set the title of the pie chart
    plt.title('The "Churn vs Active" Rate of Customers')

    # Display the pie chart
    plt.show()
    
def bar_tenure(train):
    """
    Generate a bar chart to compare the average tenure of churned and active customers.

    Parameters:
    - train (pd.DataFrame): A Pandas DataFrame containing the data with 'tenure' and 'churn' columns.

    Returns:
    None
    """
    # Calculate the mean tenure for churned and active customers
    churned_mean_tenure = train.tenure[train.churn == True].mean()
    active_mean_tenure = train.tenure[train.churn == False].mean()

    # Create lists for values and labels for the bar chart
    values = [churned_mean_tenure, active_mean_tenure]
    labels = ['Churned', 'Active']

    # Create a bar chart with custom colors
    plt.figure(figsize=(6, 6))
    plt.bar(height=values, x=labels, color=['lightsalmon', 'lightseagreen'])

    # Set the title of the bar chart
    plt.title('Comparing Avg Tenure of Churn vs Active')

    # Display the bar chart
    plt.show()

def bar_monthly_charges(train):
    """
    Generate a bar chart to compare the average monthly charges of churned and active customers.

    Parameters:
    - train (pd.DataFrame): A Pandas DataFrame containing the data with 'monthly_charges' and 'churn' columns.

    Returns:
    None
    """
    # Calculate the mean monthly charges for churned and active customers
    churned_mean_charges = train.monthly_charges[train.churn == True].mean()
    active_mean_charges = train.monthly_charges[train.churn == False].mean()

    # Create lists for values and labels for the bar chart
    values = [churned_mean_charges, active_mean_charges]
    labels = ['Churned', 'Active']

    # Create a bar chart with custom colors
    plt.figure(figsize=(6, 6))
    plt.bar(height=values, x=labels, color=['lightsalmon', 'lightseagreen'])

    # Set the title of the bar chart
    plt.title('Comparing Avg Monthly Charges of Churn vs Active')

    # Display the bar chart
    plt.show()

def pie_churn_by_contract_type(train):
    """
    Generate a set of three pie charts to visualize the churn rate for each contract type.

    Parameters:
    - train (pd.DataFrame): A Pandas DataFrame containing the data with 'contract_type' and 'churn' columns.

    Returns:
    None
    """
    # Create subplots with three pie charts in a single row
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    
    # Common labels for the pie charts
    labels = ['Churned', 'Active']

    # Plot the pie chart for 'Month-to-month' contract type
    values_month_to_month = [len(train.churn[(train.contract_type == 'Month-to-month') & (train.churn == True)]),
                             len(train.churn[(train.contract_type == 'Month-to-month') & (train.churn == False)])]
    ax1.pie(values_month_to_month, labels=labels, autopct='%.0f%%', colors=['lightsalmon', 'lightseagreen'])
    ax1.set_title('Month-to-month')

    # Plot the pie chart for 'One year' contract type
    values_one_year = [len(train.churn[(train.contract_type == 'One year') & (train.churn == True)]),
                       len(train.churn[(train.contract_type == 'One year') & (train.churn == False)])]
    ax2.pie(values_one_year, labels=labels, autopct='%.0f%%', colors=['lightsalmon', 'lightseagreen'])
    ax2.set_title('One year')

    # Plot the pie chart for 'Two year' contract type
    values_two_year = [len(train.churn[(train.contract_type == 'Two year') & (train.churn == True)]),
                       len(train.churn[(train.contract_type == 'Two year') & (train.churn == False)])]
    ax3.pie(values_two_year, labels=labels, autopct='%.0f%%', colors=['lightsalmon', 'lightseagreen'])
    ax3.set_title('Two year')

    # Set a common title for the entire plot
    plt.suptitle('Churn vs Active by Contract Type')

    # Adjust layout for better visualization
    plt.tight_layout()

    # Display the plot
    plt.show()
        
def chi_squared_contract_type(train):
    """
    Perform a chi-squared test for independence between contract_type and churn.

    Parameters:
    - train (pd.DataFrame): A Pandas DataFrame containing the data with 'contract_type' and 'churn' columns.

    Returns:
    None
    """
    # Create a contingency table (observed) for contract_type and churn
    observed = pd.crosstab(train.contract_type, train.churn)

    # Set the significance level
    α = 0.05

    # Perform the chi-squared test
    chi2, p, dof, expected = stats.chi2_contingency(observed)

    # Print the p-value
    print(f'p-value: {p:.4f}')

    # Check the p-value against the significance level
    if p < α:
        print('There IS a relationship between contract_type & churn rate!')
    else:
        print('There is NO relationship between contract_type & churn rate!')

def mann_whitney_tenure(train):
    """
    Perform the Mann-Whitney test to assess the relationship between tenure and churn.

    Parameters:
    - train (pd.DataFrame): A Pandas DataFrame containing the data with 'tenure' and 'churn' columns.

    Returns:
    None
    """
    # Separate data into churned and active groups
    churned = train[train.churn == 1]
    active = train[train.churn == 0]

    # Perform Mann-Whitney test
    t, p = stats.mannwhitneyu(churned.tenure, active.tenure)

    # Set the significance level
    α = 0.05

    # Print the p-value
    print(f'p-value: {p:.4f}')

    # Check the p-value against the significance level
    if p < α:
        print('There IS a relationship between tenure & churn rate!')
    else:
        print('There is NO relationship between tenure & churn rate!')

        
def mann_whitney_monthly_charges(train):
    """
    Perform the Mann-Whitney test to assess the relationship between monthly charges and churn.

    Parameters:
    - train (pd.DataFrame): A Pandas DataFrame containing the data with 'monthly charges' and 'churn' columns.

    Returns:
    None
    """
    # Separate data into churned and active groups
    churned = train[train.churn == 1]
    active = train[train.churn == 0]
    
    # Perform Mann-Whitney test
    t,p = stats.mannwhitneyu(churned.monthly_charges, active.monthly_charges)
    
    # Set the significance level
    α = 0.05
    
    # Print the p-value
    print(f'p-value: {p:4f}')

    # Check the p-value against the significance level
    if p < α:
        print('There IS a relationship between monthly_charges & churn rate!')
    else:
        print('There is NO relationship between monthly_charges & churn rate!')