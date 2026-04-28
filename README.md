# Dossier AECANI · CNMC · Abril 2026

Este repositorio contiene el **dossier que la Asociación Española del Cáñamo Industrial (AECANI) presenta a la Comisión Nacional de los Mercados y la Competencia (CNMC)** en abril de 2026, junto con la totalidad de los anexos documentales que lo soportan.

## Documento principal

- **`Dossier_CNMC_AECANI_v4.docx`** — versión editable (master) del dossier. 9 secciones, 30 páginas, ≈68 K caracteres.
- **`Dossier_CNMC_AECANI_v4.pdf`** — exportación PDF de la versión anterior, lista para entrega institucional.
- **`Dossier_CNMC_AECANI_v3.docx` / `.pdf`** — versión inmediatamente previa, conservada como referencia para diff.

## Entrega institucional

- **`Dossier_AECANI_CNMC_Abril_2026.zip`** (≈58 MB) — paquete completo con dossier + 114 anexos numerados conforme al §9 del propio dossier. Estructura jerárquica navegable.
- **`Dossier_AECANI_CNMC_Abril_2026/`** — la misma estructura del ZIP descomprimida (carpeta de entrega), por si se prefiere navegar sin descomprimir.

## Trabajo y soportes

| Carpeta | Contenido |
|---|---|
| `01_datos_mercado/` | Cannamonitor (resumen público), FEGA, INE, recortes de prensa con cifras agregadas. |
| `02_marco_ue/` | Reglamentos PAC y OCM, Directiva TPD, Kanavape, Hammarsten, Decisión UE 2021/3, COM(2025) 553 y 560 (ES + EN + anexos), TPD3, Carta JIFE/INCB CL.20/2024 (ES + EN), WHO ECDD CBD 2018, AG Tanchev. |
| `03_marco_espana/` | RD 903/2025, RD 579/2017, TRIS 2025/0044/ES, Recurso TS 395/2025 (demanda formalizada), Informe Manjón-Cabeza UCM, Notas MAPA, leyes espejo (RD 969/2014, Ley 24/2003 vino), Circular 3/2020 Comisionado Tabacos, DGT V2242-22, PPT Verdejo (Min. Sanidad). |
| `04_informes_cnmc/` | IPN/CNMC/029/22, IPN/CNMC/040/24, IPN/CNMC/028/25, Memoria CNMC 2024, Guía estudios de mercado MET/DP/01/13, Ley 3/2013 (creación CNMC). |
| `05_evidencia_cientifica/` | Programa Tashkin (UCLA-NIDA), FOPH Suiza Zobel 2019, Weed Care Basel (Addiction 2025), EDADES 2024 OEDA. |
| `06_derecho_comparado/` | 9 fichas país con fuentes primarias: Alemania (CanG/MedCanG), Austria, Bélgica, Francia, Luxemburgo, Italia (Sentenza 83/2015 Corte Cost. + 240/2017 + TUA), República Checa (Zakon 167/1998 umbral 1%), Suiza (BGer 2C_348/2019 — flor cáñamo no es sucedáneo del tabaco fiscalmente), Canadá (Cannabis Act 2018). |
| `07_aecani_interno/` | Plan equipo asesor AECANI para borrador RD, correspondencia CND con Pavel Pachta y Studio Bulleri, BOCG proposiciones, PNL Comisión Agricultura (ERC+Sumar+Bildu), Rapporto strategia demonopolizzazione vaping (Sentenza 83/2015 italiana). |

## Enriquecimiento v3 → v4

12 inserciones quirúrgicas + 3 erratas corregidas. Detalle completo en `propuestas_v4.md`. Cambios cuantificables: +41 párrafos, +12 K caracteres, +4 páginas, §9 ampliado con doctrina administrativa española adicional, jurisprudencia comparada italiana y suiza, y apoyo parlamentario.

Triple muralla jurisprudencial sobre la NO equiparación cáñamo/tabaco:

1. **TJUE C-663/18 *Kanavape*** (2020) — el cáñamo no psicoactivo no puede tratarse como estupefaciente por los Estados miembros.
2. **Bundesgericht suizo 2C_348/2019** (2020) — falta base legal para someter las flores de cáñamo al impuesto sobre el tabaco; no hay relación de sustitución con el tabaco desde la perspectiva del consumidor; devolución de 33 M CHF a productores.
3. **Corte Costituzionale italiana, Sentenza 83/2015** (con 240/2017) — *del tutto irragionevole* extender el régimen administrativo y tributario del tabaco a productos sin nicotina.

Trinidad de incoherencia interna española:

1. **DGT V2242-22** (Hacienda) — flor de cáñamo = planta ornamental, IVA 10%.
2. **Circular 3/2020 Comisionado para el Mercado de Tabacos** (Hacienda) — productos de cannabis prohibidos en estancos, independientemente de su contenido en THC.
3. **PPT Verdejo · Jefa de Área de Tabaquismo** (Sanidad) — cáñamo, cannabis y CBD no autorizados como hierbas para fumar, contra el régimen general de venta libre del Documento de Consenso 2019.

## Scripts de trabajo

- `_apply_v4.py` — aplica las inserciones de `propuestas_v4.md` sobre `Dossier_CNMC_AECANI_v3.docx` y produce el v4 docx.
- `_convert_v4.py` — convierte el v4 docx a PDF vía Word COM (docx2pdf).
- `_build_entrega.py` — construye la estructura jerárquica de anexos y empaqueta el ZIP.
- `_analyze_v3.py` — análisis de estructura del docx para localizar anclajes de inserción.

## Procedimiento de referencia

Recurso contencioso-administrativo nº **395/2025**, Sala Tercera (Sección Cuarta) del Tribunal Supremo, *Asociación Cannabis Hub vs. Administración del Estado*, demanda formalizada el 10 de marzo de 2026 bajo dirección letrada del despacho **Baño León (José María Baño Fos)**.

---

Material confidencial · uso institucional AECANI · abril 2026.
