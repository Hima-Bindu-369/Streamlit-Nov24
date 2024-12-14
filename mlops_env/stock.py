import streamlit as st
import yfinance as yf
st.title("Stock Price Analyzer! ")

import yfinance as yf

# Example: Get stock data for a particular ticker (e.g., Apple)
ticker_data = yf.Ticker("MSFT")

ticker_df = ticker_data.history(period="1d", start="2023-12-02", end="2024-12-02")

st.write("Here is the raw day wise stock price.")
st.dataframe(ticker_df)

st.write("Price movement over time")
st.line_chart(ticker_df['Close'])

st.write("Volume movement over time")
st.line_chart(ticker_df['Volume'])
