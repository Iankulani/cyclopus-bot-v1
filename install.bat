@echo off
REM ============================================================
REM 🐙 CYCLOPUS-BOT-V1 - Batch Installation Script (Windows)
REM Author: Ian Carter Kulani, MSc
REM Version: 1.0.0
REM ============================================================

setlocal enabledelayedexpansion

REM Colors (Windows 10+)
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "CYAN=[96m"
set "PURPLE=[95m"
set "RESET=[0m"
set "BOLD=[1m"

REM =====================
REM BANNER
REM =====================
echo %CYAN%
echo ================================================================================
echo        🐙 CYCLOPUS-BOT-V1 - Ultimate Cybersecurity Platform
echo        Batch Installation Script v1.0.0
echo        Author: Ian Carter Kulani, MSc
echo ================================================================================
echo %RESET%

REM =====================
REM CHECK ADMIN
REM =====================
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%⚠️  Not running as administrator. Some features may not work.%RESET%
    echo %YELLOW%   Right-click and select "Run as Administrator" for full functionality.%RESET%
    echo.
)

REM =====================
REM CHECK PYTHON
REM =====================
echo %CYAN%🔍 Checking Python...%RESET%

python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%⚠️  Python not found. Attempting to install...%RESET%
    
    REM Try winget first
    winget install Python.Python.3.11 --accept-package-agreements --accept-source-agreements >nul 2>&1
    if %errorLevel% neq 0 (
        REM Try chocolatey
        choco install python -y >nul 2>&1
    )
    
    if %errorLevel% neq 0 (
        echo %RED%❌ Failed to install Python automatically.%RESET%
        echo %YELLOW%   Please install Python 3.7+ manually from https://python.org%RESET%
        pause
        exit /b 1
    )
)

python --version
echo %GREEN%✅ Python found%RESET%

REM =====================
REM CHECK PIP
REM =====================
echo.
echo %CYAN%🔍 Checking pip...%RESET%

pip --version >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%⚠️  pip not found. Installing...%RESET%
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip
)

pip --version
echo %GREEN%✅ pip found%RESET%

REM =====================
REM INSTALL SYSTEM TOOLS
REM =====================
echo.
echo %CYAN%🔧 Installing system tools...%RESET%

REM Check for winget
where winget >nul 2>&1
if %errorLevel% equ 0 (
    echo Installing tools via winget...
    winget install Nmap.Nmap --accept-package-agreements --accept-source-agreements >nul 2>&1
    winget install cURL.cURL --accept-package-agreements --accept-source-agreements >nul 2>&1
    winget install Git.Git --accept-package-agreements --accept-source-agreements >nul 2>&1
    winget install OpenSSH.OpenSSH --accept-package-agreements --accept-source-agreements >nul 2>&1
    winget install Docker.DockerDesktop --accept-package-agreements --accept-source-agreements >nul 2>&1
)

REM Check for chocolatey
where choco >nul 2>&1
if %errorLevel% equ 0 (
    echo Installing tools via chocolatey...
    choco install nmap -y >nul 2>&1
    choco install curl -y >nul 2>&1
    choco install wget -y >nul 2>&1
    choco install git -y >nul 2>&1
    choco install docker-desktop -y >nul 2>&1
    choco install hashcat -y >nul 2>&1
)

echo %GREEN%✅ System tools installation attempted%RESET%

REM =====================
REM INSTALL PYTHON PACKAGES
REM =====================
echo.
echo %CYAN%📦 Installing Python packages...%RESET%

REM Upgrade pip
python -m pip install --upgrade pip setuptools wheel

REM Install from requirements
if exist "requirements-full.txt" (
    echo Installing from requirements-full.txt...
    python -m pip install -r requirements-full.txt
) else if exist "requirements.txt" (
    echo Installing from requirements.txt...
    python -m pip install -r requirements.txt
) else (
    echo %YELLOW%⚠️  No requirements file found. Installing essential packages...%RESET%
    python -m pip install requests colorama psutil scapy paramiko dnspython flask flask-socketio flask-cors discord.py telethon slack-sdk selenium webdriver-manager pynput pyautogui pyperclip pillow matplotlib seaborn numpy pandas reportlab python-dotenv pyyaml python-dateutil python-nmap whois pyshorteners qrcode
)

echo %GREEN%✅ Python packages installed%RESET%

REM =====================
REM CREATE DIRECTORIES
REM =====================
echo.
echo %CYAN%📁 Creating directories...%RESET%

mkdir .cyclopus_bot_v1 2>nul
mkdir .cyclopus_bot_v1\payloads 2>nul
mkdir .cyclopus_bot_v1\workspaces 2>nul
mkdir .cyclopus_bot_v1\scans 2>nul
mkdir .cyclopus_bot_v1\phishing_pages 2>nul
mkdir .cyclopus_bot_v1\phishing_templates 2>nul
mkdir .cyclopus_bot_v1\captured_credentials 2>nul
mkdir .cyclopus_bot_v1\ssh_keys 2>nul
mkdir .cyclopus_bot_v1\traffic_logs 2>nul
mkdir .cyclopus_bot_v1\nikto_results 2>nul
mkdir cyclopus_reports 2>nul
mkdir cyclopus_reports\graphics 2>nul
mkdir cyclopus_reports\pdf_reports 2>nul
mkdir temp 2>nul
mkdir .cyclopus_bot_v1\web_templates 2>nul
mkdir .cyclopus_bot_v1\sessions 2>nul
mkdir .cyclopus_bot_v1\spear_phishing 2>nul
mkdir .cyclopus_bot_v1\email_templates 2>nul
mkdir .cyclopus_bot_v1\dos_logs 2>nul
mkdir .cyclopus_bot_v1\agents 2>nul
mkdir .cyclopus_bot_v1\c2_logs 2>nul
mkdir .cyclopus_bot_v1\modules 2>nul
mkdir .cyclopus_bot_v1\network_monitor 2>nul
mkdir .cyclopus_bot_v1\keylog_exfil 2>nul
mkdir .cyclopus_bot_v1\deployments 2>nul
mkdir .cyclopus_bot_v1\domain_hosting 2>nul
mkdir .cyclopus_bot_v1\cracking 2>nul
mkdir .cyclopus_bot_v1\arp_logs 2>nul
mkdir .cyclopus_bot_v1\mac_logs 2>nul
mkdir .cyclopus_bot_v1\nat_logs 2>nul
mkdir .cyclopus_bot_v1\animation_cache 2>nul
mkdir .cyclopus_bot_v1\platform_logs 2>nul
mkdir .cyclopus_bot_v1\docker_scans 2>nul
mkdir .cyclopus_bot_v1\email_composer 2>nul
mkdir .cyclopus_bot_v1\templates 2>nul
mkdir .cyclopus_bot_v1\custom_templates 2>nul

echo %GREEN%✅ Directories created%RESET%

REM =====================
REM VERIFY INSTALLATION
REM =====================
echo.
echo %CYAN%🔍 Verifying installation...%RESET%

if exist "requirements-check.py" (
    python requirements-check.py
) else (
    echo %YELLOW%⚠️  requirements-check.py not found%RESET%
)

REM =====================
REM COMPLETE
REM =====================
echo.
echo %GREEN%╔══════════════════════════════════════════════════════════════╗%RESET%
echo %GREEN%║        ✅ CYCLOPUS-BOT-V1 Installation Complete!            ║%RESET%
echo %GREEN%╚══════════════════════════════════════════════════════════════╝%RESET%

echo.
echo %CYAN%To start CYCLOPUS-BOT-V1:%RESET%
echo %PURPLE%  python cyclopus_bot_v1.py%RESET%
echo.
echo %CYAN%To run tests:%RESET%
echo %PURPLE%  python test-commands.py%RESET%
echo.
echo %CYAN%To check dependencies:%RESET%
echo %PURPLE%  python requirements-check.py%RESET%
echo.
echo %YELLOW%⚠️  For full functionality, run as Administrator.%RESET%
echo.

pause
endlocal
