import pandas as pd

def alert_group(messages):
    if messages <= 300:
        return 'средний'
    elif 301 <= messages <= 500:
        return 'высокий'
    else:
        return 'критичный'

support_log = pd.read_csv('support_log.csv')
support_log_grouped = support_log.groupby('type_id').count()

# print(support_log_grouped)

support_log_grouped['alert_group'] = support_log_grouped['user_id'].apply(alert_group)
print(support_log_grouped.head(10))

print(support_log_grouped.groupby('alert_group')['user_id'].sum())

