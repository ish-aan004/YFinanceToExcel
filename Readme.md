# YFinance to Excel

In a _freedy_ world, access to data shouldn’t come with a price tag.

Yahoo Finance — once the go-to data source for everyone — now charges **$500 per year** just to download stock data... unless you know Python.

With this simple tool powered by the `yfinance` library, you can:
- Fetch stock data for **free**
- Export it into a clean **Excel file**
- Use it with no subscription, no limits, no hassle

---

## Who Is This For?

- Investors who want raw stock data in Excel
-  Students or researchers needing historical prices
-  Anyone tired of paywalls and just wants their data

Even if you don’t know Python, this script can be run once and give you the `.xlsx` file you need.

---

## Features

- Supports all tickers from Yahoo Finance (including ASX tickers like `AUB.AX`)
- Choose your time period (`1d`, `1mo`, `10y`, `max`, etc.)
- Choose your interval (`1d`, `1wk`, `1mo`, etc.)
- Outputs a ready-to-use Excel file

---

## Requirements

Make sure you have Python 3 installed, then install the required libraries by running:

```bash
-- Windows
pip install yfinance pandas openpyxl


-- MacOS
pip3 install yfinance pandas openpyxl


-- Or from the dependecies.txt file

-- Windows
pip install -r dependencies.txt

--MacOS
pip3 install -r dependencies.txt 
```

----

## How to Run

Once everything is installed, launch the GUI using:

```bash
# Windows
python y2e.py

# macOS
python3 y2e.py
```

---