# 📑 Automated Report Generation – Python Internship Project

This project is part of my Python Internship at **CodTech Technologies** (5th June – 5th July 2025).  
It demonstrates **automated data analysis** and **PDF report generation** using Python.

---

## 📌 Project Overview

**Title:** Automated Report Generation  
**Objective:**  
- Read student performance data from a CSV file  
- Perform analysis and generate visualizations using `pandas` and `matplotlib`  
- Create a structured, formatted **PDF report** using the `ReportLab` library

---

## 🛠️ Tools & Libraries Used

- **Python 3.11+**
- [`pandas`](https://pandas.pydata.org/) – Data analysis  
- [`matplotlib`](https://matplotlib.org/) – Data visualization  
- [`ReportLab`](https://www.reportlab.com/) – PDF generation  

---

## 📊 Features

- ✅ Reads dataset (`students_performance.csv`)
- ✅ Calculates average scores by gender and parental education
- ✅ Visualizations: bar charts, pie chart, histogram
- ✅ Automatically generates a multi-page, styled PDF report
- ✅ Cover page with:
  - Logo
  - Internship details
  - Author name
- ✅ Key bullet-point insights page
- ✅ Footer with auto date and page numbers on every page

---

## 📁 Files

| File Name               | Description                                  |
|------------------------|----------------------------------------------|
| `report_generator.py`  | Main Python script for report generation     |
| `students_performance.csv` | Input dataset used for analysis         |
| `logo.png`             | Internship or organization logo              |
| `generated_report.pdf` | Output PDF report with charts and insights   |

---

## 📷 Sample Report Pages

<img src="https://via.placeholder.com/600x300.png?text=Cover+Page" alt="Cover Page Sample" width="600"/>
<img src="https://via.placeholder.com/600x300.png?text=Data+Visualization+Page" alt="Chart Page Sample" width="600"/>

---

## 📦 How to Run

1. Install required libraries:

```bash
pip install pandas matplotlib reportlab

