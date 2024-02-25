import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
'''
For linear regression analysis to predict survivability on the Titanic dataset, we need to process the data to make it suitable for modeling. Here's a step-by-step approach:

Handle Missing Data: Identify and impute or drop missing values.
Feature Engineering: Extract and create relevant features that could have an impact on the outcome.
Encode Categorical Variables: Convert categorical variables into a format that can be provided to machine learning algorithms (e.g., one-hot encoding).
Normalize Data: Scale features to ensure they have similar scales, which helps with the regression algorithm.
Remove Unnecessary Columns: Drop columns that aren't useful for the regression analysis.

'''
# read in Titanic data set
train = ????
st.write("Titanic Data")


# Clean the data 
# Change survived to 0 or 1
train['Survived'] = train['Survived'].replace('No', 0)
train['Survived'] = train['Survived'].replace('Yes', 1)

# Convert 'Sex' column to numeric values
train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
