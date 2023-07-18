import numpy
import matplotlib
import matplotlib.pyplot as plt

# Data
categories = ['has_nested', 'not_nested']
values = [2660, 214]

# Plotting the bar graph
plt.bar(categories, values)

# Adding labels and titles
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Nested vs Not Nested')

# Displaying the graph
plt.show()
