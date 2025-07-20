""" bar chart line chart using plot"""
import pandas as pd
df = pd.DataFrame({'Item1':[22,15,16,11,18],'Item2':[10,9,17,18,21]})
df.plot.line()

import pandas as pd
df =pd.DataFrame({'Item1':[22, 15, 470, 660, 1876],'Item2':[500, 1200, 1600, 2100, 2400]},index=[2020,2021,2022,2023,2024])
df.plot.bar()

"""pie chart """

import pandas as pd
df = pd.DataFrame({'LH Seats': [88, 79, 32, 21, 14, 10], 'UH Seats': [16, 11, 18, 0, 0, 8]}, index=['NC', 'UML', 'MC', 'R3P', 'RPP', 'US'])
df.plot.pie(y='LH Seats')

"""Scatter Plot"""
import pandas as pd
df =pd.DataFrame({'Item1': [22, 15, 470, 660, 1766], 'Item2': [500, 1200, 1600, 2100, 2400], 'Year': [2020, 2021, 2022, 2023, 2024]})
df.plot.scatter(x="Year", y="Item2", title="Item1 vs. Year Sales")

"""boxplot"""
import pandas as pd
df = pd.DataFrame({'Item1': [22, 15, 470, 660, 1766]})
df.plot.box()

"""Histogram"""
import pandas as pd
df = pd.DataFrame({'Item1': [22, 15, 470, 660, 1766]})
df.plot.hist(bins=5)

"""Now using matplotlib"""

