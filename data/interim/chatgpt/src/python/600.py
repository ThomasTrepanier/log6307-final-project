import tkinter as tk
from tkinter import ttk
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data():
    ticker = ticker_entry.get()
    if not ticker:
        result_label.config(text="Please enter a stock ticker.")
        return

    try:
        stock = yf.Ticker(ticker)
        hist_data = stock.history(period="1y")
        if hist_data.empty:
            result_label.config(text="Invalid stock ticker or no data available.")
            return
        display_data(hist_data)
        result_label.config(text=f"Showing data for {ticker}")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}")


def display_data(data: pd.DataFrame):
    plt.figure(figsize=(14, 7))
    plt.title('Historical Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.plot(data['Close'])
    plt.show()


# UI Setup
root = tk.Tk()
root.title("Stock Analysis Tool")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ticker_label = ttk.Label(frame, text="Enter Stock Ticker:")
ticker_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
ticker_entry = ttk.Entry(frame, width=20)
ticker_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
ticker_entry.focus()

fetch_button = ttk.Button(frame, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=1, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, columnspan=2, pady=10)

root.mainloop()
