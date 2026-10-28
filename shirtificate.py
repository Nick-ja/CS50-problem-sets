from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", size=50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 55, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", x=10, y=75, w=185, h=185, keep_aspect_ratio=True)
#pdf.set_font("helvetica", size=25)
pdf.set_font_size(25)
pdf.set_text_color(255, 255, 255)
name = input("Name: ")
pdf.text(x=55, y=140, text=f"{name} took CS50")
pdf.output("CS50.pdf")
