# Script para compilar LaTeX en el directorio actual
Write-Host "Compilando general.tex..." -ForegroundColor Green

# Cambiar al directorio sin_cos (hardcodeado)
Set-Location "D:\resources_psycho\resources_github\repos_publicos\matematicas\sin_cos"

Write-Host "Directorio actual: $(Get-Location)" -ForegroundColor Cyan

# Compilar LaTeX
pdflatex -interaction=nonstopmode -file-line-error general.tex

# Verificar si se creó el PDF
if (Test-Path "general.pdf") {
    Write-Host "Compilación exitosa! PDF creado: general.pdf" -ForegroundColor Green
    # Abrir el PDF automáticamente
    Start-Process "general.pdf"
} else {
    Write-Host "Error en la compilación" -ForegroundColor Red
}

Write-Host "Presiona cualquier tecla para continuar..." -ForegroundColor Yellow
Read-Host
