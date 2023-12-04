# **Project Description**
Telco, a telecommunications service provider, currently faces about a 25% likelihood that their customers will leave their company. 

# **Project Goals**
* Find out what is driving the customers at Telco to leave (churn).
* Build a ML model using classification algorithms to predict if a customer will churn
* This information can be use to 

Present your process and findings to the lead data scientist

# **Initial Thoughts** 
My initial hypothesis is that 
    * **Tenure**: The length of time a customer has been with the service is a crucial factor. Generally, longer tenure is associated with lower churn rates.
    * **Monthly Charges**: Higher monthly charges may increase the likelihood of churn, especially if customers perceive the costs as too high relative to the value they receive.
    * **Contract Type**: Customers with month-to-month contracts are typically more likely to churn than those with longer-term contracts (e.g., annual contracts).


# **Data Dictionary**

| Feature | Definition |
|:--------|:-----------|
|payment_type_id|
|internet_service_type_id|
|contract_type_id|
|customer_id|
|gender|
|senior_citizen|
|partner|
|dependents|
|tenure|
|phone_service|
|multiple_lines|
|online_security|
|online_backup|
|device_protection|
|tech_support|
|streaming_tv|
|streaming_movies|
|paperless_billing|
|monthly_charges|
|total_charges|
|churn|
|contract_type|
|internet_service_type|
|payment_type|

# **Project Plan** 
* Acquire
* Prepare
* Explore
* Preprocessing
* Model
* Evaluation

# **Steps to Reproduce**
1. Clone this repo.
2. Create an `env.py` file that follows the "sample `env.py` file" format below.
3. Save your `env.py` file into the cloned repo.
4. Run notebook.

**sample** `env.py` **file:**<br>
host = 'data.codeup.com'<br>
username = 'sample_username'<br>
password = 'sample_password'<br>

def get_db_url(database_name, host_name=host, password=password, username=username):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return f'mysql+pymysql://{username}:{password}@{host_name}/{database_name}'


key findings, recommendations, and takeaways