# **Telco Churn Analysis**

## **Project Description**
This data science project aims to identify the root causes of customer departures and develop a predictive model to assist in mitigating churn risk.

## **Project Goals**
* Find out what is causing the customer churn at Telco.
* Construct a ML model using classification algorithms that accurately predicts customer churn.

## **Initial Thoughts** 
* My initial hypothesis is that the following features affect whether or not a customer will churn greater than the others:
    * **Tenure**
    * **Monthly Charges**
    * **Contract Type**

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
* **Aquire**
    * In the Acquire phase, we obtained the data from the Codeup MySQL database `telco_churn`.
    * The dataset is comprised of 7,043 rows and 22 columns.
    * Every row corresponds to a distinct Telco customer & each column signifies a specific customer attribute.

* **Prepare**
    * Remove duplicate columns (`payment_type_id`, `internet_service_type_id`, `contract_type_id`) as the same data is available elsewhere.
    * Introduce `internet_service` column to signify customer subscription to internet service.
    * Adjust values and datatypes:
        * Convert `senior_citizen` values from '1 or 0' to 'Yes or No'.
        * Convert `churn values` from 'Yes or No' to '1 or 0'.
        * Fill null values in `internet_service_type` with 'No internet service'.
        * Convert `total_charges` values to float.
    * Set the index to `customer_id` for unique identification.
    * Split data into three dataframes based on `churn`:
        * Train (60% of the original dataframe)
        * Validate (20% of the original dataframe)
        * Test (20% of the original dataframe)
    * Retain all data points; no outliers have been removed.

* **Explore**
    * How often are customers churning?
        * For the question "How often do customers churn?", we found a churn rate of 26.53% based on our pie chart analysis of the training data.
    * What is the influence of tenure on the churn rate?
        * Addressing the influence of tenure on the churn rate, we conducted a Mann-Whitney test, revealing a relationship between tenure and churn rate. Visualized through a bar chart, it shows that active customers generally have higher tenure.
    * How does monthly charges correlate with the churn rate?
        * For the correlation between monthly charges and churn rate, a similar approach with a Mann-Whitney test suggests a relationship. The bar chart visualization reveals that active customers tend to have lower monthly charges.
    * What impact does contract type have on the churn rate?
        * Exploring the impact of contract type on churn rate, a chi^2 test indicates a relationship. Illustrated through a pie chart, customers with month-to-month contracts show a significantly higher churn rate compared to those with longer-term contracts.
    * Confirmed influences of tenure, monthly charges, and contract types on customer churn will guide predictive model development.
    
* **Modeling**
    * Preprocessing
        * In the model phase, we preprocessed data, handling categorical columns and ensuring data readiness.
    * Baseline accuracy, obtained by subtracting the mean of 'churn' from 1, is 73.47%.
    * Model Selection
        * We explored multiple models: Decision Tree, Random Forest, KNN, and Logistic Regression. 
        * Logistic Regression marginally outperformed other models and was selected as our final model for test data evaluation.
    * Model Evaluation
        * Our final model achieved an accuracy of 79.77% on the test data, surpassing the baseline accuracy.
* **Conclusion**
    * Recommendations
        * Customer Loyalty Programs: Encourage long-term customers to stay with the company.
        * Promotions for Longer Contracts: Offer discounts for customers willing to commit to one-year or two-year contracts.
    * Future Steps
        * The next step would be to continue monitoring customer churn and model performance, updating as new data becomes available.
    * In conclusion, our Telco Churn Analysis project has provided valuable insights into the factors influencing customer churn. The Logistic Regression model offers a practical tool for identifying and addressing churn risk. By implementing recommendations and staying proactive with continuous monitoring, we can strengthen customer retention and contribute to the long-term success of this company.

## **Steps to Reproduce**
1. Clone this repo.
2. Create an `env.py` file that follows the "sample env.py file" format below.
3. Save your `env.py` file into the cloned repo.
4. Run notebook.

**<ins>sample env.py file:</ins>**<br>
host = 'data.codeup.com'<br>
username = 'sample_username'<br>
password = 'sample_password'<br>

def get_db_url(database_name, host_name=host, password=password, username=username):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return f'mysql+pymysql://{username}:{password}@{host_name}/{database_name}'