import pandas as pd

first = pd.DataFrame([['kolan', 23, 'tt'], ['kopan', 23, 'rr'], ['topan', 44, 'qw'],], columns=['name', 'age', 'category'])
second = pd.DataFrame([['kolan', 23, 'tt', 'ss'], ['rkopan', 889, 'rr'], ['stopan', 44, 'qw'],], columns=['name', 'age', 'category', 'dop_val'])


data_name = first.merge(second, on='name', how='left')
print(data_name)
