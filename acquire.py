import os
from env import get_db_url
import pandas as pd
    
def acquire_data():
    '''
    This function sets the filename to 'telco.csv', the url to read from the codeup mysql db 'telco_churn', & the query to pull all data for the following joined tables: customers, contract_types, internet_service_types, & payment_type.

    It will then check if the file exists. If it does, it will read the file & return it to us as a dataframe. If it does not exist, it will create the file & return it to us as a dataframe.
    
    '''
    filename = 'telco.csv'
    url = get_db_url('telco_churn')
    query = '''
        select * from customers
        join contract_types using (contract_type_id)
        join internet_service_types using (internet_service_type_id)
        join payment_types using (payment_type_id);
        '''
    
    if os.path.exists(filename):
        df = pd.read_csv(filename, index_col=0)
    else:
        df = pd.read_sql(query,url)
        df.to_csv(filename)
    
    return df