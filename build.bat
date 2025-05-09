@echo off
REM Build and move frontend into static folder for FastAPI

cd /d %~dp0frontend

echo Removing old static build...
rmdir /s /q ..\static 2>nul

echo Building frontend...
call npm run build

echo Moving build output to /static...
move /Y dist ..\static

cd ..
echo Frontend build complete.

