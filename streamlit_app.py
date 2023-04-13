# Find the largest among the 3 given numbers(value greater than the other two).
# Submit the url in the following 

import streamlit as st 
import pandas as pd

st.header("Find Largest Number")

st.write(""" 

Given three numbers, this app finds the largest number among those three

	""")

st.header("Enter the numbers")

def user_input():
	num_1 = st.number_input("Enter First Number")
	num_2 = st.number_input("Enter Second Number")
	num_3 = st.number_input("Enter Third Number")
	# , min_value = -2**30, max_value=2**30

	data = {"First Number" : num_1,
	"Second Number" : num_2,
	"Third Number" : num_3}

	features = pd.DataFrame(data, index=[0])
	return features

df = user_input()

st.subheader("User Input Parameters")
st.write(df.to_dict())

st.table(df)


num_1 = df['First Number'][0]
num_2 = df['Second Number'][0]
num_3 = df['Third Number'][0]

ans = max(num_1, num_2, num_3)

st.write("The maximum number is : ", ans)



