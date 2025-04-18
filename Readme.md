# 📊 YFinance Data Downloader

In a _freedy_ world, access to data shouldn’t come with a price tag.

Yahoo Finance — once the go-to data source for everyone — now charges **$500 per year** just to download stock data... unless you know Python.

With this simple tool powered by the `yfinance` library, you can:
- Fetch stock data for **free**
- Export it into a clean **Excel file**
- Use it with no subscription, no limits, no hassle

---

## ✅ Who Is This For?

- 📈 Investors who want raw stock data in Excel
- 🧪 Students or researchers needing historical prices
- 💡 Anyone tired of paywalls and just wants their data

Even if you don’t know Python, this script can be run once and give you the `.xlsx` file you need.

---

## 🛠 Features

- Supports all tickers from Yahoo Finance (including ASX tickers like `AUB.AX`)
- Choose your time period (`1d`, `1mo`, `10y`, `max`, etc.)
- Choose your interval (`1d`, `1wk`, `1mo`, etc.)
- Outputs a ready-to-use Excel file

---

## 📦 Requirements

Make sure you have Python installed, then run:

```bash
pip install yfinance pandas openpyxl

python download_stock_to_excel.py <TICKER> [PERIOD] [INTERVAL]