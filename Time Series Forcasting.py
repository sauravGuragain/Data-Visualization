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
