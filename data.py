import pandas as pd
import plotly.graph_objects as go
import csv
df=pd.read_csv('student_data.csv')

student_df=df.loc[df['student_id']=='TRL_xsl']
print(student_df.groupby('level')['attempt'].mean())

fig=go.Figure(go.Bar(x=student_df.groupby('level')['attempt'].mean(),
y=["level1","level2","level3","level4"],orientation='h'))
fig.show()