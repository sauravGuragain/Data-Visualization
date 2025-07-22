""" Line chart simple - to show trend over time or for continuous data  """

import matplotlib.pyplot as plt
x=[1,2,3,4,5] #no of days 
y=[10,20,30,40,50] #no of sales 

plt.plot(x,y)
plt.title("Daily Sales")
plt.xlabel("Din")
plt.ylabel("Sales")
plt.show()


""" Bar chart - this is used to compare catagories"""
import matplotlib.pyplot as plt

fruits=['Apple', 'Banana' , 'Cherry' ,'Mango']
values=['100','110','50','60']

plt.bar(fruits,values)
plt.title("Fruits Price")
plt.ylabel("Price of fruit")
plt.show()

"""Pie Chart to show percentage among whole """
import matplotlib.pyplot as plt
label=['Car','Bus','Bikes']
values=['20','30','50']

plt.pie(values,labels=label )
plt.title("Vehicle occupying road")
plt.show()

"""Scatter Plot is used to show relationship between two variables"""
x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 6, 3]

plt.scatter(x, y)
plt.title("Scatter Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

"""Box Plot - To show data spread, median, and outliers """
import matplotlib.pyplot as plt
data=[1,2,3,4,5]

plt.boxplot(data)
plt.title("Box plot ")
plt.xlabel('Data')
plt.show()

"""Histogram - it is used to show distribution of datas """
import matplotlib.pyplot as plt

Age=[10,20,15,30,40]

plt.hist(Age,bins=5)
plt.title("histogram ")
plt.xlabel('Age')
plt.show()

"""Stack Plot"""
import matplotlib.pyplot as plt
day = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 2, 3, 2, 2]
working = [8, 7, 7, 8, 7]
playing = [7, 7, 8, 3, 8]
plt.stackplot(day, sleeping ,eating ,working , playing , labels =['sleeping ,eating ,working , playing'])
plt.title("Activity over 5 days in Stack Plot")
plt.legend(loc='upper center')
plt.xlabel=('day')
plt.ylabel('Hours')
plt.show()

"""Adding Text to Charts Text and annotate"""
plt.plot([1,2,3,4],[5,6,8,9])
plt.text(2,6, "this is a point (2,6)")
plt.show()

"""annotate"""
# %%

plt.plot([1, 2, 3], [3, 6, 9])
plt.annotate('Max Point', xy=(3, 9), xytext=(2, 10),
             arrowprops=dict(facecolor='blue', shrink=0.05))
plt.show()

# %%
"""Heatmap with Matplotlib"""
import matplotlib.pyplot as plt
import numpy as np 
data=np.array([[10,20,30],
               [30,40,50],
               [50,60,70]])
plt.imshow(data, cmap='hot',interpolation='nearest')
plt.title('Heatmap')
plt.colorbar()
plt.show()
# %%


"""Multiple Charts in the Same Plot (Subplots)"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [30, 25, 20, 15]

plt.subplot(1, 2, 1)   # 1 row, 2 columns, chart 1
plt.plot(x, y1)
plt.title("Chart 1")

plt.subplot(1, 2, 2)   # 1 row, 2 columns, chart 2
plt.plot(x, y2)
plt.title("Chart 2")

plt.tight_layout()
plt.show()
# %%
"""for  3 Charts  to subplots """
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]
y3 = [5, 3, 6, 2, 4]

plt.subplot(1,3,1)
plt.plot(x,y1)
plt.title("chart 1")

plt.subplot(1,3,2)
plt.plot(x,y2)
plt.title("chart 2")

plt.subplot(1,3,3)
plt.plot(x,y3)
plt.title("chart 3")
plt.tight_layout()
plt.show()
# %%


"""if we have to create a 4 chart subplots"""
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]
y3 = [5, 3, 6, 2, 4]
y4 = [9, 2, 1, 4, 1]

plt.subplot(1,4,1)
plt.plot(x,y1)
plt.title("1st chart")

plt.subplot(1,4,2)
plt.plot(x,y2)
plt.title("2nd. chart")
plt.subplot(1,4,3)
plt.plot(x,y3)
plt.title("3rd. chart")

plt.subplot(1,4,4)
plt.plot(x,y4)
plt.title("4rth chart")

plt.tight_layout()
plt.show()

# %%

""""Starting Seaborn"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "day": ["Mon", "Mon", "Tue", "Tue", "Wed", "Wed"],
    "sales": [100, 120, 130, 110, 90, 80]
}
df = pd.DataFrame(data)

sns.stripplot(x='day',y='sales',data=df)
plt.title("Custom Strip Plot")
plt.show()