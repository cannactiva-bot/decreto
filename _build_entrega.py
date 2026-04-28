"""Construye la entrega completa para CNMC: estructura + ZIP.

Pasos:
1. Convierte 00_Indice_Anexos.md -> 00_Indice_Anexos.pdf (via Word COM)
2. Genera 00_LEEME.txt
3. Crea carpeta de entrega con la estructura jerárquica de Anexos/01..09/
4. Copia cada anexo a su carpeta destino con nombre código (A1.1_..., A8.6_..., etc.)
5. Empaqueta a ZIP
"""
import sys, io, os, shutil, zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r'C:\Users\micro\Desktop\cnmc'
ENTREGA = os.path.join(BASE, 'Dossier_AECANI_CNMC_Abril_2026')

# === 1. Convertir Indice MD -> DOCX -> PDF ===
import pypandoc
indice_md = os.path.join(BASE, '00_Indice_Anexos.md')
indice_docx = os.path.join(BASE, '00_Indice_Anexos.docx')
indice_pdf = os.path.join(BASE, '00_Indice_Anexos.pdf')
print('[1/5] Convirtiendo indice MD -> DOCX...')
pypandoc.convert_file(indice_md, 'docx', outputfile=indice_docx, extra_args=['--standalone'])
print('      DOCX generado.')
print('[1/5] Convirtiendo indice DOCX -> PDF...')
from docx2pdf import convert
convert(indice_docx, indice_pdf)
print(f'      PDF: {os.path.getsize(indice_pdf)/1024:.1f} KB')

# === 2. Generar LEEME.txt ===
leeme = """DOSSIER AECANI · COMISIÓN NACIONAL DE LOS MERCADOS Y LA COMPETENCIA · ABRIL 2026

================================================================
ESTRUCTURA DEL ENVÍO
================================================================

Este envío contiene la documentación que la Asociación Española
del Cáñamo Industrial (AECANI) traslada a la Comisión Nacional
de los Mercados y la Competencia (CNMC) en abril de 2026.

CONTENIDO RAÍZ:

  00_Dossier_AECANI_CNMC_Abril_2026_v4.pdf
       Documento principal. 30 páginas. 9 secciones.
       Sus citas remiten a los Anexos numerados con la
       convención [Anexo X.Y].

  00_Indice_Anexos.pdf
       Listado completo de los anexos documentales con
       referencia cruzada a la sección del dossier que
       cita cada uno.

  00_LEEME.txt
       Este documento.

  Anexos/
       Documentación de soporte. Una subcarpeta por
       bloque temático (los nueve bloques del §9 del
       dossier). Cada documento lleva como prefijo su
       código de anexo (ej. A3.1_, A8.6_, A9.10_) que
       coincide con la cita en el cuerpo del dossier.

================================================================
NAVEGACIÓN
================================================================

Para localizar el documento referido por una cita [Anexo X.Y]:

  1. Abrir la carpeta Anexos/0X_<bloque>/
  2. Buscar el fichero con prefijo AX.Y_

Ejemplo: la cita [Anexo 9.10] (sentencia Bundesgericht suizo
2C_348/2019) está en:

  Anexos/09_Material_complementario/A9.10_BGer_...pdf

================================================================
ASUNTOS DE FORMA
================================================================

· Todos los anexos se entregan en PDF con texto buscable salvo
  donde se anota expresamente lo contrario.
· Las traducciones literales de citas en lengua extranjera
  acompañan a la cita en el cuerpo del dossier; el documento
  fuente original se aporta sin traducir como anexo.
· Para cualquier ampliación o aclaración, AECANI queda a
  disposición de la CNMC en la dirección de contacto que
  consta en la portada del dossier principal.

— AECANI · Asociación Española del Cáñamo Industrial · Abril 2026
"""
leeme_path = os.path.join(BASE, '00_LEEME.txt')
with open(leeme_path, 'w', encoding='utf-8') as f:
    f.write(leeme)
print('[2/5] LEEME.txt generado.')

# === 3. Crear estructura de carpetas ===
print('[3/5] Creando estructura de carpetas...')
if os.path.exists(ENTREGA):
    shutil.rmtree(ENTREGA)
os.makedirs(ENTREGA)
anexos_root = os.path.join(ENTREGA, 'Anexos')
os.makedirs(anexos_root)
sub_dirs = [
    '01_Marco_competencial_CNMC',
    '02_Precedentes_CNMC_propios',
    '03_Marco_regulatorio_europeo',
    '04_Jurisprudencia_y_regimen_internacional',
    '05_Marco_regulatorio_espanol',
    '06_Datos_de_mercado',
    '07_Evidencia_cientifica',
    '08_Derecho_comparado_paises',
    '09_Material_complementario',
]
for d in sub_dirs:
    os.makedirs(os.path.join(anexos_root, d))

# === 4. Mapeo de archivos: origen -> (anexo_codigo, destino_relativo) ===
# Mapeamos los archivos de las carpetas existentes a la estructura final
SRC = BASE  # raiz
mapping = []  # list of (src_relpath, dst_path_under_entrega)

def add(src_rel, dst_rel):
    src_full = os.path.join(SRC, src_rel)
    dst_full = os.path.join(ENTREGA, dst_rel)
    mapping.append((src_full, dst_full))

# Documentos raiz
add('Dossier_CNMC_AECANI_v4.pdf', '00_Dossier_AECANI_CNMC_Abril_2026_v4.pdf')
add('00_Indice_Anexos.pdf', '00_Indice_Anexos.pdf')
add('00_LEEME.txt', '00_LEEME.txt')

# === ANEXO 1 · Marco competencial CNMC ===
add('03_marco_espana/10_Ley_3-2013_CNMC.pdf', 'Anexos/01_Marco_competencial_CNMC/A1.1_Ley_3-2013_creacion_CNMC.pdf')
add('03_marco_espana/09_Ley_20-2013_unidad_mercado.pdf', 'Anexos/01_Marco_competencial_CNMC/A1.2_Ley_20-2013_unidad_mercado.pdf')

# === ANEXO 2 · Precedentes CNMC propios ===
add('04_informes_cnmc/01_IPN_CNMC_029-22_Tabacos.pdf', 'Anexos/02_Precedentes_CNMC_propios/A2.1_IPN_CNMC_029-22_Tabacos.pdf')
add('04_informes_cnmc/02_IPN_CNMC_040-24_RD_productos_tabaco.pdf', 'Anexos/02_Precedentes_CNMC_propios/A2.2_IPN_CNMC_040-24_RD_productos_tabaco.pdf')
add('04_informes_cnmc/03_IPN_CNMC_028-25_APL_prevencion_tabaquismo.pdf', 'Anexos/02_Precedentes_CNMC_propios/A2.3_IPN_CNMC_028-25_APL_prevencion_tabaquismo.pdf')
add('04_informes_cnmc/04_NP_CNMC_dic2025_promocion_tabaco.pdf', 'Anexos/02_Precedentes_CNMC_propios/A2.4_NP_CNMC_dic2025_promocion_tabaco.pdf')
add('04_informes_cnmc/05_CNMC_Memoria_2024.pdf', 'Anexos/02_Precedentes_CNMC_propios/A2.5_CNMC_Memoria_2024.pdf')
add('04_informes_cnmc/06_CNMC_Guia_estudios_mercado.pdf', 'Anexos/02_Precedentes_CNMC_propios/A2.6_CNMC_Guia_estudios_mercado.pdf')

# === ANEXO 3 · Marco regulatorio europeo ===
add('02_marco_ue/07_COM_2025_553_final.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.1a_COM_2025_553_final_ES.pdf')
add('02_marco_ue/07b_COM_2025_553_final_ANEXOS_ES.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.1b_COM_2025_553_final_ANEXOS_ES.pdf')
add('02_marco_ue/07c_COM_2025_553_final_EN.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.1c_COM_2025_553_final_EN.pdf')
add('02_marco_ue/10_COM_2025_560_final_PAC_2028-2034_ES.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.2a_COM_2025_560_final_PAC_2028-2034_ES.pdf')
add('02_marco_ue/10b_COM_2025_560_final_ANEXOS_ES.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.2b_COM_2025_560_final_ANEXOS_ES.pdf')
add('02_marco_ue/01_Reglamento_UE_2021-2115_PAC.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.3_Reglamento_UE_2021-2115_PAC.pdf')
add('02_marco_ue/08_Reglamento_UE_1308-2013_OCM.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.4a_Reglamento_UE_1308-2013_OCM.pdf')
add('02_marco_ue/08b_Reglamento_UE_1308-2013_OCM_consolidada_20230101.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.4b_Reglamento_UE_1308-2013_OCM_consolidada_20230101.pdf')
add('02_marco_ue/02_Directiva_2014-40_TPD.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.5a_Directiva_2014-40_TPD.pdf')
add('02_marco_ue/02b_Directiva_2014-40_TPD_consolidada.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.5b_Directiva_2014-40_TPD_consolidada.pdf')
add('02_marco_ue/03_TPD3_revision_call_for_evidence_ES.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.6a_TPD3_revision_call_for_evidence_ES.pdf')
add('02_marco_ue/03b_TPD3_revision_call_for_evidence_EN.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.6b_TPD3_revision_call_for_evidence_EN.pdf')
add('02_marco_ue/03c_TPD3_evaluation_SWD_2026_111_EN.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.6c_TPD3_evaluation_SWD_2026_111_EN.pdf')
add('02_marco_ue/03d_TPD3_evaluation_executive_summary_SWD_2026_112_EN.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.6d_TPD3_evaluation_executive_summary_SWD_2026_112_EN.pdf')
add('02_marco_ue/03e_TPD3_RSB_opinion_SEC_2026_111_EN.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.6e_TPD3_RSB_opinion_SEC_2026_111_EN.pdf')
add('02_marco_ue/06_Decision_UE_2021-3_Consejo.pdf', 'Anexos/03_Marco_regulatorio_europeo/A3.7_Decision_UE_2021-3_Consejo.pdf')

# === ANEXO 4 · Jurisprudencia y regimen internacional ===
add('02_marco_ue/04_TJUE_C-663-18_Kanavape.pdf', 'Anexos/04_Jurisprudencia_y_regimen_internacional/A4.1a_TJUE_C-663-18_Kanavape_EUR-Lex.pdf')
add('02_marco_ue/04c_TJUE_C-663-18_Kanavape_sentencia_limpia.pdf', 'Anexos/04_Jurisprudencia_y_regimen_internacional/A4.1b_TJUE_C-663-18_Kanavape_sentencia_limpia.pdf')
add('02_marco_ue/04b_Conclusiones_AG_Tanchev_C-663-18_Kanavape_2020-05-14.pdf', 'Anexos/04_Jurisprudencia_y_regimen_internacional/A4.2_Conclusiones_AG_Tanchev_C-663-18_2020-05-14.pdf')
add('02_marco_ue/05_TJUE_C-462-01_Hammarsten.pdf', 'Anexos/04_Jurisprudencia_y_regimen_internacional/A4.3_TJUE_C-462-01_Hammarsten.pdf')
add('02_marco_ue/09_Carta_JIFE_CL20-2024_ES.pdf', 'Anexos/04_Jurisprudencia_y_regimen_internacional/A4.4a_Carta_JIFE_CL20-2024_ES.pdf')
add('02_marco_ue/09b_Carta_JIFE_CL20-2024_EN.pdf', 'Anexos/04_Jurisprudencia_y_regimen_internacional/A4.4b_Carta_JIFE_CL20-2024_EN.pdf')

# === ANEXO 5 · Marco regulatorio espanol ===
add('03_marco_espana/01_RD_903-2025_cannabis_medicinal.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.1_RD_903-2025_cannabis_medicinal.pdf')
add('03_marco_espana/02_RD_579-2017_tabaco.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.2_RD_579-2017_tabaco.pdf')
add('03_marco_espana/03_TRIS_notif_26624_RD579-2017_modif_ES.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.3a_TRIS_2025-0044-ES_notif_26624_ES.pdf')
add('03_marco_espana/03_TRIS_notif_26624_RD579-2017_modif_EN.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.3b_TRIS_2025-0044-ES_notif_26624_EN.pdf')
add('03_marco_espana/05_Recurso_395-2025_Cannabis_Hub_TS_demanda_formalizada.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.4_Recurso_395-2025_Cannabis_Hub_TS_demanda_formalizada.pdf')
add('03_marco_espana/06_Informe_Manjon-Cabeza_UCM_CannabisHub_2024-07-14_signed.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.5_Informe_Manjon-Cabeza_UCM_CannabisHub_2024-07-14.pdf')
add('03_marco_espana/04_Nota_informativa_MAPA_flores_canamo.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.6_Nota_informativa_MAPA_flores_canamo.pdf')
add('03_marco_espana/04b_Nota_DDGG_MAPA_canamo_dic2020.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.7_Nota_DDGG_MAPA_canamo_dic2020.pdf')
add('03_marco_espana/07_RD_969-2014_tabaco_cultivo_espejo.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.8_RD_969-2014_tabaco_cultivo_espejo.pdf')
add('03_marco_espana/08_Ley_24-2003_vino_cultivo_espejo.pdf', 'Anexos/05_Marco_regulatorio_espanol/A5.9_Ley_24-2003_vino_cultivo_espejo.pdf')

# === ANEXO 6 · Datos de mercado ===
add('01_datos_mercado/cannamonitor_resumen_publico.md', 'Anexos/06_Datos_de_mercado/A6.1_Cannamonitor_resumen_publico.md')
add('05_evidencia_cientifica/09_EDADES_2024_OEDA.pdf', 'Anexos/06_Datos_de_mercado/A6.2_EDADES_2024_OEDA.pdf')
add('01_datos_mercado/FEGA_Resumen_Informe_Actividades_2024.pdf', 'Anexos/06_Datos_de_mercado/A6.3_FEGA_Resumen_Informe_Actividades_2024.pdf')

# === ANEXO 7 · Evidencia cientifica ===
add('05_evidencia_cientifica/05_Tashkin_AnnATS_2013.pdf', 'Anexos/07_Evidencia_cientifica/A7.1a_Tashkin_AnnATS_2013.pdf')
add('05_evidencia_cientifica/01_Wu_Tashkin_NEJM_1988.txt', 'Anexos/07_Evidencia_cientifica/A7.1b_Wu_Tashkin_NEJM_1988_metadatos.txt')
add('05_evidencia_cientifica/02_Tashkin_PharmacolBiochemBehav_1991.txt', 'Anexos/07_Evidencia_cientifica/A7.1c_Tashkin_PBB_1991_metadatos.txt')
add('05_evidencia_cientifica/03_Barsky_Tashkin_1998.txt', 'Anexos/07_Evidencia_cientifica/A7.1d_Barsky_Tashkin_JNCI_1998_metadatos.txt')
add('05_evidencia_cientifica/04_Hashibe_Tashkin_CancerEpi_2006.txt', 'Anexos/07_Evidencia_cientifica/A7.1e_Hashibe_Tashkin_CancerEpi_2006_metadatos.txt')
add('05_evidencia_cientifica/06_Tashkin_Roth_Chest_2018.txt', 'Anexos/07_Evidencia_cientifica/A7.1f_Tashkin_Roth_Chest_2018_metadatos.txt')
add('05_evidencia_cientifica/07_Zobel_OFSP_CBD_2019.pdf', 'Anexos/07_Evidencia_cientifica/A7.2_Zobel_OFSP_CBD_2019.pdf')
add('05_evidencia_cientifica/08_WeedCare_Basel_Addiction_2025.pdf', 'Anexos/07_Evidencia_cientifica/A7.3_WeedCare_Basel_Addiction_2025.pdf')
add('02_marco_ue/11_WHO_ECDD_CBD_Critical_Review_2018-06.pdf', 'Anexos/07_Evidencia_cientifica/A7.4_WHO_ECDD_CBD_Critical_Review_2018-06.pdf')

# === ANEXO 8 · Derecho comparado por paises ===
# Por subdirectorio de pais. Copiamos cada pais como subcarpeta.
country_map = {
    'alemania': 'A8.1_Alemania',
    'austria': 'A8.2_Austria',
    'belgica': 'A8.3_Belgica',
    'francia': 'A8.4_Francia',
    'luxemburgo': 'A8.5_Luxemburgo',
    'italia': 'A8.6_Italia',
    'republica_checa': 'A8.7_Republica_Checa',
    'suiza': 'A8.8_Suiza',
    'canada': 'A8.9_Canada',
}
# Tratamos los paises por separado en una pasada al final

# === ANEXO 9 · Material complementario ===
add('03_marco_espana/14_PPT_Sanidad_Tabaquismo_canamo_CBD_Verdejo_2024-10-15.pdf', 'Anexos/09_Material_complementario/A9.1_PPT_Verdejo_Sanidad_Tabaquismo_2024-10-15.pdf')
# Doc Consenso 2019 y Lista positivos: descargados como adjuntos auxiliares; ubicados aun en 03_marco_espana
# Si existen como files separados, los copiamos
extras_to_check = {
    '03_marco_espana/14b_Doc_Consenso_Aplicacion_Ley28_2005.pdf': 'Anexos/09_Material_complementario/A9.2_Doc_Consenso_Aplicacion_Ley28_2005_2019.pdf',
    '03_marco_espana/14a_Lista_positivos_Hierbas.pdf': 'Anexos/09_Material_complementario/A9.3_Lista_positivos_Hierbas_para_fumar.pdf',
    '03_marco_espana/14c_Acuerdo_Lineas_actuacion.pdf': 'Anexos/09_Material_complementario/A9.3b_Acuerdo_CSP_Lineas_actuacion_tabaquismo.pdf',
}
for src_rel, dst_rel in extras_to_check.items():
    if os.path.exists(os.path.join(SRC, src_rel)):
        add(src_rel, dst_rel)
add('03_marco_espana/11_Circular_3-2020_Comisionado_Tabaco_CBD_estancos.pdf', 'Anexos/09_Material_complementario/A9.4_Circular_3-2020_Comisionado_Tabacos_CBD.pdf')
add('03_marco_espana/13_DGT_Consulta_V2242-22_IVA_flores_canamo_2022-10-26.pdf', 'Anexos/09_Material_complementario/A9.5_DGT_V2242-22_IVA_flores_canamo_2022-10-26.pdf')
# A9.6 (Tanchev) ya en 04
# A9.7 (WHO ECDD) ya en 07
add('06_derecho_comparado/italia/Sentenza_83-2015_Corte_Costituzionale.pdf', 'Anexos/09_Material_complementario/A9.8a_Sentenza_83-2015_Corte_Costituzionale_oficial.pdf')
add('06_derecho_comparado/italia/Sentenza_83-2015_GazzettaUfficiale.pdf', 'Anexos/09_Material_complementario/A9.8b_Sentenza_83-2015_GazzettaUfficiale.pdf')
add('06_derecho_comparado/italia/Sentenza_240-2017_GazzettaUfficiale.pdf', 'Anexos/09_Material_complementario/A9.9_Sentenza_240-2017_GazzettaUfficiale.pdf')
suiza_files = {
    'tabaksteuer_BGer_2C_348_2019_oficial.html': 'A9.10a_BGer_2C_348-2019_oficial.html',
    'tabaksteuer_BGer_2C_348_2019.html': 'A9.10b_BGer_2C_348-2019_DFR_Berna.html',
    'tabaksteuer_BGer_2C_402_2019.html': 'A9.10c_BGer_2C_402-2019_gemela.html',
    'tabaksteuer_BVGer_A-1211_2018.html': 'A9.10d_BVGer_A-1211-2018_revocada.html',
    'tabaksteuer_TStG_de.pdf': 'A9.10e_Tabaksteuergesetz_TStG_RS_641-31.pdf',
    'tabaksteuer_TStV_de.pdf': 'A9.10f_Tabaksteuerverordnung_TStV_RS_641-311.pdf',
}
for src_name, dst_name in suiza_files.items():
    src_p = f'06_derecho_comparado/suiza/{src_name}'
    if os.path.exists(os.path.join(SRC, src_p)):
        add(src_p, f'Anexos/09_Material_complementario/{dst_name}')
add('07_aecani_interno/PNL_Comision_Agricultura_AEMPS_Kanavape_Rufian_Guijarro.pdf', 'Anexos/09_Material_complementario/A9.11_PNL_Comision_Agricultura_AEMPS_Kanavape.pdf')

# === Ejecucion: copia ===
print(f'[4/5] Copiando {len(mapping)} archivos a la estructura de entrega...')
copied = 0
missing = []
for src_full, dst_full in mapping:
    if not os.path.exists(src_full):
        missing.append(src_full)
        continue
    os.makedirs(os.path.dirname(dst_full), exist_ok=True)
    shutil.copy2(src_full, dst_full)
    copied += 1
print(f'      Copiados: {copied}.  Faltantes: {len(missing)}.')

# Anexo 8: copia de subcarpetas pais completas
print('[4/5] Copiando subcarpetas pais (Anexo 8)...')
src_dc = os.path.join(BASE, '06_derecho_comparado')
dst_dc = os.path.join(anexos_root, '08_Derecho_comparado_paises')
for src_name, dst_name in country_map.items():
    src_country = os.path.join(src_dc, src_name)
    dst_country = os.path.join(dst_dc, dst_name)
    if os.path.exists(src_country):
        shutil.copytree(src_country, dst_country)
        print(f'      Copiada subcarpeta: {dst_name}')

if missing:
    print('\n  AVISO archivos no encontrados (omitidos):')
    for m in missing[:10]:
        print(f'    {m}')

# === 5. Crear ZIP ===
print('[5/5] Creando ZIP...')
zip_path = os.path.join(BASE, 'Dossier_AECANI_CNMC_Abril_2026.zip')
if os.path.exists(zip_path):
    os.remove(zip_path)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
    for root, dirs, files in os.walk(ENTREGA):
        for f in files:
            fp = os.path.join(root, f)
            arc = os.path.relpath(fp, BASE)
            zf.write(fp, arc)
mb = os.path.getsize(zip_path) / (1024*1024)
print(f'\n>>> ZIP listo: {zip_path}  ({mb:.1f} MB)')
print(f'>>> Carpeta entrega: {ENTREGA}')
