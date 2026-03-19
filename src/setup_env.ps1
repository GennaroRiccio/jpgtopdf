$venvDir = ".venv"

if (-not (Test-Path $venvDir)) {
    Write-Host "Creazione virtual environment '$venvDir'..."
    python -m venv $venvDir
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Errore durante la creazione del virtual environment."
        exit 1
    }
}

Write-Host "Attivazione virtual environment..."
& "$venvDir\Scripts\Activate.ps1"

Write-Host "Installazione dipendenze da requirements.txt..."
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
