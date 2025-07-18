import yfinance as yf
import pandas as pd

def get_hourly_data():
    df = yf.download("USDBRL=X", interval="60m", period="7d")
    return df
