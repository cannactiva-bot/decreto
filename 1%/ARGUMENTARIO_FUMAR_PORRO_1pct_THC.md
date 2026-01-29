---
title: "¿Es psicoactivo fumar un porro de cáñamo al 1% de THC? (Δ9-THC nominal vs dosis sistémica)"
date: 2026-01-23
scope: "Argumentario regulatorio (CN 1211 90 86) – escenario de combustión (smoking/vaping) como 'abuse liability'"
status: draft
---

## Resumen ejecutivo (respuesta corta)

- **Si la pregunta es “¿puede producir *intoxicación* (efecto estupefaciente claro) fumando 1 porro típico?”**: **lo más defendible es “NO (en condiciones realistas)”**, porque la **dosis sistémica** que llega a sangre es **una fracción** de la dosis nominal y, a 1% THC, un porro típico queda **muy por debajo** de los escenarios usados como “dosis mínima intoxicante” en argumentarios forenses/regulatorios.
- **Si la pregunta es “¿puede producir *algún* micro‑efecto subjetivo en un consumidor naïve?”**: **no se puede excluir al 100%** por la **alta variabilidad** interindividual y de la topografía de fumado (Huestis, 2007).

**Idea-fuerza para dossier**: en combustión, el cáñamo al 1% THC **no equivale** a “1% de dosis efectiva”: hay pérdidas físicas (pirólisis + humo lateral + colilla) y, además, variabilidad en absorción. Esto reduce mucho el riesgo de intoxicación “prácticamente alcanzable”.

---

## 1) Definiciones y marco (para evitar errores de concepto)

### 1.1 THC “nominal” (en planta) vs THC “sistémico” (en sangre)

- **THC nominal**: cantidad de THC (idealmente **THC total**, p.ej. \(THC_{total} = THC + 0.877 \times THCA\)) que “hay en el material” en % peso/peso sobre materia seca.
- **THC sistémico**: cantidad que **llega a circulación** tras fumar/vapear. Es la variable relevante para discutir “psicoactividad” real.

### 1.2 Por qué la combustión reduce la dosis efectiva

En un porro, el THC se reparte (y se pierde) entre:
- **mainstream smoke** (humo principal, el que potencialmente inhala el consumidor),
- **sidestream smoke** (humo lateral, pérdidas ambientales),
- **pirólisis/destrucción térmica**,
- **residuo** (colilla/ceniza/depósitos).

Un resumen clásico cita esta partición en términos de orden de magnitud:

> “**20 to 37 percent** of the THC in a joint hits the consumer in mainstream smoke. **Twenty-three to 30 percent** is lost to pyrolytic destruction, and **40 to 50 percent** goes up in sidestream smoke.”  
> — Perez‑Reyes M. (1990), NIDA Research Monograph 99:42‑62. *(cita recogida en `RESEARCH_THC_FARMACOCINETICA_SCCS_STYLE.md`)*

Y un estudio con máquina de fumar (condiciones tipo ISO) cuantifica una eficiencia de entrega aún menor:

> “The Δ9‑THC delivery efficiency during smoking … **mean and median of 12.6% and 10.8%** … (ranging from **7.2% to 28.0%**).”  
> — Sheehan et al. (PMID: **31304445**). *(cita recogida en `RESEARCH_THC_FARMACOCINETICA_SCCS_STYLE.md`)*

---

## 2) Cálculo directo: ¿cuánto THC “hay” en un porro al 1%?

Regla rápida (1% = 10 mg THC por gramo de material seco):

\[
THC_{nominal}(\text{mg}) = \text{masa (g)} \times 10
\]

| Masa de porro (g) | THC nominal al 1% (mg) |
|---:|---:|
| 0,3 g | 3 mg |
| 0,5 g | 5 mg |
| 1,0 g | 10 mg |
| 1,5 g | 15 mg |
| 3,0 g | 30 mg |

**Nota de método (importante):** esto es “THC total equivalente” si el 1% se expresa como THC total (como en Farmacopea). En combustión la descarboxilación de THCA tiende a ser alta, pero el dossier debe **dejar claro** si el umbral es Δ9‑THC o THC total.

---

## 3) De THC nominal → dosis realmente inhalada → dosis sistémica

### 3.1 Dos formas correctas de modelar (elige una y sé consistente)

**Modelo A (recomendado para dossier por robustez):** usar **bio‑disponibilidad global por fumado** \(F_{smoke}\), ya que integra pérdidas físicas + inhalación + absorción (y evita doble contabilidad).

- Huestis (2007) resume que la bio‑disponibilidad por fumado reportada en literatura puede variar **2–56%** por dinámica de fumado (PMID: **17712819**).
- Ohlsson et al. (1980) es el estudio clásico comparando rutas con referencia IV (PMID: **6250760**), citado en literatura como base para estimar disponibilidad sistémica por fumado.

Entonces:

\[
THC_{sistémico} \approx THC_{nominal} \times F_{smoke}
\]

**Modelo B (solo si documentas bien cada factor):** separar en:
- \(f_{transfer}\): fracción de THC nominal que llega a mainstream smoke (p.ej. 7–28% en Sheehan et al.).
- \(f_{abs}\): fracción de lo inhalado que se absorbe sistémicamente (pulmonar).

Entonces:

\[
THC_{sistémico} \approx THC_{nominal} \times f_{transfer} \times f_{abs}
\]

⚠️ **Advertencia**: no mezclar el \(F_{smoke}\) (global) con el \(f_{transfer}\) (solo mainstream), porque se duplican pérdidas.

### 3.2 Tabla de escenarios (porro 0,5 g @ 1% THC)

Para un porro “típico” de **0,5 g** a **1% THC**:

- \(THC_{nominal} = 5 \text{ mg}\)

Escenarios con \(F_{smoke}\) (global) para acotar:

| Escenario | \(F_{smoke}\) asumido | THC sistémico estimado (mg) |
|---|---:|---:|
| Muy conservador (bajo) | 2% | 0,10 |
| Conservador (ocasional) | 10% | 0,50 |
| Central | 20% | 1,00 |

**Lectura**: incluso en un escenario relativamente alto (20%), la dosis sistémica ronda **~1 mg** por un porro de 0,5 g al 1% THC. Esto es **muy inferior** al orden de magnitud que suele usarse para hablar de “intoxicación mínima” en argumentarios forenses basados en mg de THC.

---

## 4) Conexión con “dosis mínima intoxicante” (forense/regulatorio) y con EIHA

### 4.1 EIHA usa 15 mg THC como “minimal intoxicating dose”

El paper de EIHA (PAC 2028‑2032) formula:

> “To obtain a minimal intoxicating dose of approximately **15 mg of THC** (an amount recognised in case law as sufficient to induce intoxication)…”  
> — `EIHA_PAC_2028_2032.md` (Anexo I)

**Cálculo inmediato para 1% THC:**
- 15 mg THC nominal equivalen a **1,5 g** de biomasa al 1% (tabla de la Sección 2).
- Y esto es **antes** de pérdidas por combustión y humo lateral.

### 4.2 “15 mg” entregados al consumidor: acotación por física de combustión (mainstream smoke)

Si el umbral de “15 mg THC” se interpreta como “dosis que realmente llega al consumidor” (al menos al **humo mainstream**, previo a absorción), entonces la cantidad de biomasa necesaria crece mucho por las pérdidas en combustión.

Usando el rango de eficiencia de entrega a mainstream reportado en Sheehan et al. (PMID: **31304445**) — **7,2% a 28%**—:

\[
THC_{nominal}\ \text{necesario para 15 mg en mainstream} = \frac{15\ \text{mg}}{f_{transfer}}
\]

| \(f_{transfer}\) a mainstream | THC nominal necesario (mg) | Biomasa al 1% necesaria (g) |
|---:|---:|---:|
| 28% | 53,6 mg | 5,36 g |
| 12,6% (media) | 119,0 mg | 11,90 g |
| 7,2% | 208,3 mg | 20,83 g |

**Lectura**: incluso antes de considerar absorción pulmonar incompleta, para “poner 15 mg de THC” en el humo realmente inhalable harían falta **varios gramos (5–21 g)** de biomasa al 1% bajo esos supuestos. Este orden de magnitud es coherente con el argumento de EIHA de que la intoxicación por combustión con cáñamo “no es una vía realista”, pero aquí queda cuantificado para el caso 1%.

### 4.2 Ancla española útil: INTCF (dosis mínima psicoactiva)

El **Instituto Nacional de Toxicología** (tabla vigente/revisada) incluye para “Marihuana” una **dosis mínima psicoactiva** expresada como:

- “**10 mg (vía oral)** …”  
— `20210730_INTF_dosis_minimas_psicoactivas_trafico_de_drogas_1.md`

**Uso estratégico (sin sobre‑interpretar):**
- Sirve para justificar que el orden de magnitud “10–15 mg THC” aparece en **material forense** utilizado en práctica.
- Para combustión, el dossier debe aclarar que **vía y cinética** son distintas, pero el número es útil como *marco* del debate (especialmente si EIHA invoca “case law” sin concretar).

---

## 5) Conclusión defendible para dossier (frase lista para pegar)

**Conclusión (versión corta, técnicamente honesta):**

> Fumar un porro de cáñamo al 1% THC no implica una dosis sistémica equivalente al THC nominal del material. La combustión introduce pérdidas sustanciales (pirólisis y humo lateral) y la exposición efectiva depende de la topografía de fumado, con variabilidad amplia (Huestis, 2007). Bajo supuestos realistas de masa de porro (0,3–0,5 g) y bio‑disponibilidad global por fumado, la dosis sistémica esperable se sitúa típicamente en el rango de **sub‑mg a ~1 mg**, muy por debajo del orden de magnitud de “dosis mínima intoxicante” (10–15 mg THC) invocado en argumentarios forenses/regulatorios. Por tanto, **no es una vía realista para intoxicación** con un porro típico, aunque no puede excluirse a priori algún micro‑efecto en consumidores naïve debido a la variabilidad individual.

---

## 6) Fuentes y documentos internos relacionados (para trazabilidad en este repo)

- `RESEARCH_THC_FARMACOCINETICA_SCCS_STYLE.md` (mapa de evidencia PK/PD y citas textuales)
- `EIHA_PAC_2028_2032.md` (argumento EIHA “15 mg THC” y “case law”)
- `PROTOCOLO_ANALISIS_CRITICO_EIHA_15MG_THC.md` (deconstrucción crítica del argumento EIHA; ojo con supuestos de biodisponibilidad)
- `Farmacopea_EU_3028_Cannabis_flos.md` (definición “CBD‑dominant type”: **THC total máx. 1%**, CBD mín. 5%)
- `20210730_INTF_dosis_minimas_psicoactivas_trafico_de_drogas_1.md` (INTCF: tabla dosis mínimas psicoactivas)

