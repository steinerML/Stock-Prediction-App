import streamlit as st
from datetime import date
import time

#In case you get any 'ModuleNotFoundError' try to update the modules
#via pip install {module_name}, it worked in my case after several errors!
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
# from chart_studio import plotly as ply
from plotly import graph_objs as go

START = "2005-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Prediction Service v.0.1(Work in progress)')
st.subheader("Correlation between money supply measures (M1,M2,M3) and stock market trends behavior.")
st.text('''This is a personal project that tries to find a correlation between the three 
main money supply indicators namely M1, M2 and M3 published by The Federal Reserve.''')
st.text('''Berkshire Hathaway Inc. (BRK-B)","S&P 500 (^GSPC)", "NASDAQ Composite (^IXIC)",
"Russell 2000 (^RUT)''')
st.markdown('Federal Reserve Data Source : '
            "https://www.federalreserve.gov/releases/h6/current/default.htm")
stocks = ('BRK-B', '^GSPC', '^IXIC', '^RUT')
selected_stock = st.selectbox('Select stock for prediction', stocks)

#Slider for years
n_years = st.slider('Select years of prediction:', 1, 15)
period = n_years * 365


@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True) #Date in first column
    return data

#Loading data messages
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.success('Data loaded successfully!')

st.subheader('Historical Data:')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

#Forecasting model
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)