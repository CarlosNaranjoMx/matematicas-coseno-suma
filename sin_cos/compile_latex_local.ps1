# Script para compilar LaTeX en el directorio actual
Write-Host "Compilando general.tex..." -ForegroundColor Green

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
