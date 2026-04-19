$pythonPath = Get-Command python -ErrorAction SilentlyContinue
if ($pythonPath -eq $null) {
    $pythonPath = Get-Command py -ErrorAction SilentlyContinue
}

if ($pythonPath -eq $null) {
    Write-Host "Python não encontrado no sistema. Por favor, instale o Python primeiro."
    exit 1
}

$pythonPath.Path
& $pythonPath.Path app.py
