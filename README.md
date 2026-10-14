# Python CSV Data Cleaning Portfolio

A small portfolio project demonstrating CSV data cleaning and reporting with Python.

## Features
- Removes duplicate rows
- Identifies missing or invalid sales amounts
- Standardizes valid amounts to two decimal places
- Exports a cleaned CSV file
- Generates a summary report

## Files
- sales_raw.csv — synthetic sample input
- sales_cleaned.csv — cleaned output
- clean_sales.py — data cleaning script
- make_report.py — report generation script
- cleaning_report.txt — sample summary report

## Sample Results
- Original rows: 6
- Duplicate rows removed: 1
- Cleaned rows: 5
- Valid sales total: $410.50
- Average valid sale: $136.83

## How to Run
Run these commands in Termux:
python clean_sales.py
python make_report.py

This project uses synthetic sample data, not client data.
