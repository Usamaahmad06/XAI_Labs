# Run XAI assignments using the causalai conda env (not base).
#
# Usage:
#   .\assignments\run.ps1 1
#   .\assignments\run.ps1 4

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [int]$Number
)

$python = "C:\Users\Usama\miniconda3\envs\causalai\python.exe"
if (-not (Test-Path $python)) {
    Write-Error "causalai env not found at $python. Run: conda create -n causalai python=3.10"
    exit 1
}

Write-Host "Using: $python" -ForegroundColor Cyan
& $python "$PSScriptRoot\run_assignment.py" $Number
exit $LASTEXITCODE
