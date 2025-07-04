 🧾 Task 2: Automated Report Generation

 Internship: CodTech Technologies - Python Internship  
Duration: 5th June – 5th July 2025  
Name:CHRYSL SHECKINA THOMAS  
Intern ID: CT04DG328  
Domain: Python Programming  
Mentor: Ms. Neela Santhosh Kumar

---

Output Screenshots



![Cover Page](Screenshot%202025-07-04%20172002.png)  
![Stats Table](Screenshot%202025-07-04%20171940.png)  
![Bar Chart: Gender Performance](Screenshot%202025-07-04%20171912-1.png)  
![Pie Chart: Test Prep](Screenshot%202025-07-04%20171839.png)  
![Histogram: Math Scores](Screenshot%202025-07-04%20171823.png)  
![Education vs Scores](Screenshot%202025-07-04%20171736.png)  
![Grouped Bar: Gender vs Test Prep](Screenshot%202025-07-04%20171701.png)

---

Title: Automated Report Generation

Objective:  
To build a Python script that reads a dataset, performs analysis, creates visualizations, and generates a formatted multi-page PDF report using the ReportLab library.

This task focused on integrating data processing, statistical analysis, chart creation, and professional document formatting using open-source libraries. It closely simulates real-world scenarios like generating business reports, academic analysis, and automated dashboards — all in PDF format.

---

Dataset Used:

Name:Students Performance in Exams  
Source:Kaggle  
This dataset contains student-level data including gender, parental education levels, math/reading/writing scores, and whether they completed a test preparation course.

---

Technologies Used:

1. Pandas– Data processing  
2. matplotlib – Chart generation  
3. ReportLab– PDF creation  
4. students_performance.csv– Kaggle dataset  
5. logo.png– Branded internship logo  
6. VS Code + Git + GitHub– Version control and collaboration

---

Features Implemented:

Cover Page
- Includes internship title, duration, candidate name, and logo branding.
- Logo added using `drawImage()` with scaling and alignment.
- Date generated using Python's `datetime` module.

Key Insights Page
- Summary of 5 key observations from the dataset.
- Gender-based performance, test prep impact, education level influence.

Data Visualizations
- Bar Chart: Average scores by gender (Math, Reading, Writing)
- Pie Chart: Test preparation course completion ratio
- Histogram: Math score distribution
- Bar Chart: Scores by parental education level
- Grouped Bar Chart: Gender vs Test Prep comparison

Summary Statistics
- Table with min, max, mean, and standard deviation of all scores.

PDF Report Generation
- Used `canvas.Canvas()` to generate a multi-page report.
- Titles centered, margins consistent.
- Footer with date and page numbers.
- Embedded chart images using `drawImage()`.

---

Challenges and Solutions:

- Chart Overlap/Layout Issues – Solved using `tight_layout()` and fixed positions.
- Text Wrapping– Managed manually with string drawing logic.
- Image Clarity– Standardized figure sizes and aspect ratios.

---

Learning Outcomes:

- Practical experience with data-to-report pipeline  
- Learned internals of PDF generation using ReportLab  
- Strengthened data storytelling skills  
- Gained confidence in modular scripting and file management  
- Understood visualization techniques and chart selection

---

Conclusion:

This task provided a comprehensive foundation in automating data-driven reporting using Python. By combining data processing, analysis, and visualization into a well-formatted PDF, this project reflects skills used in real-world data science, education, and enterprise reporting.

The script is reusable and adaptable to different datasets, making it a flexible reporting solution.  
The final product — `generated_report.pdf` — presents insights in a clear, professional format suitable for submission, sharing, or business use.

---

