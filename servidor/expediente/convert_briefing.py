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
title: "Briefing Recurso RD Cannabis Medicinal - CannabisHub AECANI"
source: "{pdf_filename}"
converted: "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
pages: {doc.page_count}
---

"""
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        
        # Add page marker
        markdown_content += f"**[Pagina {page_num + 1}]**\n\n"
        
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
                    if max_font_size >= 16 and has_bold:
                        markdown_content += f"# {line_text}\n\n"
                    elif max_font_size >= 14 and has_bold:
                        markdown_content += f"## {line_text}\n\n"
                    elif max_font_size >= 12 and has_bold:
                        markdown_content += f"### {line_text}\n\n"
                    else:
                        # Regular text
                        # Check for list items
                        if re.match(r'^[•\-\*]\s+', line_text) or re.match(r'^\d+[\.\)]\s+', line_text):
                            # Convert to markdown list
                            if re.match(r'^[•\-\*]\s+', line_text):
                                line_text = re.sub(r'^[•\-\*]\s+', '- ', line_text)
                            else:
                                line_text = re.sub(r'^(\d+)[\.\)]\s+', r'\1. ', line_text)
                        
                        markdown_content += f"{line_text}\n"
                
                markdown_content += "\n"
        
        # Add page separator
        markdown_content += "---\n\n"
    
    # Clean up excessive newlines
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    doc.close()
    print(f"Conversion completed: {output_path}")
    return True

if __name__ == "__main__":
    pdf_path = r"C:\Users\micro\Downloads\Briefing_Recurso_RD_Cannabis_Medicinal_CannabisHub_AECANI (4).pdf"
    output_path = "Briefing_Recurso_CannabisHub_AECANI.md"
    
    try:
        convert_pdf_to_markdown(pdf_path, output_path)
    except Exception as e:
        print(f"Error: {e}")