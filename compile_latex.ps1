# Script para compilar LaTeX
Write-Host "Compilando general.tex..." -ForegroundColor Green

# Navegar al subdirectorio sin_cos
Set-Location "sin_cos"

# Compilar LaTeX
pdflatex general.tex

# Verificar si se creó el PDF
if (Test-Path "general.pdf") {
    Write-Host "Compilación exitosa! PDF creado: general.pdf" -ForegroundColor Green
    # Abrir el PDF automáticamente
    Start-Process "general.pdf"
} else {
    Write-Host "Error en la compilación" -ForegroundColor Red
}

# Regresar al directorio original
Set-Location ".."
