import pandas as pd
import numpy as np
import os

import warnings
warnings.filterwarnings("ignore")

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

def preprocess(train, validate, test):
    """
    Preprocess the data by encoding categorical columns using one-hot encoding.

    Parameters:
    - train (pd.DataFrame): Training data.
    - validate (pd.DataFrame): Validation data.
    - test (pd.DataFrame): Testing data.

    Returns:
    List of preprocessed DataFrames [train_encoded, validate_encoded, test_encoded].
    """
    encoded_df = []
    
    for df in [train, validate, test]:
        yes_no_columns = ['multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']

        for col in yes_no_columns:
            df[col] = np.where(df[col] == 'Yes', 'Yes', 'No')
            
        encoded_columns = df.columns[df.nunique() < 10].tolist()
        encoded_columns.remove('churn')
        
        df_encoded_columns = pd.get_dummies(df[encoded_columns], drop_first=True).astype(int)
        df = pd.concat([df, df_encoded_columns], axis=1).drop(columns=encoded_columns)
        encoded_df.append(df)
    
    return encoded_df

def decision_tree(train, validate, test):
    """
    Train a Decision Tree classifier and evaluate its performance on train, validate, and test sets.

    Parameters:
    - train (pd.DataFrame): Training data.
    - validate (pd.DataFrame): Validation data.
    - test (pd.DataFrame): Testing data.

    Returns:
    Test accuracy.
    """
    X_train = train.drop(columns=['churn'])
    y_train = train.churn

    X_val = validate.drop(columns=['churn'])
    y_val = validate.churn
    
    X_test = test.drop(columns=['churn'])
    y_test = test.churn
    
    clf = DecisionTreeClassifier(max_depth=4, random_state=913)
    clf = clf.fit(X_train, y_train)

    train_y_pred = pd.DataFrame({
    'y_true': y_train.values,
    'baseline':0,
    'train': clf.predict(X_train)
    }, index=train.index)

    val_y_pred = pd.DataFrame({
    'y_true': y_val.values,
    'baseline':0,
    'validate': clf.predict(X_val)
    }, index=validate.index)
    
    test_y_pred = pd.DataFrame({
    'y_true': y_test.values,
    'baseline':0,
    'test': clf.predict(X_test)
    }, index=test.index)

    train_acc = accuracy_score(train_y_pred.y_true, train_y_pred.train)
    validate_acc = accuracy_score(val_y_pred.y_true, val_y_pred.validate)
    test_acc = accuracy_score(test_y_pred.y_true, test_y_pred.test)
    
    print(F'Train Accuracy: {train_acc:.4f}')
    print(F'Validate Accuracy: {validate_acc:.4f}')
    
    return test_acc
      
def random_forest(train, validate, test):
    """
    Train a Random Forest classifier and evaluate its performance on train, validate, and test sets.

    Parameters:
    - train (pd.DataFrame): Training data.
    - validate (pd.DataFrame): Validation data.
    - test (pd.DataFrame): Testing data.

    Returns:
    Test accuracy.
    """
    X_train = train.drop(columns=['churn'])
    y_train = train.churn

    X_val = validate.drop(columns=['churn'])
    y_val = validate.churn
    
    X_test = test.drop(columns=['churn'])
    y_test = test.churn
    
    rf = RandomForestClassifier(max_depth=3, min_samples_leaf=3, random_state=913)
    rf = rf.fit(X_train, y_train)
    
    train_y_pred = pd.DataFrame({
    'y_true': y_train.values,
    'baseline':0,
    'train': rf.predict(X_train)
    }, index=train.index)
    
    val_y_pred = pd.DataFrame({
    'y_true': y_val.values,
    'baseline':0,
    'validate': rf.predict(X_val)
    }, index=validate.index)
    
    test_y_pred = pd.DataFrame({
    'y_true': y_test.values,
    'baseline':0,
    'test': rf.predict(X_test)
    }, index=test.index)

    train_acc = accuracy_score(train_y_pred.y_true, train_y_pred.train)
    validate_acc = accuracy_score(val_y_pred.y_true, val_y_pred.validate)
    test_acc = accuracy_score(test_y_pred.y_true, test_y_pred.test)
    
    print(F'Train Accuracy: {train_acc:.4f}')
    print(F'Validate Accuracy: {validate_acc:.4f}')
    
    return test_acc
    
def knn(train, validate, test):
    """
    Train a K-Nearest Neighbors classifier and evaluate its performance on train, validate, and test sets.

    Parameters:
    - train (pd.DataFrame): Training data.
    - validate (pd.DataFrame): Validation data.
    - test (pd.DataFrame): Testing data.

    Returns:
    Test accuracy.
    """
    X_train = train.drop(columns=['churn'])
    y_train = train.churn

    X_val = validate.drop(columns=['churn'])
    y_val = validate.churn
    
    X_test = test.drop(columns=['churn'])
    y_test = test.churn
    
    knn = KNeighborsClassifier(n_neighbors=14)
    knn = knn.fit(X_train, y_train)
    
    train_y_pred = pd.DataFrame({
    'y_true': y_train.values,
    'baseline':0,
    'train': knn.predict(X_train.values)
    }, index=train.index)
    
    val_y_pred = pd.DataFrame({
    'y_true': y_val.values,
    'baseline':0,
    'validate': knn.predict(X_val.values)
    }, index=validate.index)
    
    test_y_pred = pd.DataFrame({
    'y_true': y_test.values,
    'baseline':0,
    'test': knn.predict(X_test.values)
    }, index=test.index)

    train_acc = accuracy_score(train_y_pred.y_true, train_y_pred.train)
    validate_acc = accuracy_score(val_y_pred.y_true, val_y_pred.validate)
    test_acc = accuracy_score(test_y_pred.y_true, test_y_pred.test)
    
    print(F'Train Accuracy: {train_acc:.4f}')
    print(F'Validate Accuracy: {validate_acc:.4f}')
    
    return test_acc

def logistic_regression(train, validate, test):
    """
    Train a Logistic Regression classifier and evaluate its performance on train, validate, and test sets.

    Parameters:
    - train (pd.DataFrame): Training data.
    - validate (pd.DataFrame): Validation data.
    - test (pd.DataFrame): Testing data.

    Returns:
    Test accuracy.
    """
    X_train = train.drop(columns=['churn'])
    y_train = train.churn

    X_val = validate.drop(columns=['churn'])
    y_val = validate.churn
    
    X_test = test.drop(columns=['churn'])
    y_test = test.churn
    
    logit = LogisticRegression(random_state=913)
    logit = logit.fit(X_train, y_train)
    
    train_y_pred = pd.DataFrame({
    'y_true': y_train.values,
    'baseline':0,
    'train': logit.predict(X_train)
    }, index=train.index)
    
    val_y_pred = pd.DataFrame({
    'y_true': y_val.values,
    'baseline':0,
    'validate': logit.predict(X_val)
    }, index=validate.index)
    
    test_y_pred = pd.DataFrame({
    'y_true': y_test.values,
    'baseline':0,
    'test': logit.predict(X_test)
    }, index=test.index)

    train_acc = accuracy_score(train_y_pred.y_true, train_y_pred.train)
    validate_acc = accuracy_score(val_y_pred.y_true, val_y_pred.validate)
    test_acc = accuracy_score(test_y_pred.y_true, test_y_pred.test)
    
    prob_of_churn = pd.DataFrame(logit.predict_proba(X_test))
    
    predict_prob_df = pd.DataFrame({
        'customer_id': test.index,
        'probability_of_churn': prob_of_churn[1],
        'churn_predict': test_y_pred.test.values})
    
    predict_prob_df['churn_predict'] = np.where(predict_prob_df['churn_predict'] == 1, 'Yes', 'No')
    
    if os.path.exists('predictions.csv'):
        pass
    else:
        predict_prob_df.to_csv('predictions.csv',index=False)
    
    print(F'Train Accuracy: {train_acc:.4f}')
    print(F'Validate Accuracy: {validate_acc:.4f}')
    
    return test_acc