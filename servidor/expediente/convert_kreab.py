import fitz  # PyMuPDF
import os
import re
from datetime import datetime

def convert_pdf_to_markdown(pdf_path, output_path):
    """Convert PDF to Markdown with proper heading detection and formatting"""
    
    # Open PDF
    doc = fitz.open(pdf_path)
    
    # Get PDF filename for metadata
    pdf_filename = os.path.basename(pdf_path)
    
    # Start with YAML metadata
    markdown_content = f"""---
title: "{pdf_filename.replace('.pdf', '')}"
source: "{pdf_filename}"
converted: "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
pages: {doc.page_count}
---

"""
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        
        # Add page marker
        markdown_content += f"\n**[Pagina {page_num + 1}]**\n\n"
        
        # Get text blocks with formatting info
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if "lines" not in block:
                continue
                
            for line in block["lines"]:
                line_text = ""
                line_fonts = []
                
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue
                    
                    # Collect font info
                    font_size = span["size"]
                    font_flags = span["flags"]
                    is_bold = bool(font_flags & 2**4)  # Bold flag
                    
                    line_fonts.append((font_size, is_bold))
                    line_text += text + " "
                
                line_text = line_text.strip()
                if not line_text:
                    continue
                
                # Determine heading level based on font size
                if line_fonts:
                    max_font_size = max(f[0] for f in line_fonts)
                    has_bold = any(f[1] for f in line_fonts)
                    
                    # Heading detection
                    if max_font_size >= 18:
                        markdown_content += f"# {line_text}\n\n"
                    elif max_font_size >= 14 and has_bold:
                        markdown_content += f"## {line_text}\n\n"
                    elif max_font_size >= 12 and has_bold:
                        markdown_content += f"### {line_text}\n\n"
                    else:
                        # Regular text - check for list items
                        if re.match(r'^[*\-]\s+', line_text) or re.match(r'^\d+[\.\)]\s+', line_text):
                            if re.match(r'^[*\-]\s+', line_text):
                                line_text = re.sub(r'^[*\-]\s+', '- ', line_text)
                            else:
                                line_text = re.sub(r'^(\d+)[\.\)]\s+', r'\1. ', line_text)
                        
                        markdown_content += f"{line_text}\n"
        
        # Add page separator
        markdown_content += "\n---\n"
    
    # Clean up excessive newlines
    markdown_content = re.sub(r'\n{4,}', '\n\n\n', markdown_content)
    
    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    doc.close()
    print(f"Conversion completada: {output_path}")
    return True

if __name__ == "__main__":
    # Lista de PDFs a convertir
    conversiones = [
        (r"C:\Users\micro\Downloads\Kreab (4).pdf", 
         r"C:\Users\micro\Desktop\DECRETO\contexto_realidad_mercado\Informe_Kreab_Sector_CBD.md"),
        (r"C:\Users\micro\Downloads\Informe-de-Posicion-Estrategica-Sector-del-Canamo-Industrial-y-Flor-de-CBD (1) (2) (3).pdf",
         r"C:\Users\micro\Desktop\DECRETO\contexto_realidad_mercado\Informe_Posicion_Estrategica_Canamo_CBD.md"),
        (r"C:\Users\micro\Downloads\PAPER_AECANI_PNSD_2026 (1).pdf",
         r"C:\Users\micro\Desktop\DECRETO\contexto_realidad_mercado\Paper_AECANI_PNSD_2026.md"),
    ]
    
    for pdf_path, output_path in conversiones:
        try:
            if os.path.exists(pdf_path):
                convert_pdf_to_markdown(pdf_path, output_path)
            else:
                print(f"No encontrado: {pdf_path}")
        except Exception as e:
            print(f"Error con {pdf_path}: {e}")
