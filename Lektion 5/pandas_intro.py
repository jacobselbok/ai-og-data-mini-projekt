# Chapter 1
import pandas as pd

# Chapter 2
series = pd.Series(data=["UK", "France", "Italy"], index = ["a", "b", "c"], name = "Country")

print(series)

series_array = series.to_numpy()
print(type(series_array))
print(series_array)

series_list = series.to_list()
print(type(series_list))
print(series_list)

# Chapter 3
data = [["UK", "London"], ["France", "Paris"], ["Italy", "Rome"]]
prefixes = ["+44", "+33", "+39"]
col_names = ["country", "capital"]
df = pd.DataFrame(data=data, index = prefixes, columns = col_names)
print(df)

df = pd.read_csv(r"Lektion 5\capitals.csv", dtype=str)

print(df)

df = pd.read_csv(r"Lektion 5\pokemon.csv", dtype=str)

print(len(df.columns))
print(list(df.columns))
print(df.dtypes)
print(df.shape[0])
print(type(df.dtypes))
print(type(df.columns))
print(type(list(df.columns)))

print(df.head(20))
print(df.tail(10))

# Chapter 4
df.rename(columns = {"Sp. Atk": "Special Attack",
                     "Sp. Def": "Special Defense"})

name_column = df["Name"]
print(type(name_column))
name_column.head(20)

columns_df = df[["Name", "Type 1", "Type 2"]] 
print(type(columns_df))
columns_df.head(20)

df = pd.read_csv(r"Lektion 5\pokemon.csv", index_col="Name")
df.head(10)

charmeleon_series = df.loc["Charmeleon"]
print(type(charmeleon_series))

print(charmeleon_series)

charmeleon_series = df.iloc[5]
print(charmeleon_series)

df.head()

pokemon_subset = df.loc["Ivysaur":"Charmander"]
print(len(pokemon_subset))

print(pokemon_subset)

pokemon_subset = df.iloc[1:4]
print(len(pokemon_subset)) 

print(pokemon_subset)

print(df.loc[:, "Type 1"])

print(df.loc[:, ["Type 1", "Generation"]]) 

print(df.loc[["Squirtle", "Pikachu"], ["Type 1", "Generation"]])

print(df.iloc[1:3, -4:-2])

df["Speed"].describe()

df["Type 1"].describe()

df["Type 1"].value_counts()

for col in df:
    print(col)

for (key, value) in df.items():
    print(key, value)

for (row_index, row) in df.iterrows():
    print(row_index, row)

for row in df.itertuples():
    print(row)

# Chapter 5
condition_series = (df["Type 1"] == "Grass")
condition_series.head()

filtered_df = df[df["Type 1"] == "Grass"]
filtered_df.head(10)

df[df["Type 1"].isin(["Water", "Fire"])].head(10)

filtered_df = df[(df["Type 1"] == "Psychic") & 
                    (df["Generation"] <=3) & 
                    (df["Legendary"] == True)]
filtered_df = filtered_df[["Type 1", "Type 2", "Generation"]]
print(filtered_df)

filtered_df = df[(df["Type 1"] == "Water")
                 & (df["Type 2"] == "Dragon")]
print(filtered_df)

filtered_df = df[(df["Type 1"] == "Eelctric")
                 & (df["Type 2"] == "Ice")]
print(filtered_df)

df.info()

df.isna().sum()

null_type2 = df[df["Type 2"].isna()]
print(null_type2)

print(df.shape)

clean_df = df.dropna()  # Drop all rows with null!
print(clean_df.shape)

print(df.shape)

clean_df = df.dropna(axis=1)  # Drop columns with NA values
print(clean_df.shape)

df.dropna(inplace=True)
print(df.shape) 

df = pd.read_csv(r"Lektion 5\pokemon.csv", index_col="Name")
df["Type 2"].fillna("Standard", inplace=True)

print(df.isna().sum())

# Chapter 6
df = pd.read_csv(r"Lektion 5\pokemon.csv", index_col="Name")
print(df.shape)

df = pd.DataFrame(data=df.values, columns=df.columns)
print(df.shape)

doubled_df = df._append(df)
print(doubled_df.shape)

df = pd.read_csv(r"Lektion 5\pokemon.csv", index_col="Name")
print(df.shape)

df.drop_duplicates(inplace=True)
print(df.shape)

def standardise(data):
    return (data - data.mean()) / data.std()

df = pd.read_csv(r"Lektion 5\pokemon.csv", index_col="Name")
df[["Attack", "Defense"]] = df[["Attack", "Defense"]].apply(standardise)
print(df)

df["Type 1"] = df["Type 1"].apply(lambda x:x.upper())
print(df)

import matplotlib.pyplot as plt
df = pd.read_csv(r"Lektion 5\pokemon.csv", index_col="Name")
fig = plt.figure()
axis = df["Defense"].plot.hist()
plt.show()

# Chapter 7
df = pd.read_csv(r"Lektion 5\football.csv", index_col="Team")
print(len(df.index))

for team in df.index:
    print(df[df.index == team])

print(df["Yellow Cards"].sum())
print(df["Red Cards"].sum())

print(df[df["Goals"] > 5])

print(df[df["Goals"] > 5].sort_values(by="Goals", ascending=False))

print(df[df["Shots on target"] > df["Shots off target"]])

print(df[df["Yellow Cards"] + df["Red Cards"] > 7])
