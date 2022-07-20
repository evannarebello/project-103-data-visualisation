import pandas as pd
df=pd.DataFrame()
import plotly.express as px
df=pd.read_csv("Copy+of+data+-+data.csv")
fig=px.scatter(df,x="date",y="cases",color="country",title="COVID DATA")
fig.show()