from reportlab.pdfgen import canvas

def generate_certificate(name, email):
    file_name = f"certificate_{name.replace(' ', '_')}.pdf"
    c = canvas.Canvas(file_name)
    c.setFont("Helvetica", 24)
    c.drawString(100, 700, "Webinar Certificate of Participation")
    c.setFont("Helvetica", 18)
    c.drawString(100, 650, f"This certifies that {name}")
    c.drawString(100, 600, "has successfully participated in the webinar.")
    c.save()
    return file_name
