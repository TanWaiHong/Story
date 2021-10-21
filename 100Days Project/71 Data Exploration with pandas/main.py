import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.isna())
clean_df = df.dropna()
print(clean_df.tail())
print(clean_df['Starting Median Salary'])
print(clean_df['Starting Median Salary'].idxmax())
print(clean_df['Undergraduate Major'].loc[43])
print(clean_df['Undergraduate Major'][43])
print(clean_df['Mid-Career 10th Percentile Salary'].idxmax())
print(clean_df['Starting Median Salary'].idxmin())
print(clean_df['Mid-Career 10th Percentile Salary'].idxmin())
print(clean_df.loc[39])
print(clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary'])
print(clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']))
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']]).head()
print(clean_df.groupby('Group').count())
print(clean_df.groupby('Group').mean())
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean())