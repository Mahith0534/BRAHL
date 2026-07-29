@echo off
setlocal
cd /d "%~dp0"
set FOXYIZ_ROOT=%~dp0FoXYiZ
set BRAHL_LOCAL=1
set QOA_DESKTOP=1
echo Starting BRAHL - engine at FoXYiZ\f\FoXYiZ.exe
echo FOXYIZ_ROOT=%FOXYIZ_ROOT%
python BRAHL\run_local.py
endlocal
