@echo off
setlocal
cd /d "%~dp0"
set FOXYIZ_ROOT=%~dp0FoXYiZ
echo FoXYiZ_User 1.0.1
echo FOXYIZ_ROOT=%FOXYIZ_ROOT%
echo.
if "%~1"=="" (
  "FoXYiZ\f\FoXYiZ.exe" --config FoXYiZ\f\fStart\default.json
) else (
  "FoXYiZ\f\FoXYiZ.exe" %*
)
endlocal
