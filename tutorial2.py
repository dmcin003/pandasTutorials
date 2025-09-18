import pandas as pd

titantic = pd.read_csv("data/titantic.csv")

print(titantic)
print(titantic.head(8))
print(titantic.dtypes)

titantic.to_excel("titantic.xlsx", sheet_name="passengers", index=False)
print(titantic.head())
print(titantic.info())