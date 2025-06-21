import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

# Total number of content pages (excluding cover)
TOTAL_PAGES = 7

# Footer function
def add_footer(pdf, page_num, total_pages):
    width, height = A4
    pdf.setFont("Helvetica", 9)
    pdf.drawString(50, 30, datetime.now().strftime("Generated on: %d %B %Y"))
    pdf.drawRightString(width - 50, 30, f"Page {page_num} of {total_pages}")

# Step 1: Read dataset
df = pd.read_csv("students_performance.csv")

# Step 2: Analysis
avg_scores_by_gender = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
prep_course_counts = df["test preparation course"].value_counts()
summary_stats = df.describe()
avg_by_edu = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()
avg_by_gender_prep = df.groupby(["gender", "test preparation course"])[["math score", "reading score", "writing score"]].mean().unstack()

# Step 3: Charts
avg_scores_by_gender.plot(kind='bar', figsize=(6, 4))
plt.title("Average Scores by Gender")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("avg_scores_by_gender.png")
plt.close()

prep_course_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(4, 4))
plt.title("Test Preparation Course Completion")
plt.ylabel('')
plt.tight_layout()
plt.savefig("test_prep_pie.png")
plt.close()

df["math score"].plot(kind='hist', bins=10, color='skyblue', edgecolor='black', figsize=(6, 4))
plt.title("Math Score Distribution")
plt.xlabel("Score")
plt.tight_layout()
plt.savefig("math_score_hist.png")
plt.close()

avg_by_edu.plot(kind='bar', figsize=(7, 4))
plt.title("Average Scores by Parental Education Level")
plt.ylabel("Score")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig("avg_by_education.png")
plt.close()

avg_by_gender_prep["math score"].plot(kind='bar', figsize=(6, 4), title="Math Score by Gender & Test Prep")
plt.ylabel("Math Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("test_prep_gender_comparison.png")
plt.close()

# Step 4: PDF Report
pdf = canvas.Canvas("generated_report.pdf", pagesize=A4)
width, height = A4

# COVER PAGE
pdf.setFont("Helvetica-Bold", 24)
pdf.drawCentredString(width / 2, height - 100, "📘 Student Performance Report")

# ✅ Insert logo at center-top
if os.path.exists("logo.png"):
    pdf.drawImage("logo.png", width/2 - 40, height - 150, width=80, height=50)

pdf.setFont("Helvetica", 14)
pdf.drawCentredString(width / 2, height - 170, "Generated using Python, pandas, matplotlib & ReportLab")

pdf.setFont("Helvetica", 12)
pdf.drawCentredString(width / 2, height - 200, "Prepared by: CHRYSL SHECKINA THOMAS")
pdf.drawCentredString(width / 2, height - 220, "Internship: CodTech Technologies - Python Internship")
pdf.drawCentredString(width / 2, height - 240, "Duration: 5th June – 5th July 2025")
pdf.drawString(50, 100, f"Date: {datetime.now().strftime('%d-%m-%Y')}")
pdf.showPage()

# PAGE 1 - Key Insights
page_num = 1
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "1. Key Insights")

pdf.setFont("Helvetica", 12)
bullets = [
    "✔️ Female students scored higher in reading and writing.",
    "✔️ Completing test preparation improves all subject scores.",
    "✔️ Math scores vary more widely than reading/writing.",
    "✔️ Higher parental education levels tend to correlate with better scores.",
    "✔️ Majority of students did not complete test preparation."
]

y = height - 100
for bullet in bullets:
    pdf.drawString(70, y, bullet)
    y -= 25

add_footer(pdf, page_num, TOTAL_PAGES)
pdf.showPage()

# PAGE 2 - Avg Scores by Gender
page_num = 2
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "2. Average Scores by Gender")
y = height - 80
pdf.setFont("Helvetica", 12)
for gender, row in avg_scores_by_gender.iterrows():
    line = f"{gender.capitalize()} → Math: {row['math score']:.1f}, Reading: {row['reading score']:.1f}, Writing: {row['writing score']:.1f}"
    pdf.drawString(60, y, line)
    y -= 20
pdf.drawImage("avg_scores_by_gender.png", 100, y - 220, width=400, height=250)
add_footer(pdf, page_num, TOTAL_PAGES)
pdf.showPage()

# PAGE 3 - Pie Chart
page_num = 3
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "3. Test Preparation Course Completion")
pdf.drawImage("test_prep_pie.png", 180, height - 300, width=200, height=200)
add_footer(pdf, page_num, TOTAL_PAGES)
pdf.showPage()

# PAGE 4 - Histogram
page_num = 4
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "4. Math Score Distribution")
pdf.drawImage("math_score_hist.png", 80, height - 350, width=450, height=300)
add_footer(pdf, page_num, TOTAL_PAGES)
pdf.showPage()

# PAGE 5 - Parental Education
page_num = 5
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "5. Scores by Parental Education Level")
pdf.drawImage("avg_by_education.png", 70, height - 350, width=450, height=300)
add_footer(pdf, page_num, TOTAL_PAGES)
pdf.showPage()

# PAGE 6 - Gender-wise Test Prep Impact
page_num = 6
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "6. Gender-wise Test Prep Impact on Math Score")
pdf.drawImage("test_prep_gender_comparison.png", 70, height - 350, width=450, height=300)
add_footer(pdf, page_num, TOTAL_PAGES)
pdf.showPage()

# PAGE 7 - Summary Statistics
page_num = 7
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "7. Summary Statistics")
pdf.setFont("Helvetica", 10)
y = height - 80
for col in ["math score", "reading score", "writing score"]:
    pdf.drawString(50, y, f"{col.upper()}")
    for stat in ["mean", "std", "min", "max"]:
        val = summary_stats.loc[stat, col]
        pdf.drawString(80, y - 15, f"{stat.capitalize()}: {val:.2f}")
        y -= 15
    y -= 10
add_footer(pdf, page_num, TOTAL_PAGES)

pdf.save()
print("✅ Final PDF report generated: generated_report.pdf")

