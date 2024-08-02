import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """ 
       # stock price analyser
       
       shown are the stock prices of Reliance 
       """ 
         )

ticker_symbol=st.text_input("ENter a stock symbol","AAPL",key="Placeholder")
col1,col2=st.columns(2)
with col1:
    start_date=st.date_input("Input starting data",datetime.date(2019,1,1))
with col2:
    end_date=st.date_input("Input ending data",datetime.date(2020,12,1))
ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",start=f"{start_date}",end=f"{end_date}")
st.dataframe(ticker_df)
st.write(
    f"""{ticker_symbol}
        Daily closing price chart
       """ 
         )

st.line_chart(ticker_df.Close)

st.write(
    """
       # Daily Volume chart
       """ 
         )

st.line_chart(ticker_df.Volume)



