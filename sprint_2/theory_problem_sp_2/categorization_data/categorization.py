import pandas as pd

support = pd.read_csv('support_upd.csv')
support_dict = support[['type_message', 'type_id']]

support_dict = support_dict.drop_duplicates().reset_index(drop=True)
print(support_dict.sort_values('type_id'))
