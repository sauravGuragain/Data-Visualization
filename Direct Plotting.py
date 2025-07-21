
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
"""for line chart"""
import matplotlib.pyplot as plt 
x=[1,2,3,4,5,6,7] 
y=[3,5,7,9,11,13,15] 
line,=plt.plot(x,y) 
print(line) 
line.set_label("y=2x+1") 
line.set_linewidth(4) 
line.set_linestyle("-") 
line.set_color("green") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Line Chart Example") 
plt.legend(loc='upper center') 
plt.show()


""" For bar chart""" 
import matplotlib.pyplot as plt
country=["Nepal", "SriLanka", "Bangladesh", "India", "Bhutan", "Maldives", "Pakistan", "Afghanistan"]
GDP_growth_rate = [4.2, 3.5, 6.1, 5.0, 4.8, 3.7, 3.9, 2.1]
plt.figure(figsize=(9, 4))
plt.bar(country, GDP_growth_rate, label="GDP Growth Rate")
plt.title("GDP Growth Rates of SAARC Countries")
plt.ylabel("GDP Growth Rate")
plt.xlabel("country")
plt.legend()
plt.show()

""""or """""
 
import matplotlib.pyplot as plt 
x1=[3,6,8,11,13,14,17,19,21,24,33,37] 
y1=[7.5,12,13.2,15,17,22,24,37,34,38.5,42,47] 
x2=[3,6,8,11,13,14,17,19,21,24,33] 
y2=[50,45,33,24,21.5,19,14,13,10,6,3] 
plt.plot(x1,y1, label='First Line') 
plt.plot(x2, y2, label='Second Line') 
plt.xlabel('Plot Number') 
plt.ylabel('Important var') 
plt.title('Interesting Graph\n2018 ') 
plt.yticks([0,5,10,15,20,25,30,35,40,45,50], 
['0B','5B','10B','15B','20B','25B','30B','35B', 
'40B','45B','50B']) 
plt.legend() 
plt.show() 

""" Histogram"""

import numpy as np 
import matplotlib.pyplot as plt 
x = np.random.normal(170, 10, 250) 
plt.figure(figsize=(4,3)) 
plt.hist(x, bins=10, color='Blue', alpha=0.5) 
plt.show() 

import matplotlib.pyplot as plt 
import pandas as pd 
flights = pd.read_csv('/content/drive/My Drive/Data/flights.csv') 
plt.figure(figsize=(9,7)) 
plt.hist(flights['arr_delay'], color = 'blue', edgecolor = 'black', bins 
=20) 
plt.show() 

"""scatter plot """
import matplotlib.pyplot as plt 
scores =[80, 90, 75, 80, 90, 50, 65, 85, 40, 100] 
teams=['A','B','C','D','E','E','F','G','H','I']  
plt.scatter(teams, scores, c ="blue", linewidths=0.25) 
plt.title("Game Scores") 
plt.xlabel("Team") 
plt.ylabel("Scores") 
plt.show() 

import matplotlib.pyplot as plt 
ngames =[3, 5, 2, 6, 7, 1, 2, 7, 1, 7] 
scores =[80, 90, 75, 80, 90, 50, 65, 85, 40, 100] 
teams=['A','B','C','D','E','E','F','G','H','I']  
plt.scatter(ngames, scores, c ="blue", marker='*', linewidths=0.25, 
label="Team Scores") 
plt.title("Game Scores") 
plt.xlabel("#Games") 
plt.ylabel("Scores") 
plt.legend() 
 
#Labeling Scatter plot 
for i,txt in enumerate(teams): 
    plt.annotate(txt, (ngames[i], scores[i])) 
  
plt.show() 


"""Stack plots"""
import matplotlib.pyplot as plt 
days = [1,2,3,4,5] 
sleeping = [7,8,6,11,7] 
eating = [2,3,4,3,2] 
working = [7,8,7,2,2] 
playing = [8,5,7,8,13] 
plt.stackplot(days, sleeping, eating,working,playing, colors =['r', 
'g','b','c']) 
plt.xlabel('Days') 
plt.ylabel('No of Hours') 
plt.title('Daily Activities') 
plt.show() 


