"""Debug: inspeccionar styleId real de los Headings en el docx para arreglar el detector."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document
from docx.oxml.ns import qn

d = Document(r'C:\Users\micro\Desktop\cnmc\Dossier_CNMC_AECANI_v4.docx')

# Localizar §4.2.5 y los siguientes parrafos hasta encontrar §4.3
found_425 = False
count = 0
for i, p in enumerate(d.paragraphs):
    txt = p.text.strip()
    if txt.startswith("4.2.5"):
        found_425 = True
    if found_425:
        count += 1
        # Inspeccionar el pStyle XML
        pPr = p._element.find(qn('w:pPr'))
        sval = ''
        if pPr is not None:
            pStyle = pPr.find(qn('w:pStyle'))
            if pStyle is not None:
                sval = pStyle.get(qn('w:val')) or ''
        # Tambien estilo "name" via python-docx
        sname = p.style.name if p.style else ''
        print(f'P[{i:3d}] sval={sval!r:25s} name={sname!r:18s} txt={txt[:80]!r}')
        if count > 25:  # limitar salida
            break
        if txt.startswith("4.3 ") and 'Heading' in (sname or ''):
            print(f'  >> §4.3 detectado en P[{i}]')
            break
