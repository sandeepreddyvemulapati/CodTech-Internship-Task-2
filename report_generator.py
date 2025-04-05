import pandas as pd
from fpdf import FPDF

# Step 1: Load data
data = pd.read_csv("sales_data.csv")

# Step 2: Analyze data (summary)
summary = data.describe()

# Step 3: Create a class for PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Sales Report", ln=True, align="C")

    def add_table(self, dataframe):
        self.set_font("Arial", "", 12)
        page_width = self.w - 2 * self.l_margin
        col_width = page_width / len(dataframe.columns)

        # Header
        for column in dataframe.columns:
            self.cell(col_width, 10, column, border=1, align="C")
        self.ln()

        # Rows
        for _, row in dataframe.iterrows():
            for item in row:
                if isinstance(item, (int, float)):
                    text = str(round(item, 2))
                else:
                    text = str(item)
                self.cell(col_width, 10, text, border=1, align="C")
            self.ln()

# Step 4: Generate PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Summary Statistics", ln=True, align="L")
pdf.ln(5)

# Add the summary table
pdf.add_table(summary)

# Step 5: Output the PDF
pdf.output("Sales_Report.pdf")
print("PDF report generated successfully!")
import os

# Open the PDF automatically after generating
os.startfile("Sales_Report.pdf")  # For Windows
