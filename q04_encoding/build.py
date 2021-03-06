# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df):
    lablel_encoder = LabelEncoder()
    df['LotShape'] = lablel_encoder.fit_transform(df['LotShape'])
    #print(df['LotShape'])
    df1=pd.get_dummies(df['GarageType'], drop_first=False)
    #print(df['GarageType'])
    return pd.concat([df,df1],axis=1)

# encoded_housing_data=encoding(housing_data)
# print(type(encoded_housing_data))
# print(encoded_housing_data.shape)
