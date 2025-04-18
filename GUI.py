import tkinter as tk
from tkinter import messagebox
import webbrowser
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

    def open_contact_link(event):
        webbrowser.open_new("https://www.linkedin.com/in/tejastagra/")  # 🔗 Replace with your own

    # --- Root window config ---
    root = tk.Tk()
    root.title("YFinance to Excel")
    root.configure(bg="#1c1c1c")  # Goldman Sachs charcoal grey
    root.geometry("620x520")
    root.resizable(False, False)

    # --- Fonts ---
    try:
        inter_font = ("Inter", 12)
        inter_font_bold = ("Inter", 13, "bold")
        inter_font_small = ("Inter", 10)
        inter_font_italic = ("Inter", 11, "italic")
    except:
        # Fallback if Inter is not available
        inter_font = ("Helvetica", 12)
        inter_font_bold = ("Helvetica", 13, "bold")
        inter_font_small = ("Helvetica", 10)
        inter_font_italic = ("Helvetica", 11, "italic")

    # --- Header ---
    tk.Label(root, text="Welcome Analysts!", font=("Inter", 20, "bold"),
             fg="#f5f5f5", bg="#1c1c1c").pack(pady=(30, 10))

    # --- Ticker ---
    tk.Label(root, text="Stock Ticker", font=inter_font, fg="#dddddd", bg="#1c1c1c").pack()
    ticker_entry = tk.Entry(root, width=40, font=("Inter", 12), bg="#2a2a2a", fg="white", insertbackground="white", relief="flat")
    ticker_entry.pack(pady=(0, 5))
    tk.Label(root, text="e.g. AAPL, RELIANCE.NS, AUB.AX, BP.L, 7203.T",
             fg="#999999", bg="#1c1c1c", font=inter_font_small).pack(pady=(0, 12))

    # --- Period ---
    tk.Label(root, text="Time Period (default 1y)", font=inter_font, fg="#dddddd", bg="#1c1c1c").pack()
    period_entry = tk.Entry(root, width=40, font=("Inter", 12), bg="#2a2a2a", fg="white", insertbackground="white", relief="flat")
    period_entry.pack(pady=(0, 5))
    tk.Label(root, text="Valid: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max",
             fg="#999999", bg="#1c1c1c", font=inter_font_small).pack(pady=(0, 12))

    # --- Interval ---
    tk.Label(root, text="Interval (default 1d)", font=inter_font, fg="#dddddd", bg="#1c1c1c").pack()
    interval_entry = tk.Entry(root, width=40, font=("Inter", 12), bg="#2a2a2a", fg="white", insertbackground="white", relief="flat")
    interval_entry.pack(pady=(0, 5))
    tk.Label(root, text="Valid: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 4h,\n1d, 5d, 1wk, 1mo, 3mo",
             fg="#999999", bg="#1c1c1c", font=inter_font_small).pack(pady=(0, 20))

    # --- Button ---
    tk.Button(root,
              text="⬇ Download Excel File",
              command=handle_download,
              bg="#d4af37",  # gold
              fg="#000000",
              activebackground="#bfa12f",
              activeforeground="#000000",
              font=inter_font_bold,
              relief="flat",
              padx=14,
              pady=8).pack(pady=10)

    # --- Footer (Side-by-side frame) ---
    footer_frame = tk.Frame(root, bg="#1c1c1c")
    footer_frame.pack(side="bottom", pady=15)

    tk.Label(footer_frame,
             text="Locally brewed at ANU. For ANU. 🦆",
             fg="#777777",
             bg="#1c1c1c",
             font=inter_font_italic).pack(side="left")

    contact_link = tk.Label(footer_frame,
                            text="Get in touch.",
                            fg="#4da6ff",
                            bg="#1c1c1c",
                            cursor="hand2",
                            font=("Inter", 11, "underline"))
    contact_link.pack(side="left", padx=(10, 0))
    contact_link.bind("<Button-1>", open_contact_link)

    root.mainloop()

if __name__ == "__main__":
    run_app()
