# **Telco Churn Analysis**

## **Project Description**
Telco, a telecommunications service provider, currently faces about a 25% likelihood that their customers will leave their company. 

## **Project Goals**
* Find out what is driving the customers at Telco to leave (churn).
* Build a ML model using classification algorithms to predict if a customer will churn
* This information can be use to 

## **Initial Thoughts** 
* My initial hypothesis is that the following features affect whether or not a customer will churn greater than the others:
    * **Tenure**: The length of time a customer has been with the service is a crucial factor. Generally, longer tenure is associated with lower churn rates.
    * **Monthly Charges**: Higher monthly charges may increase the likelihood of churn, especially if customers perceive the costs as too high relative to the value they receive.
    * **Contract Type**: Customers with month-to-month contracts are typically more likely to churn than those with longer-term contracts (e.g., annual contracts).


## **Data Dictionary**

| Feature | Definition |
|:--------|:-----------|
|customer_id|Unique identifier for each customer|
|gender|The gender of the customer (male,female)|
|senior_citizen|Indicates whether the customer is a senior citizen|
|partner|Indicates whether the customer has a partner|
|dependents|Indicates whether the customer has dependents|
|tenure|The duration in months that a customer has been with the service provider|
|phone_service|Indicates whether the customer subscribes to phone service|
|multiple_lines|Indicates whether the customer has multiple phone lines|
|internet_service|Indicates whether the customer subscribes to internet service|
|online_security|Indicates whether the customer has online security features|
|online_backup|Indicates whether the customer has online backup features|
|device_protection|Indicates whether the customer has device protection features|
|tech_support|Indicates whether the customer has technical support services|
|streaming_tv|Indicates whether the customer subscribes to streaming TV services|
|streaming_movies|Indicates whether the customer subscribes to streaming movie services|
|paperless_billing|Indicates whether the customer has opted for paperless billing|
|monthly_charges|The amount charged to the customer on a monthly basis|
|total_charges|The total charges incurred by the customer|
|churn|Indicates whether the customer has churned|
|contract_type|Type of contract subscribed by the customer (month-to-month, one-year, two-year)|
|internet_service_type|Type of internet service subscribed by the customer (DSL, fiber optic)|
|payment_type|The method of payment chosen by the customer (bank transfer, credit card, electronic check, mailed check)|

## **Project Plan** 
* **Aquire** data from MySQL

* **Prepare**
    * Drop duplicate columns
        * `payment_type_id` *- data exists in the `payment_type` column*
        * `internet_service_type_id` *- data exists in the `internet_service_type` column*
        * `contract_type_id` *- data exists in the `contract_type` column*
    * Create `internet_service` column to indicate whether a customer subscribes to internet service
    * Correct values & datatypes
        * changed values in the `senior_citizen` column from '1 or 0' to 'Yes or No'
        * filled null values in the `internet_service_type` with 'No internet service' based off of comparison to the `internet_service` column
        * changed values in the `total_charges` from an object to a float
    * Split Data into 3 new dataframes:
        * Train - 60% of the original dataframe
        * Validate - 20% of the original dataframe
        * Test - 20% of the original dataframe
* Explore
* Preprocessing
* Model
* Evaluation

## **Steps to Reproduce**
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