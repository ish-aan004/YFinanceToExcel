import sys
import yfinance as yf
import pandas as pd
from datetime import datetime

def download_to_excel(ticker, period="1y", interval="1d"):
    try:
        print(f"Fetching data for {ticker}...")

        data = yf.download(ticker, period=period, interval=interval)

        if data.empty:
            print("⚠️ No data found. Please check your ticker or try a different period/interval.")
            return

        filename = f"{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        data.to_excel(filename)

        print(f"✅ Data downloaded successfully and saved as '{filename}'")

    except Exception as e:
        print("❌ Something went wrong:", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_stock_to_excel.py <TICKER> [PERIOD] [INTERVAL]")
        print("Example: python download_stock_to_excel.py AUB.AX 5y 1d")
        sys.exit(1)

    ticker = sys.argv[1]
    period = sys.argv[2] if len(sys.argv) >= 3 else "1y"
    interval = sys.argv[3] if len(sys.argv) >= 4 else "1d"

    download_to_excel(ticker, period, interval)
