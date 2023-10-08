#%%
from full_fred.fred import Fred
import pandas as pd
import numpy as np

fred = Fred('/home/fast-pc-2023/Téléchargements/python/light_gbm_tests-main/api_key.txt')



indicators = ['DTB4WK','TCU','UNRATE','RECPROUSM156N','T10Y3M'] # interest rates, total capacity utilization, unemployment rate, diff of 10Y and 3M annual interest rate (yield curve)


df = pd.DataFrame()
for i in indicators:
    df_else = fred.get_series_df(i).drop(['realtime_start','realtime_end'], axis=1)
    df_else['date'] = pd.to_datetime(df_else['date'])
    df_else = df_else.set_index('date', drop=True)
    if len(df) == 0:
        df = pd.concat([df_else, df], axis=1)
    else:
        df = pd.concat([df, df_else], axis=1)

df.columns = indicators
df = df.replace('.',np.nan).astype('Float64').ffill()
print(df.describe(), df)
df.to_csv('macroeconomic_data.csv')


# %%
df.describe()
# %%