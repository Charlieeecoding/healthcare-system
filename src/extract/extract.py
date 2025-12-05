import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz

# 設定參數
start_date = '2025-12-02'  # 設定開始日期
end_date = '2025-12-04'    # 設定結束日期
interval = '1m'            # 設定時間週期為 15 分鐘

# 設定多支股票的代號
tickers = ['^GSPC', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']  # 股票代號

# 抓取多支股票的數據
data = yf.download(tickers, start=start_date, end=end_date, interval=interval, group_by='ticker')

# 顯示數據
for ticker in tickers:
    print(f"--- {ticker} ---")
    df = data[ticker].copy()
    
    # 轉換索引時間到 HKT 和 USA 時區
    df['HKT'] = df.index.tz_convert('Asia/Hong_Kong')
    df['USA (EST)'] = df.index.tz_convert('America/New_York')
    
    # 顯示含有時區轉換的數據
    print(df)
    print("\n")