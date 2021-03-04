import pandas as pd

support_log_grouped = pd.read_csv('support_log_grouped.csv')


def alert_group_importance(row):
    priority = row['alert_group']
    importance = row['importance']

    if importance == 1:

        if priority == 'средний':
            return 'обратить внимание'
        elif priority == 'высокий':
            return 'высокий риск'
        elif priority == 'критичный':
            return 'блокер'
        else:
            return 'в порядке очереди'
    else:
        return 'в порядке очереди'


# print(support_log_grouped.head(10))
# print(support_log_grouped.apply(alert_group_importance, axis=1))

row_values = ['высокий', 1]
row_columns = ['alert_group', 'importance']

row = pd.Series(data=row_values, index=row_columns)
print(row)
