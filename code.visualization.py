# Original code prior to streamlit integration
'''import numpy
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
'''
#Streamlit integration code
import streamlit as st
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Data
categories = ['has_nested', 'not_nested']
values = [2660, 214]

# Function to create the bar graph
def create_bar_graph():
    # Plotting the bar graph
    plt.bar(categories, values)

    # Adding labels and titles
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Nested vs Not Nested')

    # Returning the figure for Streamlit to display
    return plt

# Streamlit app code
def main():
    st.title('Bar Graph Example')
    
    # Create the bar graph using the defined function
    fig = create_bar_graph()

    # Display the graph using Streamlit
    st.pyplot(fig)

if __name__ == '__main__':
    main()
