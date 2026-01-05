@echo off
setlocal

REM One-click reproduction package generation for Windows (CMD).

set "SCRIPT=%~dp0reproduce_case1.py"

where py >nul 2>&1
if %errorlevel%==0 (
  py -3 "%SCRIPT%"
  exit /b %errorlevel%
)

where python >nul 2>&1
if %errorlevel%==0 (
  python "%SCRIPT%"
  exit /b %errorlevel%
)

where python3 >nul 2>&1
if %errorlevel%==0 (
  python3 "%SCRIPT%"
  exit /b %errorlevel%
)

echo Python 3 not found. Install Python 3 and re-run.
echo - Windows: https://www.python.org/downloads/
exit /b 1

