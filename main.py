import fpdf
import pandas as pd

pdf = fpdf.FPDF(orientation="portrait",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="arial",size=24,style="B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],border=0,align="L",ln=1)
    pdf.line(10,25,pdf.w-10,25)
    
    # Footer
    pdf.ln(pdf.h-30)
    pdf.set_font(family="arial",size=8,style="I")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],border=0,align="R",ln=1)

    for i in range(row["Pages"]-1):
        pdf.add_page()

        # Footer
        pdf.ln(pdf.h-30+12)
        pdf.set_font(family="arial",size=8,style="I")
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0,h=12,txt=row["Topic"],border=0,align="R",ln=1)

# pdf.add_page()
# pdf.set_font(family="arial",size=12,style="B")
# pdf.cell(w=20,h=12,txt="Hi",border=1,align="L",ln=1)

pdf.output("result.pdf")