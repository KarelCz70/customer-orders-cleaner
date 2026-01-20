# Customer Orders Cleaner (TXT → CSV → Pandas → PNG)

A small Python project that demonstrates a complete data-cleaning and reporting pipeline:

1) Read raw numeric values from a TXT file  
2) Validate and clean the data  
3) Export valid values into a clean CSV file  
4) Generate a summary report with pandas  
5) Create a PNG chart (histogram) for quick visual insight

This is a practical example of typical freelance / business automation work:
data quality checks + clean outputs + reporting.

---

## Features

- Reads raw values from `orders.txt`
- Filters valid integers in range **1–100**
- Logs invalid lines with line number and reason
- Generates:
  - `outputs/report.txt` (human-readable TXT report)
  - `outputs/orders.csv` (clean CSV output)
  - `outputs/summary.csv` (pandas summary metrics)
  - `outputs/value_distribution.png` (histogram chart)

---

## Project Structure

customer-orders-cleaner/
│
├── txt_cleaner.py
├── pandas_summary.py
├── pandas_plot.py
├── orders.txt # your input file (example)
└── outputs/
├── report.txt
├── orders.csv
├── summary.csv
└── value_distribution.png

yaml
Zkopírovat kód

> Note: The `outputs/` folder is generated automatically.

---

## Requirements

- Python 3.9+
- pandas
- matplotlib

Install dependencies:

```bash
pip install pandas matplotlib
How to Run
Step 1: TXT → report.txt + orders.csv
bash
Zkopírovat kód
python txt_cleaner.py
Step 2: CSV → summary.csv (pandas)
bash
Zkopírovat kód
python pandas_summary.py
Step 3: CSV → value_distribution.png (chart)
bash
Zkopírovat kód
python pandas_plot.py
Input Format (orders.txt)
One value per line. Empty lines are allowed.

Example:

txt
Zkopírovat kód
12
25
abc
-5
101
30
Valid values are integers in range 1–100.

Output Explanation
report.txt – includes valid numbers, total/average, and invalid line log

orders.csv – clean dataset for Excel / other tools

summary.csv – count, total, average, min, max

value_distribution.png – histogram of valid values

