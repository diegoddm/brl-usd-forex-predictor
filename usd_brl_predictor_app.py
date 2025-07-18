import streamlit as st
import pandas as pd
import numpy as np
from utils.model import build_and_train_model
from utils.preprocess import get_hourly_data
from utils.news_scraper import get_news

st.set_page_config(layout="wide")
st.title("BRL/USD AI Forex Predictor")

data = get_hourly_data()
model, scaler = build_and_train_model(data['Close'].values.reshape(-1, 1))

# Display chart
st.line_chart(data['Close'])

# Display news
st.markdown("### Relevant News")
for item in get_news():
    st.markdown(f"[{item['title']}]({item['link']}) — {item['published']}")
