import pandas as pd

metrica = pd.read_csv('metrica_data.csv')
age_avg = metrica['age'].mean()

desktop_data = metrica.loc[metrica['device_type'] == 'desktop']
mobile_data = metrica.loc[metrica['device_type'] == 'mobile']
mobile_data_time_avg = mobile_data['time'].mean()
print(mobile_data_time_avg)