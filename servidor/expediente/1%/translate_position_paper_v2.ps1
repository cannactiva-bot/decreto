# Script mejorado para traducir Position Paper usando DeepL API
$apiKey = "00b81fc3-4afe-46d8-b629-c0952bdcd876"
$apiUrl = "https://api.deepl.com/v2/translate"

# Leer el archivo Markdown completo
$inputFile = "final position paper/POSITION_PAPER_COMPLETO_1pct_THC.md"
$outputFile = "final position paper/POSITION_PAPER_COMPLETO_1pct_THC_EN.md"

Write-Host "Leyendo documento original..." -ForegroundColor Green
$content = Get-Content $inputFile -Raw -Encoding UTF8

# Función mejorada para traducir texto usando DeepL API
function Translate-Text {
    param(
        [string]$text,
        [string]$sourceLang = "ES",
        [string]$targetLang = "EN"
    )
    
    try {
        $headers = @{
            "Authorization" = "DeepL-Auth-Key $apiKey"
            "Content-Type" = "application/x-www-form-urlencoded"
        }
        
        $body = @{
            text = $text
            source_lang = $sourceLang
            target_lang = $targetLang
        }
        
        # Convertir a formato URL-encoded (método que funciona)
        $formData = @()
        $body.GetEnumerator() | ForEach-Object {
            $formData += "$($_.Key)=$([System.Uri]::EscapeDataString($_.Value))"
        }
        $bodyString = $formData -join "&"
        
        $response = Invoke-RestMethod -Uri $apiUrl -Method POST -Headers $headers -Body $bodyString
        
        return $response.translations[0].text
    }
    catch {
        Write-Host "Error en traducción: $($_.Exception.Message)" -ForegroundColor Red
        # En caso de error, devolver texto original
        return $text
    }
}

# Dividir el documento en secciones por títulos principales (más inteligente)
Write-Host "Dividiendo documento en secciones..." -ForegroundColor Green

# Separar por secciones principales (# headers)
$sections = @()
$lines = $content -split "`r?`n"
$currentSection = ""
$maxChars = 3000  # Más conservador

foreach ($line in $lines) {
    # Si encuentra un header principal y la sección actual no está vacía
    if ($line -match "^# " -and $currentSection.Trim().Length -gt 0) {
        $sections += $currentSection.TrimEnd()
        $currentSection = $line + "`n"
    } else {
        $currentSection += $line + "`n"
        
        # También dividir si se excede el límite de caracteres
        if ($currentSection.Length -gt $maxChars -and $line.Trim() -eq "") {
            $sections += $currentSection.TrimEnd()
            $currentSection = ""
        }
    }
}

# Añadir la última sección
if ($currentSection.Trim().Length -gt 0) {
    $sections += $currentSection.TrimEnd()
}

Write-Host "Documento dividido en $($sections.Count) secciones" -ForegroundColor Green

# Traducir cada sección
$translatedSections = @()
$i = 1

foreach ($section in $sections) {
    Write-Host "Traduciendo sección $i/$($sections.Count) (${section.Length} caracteres)..." -ForegroundColor Yellow
    
    if ($section.Trim().Length -eq 0) {
        Write-Host "  Sección vacía, saltando..." -ForegroundColor Gray
        $translatedSections += $section
        continue
    }
    
    # Mostrar preview de la sección
    $preview = ($section.Trim() -split "`n")[0]
    if ($preview.Length -gt 100) { $preview = $preview.Substring(0, 100) + "..." }
    Write-Host "  Preview: $preview" -ForegroundColor Gray
    
    $translatedSection = Translate-Text -text $section
    $translatedSections += $translatedSection
    
    # Pausa entre llamadas para respetar rate limits
    Start-Sleep -Seconds 2
    $i++
}

# Unir todas las secciones traducidas
Write-Host "Uniendo secciones traducidas..." -ForegroundColor Green
$translatedContent = $translatedSections -join "`n"

# Guardar el documento traducido
Write-Host "Guardando documento traducido..." -ForegroundColor Green
$translatedContent | Out-File -FilePath $outputFile -Encoding UTF8

Write-Host "¡Traducción completada!" -ForegroundColor Green
Write-Host "Archivo guardado en: $outputFile" -ForegroundColor Cyan
Write-Host "Tamaño original: $($content.Length) caracteres" -ForegroundColor Cyan
Write-Host "Tamaño traducido: $($translatedContent.Length) caracteres" -ForegroundColor Cyan