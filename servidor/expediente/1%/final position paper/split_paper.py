# -*- coding: utf-8 -*-
"""
Script para separar el PAPER_SHORT.md en dos documentos:
1. PAPER_PRINCIPAL.md - Paper + Bibliografia (estructura profesional)
2. ANEXOS.md - Solo los anexos tecnicos A, B, C, D
"""

import re

def split_paper():
    # Leer el archivo original
    with open('PAPER_SHORT.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar donde empiezan los ANEXOS
    anexo_match = re.search(r'^# ANEXO\b', content, re.MULTILINE)
    
    # Buscar donde empieza la BIBLIOGRAFIA
    biblio_match = re.search(r'^# BIBLIOGRAFÍA', content, re.MULTILINE)
    
    if not anexo_match or not biblio_match:
        print("ERROR: No se encontraron las secciones necesarias")
        print(f"  Anexo encontrado: {anexo_match is not None}")
        print(f"  Bibliografia encontrada: {biblio_match is not None}")
        return
    
    anexo_pos = anexo_match.start()
    biblio_pos = biblio_match.start()
    
    # Extraer las tres partes
    paper_body = content[:anexo_pos].rstrip()
    anexos_content = content[anexo_pos:biblio_pos].rstrip()
    bibliografia = content[biblio_pos:]
    
    # ===========================================
    # PAPER PRINCIPAL = Cuerpo + Bibliografia
    # ===========================================
    paper_principal = paper_body + "\n\n---\n\n" + bibliografia
    
    # ===========================================
    # ANEXOS = Solo anexos tecnicos
    # ===========================================
    anexos_header = """# ANEXOS TÉCNICOS — POSITION PAPER

## Propuesta del sector del cáñamo para la PAC 2028–2034
### Alineación con estándares internacionales de THC

**Cannabis Hub — Enero 2026**

> **Este documento contiene los anexos técnicos del Position Paper.**  
> Ver documento principal con bibliografía completa: [PAPER_PRINCIPAL.md](PAPER_PRINCIPAL.md)

---

"""
    
    anexos_doc = anexos_header + anexos_content
    
    # Agregar nota final en anexos
    anexos_doc += "\n\n---\n\n> **Bibliografía completa disponible en [PAPER_PRINCIPAL.md](PAPER_PRINCIPAL.md)**\n"
    
    # ===========================================
    # GUARDAR ARCHIVOS
    # ===========================================
    
    with open('PAPER_PRINCIPAL.md', 'w', encoding='utf-8') as f:
        f.write(paper_principal)
    
    with open('ANEXOS.md', 'w', encoding='utf-8') as f:
        f.write(anexos_doc)
    
    # Estadisticas
    print("=" * 50)
    print("SEPARACION COMPLETADA - ESTRUCTURA PROFESIONAL")
    print("=" * 50)
    print(f"\nPAPER_PRINCIPAL.md")
    print(f"  - Cuerpo del paper: {len(paper_body):,} chars")
    print(f"  - Bibliografia: {len(bibliografia):,} chars")
    print(f"  - TOTAL: {len(paper_principal):,} chars")
    print(f"\nANEXOS.md")
    print(f"  - Anexos A, B, C, D: {len(anexos_content):,} chars")
    print(f"  - TOTAL: {len(anexos_doc):,} chars")
    print(f"\nOriginal: {len(content):,} chars")

if __name__ == '__main__':
    split_paper()
