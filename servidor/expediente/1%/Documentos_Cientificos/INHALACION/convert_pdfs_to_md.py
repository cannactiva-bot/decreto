# -*- coding: utf-8 -*-
"""
Conversor de PDFs a Markdown con deteccion de headings
"""
import fitz  # PyMuPDF
import os
from datetime import datetime
from pathlib import Path

# Directorios
PDF_DIR = Path(__file__).parent / "pdf"
OUTPUT_DIR = Path(__file__).parent

def get_font_info(span):
    """Extrae info de fuente de un span"""
    size = span.get("size", 12)
    flags = span.get("flags", 0)
    is_bold = bool(flags & 2**4)  # bit 4 = bold
    return size, is_bold

def detect_heading_level(size, is_bold):
    """Detecta nivel de heading segun tamanio de fuente"""
    if size >= 16:
        return 1
    elif size >= 14:
        return 2
    elif size >= 12 and is_bold:
        return 3
    return 0  # No es heading

def extract_text_with_formatting(page):
    """Extrae texto con formato de una pagina"""
    blocks = page.get_text("dict")["blocks"]
    lines = []
    
    for block in blocks:
        if block["type"] != 0:  # Solo bloques de texto
            continue
        
        for line in block.get("lines", []):
            line_text = ""
            max_size = 0
            is_any_bold = False
            
            for span in line.get("spans", []):
                text = span.get("text", "")
                size, is_bold = get_font_info(span)
                line_text += text
                max_size = max(max_size, size)
                if is_bold:
                    is_any_bold = True
            
            line_text = line_text.strip()
            if not line_text:
                continue
            
            # Detectar heading
            heading_level = detect_heading_level(max_size, is_any_bold)
            
            if heading_level > 0:
                line_text = "#" * heading_level + " " + line_text
            
            lines.append(line_text)
    
    return "\n".join(lines)

def post_process_markdown(text):
    """Post-procesa el markdown para limpiar y formatear"""
    lines = text.split("\n")
    processed = []
    
    for line in lines:
        # Convertir bullets
        stripped = line.strip()
        if stripped.startswith(("- ", "* ", "+ ")):
            # Ya es lista markdown
            processed.append(line)
        elif stripped.startswith(("o ", "- ")):
            processed.append("- " + stripped[2:])
        else:
            processed.append(line)
    
    # Unir lineas y limpiar espacios multiples
    result = "\n".join(processed)
    
    # Reducir saltos de linea excesivos
    while "\n\n\n" in result:
        result = result.replace("\n\n\n", "\n\n")
    
    return result

def convert_pdf_to_md(pdf_path, output_path):
    """Convierte un PDF a Markdown"""
    try:
        doc = fitz.open(pdf_path)
        
        # Metadatos YAML
        title = pdf_path.stem.replace("_", " ")
        yaml_header = f"""---
title: "{title}"
source: "{pdf_path.name}"
converted: "{datetime.now().strftime('%Y-%m-%d')}"
pages: {len(doc)}
---

"""
        
        # Extraer contenido
        content_parts = []
        for page_num, page in enumerate(doc):
            page_text = extract_text_with_formatting(page)
            if page_text.strip():
                content_parts.append(page_text)
        
        doc.close()
        
        # Unir y post-procesar
        full_content = "\n\n".join(content_parts)
        full_content = post_process_markdown(full_content)
        
        # Guardar
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(yaml_header + full_content)
        
        return True, len(content_parts)
    
    except Exception as e:
        return False, str(e)

def main():
    print("="*60)
    print("CONVERSION PDF -> MARKDOWN")
    print("="*60)
    
    # Listar PDFs
    pdf_files = list(PDF_DIR.glob("*.pdf"))
    print(f"\nEncontrados {len(pdf_files)} PDFs en: {PDF_DIR}")
    print("-"*60)
    
    success_count = 0
    error_count = 0
    
    for pdf_file in sorted(pdf_files):
        # Nombre de salida (mismo nombre pero .md)
        output_name = pdf_file.stem + ".md"
        output_path = OUTPUT_DIR / output_name
        
        # Saltar si ya existe
        if output_path.exists():
            print(f"[SKIP] {pdf_file.name} -> ya existe MD")
            continue
        
        print(f"[PROC] {pdf_file.name}...", end=" ")
        
        success, result = convert_pdf_to_md(pdf_file, output_path)
        
        if success:
            print(f"OK ({result} paginas)")
            success_count += 1
        else:
            print(f"ERROR: {result}")
            error_count += 1
    
    print("-"*60)
    print(f"Completado: {success_count} convertidos, {error_count} errores")
    print("="*60)

if __name__ == "__main__":
    main()
