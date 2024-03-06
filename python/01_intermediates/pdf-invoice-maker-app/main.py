import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("datas/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    filename = Path(filepath).stem

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=16)
    pdf.cell(w=0,h=8,txt="Invoice ID. ")

