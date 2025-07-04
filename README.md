## Internship: CodTech Technologies - Python Internship
## Duration: 5th June - 5th July


## NAME - CHRYSL SHECKINA THOMAS 
## INTERN ID - CT04DG328 
## DOMAIN - PYTHON PROGRAMMING 
## DURATION - 4 WEEKS 
## MENTOR - MS. NEELA SANTHOSH KUMAR

## TITLE: AUTOMATED REPORT GENERATION 
Develop a script that reads data from a file, analyzes it and generates a formatted pdf report using libraries like FPDF OR REPORTLAB 
Deliverable: A script and a sample report
## DESCRIPTION BELOW SCREENSHOTS

## OUTPUT SCREENSHOTS

![Cover Page](images/Screenshot%202025-07-04%20172002.png)  
![Stats Table](images/Screenshot%202025-07-04%20171940.png)  
![Bar Chart: Gender Performance](images/Screenshot%202025-07-04%20171912-1.png)  
![Pie Chart: Test Prep](images/Screenshot%202025-07-04%20171839.png)  
![Histogram: Math Scores](images/Screenshot%202025-07-04%20171823.png)  
![Education vs Scores](images/Screenshot%202025-07-04%20171736.png)  
![Grouped Bar: Gender vs Test Prep](images/Screenshot%202025-07-04%20171701.png)




## Objective: 
To build a Python script that reads a dataset, performs analysis, creates visualizations, and generates a formatted multi page PDF report using the reportLab library. 

This task focused on integrating data processing, statistical analysis , chart creation and professional document formatting using open source libraries. This project closely simulates real world scenarios like generating business reports, academic analysis and automated dashboards -- all in PDF format. 


## Dataset Used:
The dataset used was the "Students Performance in Exams" dataset sourced from Kaggle. It consists of student level data including gender, parental education levels, scores in math, a reading and writing and whether they completed a test preparation course. 

## Technologies used
 1. Pandas- data processing
2. matplotlib - Chart generation
3. ReportLab- PDF creation
4. students_performance.csv - Kaggle dataset
5. logo.png - branded internship logo
6. Optional: VS code + Git + GitHub for version control

## Features implemented

1. Cover Page with:

- Internship Title, duration, candidate name, and logo branding were dynamically added.
- Positioned logo using ReportLab's drawImage() function with proper scaling and alignment. 
- Date added using Python's datetime module.

2. Key Insights Page: 

- A curated list of 5 major observations from the dataset
- Included gender based performance, impact of test preps and correlations with education level

3. Data Visualization
- Bar Chart: Average scores by gender in Math, Reading and Writing 
- Pie chart : Ratio of students who completed vs didn't complete test preparation
- Histogram: Distribution of math scores
- Bar Chart by Education: Average scores group by parental education level
- Grouped bar chart: Math scores compared by gender and test prep completion.

4. Summary Statistics
 - Included a stats table with min, max, mean and standard deviation of all subject scores

5. PDF Report Generation
- Used canvas.Canvas() from ReportLab to generate a multipage PDF
- Auto-formatted layout, centred titles, consistent margins
- Page footer with generation date and automatic page numbers
- Chart images embedded directly into pages using drawImage()

## Challenges and Solutions

1. Chart Overlap and layout Issues: Resolved using precise positioning and aspect ratio control.
2. Text Wrapping: Handled using ReportLab's drawstring() and manual spacing logic.
3. Image readability: Used tight_layout in matplotlib and standardized figure size

## Learning Outcomes: 

- Gaining practical experience with the end to end pipeline data to report
- Learned th internals of programmatic PDF generation and canvas based drawing
- Improved analytical thinking and storytelling with data
- Applied visualization best practices using real world data
- Strengthened understanding of modular coding and file management for automation

## Conclusion:
This task was a comprehensive introduction to automating business intelligence workflows using Python. By combining data processing, statistical summaries and visual storytelling into a deliverable PDF, this project reflected the power of Python in professional reporting. It demonstrated skills that are relevant in fields like data science, analytics and education and enterprise documentation. 

The script is reusable and can be adapted to different datasets, making it a flexible solution for data reporting needs. The final product - generated_report.pdf - presents the information in a clear, concise and well organized format suitable for sharing or submission. 


