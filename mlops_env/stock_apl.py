import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyzer!")

# User input for ticker symbol
symbol = st.text_input("Please enter the ticker", "AAPL")


col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter the start date", datetime.date(2023, 10, 3))
with col2:
   end_date = st.date_input("Please enter the end date", datetime.date(2024, 10, 3))

# Get stock data for the given ticker and date range
ticker_data = yf.Ticker(symbol)

# Use the actual values of start_date and end_date, not strings
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

# Display the raw day-wise stock price data
st.write("Here is the raw day-wise stock price data:")
st.dataframe(ticker_df)

# Plot the stock price movement over time (Close price)
st.write("Price movement over time:")
st.line_chart(ticker_df['Close'])

# Plot the volume movement over time
st.write("Volume movement over time:")
st.line_chart(ticker_df['Volume'])
