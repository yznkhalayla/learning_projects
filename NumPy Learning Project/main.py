import numpy as np
import pandas as pd
import re # you can do all sorts of weird strings specifying with it

df = pd.read_csv("Pokemon.csv")

print(df.head(3), df.tail(3))
# print(df.columns)
# print(df[["Name", "Total"][0:5]])
# print(df.iloc[0])
# print(df.iloc[:3,1])

# for index, row in df.iterrows(): rows
#     print(index, row["Name"])

# for index, column in df.it

# print(df["Type 1"]=="Grass") # True //
# print(df.loc[df["Type 1"]=="Grass"]) # Actually DataFrame tht correlates with True

# print(df["Name"].str.contains("Mega")) # returns True/False
# print(df.loc[df["Name"].str.contains("Mega")])
# print(df.loc[:,"Name"]) it goes through rows and happens to accept a boolean array of the same length as
                        # the rows -> gives an array with the rows which were opposed with True (single label = row)
                        # -> This is why "df.loc[df["Type 1"]=="Grass"]" works the way it does

# print(df.describe())
# print(df.sort_values(["Name", "Speed"], ascending=[1,0]))

# df = df.drop(columns=["Total"])
# print(df.columns)
#
# df["Total"] = df.iloc[:,4:10].sum(axis=1)
# print(df.Total)

# cols = list(df.columns)
# print(cols)


print(df.loc[df["Name"].str.contains("Mega|Fire", regex=True)])
