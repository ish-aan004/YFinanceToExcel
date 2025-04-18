import tkinter as tk
from tkinter import messagebox

from logic import download_stock_data


def run_app():
    def handle_download():
        ticker = ticker_entry.get().strip()
        period = period_entry.get().strip() or "1y"
        interval = interval_entry.get().strip() or "1d"

        if not ticker:
            messagebox.showerror("Input Error", "Please enter a stock ticker.")
            return

        success, msg = download_stock_data(ticker, period, interval)
        if success:
            messagebox.showinfo("Download Complete", msg)
        else:
            messagebox.showerror("Error", msg)

    root = tk.Tk()
    root.title("YFinance to Excel")
    root.minsize(400, 300)
    root.resizable(True, True)

    tk.Label(root, text="Stock Ticker:").pack(pady=(20, 5))
    ticker_entry = tk.Entry(root, width=40)
    ticker_entry.pack()
    tk.Label(root, text="Examples: AAPL, RELIANCE.NS, AUB.AX, BP.L, 7203.T",
             fg="gray", font=("Arial", 9)).pack(pady=(4, 8))

    tk.Label(root, text="Period (default: 1y):").pack(pady=(10, 5))
    period_entry = tk.Entry(root, width=40)
    period_entry.pack()
    tk.Label(root, text="Valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max",
             fg="gray", font=("Arial", 9)).pack(pady=(4, 8))

    tk.Label(root, text="Interval (default: 1d):").pack(pady=(10, 5))
    interval_entry = tk.Entry(root, width=40)
    interval_entry.pack()
    tk.Label(root, text="Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 4h,\n1d, 5d, 1wk, 1mo, 3mo",
             fg="gray", font=("Arial", 9)).pack(pady=(4, 10))

    tk.Button(root,
              text="Download Excel File",
              command=handle_download,
              bg="#4CAF50",
              fg="white",
              activebackground="#45A049",
              activeforeground="white",
              relief="flat",
              padx=10,
              pady=5).pack(pady=10)

    root.mainloop()

    if __name__ == "__y2e__":
        run_app()

