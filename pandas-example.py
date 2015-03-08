import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect("./db.sqlite3")
df = pd.read_sql("SELECT * from survey_sentence order by rating", con)
print df['rating'].value_counts().plot(kind='bar')
plt.show()
