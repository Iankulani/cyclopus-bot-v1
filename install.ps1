<#
.SYNOPSIS
    🐙 CYCLOPUS-BOT-V1 - PowerShell Installation Script
.DESCRIPTION
    Installs CYCLOPUS-BOT-V1 and all dependencies on Windows
.AUTHOR
    Ian Carter Kulani, MSc
.VERSION
    1.0.0
#>

# =====================
# REQUIREMENTS
# =====================
#Requires -Version 5.0

# =====================
# PARAMETERS
# =====================
param(
    [switch]$SkipPythonInstall,
    [switch]$SkipSystemTools,
    [switch]$SkipOptional,
    [switch]$SkipDocker,
    [switch]$Force,
    [switch]$Verbose
)

# =====================
# CONFIGURATION
# =====================
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$Script:VERSION = "1.0.0"
$Script:APP_NAME = "CYCLOPUS-BOT-V1"
$Script:PYTHON_MIN_VERSION = [Version]"3.7.0"

# =====================
# COLORS
# =====================
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White",
        [switch]$NoNewline
    )
    
    $colors = @{
        "Red" = [ConsoleColor]::Red
        "Green" = [ConsoleColor]::Green
        "Yellow" = [ConsoleColor]::Yellow
        "Cyan" = [ConsoleColor]::Cyan
        "Magenta" = [ConsoleColor]::Magenta
        "White" = [ConsoleColor]::White
        "Blue" = [ConsoleColor]::Blue
    }
    
    $fg = $colors[$Color]
    if ($null -eq $fg) { $fg = [ConsoleColor]::White }
    
    if ($NoNewline) {
        Write-Host $Message -ForegroundColor $fg -NoNewline
    } else {
        Write-Host $Message -ForegroundColor $fg
    }
}

function Write-Banner {
    Write-ColorOutput @"
╔══════════════════════════════════════════════════════════════════════════════╗
║        🐙 CYCLOPUS-BOT-V1 - Ultimate Cybersecurity Platform                ║
║        PowerShell Installation Script v$Script:VERSION                            ║
║        Author: Ian Carter Kulani, MSc                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"@ -Color Cyan
}

# =====================
# ADMIN CHECK
# =====================
function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# =====================
# PYTHON CHECK & INSTALL
# =====================
function Test-Python {
    Write-ColorOutput "`n🔍 Checking Python..." -Color Cyan
    
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "Python (\d+\.\d+\.\d+)") {
            $version = [Version]$matches[1]
            if ($version -ge $Script:PYTHON_MIN_VERSION) {
                Write-ColorOutput "✅ Python $version (3.7+ required)" -Color Green
                return $true
            } else {
                Write-ColorOutput "⚠️  Python $version is too old. 3.7+ required." -Color Yellow
                return $false
            }
        }
    } catch {
        Write-ColorOutput "⚠️  Python not found." -Color Yellow
    }
    return $false
}

function Install-Python {
    if ($SkipPythonInstall) {
        Write-ColorOutput "⚠️  Skipping Python installation (--SkipPythonInstall)" -Color Yellow
        return
    }
    
    Write-ColorOutput "📦 Installing Python..." -Color Cyan
    
    # Try winget
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-ColorOutput "  Using winget..." -Color Cyan
        winget install Python.Python.3.11 --accept-package-agreements --accept-source-agreements
    }
    # Try chocolatey
    elseif (Get-Command choco -ErrorAction SilentlyContinue) {
        Write-ColorOutput "  Using chocolatey..." -Color Cyan
        choco install python -y
    }
    # Try scoop
    elseif (Get-Command scoop -ErrorAction SilentlyContinue) {
        Write-ColorOutput "  Using scoop..." -Color Cyan
        scoop install python
    }
    else {
        Write-ColorOutput "❌ Cannot install Python automatically." -Color Red
        Write-ColorOutput "   Please install Python 3.7+ from https://python.org" -Color Yellow
        exit 1
    }
    
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

# =====================
# PIP CHECK
# =====================
function Test-Pip {
    Write-ColorOutput "`n🔍 Checking pip..." -Color Cyan
    
    try {
        $pipVersion = pip --version 2>&1
        Write-ColorOutput "✅ $pipVersion" -Color Green
        return $true
    } catch {
        Write-ColorOutput "⚠️  pip not found." -Color Yellow
        return $false
    }
}

function Install-Pip {
    Write-ColorOutput "📦 Installing pip..." -Color Cyan
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip setuptools wheel
}

# =====================
# SYSTEM TOOLS
# =====================
function Install-SystemTools {
    if ($SkipSystemTools) {
        Write-ColorOutput "⚠️  Skipping system tools installation (--SkipSystemTools)" -Color Yellow
        return
    }
    
    Write-ColorOutput "`n🔧 Installing system tools..." -Color Cyan
    
    $tools = @(
        @{Name="Nmap"; Winget="Nmap.Nmap"; Choco="nmap"},
        @{Name="curl"; Winget="cURL.cURL"; Choco="curl"},
        @{Name="wget"; Winget="cURL.cURL"; Choco="wget"},
        @{Name="Git"; Winget="Git.Git"; Choco="git"},
        @{Name="OpenSSH"; Winget="OpenSSH.OpenSSH"; Choco="openssh"},
        @{Name="Docker"; Winget="Docker.DockerDesktop"; Choco="docker-desktop"}
    )
    
    foreach ($tool in $tools) {
        Write-ColorOutput "  Installing $($tool.Name)..." -Color Cyan
        
        if (Get-Command winget -ErrorAction SilentlyContinue) {
            try {
                winget install $tool.Winget --accept-package-agreements --accept-source-agreements 2>$null
            } catch {
                Write-ColorOutput "  ⚠️  Failed to install $($tool.Name) via winget" -Color Yellow
            }
        }
        
        if (Get-Command choco -ErrorAction SilentlyContinue) {
            try {
                choco install $tool.Choco -y 2>$null
            } catch {
                Write-ColorOutput "  ⚠️  Failed to install $($tool.Name) via choco" -Color Yellow
            }
        }
    }
    
    Write-ColorOutput "✅ System tools installation attempted" -Color Green
}

# =====================
# PYTHON PACKAGES
# =====================
function Install-PythonPackages {
    Write-ColorOutput "`n📦 Installing Python packages..." -Color Cyan
    
    # Upgrade pip
    python -m pip install --upgrade pip setuptools wheel
    
    # Install from requirements
    if (Test-Path "requirements-full.txt") {
        Write-ColorOutput "  Installing from requirements-full.txt..." -Color Cyan
        python -m pip install -r requirements-full.txt
    }
    elseif (Test-Path "requirements.txt") {
        Write-ColorOutput "  Installing from requirements.txt..." -Color Cyan
        python -m pip install -r requirements.txt
    }
    else {
        Write-ColorOutput "  ⚠️  No requirements file found. Installing essential packages..." -Color Yellow
        $packages = @(
            "requests", "colorama", "psutil", "scapy", "paramiko",
            "dnspython", "flask", "flask-socketio", "flask-cors",
            "discord.py", "telethon", "slack-sdk", "selenium",
            "webdriver-manager", "pynput", "pyautogui", "pyperclip",
            "pillow", "matplotlib", "seaborn", "numpy", "pandas",
            "reportlab", "python-dotenv", "pyyaml", "python-dateutil",
            "python-nmap", "whois", "pyshorteners", "qrcode"
        )
        python -m pip install $packages
    }
    
    Write-ColorOutput "✅ Python packages installed" -Color Green
}

# =====================
# OPTIONAL TOOLS
# =====================
function Install-OptionalTools {
    if ($SkipOptional) {
        Write-ColorOutput "⚠️  Skipping optional tools (--SkipOptional)" -Color Yellow
        return
    }
    
    Write-ColorOutput "`n🔧 Installing optional security tools..." -Color Cyan
    
    if (Get-Command choco -ErrorAction SilentlyContinue) {
        try {
            choco install hashcat -y 2>$null
        } catch {
            Write-ColorOutput "  ⚠️  Failed to install hashcat" -Color Yellow
        }
    }
    
    Write-ColorOutput "✅ Optional tools installation attempted" -Color Green
}

# =====================
# DOCKER
# =====================
function Install-Docker {
    if ($SkipDocker) {
        Write-ColorOutput "⚠️  Skipping Docker installation (--SkipDocker)" -Color Yellow
        return
    }
    
    Write-ColorOutput "`n🐳 Checking Docker..." -Color Cyan
    
    if (Get-Command docker -ErrorAction SilentlyContinue) {
        Write-ColorOutput "✅ Docker already installed" -Color Green
        return
    }
    
    Write-ColorOutput "📦 Installing Docker..." -Color Cyan
    
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install Docker.DockerDesktop --accept-package-agreements --accept-source-agreements
    }
    elseif (Get-Command choco -ErrorAction SilentlyContinue) {
        choco install docker-desktop -y
    }
    
    Write-ColorOutput "✅ Docker installation attempted" -Color Green
}

# =====================
# DIRECTORIES
# =====================
function New-Directories {
    Write-ColorOutput "`n📁 Creating directories..." -Color Cyan
    
    $directories = @(
        ".cyclopus_bot_v1",
        ".cyclopus_bot_v1\payloads",
        ".cyclopus_bot_v1\workspaces",
        ".cyclopus_bot_v1\scans",
        ".cyclopus_bot_v1\phishing_pages",
        ".cyclopus_bot_v1\phishing_templates",
        ".cyclopus_bot_v1\captured_credentials",
        ".cyclopus_bot_v1\ssh_keys",
        ".cyclopus_bot_v1\traffic_logs",
        ".cyclopus_bot_v1\nikto_results",
        "cyclopus_reports",
        "cyclopus_reports\graphics",
        "cyclopus_reports\pdf_reports",
        "temp",
        ".cyclopus_bot_v1\web_templates",
        ".cyclopus_bot_v1\sessions",
        ".cyclopus_bot_v1\spear_phishing",
        ".cyclopus_bot_v1\email_templates",
        ".cyclopus_bot_v1\dos_logs",
        ".cyclopus_bot_v1\agents",
        ".cyclopus_bot_v1\c2_logs",
        ".cyclopus_bot_v1\modules",
        ".cyclopus_bot_v1\network_monitor",
        ".cyclopus_bot_v1\keylog_exfil",
        ".cyclopus_bot_v1\deployments",
        ".cyclopus_bot_v1\domain_hosting",
        ".cyclopus_bot_v1\cracking",
        ".cyclopus_bot_v1\arp_logs",
        ".cyclopus_bot_v1\mac_logs",
        ".cyclopus_bot_v1\nat_logs",
        ".cyclopus_bot_v1\animation_cache",
        ".cyclopus_bot_v1\platform_logs",
        ".cyclopus_bot_v1\docker_scans",
        ".cyclopus_bot_v1\email_composer",
        ".cyclopus_bot_v1\templates",
        ".cyclopus_bot_v1\custom_templates"
    )
    
    foreach ($dir in $directories) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }
    
    Write-ColorOutput "✅ Directories created" -Color Green
}

# =====================
# VERIFY
# =====================
function Test-Installation {
    Write-ColorOutput "`n🔍 Verifying installation..." -Color Cyan
    
    if (Test-Path "requirements-check.py") {
        python requirements-check.py
    } else {
        Write-ColorOutput "⚠️  requirements-check.py not found" -Color Yellow
    }
}

# =====================
# MAIN
# =====================
function Main {
    Write-Banner
    
    Write-ColorOutput "This script will install $Script:APP_NAME and all dependencies." -Color Magenta
    Write-ColorOutput "Some operations may require Administrator privileges.`n" -Color Magenta
    
    if (-not $Force) {
        $confirm = Read-Host "Continue with installation? (y/n)"
        if ($confirm -notmatch "^[Yy]$") {
            Write-ColorOutput "Installation cancelled." -Color Yellow
            return
        }
    }
    
    # Check admin
    if (-not (Test-Administrator)) {
        Write-ColorOutput "⚠️  Not running as Administrator. Some features may not work." -Color Yellow
        Write-ColorOutput "   Run PowerShell as Administrator for full functionality.`n" -Color Yellow
    }
    
    # Python
    if (-not (Test-Python)) {
        Install-Python
    }
    
    # Pip
    if (-not (Test-Pip)) {
        Install-Pip
    }
    
    # System tools
    Install-SystemTools
    
    # Python packages
    Install-PythonPackages
    
    # Optional tools
    Install-OptionalTools
    
    # Docker
    Install-Docker
    
    # Directories
    New-Directories
    
    # Verify
    Test-Installation
    
    # Complete
    Write-ColorOutput "`n" -Color Green
    Write-ColorOutput "╔══════════════════════════════════════════════════════════════╗" -Color Green
    Write-ColorOutput "║        ✅ CYCLOPUS-BOT-V1 Installation Complete!            ║" -Color Green
    Write-ColorOutput "╚══════════════════════════════════════════════════════════════╝" -Color Green
    
    Write-ColorOutput "`nTo start CYCLOPUS-BOT-V1:" -Color Cyan
    Write-ColorOutput "  python cyclopus_bot_v1.py" -Color Magenta
    Write-ColorOutput "`nTo run tests:" -Color Cyan
    Write-ColorOutput "  python test-commands.py" -Color Magenta
    Write-ColorOutput "`nTo check dependencies:" -Color Cyan
    Write-ColorOutput "  python requirements-check.py" -Color Magenta
    Write-ColorOutput "`n⚠️  For full functionality, run as Administrator.`n" -Color Yellow
}

# Run main
Main
