def preprocess_titanic(train_df, validate_df, test_df):
    encoded_df = []
    for df in [train_df, validate_df, test_df]:
        df.pclass = df.pclass.astype(int)
        df_encoded_columns = pd.get_dummies(df[['embark_town', 'sex']],
              drop_first=True).astype(int)
        encoded_df.append(pd.concat([df, df_encoded_columns],
                                    axis=1).drop(columns=['sex', 'embark_town']))
    return encoded_df