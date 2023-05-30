import pandas as pd

#read the csv and print data
pd_alc = pd.read_csv(r"C:\Users\Admin\Desktop\Python\all-data\data\alcohol-consumption\drinks.csv")
#print(pd_alc)
"""
        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
0    Afghanistan              0                0              0                           0.0
1        Albania             89              132             54                           4.9
2        Algeria             25                0             14                           0.7
3        Andorra            245              138            312                          12.4
4         Angola            217               57             45                           5.9
..           ...            ...              ...            ...                           ...
188    Venezuela            333              100              3                           7.7
189      Vietnam            111                2              1                           2.0
190        Yemen              6                0              0                           0.1
191       Zambia             32               19              4                           2.5
192     Zimbabwe             64               18              4                           4.7

[193 rows x 5 columns]"""


#read a particular row in dataframe
print('read a particular row in df')
print(type(pd_alc.iloc[1]))  #Series datatype
print(pd_alc.iloc[1])
"""
<class 'pandas.core.series.Series'>
country                         Albania
beer_servings                        89
spirit_servings                     132
wine_servings                        54
total_litres_of_pure_alcohol        4.9
"""

#dimension of dataframe
print(pd_alc.shape)
#(193,5) - a tuple with row,columns
rows, columns = pd_alc.shape

#size of the dataframe
print(pd_alc.size)
#965 (193 rows * 5 columns)

#how many elements are there in coutry column
print(pd_alc['country'].size)
#total 193 elements in country

#information about dataframe
print(pd_alc.info())
"""
Data columns (total 5 columns):
 #   Column                        Non-Null Count  Dtype
---  ------                        --------------  -----
 0   country                       193 non-null    object
 1   beer_servings                 193 non-null    int64
 2   spirit_servings               193 non-null    int64
 3   wine_servings                 193 non-null    int64
 4   total_litres_of_pure_alcohol  193 non-null    float64
dtypes: float64(1), int64(3), object(1)
memory usage: 7.7+ KB
None
"""

#statistics about numerical columns
print(pd_alc.describe())
"""
       beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
count     193.000000       193.000000     193.000000                    193.000000
mean      106.160622        80.994819      49.450777                      4.717098
std       101.143103        88.284312      79.697598                      3.773298
min         0.000000         0.000000       0.000000                      0.000000
25%        20.000000         4.000000       1.000000                      1.300000
50%        76.000000        56.000000       8.000000                      4.200000
75%       188.000000       128.000000      59.000000                      7.200000
max       376.000000       438.000000     370.000000                     14.400000"""
#country is non numeric (object datatype), hence not part of the output

#unique values of series object
print(type(pd_alc['beer_servings'].unique()))
#returns a numpy array of unique values

pd_rsr = pd.read_csv(r"C:\Users\Admin\Desktop\Python\data\religion-survey\religion-survey-results.csv")
print(pd_rsr['US Region'].unique())
"""<class 'numpy.ndarray'>
['Response' 'East North Central' 'Middle Atlantic' 'South Atlantic'
 'Pacific' 'Mountain' 'West South Central' 'West North Central'
 'East South Central' 'New England' nan]
 """

#count of each value in the column
print(pd_rsr['US Region'].value_counts())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 193 entries, 0 to 192
South Atlantic        196
East North Central    180
Pacific               150
Middle Atlantic       135
West South Central     97
Mountain               74
West North Central     73
New England            67
East South Central     54
Response                1
Name: count, dtype: int64"""

#data cleansing with Pandas
list_of_countries = (
    {'Country Name':'China','ISO Code':'CN','Country Population':1435555},
    {'Country Name':'India','ISO Code':'IND','Country Population':135555},
    {'Country Name':'New Zealand','ISO Code':'NZ','Country Population':323433},
    {'Country Name':'United States','ISO Code':'USA','Country Population':3000000},
    {'Country Name':'Australia','ISO Code':'AUS','Country Population':3500000},
    {'Country Name':'China','ISO Code':'CN','Country Population':1435555},
)

df_countries = pd.DataFrame(list_of_countries)
print(df_countries)







#data frame is mutable or immutable
#new_row = pd_alc.head(2)
#print(type(new_row)) #DataFrame datatype
#print(list(new_row))
#app_row = list(new_row)
#app_row[1] = 'Kailasa'
#print('modified new row')
#print(app_row)
#read the shape of pandas dataframe

