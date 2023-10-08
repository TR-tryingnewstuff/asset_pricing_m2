#%%
import pandas as pd
import numpy as np
import yfinance as yf
from statsmodels.regression.linear_model import OLS

df = yf.Ticker('^SPX').history(start='2020-01-01')['Close']
df.index = df.index.tz_localize(None)


factors = pd.read_csv('macroeconomic_data.csv')
factors.date = pd.to_datetime(factors.date)


df = pd.merge(df, factors, how='left', left_index=True, right_on='date').set_index('date')
df['pct_change'] = df.Close.pct_change(1)

df = df.drop('Close', axis=1).dropna()
# %%

# https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.RegressionResults.html#statsmodels.regression.linear_model.RegressionResults
# See the above link for further 'results' class methods

model = OLS(df['pct_change'], df.drop('pct_change', axis=1))
results = model.fit()
results.params, results.pvalues, results.conf_int(), results.HC0_se
# %%
