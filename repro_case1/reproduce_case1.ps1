param()

$ErrorActionPreference = "Stop"

$scriptPath = Join-Path $PSScriptRoot "reproduce_case1.py"

function Get-Python {
  if (Get-Command py -ErrorAction SilentlyContinue) {
    try {
      & py -3 -c "import sys; print(sys.version)" *> $null
      return @("py", "-3")
    } catch {}
  }
  foreach ($cmd in @("python", "python3")) {
    if (Get-Command $cmd -ErrorAction SilentlyContinue) {
      return @($cmd)
    }
  }
  throw "Python 3 not found. Install Python 3 and re-run. (https://www.python.org/downloads/)"
}

$py = Get-Python
$pythonExe = $py[0]
$pythonArgs = @()
if ($py.Length -gt 1) { $pythonArgs += $py[1..($py.Length - 1)] }
$pythonArgs += $scriptPath

& $pythonExe @pythonArgs

