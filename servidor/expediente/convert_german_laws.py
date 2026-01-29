#!/usr/bin/env python3
"""
Convierte los PDFs de las leyes alemanas de cannabis a Markdown
"""

import fitz  # PyMuPDF
import os
from datetime import datetime

def pdf_to_markdown(pdf_path, output_path):
    """Convierte un PDF a Markdown con deteccion de headings"""
    
    print(f"Procesando: {pdf_path}")
    
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error abriendo PDF: {e}")
        return False
    
    markdown_lines = []
    
    # Metadata YAML
    filename = os.path.basename(pdf_path)
    markdown_lines.append("---")
    markdown_lines.append(f"title: {filename.replace('.pdf', '')}")
    markdown_lines.append(f"source: {pdf_path}")
    markdown_lines.append(f"converted: {datetime.now().isoformat()}")
    markdown_lines.append(f"pages: {len(doc)}")
    markdown_lines.append("language: de")
    markdown_lines.append("---")
    markdown_lines.append("")
    
    for page_num, page in enumerate(doc):
        markdown_lines.append(f"\n---\n\n**[Pagina {page_num + 1}]**\n")
        
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if "lines" not in block:
                continue
                
            for line in block["lines"]:
                line_text = ""
                max_font_size = 0
                is_bold = False
                
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue
                    
                    font_size = span["size"]
                    font_name = span["font"].lower()
                    
                    if font_size > max_font_size:
                        max_font_size = font_size
                    
                    if "bold" in font_name or "black" in font_name:
                        is_bold = True
                    
                    line_text += text + " "
                
                line_text = line_text.strip()
                if not line_text:
                    continue
                
                # Detectar headings por tamano de fuente
                if max_font_size >= 16:
                    markdown_lines.append(f"\n# {line_text}\n")
                elif max_font_size >= 14 or (max_font_size >= 12 and is_bold):
                    markdown_lines.append(f"\n## {line_text}\n")
                elif max_font_size >= 11 and is_bold:
                    markdown_lines.append(f"\n### {line_text}\n")
                else:
                    # Detectar listas
                    if line_text.startswith(("- ", "• ", "* ", "– ")):
                        markdown_lines.append(f"- {line_text[2:].strip()}")
                    elif len(line_text) > 2 and line_text[0].isdigit() and line_text[1] in ".)" :
                        markdown_lines.append(f"{line_text}")
                    else:
                        markdown_lines.append(line_text)
    
    doc.close()
    
    # Post-procesar para unir parrafos
    final_content = "\n".join(markdown_lines)
    
    # Guardar
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    
    print(f"Guardado: {output_path}")
    return True


if __name__ == "__main__":
    # Rutas de los PDFs
    pdfs = [
        (r"C:\Users\micro\Downloads\regelungstext (1).pdf", 
         r"C:\Users\micro\Desktop\DECRETO\markdown\Alemania_Regelungstext_CanG.md"),
        (r"C:\Users\micro\Downloads\MedCanG (2).pdf",
         r"C:\Users\micro\Desktop\DECRETO\markdown\Alemania_MedCanG.md")
    ]
    
    for pdf_path, output_path in pdfs:
        if os.path.exists(pdf_path):
            pdf_to_markdown(pdf_path, output_path)
        else:
            print(f"No encontrado: {pdf_path}")
    
    print("\nConversion completada!")
