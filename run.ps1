# run.ps1
# attiva il virtualenv
. .\venv\Scripts\Activate.ps1

# avvia il tuo CLI
python .\cli.py

# rimani nella console fino a un tasto
Write-Host "`nPremi un tasto per chiudere..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
