import pandas as pd

data = {
    'Name': ['Ali', 'Hassan', 'Waleed', 'Shahnawaz', 'Ayesha', 'Zara', 'Ahmed'],
    'Age': [18, 15, 14, 17, 16, 13, None],
    'Salary': [30000, 20000, 22000, 250000, None, 43000, 12000]
}

df = pd.DataFrame(data)
print("Original Data")
print(df)

print(df.isnull().sum())
df_drop = df.dropna()
print(df_drop)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)