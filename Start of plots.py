""" Line chart simple - to show trend over time or for continuous data  """

import matplotlib.pyplot as plt
x=[1,2,3,4,5] #no of days 
y=[10,20,30,40,50] #no of sales 

plt.plot(x,y)
plt.title("Daily Sales")
plt.xlabel("Days")
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




