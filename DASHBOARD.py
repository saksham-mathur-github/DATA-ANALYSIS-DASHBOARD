#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[3]:
!pip install plotly

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Function to preprocess the uploaded DataFrame
def preprocess_data(df):
    # Handle missing values by filling with zeros
    df.fillna(0, inplace=True)

    # Convert numeric columns to appropriate data types (optional, adjust based on your data)
    numeric_cols = df.select_dtypes(include=[int, float]).columns
    df[numeric_cols] = df[numeric_cols].astype(float)

    return df

# Function to create a Line Chart using Plotly
def create_line_chart(df):
    st.subheader("Line Chart")

    # Choose columns for visualization
    x_col = st.selectbox("Select X Axis", df.columns)
    y_col = st.selectbox("Select Y Axis", df.columns)
    color_col = st.selectbox("Select Color Column", df.columns)

    fig_line_chart = px.line(df, x=x_col, y=y_col, color=color_col, title='Line Chart')
    st.plotly_chart(fig_line_chart)

# Function to create a Bar Chart using Plotly
def create_bar_chart(df):
    st.subheader("Bar Chart")

    # Choose columns for visualization
    x_col = st.selectbox("Select X Axis", df.columns)
    y_col = st.selectbox("Select Y Axis", df.columns)
    color_col = st.selectbox("Select Color Column", df.columns)

    fig_bar_chart = px.bar(df, x=x_col, y=y_col, color=color_col, title='Bar Chart')
    st.plotly_chart(fig_bar_chart)

# Function to create a Scatter Plot using Plotly
def create_scatter_plot(df):
    st.subheader("Scatter Plot")

    # Choose columns for visualization
    x_col = st.selectbox("Select X Axis", df.columns)
    y_col = st.selectbox("Select Y Axis", df.columns)
    color_col = st.selectbox("Select Color Column", df.columns)
    size_col = st.selectbox("Select Size Column", df.columns)

    fig_scatter_plot = px.scatter(df, x=x_col, y=y_col, color=color_col, size=size_col, title='Scatter Plot')
    st.plotly_chart(fig_scatter_plot)

# Function to create a Pie Chart using Plotly
def create_pie_chart(df):
    st.subheader("Pie Chart")

    # Choose columns for visualization
    labels_col = st.selectbox("Select Labels Column", df.columns)
    values_col = st.selectbox("Select Values Column", df.columns)

    fig_pie_chart = px.pie(df, names=labels_col, values=values_col, title='Pie Chart')
    st.plotly_chart(fig_pie_chart)

# Function to create a Doughnut Chart using Plotly
def create_doughnut_chart(df):
    st.subheader("Doughnut Chart")

    # Choose columns for visualization
    labels_col = st.selectbox("Select Labels Column", df.columns)
    values_col = st.selectbox("Select Values Column", df.columns)

    fig_doughnut_chart = px.pie(df, names=labels_col, values=values_col, hole=0.4, title='Doughnut Chart')
    st.plotly_chart(fig_doughnut_chart)

# Function to create a Gauge Chart using Plotly
def create_gauge_chart(df):
    st.subheader("Gauge Chart")

    # Choose columns for visualization
    value_col = st.selectbox("Select Value Column", df.columns)

    fig_gauge_chart = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df[value_col].iloc[0],
        title={'text': "Gauge Chart"},
        gauge={'axis': {'range': [None, df[value_col].max()]}}
    ))

    st.plotly_chart(fig_gauge_chart)

# Function to create a Funnel Chart using Plotly
def create_funnel_chart(df):
    st.subheader("Funnel Chart")

    # Choose columns for visualization
    labels_col = st.selectbox("Select Labels Column", df.columns)
    values_col = st.selectbox("Select Values Column", df.columns)

    fig_funnel_chart = px.funnel(df, x=values_col, y=labels_col, title='Funnel Chart')
    st.plotly_chart(fig_funnel_chart)

# Function to create Power View using Plotly
def create_power_view(df):
    st.subheader("Power View")

    # Choose columns for visualization
    x_col = st.selectbox("Select X Axis", df.columns)
    y_col = st.selectbox("Select Y Axis", df.columns)
    color_col = st.selectbox("Select Color Column", df.columns)
    size_col = st.selectbox("Select Size Column", df.columns)

    # Check if X and Y columns are numeric for scatter plot
    if df[x_col].dtype in [int, float] and df[y_col].dtype in [int, float]:
        fig_power_view = px.scatter(df, x=x_col, y=y_col, color=color_col, size=size_col, title='Power View')
    else:
        fig_power_view = px.bar(df, x=x_col, y=y_col, color=color_col, title='Power View')

    st.plotly_chart(fig_power_view)

# Function to create Power Map using Plotly
def create_power_map(df):
    st.subheader("Power Map")

    # Choose columns for visualization
    x_col = st.selectbox("Select X Axis", df.columns)
    y_col = st.selectbox("Select Y Axis", df.columns)
    z_col = st.selectbox("Select Z Axis", df.columns)
    color_col = st.selectbox("Select Color Column", df.columns)
    size_col = st.selectbox("Select Size Column", df.columns)

    # Create a 3D scatter plot with selected columns
    fig_power_map = px.scatter_3d(df, x=x_col, y=y_col, z=z_col, color=color_col, size=size_col, title='Power Map')
    st.plotly_chart(fig_power_map)

# Function to perform Power Query operations (Placeholder)
def perform_power_query(df):
    # Placeholder function, return DataFrame unchanged for now
    return df

# Function to perform Power Pivot operations (Placeholder)
def perform_power_pivot(df):
    # Placeholder function, return DataFrame unchanged for now
    return df

# Main Streamlit app code
def main():
    st.title("Data Analysis Dashboard")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            # Read the data from the uploaded file
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)

            # Preprocess the data
            df = preprocess_data(df)

            st.write("Sample Data:")
            st.dataframe(df.head())

            # Store the original data
            original_df = df.copy()

            # Perform Power Query operations
            df = perform_power_query(df)

            st.write("Transformed Data:")
            st.dataframe(df)

            # Perform Power Pivot operations (Data Modeling)
            df = perform_power_pivot(df)

            # Select visualization type for the original data
            st.subheader("Visualization for Original Data")
            visualization_type = st.selectbox("Select Visualization Type", ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart",
                                                                             "Doughnut Chart", "Gauge Chart", "Funnel Chart", "Power View", "Power Map"])

            if visualization_type == "Line Chart":
                create_line_chart(original_df)
            elif visualization_type == "Bar Chart":
                create_bar_chart(original_df)
            elif visualization_type == "Scatter Plot":
                create_scatter_plot(original_df)
            elif visualization_type == "Pie Chart":
                create_pie_chart(original_df)
            elif visualization_type == "Doughnut Chart":
                create_doughnut_chart(original_df)
            elif visualization_type == "Gauge Chart":
                create_gauge_chart(original_df)
            elif visualization_type == "Funnel Chart":
                create_funnel_chart(original_df)
            elif visualization_type == "Power View":
                create_power_view(original_df)
            elif visualization_type == "Power Map":
                create_power_map(original_df)

        except pd.errors.ParserError:
            st.error("Error: Unable to parse the uploaded file. Please ensure it is a valid CSV or Excel file.")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
       


# In[ ]:





# In[ ]:





# In[ ]:




