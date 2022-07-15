def custom_one_hot_encode_columns(df, col_list) :
    # One hot encoding (Built-in version)   
    for col in col_list :
        df=df.drop(columns = col).join(pd.get_dummies(df[col], prefix = col))
    return df
#
