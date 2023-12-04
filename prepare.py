from sklearn.model_selection import train_test_split
import numpy as np

def prepare_data(dataframe):
    '''
    This function takes in a dataframe & drops the 'payment_type_id', 'internet_service_type_id', & 'contract_type_id' columns, fills the null values in the 'internet_service_type' column with 'No internet service', & replaces the empty values in the 'total_charges' column with '0.0' & casts the column as a float. It then returns the prepped dataframe.
    '''
    df = dataframe.drop(columns=['payment_type_id','internet_service_type_id','contract_type_id'])
    df.internet_service_type = df.internet_service_type.fillna('No internet service')
    df.senior_citizen = np.where(df['senior_citizen'] == 1, 'Yes', 'No')
    df.loc[:,'internet_service'] = np.where(df['online_security'] == 'No internet service', 'No', 'Yes')
    df.churn = np.where(df['churn'] == 'Yes',1,0)
    df.insert(8, 'internet_service', df.pop('internet_service')) 
    df.total_charges = df.total_charges.replace(' ','0.0').astype('float')
    return df

def split_data(dataframe, col):
    '''
    This function takes in a dataframe & the column on which you want to stratify. It first splits the dataframe by 60/40 & sets them as new dataframes to the variables: train & validate_test. It then splits the validate_test dataframe 50/50 & sets them as new dataframes to the variables: validate & test. It them returns the variables: train, validate, & test.
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