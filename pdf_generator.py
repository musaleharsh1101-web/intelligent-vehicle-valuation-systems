from fpdf import FPDF
import io

class ValuationPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "MUSALE MOTORS - CARMITRA", border=False, ln=True, align="C")
        self.set_font("Helvetica", "I", 10)
        self.cell(0, 5, "Vehicle Valuation Summary Report", border=False, ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, "Thank you for choosing Musale Motors | Confidential", align="C")

def generate_pdf(customer_data, vehicle_data, price):
    pdf = ValuationPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=11)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Customer Information", ln=True)
    pdf.set_font("Helvetica", size=11)
    for key, val in customer_data.items():
        pdf.cell(50, 7, f"{key}:", border=0)
        pdf.cell(0, 7, f"{val}", border=0, ln=True)

    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Vehicle Specifications", ln=True)
    pdf.set_font("Helvetica", size=11)
    for key, val in vehicle_data.items():
        pdf.cell(50, 7, f"{key}:", border=0)
        pdf.cell(0, 7, f"{val}", border=0, ln=True)

    pdf.ln(8)

    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, f"Estimated Market Price: Rs. {price:,.2f}", border=1, ln=True, align="C")

    pdf_buffer = io.BytesIO()
    pdf_bytes = pdf.output()
    pdf_buffer.write(pdf_bytes)
    pdf_buffer.seek(0)
    return pdf_buffer