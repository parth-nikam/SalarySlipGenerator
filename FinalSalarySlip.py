import mysql.connector
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Connect to the database
db = mysql.connector.connect(
    host="Parths-MacBook-Pro-2.local",
    user="root",
    password="parthnikam",
    database="salarySlip"
)

# Create a cursor
cursor = db.cursor()

# Read data from Excel file
data = pd.read_csv('salaries.csv')

# Iterate over each row of the data and insert it into the database
for index, row in data.iterrows():
    company_name = row['company_name']
    company_address = row['company_address']
    employee_id = row['employee_id']
    employee_name = row['employee_name']
    salary = row['salary']
    pay_period_start = row['pay_period_start']
    pay_period_end = row['pay_period_end']

    # Insert the salary slip into the database
    query = "INSERT INTO salaries (company_name, company_address, employee_id, employee_name, salary, pay_period_start, pay_period_end) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (company_name, company_address, employee_id, employee_name, salary, pay_period_start, pay_period_end)
    cursor.execute(query, values)
    db.commit()

    # Generate the salary slip PDF
    pdf_name = f"{employee_name}_{pay_period_start}_to_{pay_period_end}.pdf"
    c = canvas.Canvas(pdf_name, pagesize=letter)

    # Draw the sections and lines
    c.setStrokeColorRGB(0, 0, 0)
    c.setFont('Helvetica', 16)
    c.drawString(50, 750, f"{company_name}")
    c.setFont('Helvetica', 12)
    c.drawString(50, 730, f"{company_address}")
    c.line(50, 725, 575, 725)
    c.setFont('Helvetica-Bold', 14)
    c.drawString(50, 690, "Salary Slip")
    c.setFont('Helvetica', 12)
    c.drawString(50, 660, "Employee Details:")
    c.line(50, 655, 575, 655)
    c.drawString(50, 635, f"Employee ID: {employee_id}")
    c.drawString(50, 615, f"Employee Name: {employee_name}")
    c.line(50, 610, 575, 610)
    c.drawString(50, 590, "Salary Details:")
    c.line(50, 585, 575, 585)
    c.drawString(50, 565, f"Salary: ${salary:.2f}")
    c.drawString(50, 545, f"Pay Period: {pay_period_start} to {pay_period_end}")
    c.line(50, 540, 575, 540)

    c.save()

# Close the database connection
db.close()
