from reportlab.pdfgen import canvas
import os

os.makedirs("docs", exist_ok=True)
c = canvas.Canvas("docs/test.pdf")
c.drawString(100, 750, "Questo è un PDF di prova per l'indicizzazione.")
c.save()
print("PDF di prova creato: docs/test.pdf")
