from sklearn.model_selection import train_test_split
import numpy as np

def prepare_data(dataframe):
    '''
    This function prepares the input dataframe for modeling:
    - Drops 'payment_type_id', 'internet_service_type_id', and 'contract_type_id' columns.
    - Fills null values in the 'internet_service_type' column with 'No internet service'.
    - Converts 'senior_citizen' values to 'Yes' or 'No'.
    - Creates a new 'internet_service' column based on the 'online_security' column.
    - Converts 'churn' values to binary (1 for 'Yes', 0 for 'No').
    - Moves the 'internet_service' column to the 9th position.
    - Replaces empty values in the 'total_charges' column with '0.0' and casts the column as float.
    - Sets the 'customer_id' as the index.

    Parameters:
    - dataframe (pd.DataFrame): Input dataframe.

    Returns:
    pd.DataFrame: Prepared dataframe.
    '''
    df = dataframe.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    df.internet_service_type = df.internet_service_type.fillna('No internet service')
    df.senior_citizen = np.where(df['senior_citizen'] == 1, 'Yes', 'No')
    df.loc[:, 'internet_service'] = np.where(df['online_security'] == 'No internet service', 'No', 'Yes')
    df.churn = np.where(df['churn'] == 'Yes', 1, 0)
    df.insert(8, 'internet_service', df.pop('internet_service')) 
    df.total_charges = df.total_charges.replace(' ', '0.0').astype('float')
    df = df.set_index('customer_id')
    return df

def split_data(dataframe, col):
    '''
    This function splits the input dataframe into training, validation, and test sets:
    - Splits the dataframe by 60/40, setting them as new dataframes to variables 'train' and 'validate_test'.
    - Splits 'validate_test' by 50/50, setting them as new dataframes to variables 'validate' and 'test'.

    Parameters:
    - dataframe (pd.DataFrame): Input dataframe.
    - col (str): The column used for stratification.

    Returns: training, validation, and test dataframes.
    '''
    train, validate_test = train_test_split(dataframe, 
                                            train_size=.6, 
                                            random_state=913,
                                            stratify=dataframe[col]
                                           )
    validate, test = train_test_split(validate_test,
                                      test_size=0.50, 
                                      random_state=913,
                                      stratify=validate_test[col]
                                     )
    return train, validate, test