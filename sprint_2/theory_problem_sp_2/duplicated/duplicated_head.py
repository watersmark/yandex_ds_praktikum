import pandas as pd
from pymystem3 import Mystem
feedback = pd.read_csv('feedback.csv')

lemmatize_text = Mystem()
lemmas = lemmatize_text.lemmatize(feedback['text'][1])
print(lemmas)
