import yfinance as yf
import streamlit as st
import pandas as pd


st.write(
    """
    Shown are the stock closing price and volume of google!
    """             
         )

ticker_symbol = 'GOOGL'
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)









