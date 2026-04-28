"""Convierte v4.docx a PDF usando Microsoft Word via docx2pdf."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx2pdf import convert
import os

src = r'C:\Users\micro\Desktop\cnmc\Dossier_CNMC_AECANI_v4.docx'
dst = r'C:\Users\micro\Desktop\cnmc\Dossier_CNMC_AECANI_v4.pdf'
print(f'Convirtiendo {os.path.basename(src)} -> PDF...')
convert(src, dst)
sz = os.path.getsize(dst) / 1024
print(f'OK · PDF generado · {sz:.1f} KB · {dst}')
