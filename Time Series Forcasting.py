"""Loading the AirPassengers Dataset from Stats Model for Time Series forcasting"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = sm.datasets.get_rdataset("AirPassengers", "datasets").data
data.index = pd.date_range(start="1949-01", periods=len(data), freq="ME")
ts = data["value"] 
ts.plot(title="Monthly Air Passengers (1949–1960)")
plt.ylabel("Passengers (1000s)")
plt.show()

# %%

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(ts, lags=40)
plot_pacf(ts, lags=40)
plt.show()

# %%

"""Univariant Time Series Forecasting, AR Model Using statsmodels """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error

np.random.seed(1)
sales = np.random.randint(80, 140, size=100)
ts = pd.Series(sales)

train, test = ts[:-10], ts[-10:]
model = AutoReg(train, lags=3)
model_fit = model.fit()

predictions = model_fit.predict(start=len(train), end=len(ts)-1)
plt.plot(test.values, label='Actual')
plt.plot(predictions, label='Predicted')
plt.title("AR Model Forecast")
plt.legend()
plt.show()

mse = mean_squared_error(test, predictions)
rmse = np.sqrt(mse)
print("RMSE:", rmse)

# %%
"""Using VAR to see what and how other influence series"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR
np.random.seed(42)

dates = pd.date_range(start='2015-01', periods=100, freq='ME')
ads = np.random.normal(loc=2000, scale=300, size=100)  
sales = 50 + 0.5 * ads + np.random.normal(scale=100, size=100)  

df = pd.DataFrame({'Ads': ads, 'Sales': sales}, index=dates)

df.plot(title="Sales vs Ads over Time", figsize=(10,5))
plt.show()

df_diff = df.diff().dropna()

df_diff.plot(title="Differenced Sales and Ads", figsize=(10,5))
plt.show()

model = VAR(df_diff)
lag_selection = model.select_order(maxlags=15)
print(lag_selection.summary())
fitted_model = model.fit(lag_selection.aic)
forecast_input = df_diff.values[-lag_selection.aic:]
forecast = fitted_model.forecast(y=forecast_input, steps=5)

forecast_df = pd.DataFrame(forecast, columns=['Ads_forecast', 'Sales_forecast'])
print(forecast_df)

last_known = df.iloc[-1]
forecast_original = forecast_df.cumsum() + last_known
print(forecast_original)
# %%


