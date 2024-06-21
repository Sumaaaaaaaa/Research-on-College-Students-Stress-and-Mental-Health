import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_file():
    filepath = filedialog.askopenfilename(
        initialdir="/CsvFiles", 
        title="Select a CSV file", 
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))
    )
    if filepath:
        try:
            df = pd.read_csv(filepath)
            print(df.head())  # or any other operation you want to perform on the DataFrame
        except Exception as e:
            print(f"Error reading the file: {e}")
            
            
open_file()