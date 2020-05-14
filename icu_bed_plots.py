# pip install plotly
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('./ICU_beds_2018_2019.csv')

fip_codes_df = pd.read_csv('./county_fips.csv', encoding = "ISO-8859-1")

fip_codes_df['county_name'] = fip_codes_df['county_name'].apply(lambda x: x.replace(' County', ''))

fip_codes = fip_codes_df.set_index('county_name')['fips'].to_dict()


df['county_fips_code'] = df['County'].apply(lambda x: fip_codes.get(x))


df_county = df[pd.notnull(df['county_fips_code'])]


icu_by_state = df.groupby('State')[['ICU Beds']].sum()

plt.figure(figsize=(15, 10))
ax = sns.barplot(x='ICU Beds', y='State', data=icu_by_state.reset_index().sort_values(by=['ICU Beds'], ascending=False))


plt.show(	)

df = (icu_by_state.reset_index().sort_values(by=['ICU Beds'], ascending=False))

df = df[(df['State'] == 'California') | (df['State'] == 'Illinois') | (df['State'] == 'New Jersey') | (df['State'] == 'New York') | (df['State'] == 'Massachusetts')]

plt.figure(figsize=(15, 10))
ax = sns.barplot(x='ICU Beds', y='State', data=df)


plt.show(	)