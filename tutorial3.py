import pandas as pd

titantic = pd.read_csv("data/titantic.csv")
ages = titantic["Age"]
print(ages.head())
print(type(titantic["Age"]))
print(titantic['Age'].shape)
age_sex = titantic[['Age','Sex']]
print(age_sex)
print(type(age_sex))
print(age_sex.shape)
above_35 = titantic[titantic['Age'] > 35]
print(above_35.head())
print(above_35.shape)
class_23 = titantic[titantic['Pclass'].isin([2,3])]
print(class_23.head())
class_23 = titantic[(titantic['Pclass'] == 2) | (titantic['Pclass'] == 3)]
print(class_23.head())
age_no_na = titantic[titantic['Age'].notna()]
print(age_no_na.head())
print(age_no_na.shape)

adult_names = titantic.loc[titantic['Age'] > 35,'Name']
print(adult_names.head())

print(titantic.iloc[9:25,2:5])
titantic.iloc[0:3,3] = 'anonymous'
print(titantic.head())
