# Stock-Prediction-App (Under Construction)
Stock Prediction App (Python + Streamlit) - Small app that correlates money supply metrics w/ US stock indexes
This is a personal project that tries to find a correlation between the three 
main money supply indicators namely M1, M2 and M3 published by The Federal Reserve.
These are the tickers used: Berkshire Hathaway Inc. (BRK-B)","S&P 500 (^GSPC)", "NASDAQ Composite (^IXIC)",
"Russell 2000 (^RUT).

<br>Federal Reserve Data Source : https://www.federalreserve.gov/releases/h6/current/default.htm</br>

## Prerequisites
Python 3.8 is fine, even though I used Python 3.10.
I would recommend to update ALL imports, just in case there is something outdated. 
It happened to me that I got several error messages due to outdated libraries and fixed it by updating several libraries.

In my case:
```pip install --upgrade streamlit
pip install --upgrade yfinance
pip install --upgrade prophet
pip install --upgrade plotly
```

## Installation
Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services.

Get a free API Key at https://example.com
Clone the repo
git clone https://github.com/your_username_/Project-Name.git
Install NPM packages
npm install
Enter your API in config.js
const API_KEY = 'ENTER YOUR API';
(back to top)

## Usage
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

For more examples, please refer to the Documentation
