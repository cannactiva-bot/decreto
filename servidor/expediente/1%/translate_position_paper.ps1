# Script para traducir Position Paper usando DeepL API
# API Key de DeepL
$apiKey = "00b81fc3-4afe-46d8-b629-c0952bdcd876"
$apiUrl = "https://api.deepl.com/v2/translate"

# Cargar ensamblado para URL encoding
Add-Type -AssemblyName System.Web

# Leer el archivo Markdown completo
$inputFile = "final position paper/POSITION_PAPER_COMPLETO_1pct_THC.md"
$outputFile = "final position paper/POSITION_PAPER_COMPLETO_1pct_THC_EN.md"

Write-Host "Leyendo documento original..." -ForegroundColor Green
$content = Get-Content $inputFile -Raw -Encoding UTF8

# Función para traducir texto usando DeepL API
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
            "text" = $text
            "source_lang" = $sourceLang
            "target_lang" = $targetLang
            "preserve_formatting" = "1"
            "formality" = "more"
        }
        
        $bodyString = ($body.GetEnumerator() | ForEach-Object { 
            "$($_.Key)=$([System.Web.HttpUtility]::UrlEncode($_.Value))" 
        }) -join "&"
        
        $response = Invoke-RestMethod -Uri $apiUrl -Method POST -Headers $headers -Body $bodyString
        
        return $response.translations[0].text
    }
    catch {
        Write-Host "Error en traducción: $($_.Exception.Message)" -ForegroundColor Red
        return $text
    }
}

# Dividir el documento en secciones manejables (máximo ~4000 caracteres)
Write-Host "Dividiendo documento en secciones..." -ForegroundColor Green

$sections = @()
$lines = $content -split "`r?`n"
$currentSection = ""
$maxChars = 4000

foreach ($line in $lines) {
    $testSection = $currentSection + $line + "`n"
    
    if ($testSection.Length -gt $maxChars -and $currentSection.Length -gt 0) {
        $sections += $currentSection.TrimEnd()
        $currentSection = $line + "`n"
    } else {
        $currentSection = $testSection
    }
}

# Añadir la última sección
if ($currentSection.Length -gt 0) {
    $sections += $currentSection.TrimEnd()
}

Write-Host "Documento dividido en $($sections.Count) secciones" -ForegroundColor Green

# Traducir cada sección
$translatedSections = @()
$i = 1

foreach ($section in $sections) {
    Write-Host "Traduciendo sección $i/$($sections.Count)..." -ForegroundColor Yellow
    
    $translatedSection = Translate-Text -text $section
    $translatedSections += $translatedSection
    
    # Pausa entre llamadas para respetar rate limits
    Start-Sleep -Seconds 1
    $i++
}

# Unir todas las secciones traducidas
$translatedContent = $translatedSections -join "`n`n"

# Guardar el documento traducido
Write-Host "Guardando documento traducido..." -ForegroundColor Green
$translatedContent | Out-File -FilePath $outputFile -Encoding UTF8

Write-Host "¡Traducción completada!" -ForegroundColor Green
Write-Host "Archivo guardado en: $outputFile" -ForegroundColor Cyan