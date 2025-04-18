import yfinance as yf
import os
from datetime import datetime
from pathlib import Path

def get_downloads_folder():
    return str(Path.home() / "Downloads")

def download_stock_data(ticker, period="1y", interval="1d"):
    try:
        data = yf.download(ticker, period=period, interval=interval)

        if data.empty:
            return False, "No data returned. Please check your inputs."

        filename = f"{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        downloads_path = get_downloads_folder()
        full_path = os.path.join(downloads_path, filename)

        data.to_excel(full_path)
        return True, f"Saved to Downloads folder as:\n{filename}"

    except Exception as e:
        return False, str(e)