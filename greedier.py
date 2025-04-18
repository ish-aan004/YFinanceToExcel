import sys
import os
import yfinance as yf
import pandas as pd
from datetime import datetime
from pathlib import Path

def get_downloads_folder():
    # Cross-platform way to get Downloads folder (works for macOS/Linux/Windows)
    return str(Path.home() / "Downloads")

def download_to_excel(ticker, period="1y", interval="1d"):
    try:
        print(f"📡 Fetching data for {ticker}...")

        data = yf.download(ticker, period=period, interval=interval)

        if data.empty:
            print("⚠️ No data found. Please check your ticker or try a different period/interval.")
            return

        filename = f"{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        downloads_path = get_downloads_folder()
        full_path = os.path.join(downloads_path, filename)

        data.to_excel(full_path)

        print(f"✅ Success! Data saved to your Downloads folder as:\n{full_path}")

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python greedier.py <TICKER> [PERIOD] [INTERVAL]")
        print("Example: python greedier.py AUB.AX 5y 1d")
        sys.exit(1)

    ticker = sys.argv[1]
    period = sys.argv[2] if len(sys.argv) >= 3 else "1y"
    interval = sys.argv[3] if len(sys.argv) >= 4 else "1d"

    download_to_excel(ticker, period, interval)
