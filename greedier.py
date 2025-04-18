import yfinance as yf
import pandas as pd
import os
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def get_downloads_folder():
    return str(Path.home() / "Downloads")

def download_data():
    ticker = ticker_entry.get().strip()
    period = period_entry.get().strip() or "1y"
    interval = interval_entry.get().strip() or "1d"

    if not ticker:
        messagebox.showerror("Error", "Please enter a stock ticker.")
        return

    try:
        data = yf.download(ticker, period=period, interval=interval)

        if data.empty:
            messagebox.showwarning("No Data", "No data found for the given inputs.")
            return

        filename = f"{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        downloads_path = get_downloads_folder()
        full_path = os.path.join(downloads_path, filename)

        data.to_excel(full_path)

        messagebox.showinfo("Success", f"Data saved to Downloads:\n{filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("📈 YFinance to Excel")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Stock Ticker:").pack(pady=(20, 5))
ticker_entry = tk.Entry(root, width=30)
ticker_entry.pack()

tk.Label(root, text="Period (default: 1y):").pack(pady=(10, 5))
period_entry = tk.Entry(root, width=30)
period_entry.pack()

tk.Label(root, text="Interval (default: 1d):").pack(pady=(10, 5))
interval_entry = tk.Entry(root, width=30)
interval_entry.pack()

tk.Button(root, text="Download Excel File", command=download_data, bg="#4CAF50", fg="white").pack(pady=20)

root.mainloop()
