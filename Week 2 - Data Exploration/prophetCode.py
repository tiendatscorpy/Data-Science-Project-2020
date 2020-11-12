import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
df = pd.read_csv('gases.csv')
df.head()

df_prophet = pd.DataFrame()
df_prophet['ds'] = df[df['country_or_area'] == 'Finland']['year'].values
df_prophet['y'] = df[df['country_or_area'] == 'Finland']['value'].values
m = Prophet()
m.fit(df_prophet)
future = m.make_future_dataframe(periods=36)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
from fbprophet.plot import plot_plotly, plot_components_plotly

plot_plotly(m, forecast)
plot_components_plotly(m, forecast)
