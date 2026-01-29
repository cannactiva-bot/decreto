# Test simple de DeepL API
$apiKey = "00b81fc3-4afe-46d8-b629-c0952bdcd876"
$apiUrl = "https://api.deepl.com/v2/translate"

# Test simple con texto corto
$testText = "Hola mundo. Este es un test."

try {
    Write-Host "Probando conexión a DeepL API..." -ForegroundColor Yellow
    
    # Headers para DeepL API
    $headers = @{
        "Authorization" = "DeepL-Auth-Key $apiKey"
        "Content-Type" = "application/x-www-form-urlencoded"
    }
    
    # Cuerpo de la petición
    $body = @{
        text = $testText
        source_lang = "ES"
        target_lang = "EN"
    }
    
    # Convertir a formato URL-encoded
    $formData = @()
    $body.GetEnumerator() | ForEach-Object {
        $formData += "$($_.Key)=$([System.Uri]::EscapeDataString($_.Value))"
    }
    $bodyString = $formData -join "&"
    
    Write-Host "Enviando petición..." -ForegroundColor Yellow
    Write-Host "URL: $apiUrl" -ForegroundColor Gray
    Write-Host "Body: $bodyString" -ForegroundColor Gray
    
    $response = Invoke-RestMethod -Uri $apiUrl -Method POST -Headers $headers -Body $bodyString
    
    Write-Host "¡Éxito!" -ForegroundColor Green
    Write-Host "Texto original: $testText" -ForegroundColor Cyan
    Write-Host "Traducción: $($response.translations[0].text)" -ForegroundColor Cyan
}
catch {
    Write-Host "Error detallado:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    if ($_.Exception.Response) {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        $responseBody = $reader.ReadToEnd()
        Write-Host "Respuesta del servidor: $responseBody" -ForegroundColor Red
    }
}