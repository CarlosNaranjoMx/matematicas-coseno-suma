# Script para compilación completa con múltiples pasadas
Write-Host "Compilación completa de LaTeX (múltiples pasadas)..." -ForegroundColor Green

# Cambiar al directorio sin_cos (hardcodeado)
Set-Location "D:\resources_psycho\resources_github\repos_publicos\matematicas\sin_cos"

Write-Host "Directorio actual: $(Get-Location)" -ForegroundColor Cyan

# Primera pasada
Write-Host "Primera pasada..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode general.tex

# Segunda pasada (para referencias cruzadas)
Write-Host "Segunda pasada..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode general.tex

# Tercera pasada (para asegurar todas las referencias)
Write-Host "Tercera pasada..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode general.tex

# Verificar si se creó el PDF
if (Test-Path "general.pdf") {
    Write-Host "Compilación completa exitosa! PDF creado: general.pdf" -ForegroundColor Green
    # Abrir el PDF automáticamente
    Start-Process "general.pdf"
} else {
    Write-Host "Error en la compilación" -ForegroundColor Red
}

Write-Host "Presiona cualquier tecla para continuar..." -ForegroundColor Yellow
Read-Host
