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

