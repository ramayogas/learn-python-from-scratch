def font_size():
    output = []

    output.append("Reading font information from PDF using PyMuPDF (fitz)")
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")

    import fitz
    doc = fitz.open("epk.pdf")

    for page in doc:
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                for span in line["spans"]:
                    output.append(
                        f"{span['text']} Font: {span['font']} Size: {span['size']}"
                    )
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")
    output.append("----------------------------------------------------")
    pt = span['size']
    output.append(f"font in inches: {pt / 72}")
    output.append(f"font in millimeters: {pt * 25.4 / 72}")
    output.append(f"font in pixels (96 DPI): {pt * 96 / 72}")
    output.append(f"font in pixels (300 DPI): {pt * 300 / 72}")

    return "\n".join(output)

with open("font_size_epk.txt", "w") as file:
    file.write(font_size())

print("Printed txt")