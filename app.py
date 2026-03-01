import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

st.title("📊 Interactive Data Analytics Dashboard")

st.write("Upload any CSV file to analyze and visualize your data.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    # Read dataset
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Show dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Show basic info
    st.subheader("Dataset Information")
    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Numeric Columns", len(df.select_dtypes(include='number').columns))

    # Select columns for visualization
    numeric_columns = df.select_dtypes(include='number').columns.tolist()

    if len(numeric_columns) >= 1:

        st.subheader("Visualization")

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Histogram", "Scatter Plot", "Line Chart"]
        )

        if chart_type == "Histogram":

            column = st.selectbox("Select column", numeric_columns)
            fig = px.histogram(df, x=column)
            st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Scatter Plot":

            col1, col2 = st.columns(2)
            x_col = col1.selectbox("X-axis", numeric_columns)
            y_col = col2.selectbox("Y-axis", numeric_columns)

            fig = px.scatter(df, x=x_col, y=y_col)
            st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Line Chart":

            column = st.selectbox("Select column", numeric_columns)
            fig = px.line(df, y=column)
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("No numeric columns found for visualization.")

else:
    st.info("Please upload a CSV file to begin analysis.")