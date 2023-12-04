def preprocess_titanic(train, validate, test):
    encoded_df = []
    for df in [train, validate, test]:
        df.pclass = df.pclass.astype(int)
        df_encoded_columns = pd.get_dummies(df[['embark_town', 'sex']],
              drop_first=True).astype(int)
        encoded_df.append(pd.concat([df, df_encoded_columns],
                                    axis=1).drop(columns=['sex', 'embark_town']))
    return encoded_df