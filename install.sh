#!/bin/bash
#
# 🐙 CYCLOPUS-BOT-V1 - Bash Installation Script
# Author: Ian Carter Kulani, MSc
# Version: 1.0.0
#
# Supports: Ubuntu, Debian, CentOS, RHEL, Fedora, Arch, macOS
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'
BOLD='\033[1m'

# =====================
# BANNER
# =====================
print_banner() {
    echo -e "${CYAN}"
    cat << "EOF"
╔══════════════════════════════════════════════════════════════════════════════╗
║        🐙 CYCLOPUS-BOT-V1 - Ultimate Cybersecurity Platform                ║
║        Installation Script v1.0.0                                          ║
║        Author: Ian Carter Kulani, MSc                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# =====================
# DETECT OS
# =====================
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            OS="debian"
            PKG_MANAGER="apt-get"
            PKG_INSTALL="sudo apt-get install -y"
            PKG_UPDATE="sudo apt-get update"
        elif [ -f /etc/redhat-release ]; then
            OS="redhat"
            PKG_MANAGER="yum"
            PKG_INSTALL="sudo yum install -y"
            PKG_UPDATE="sudo yum update -y"
        elif [ -f /etc/arch-release ]; then
            OS="arch"
            PKG_MANAGER="pacman"
            PKG_INSTALL="sudo pacman -S --noconfirm"
            PKG_UPDATE="sudo pacman -Sy"
        elif [ -f /etc/alpine-release ]; then
            OS="alpine"
            PKG_MANAGER="apk"
            PKG_INSTALL="sudo apk add"
            PKG_UPDATE="sudo apk update"
        else
            OS="linux"
            PKG_MANAGER="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        PKG_MANAGER="brew"
        PKG_INSTALL="brew install"
        PKG_UPDATE="brew update"
    else
        OS="unknown"
    fi
    
    echo -e "${GREEN}✅ Detected OS: $OS${NC}"
}

# =====================
# CHECK PYTHON
# =====================
check_python() {
    echo -e "\n${CYAN}🔍 Checking Python...${NC}"
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
        
        if [ "$PYTHON_MAJOR" -ge 3 ] && [ "$PYTHON_MINOR" -ge 7 ]; then
            echo -e "${GREEN}✅ Python $PYTHON_VERSION (3.7+ required)${NC}"
            PYTHON_CMD="python3"
            PIP_CMD="pip3"
        else
            echo -e "${RED}❌ Python $PYTHON_VERSION is too old. 3.7+ required.${NC}"
            install_python
        fi
    else
        echo -e "${YELLOW}⚠️  Python3 not found. Installing...${NC}"
        install_python
    fi
    
    # Check pip
    if ! command -v $PIP_CMD &> /dev/null; then
        echo -e "${YELLOW}⚠️  pip not found. Installing...${NC}"
        install_pip
    fi
    
    echo -e "${GREEN}✅ pip: $($PIP_CMD --version 2>&1 | head -1)${NC}"
}

# =====================
# INSTALL PYTHON
# =====================
install_python() {
    case $OS in
        debian)
            $PKG_UPDATE
            $PKG_INSTALL python3 python3-pip python3-venv python3-dev
            ;;
        redhat)
            $PKG_INSTALL python3 python3-pip python3-devel
            ;;
        arch)
            $PKG_INSTALL python python-pip
            ;;
        alpine)
            $PKG_UPDATE
            $PKG_INSTALL python3 py3-pip python3-dev
            ;;
        macos)
            $PKG_INSTALL python3
            ;;
        *)
            echo -e "${RED}❌ Cannot install Python automatically. Please install Python 3.7+ manually.${NC}"
            exit 1
            ;;
    esac
    
    PYTHON_CMD="python3"
    PIP_CMD="pip3"
}

# =====================
# INSTALL PIP
# =====================
install_pip() {
    case $OS in
        debian)
            $PKG_INSTALL python3-pip
            ;;
        redhat)
            $PKG_INSTALL python3-pip
            ;;
        arch)
            $PKG_INSTALL python-pip
            ;;
        alpine)
            $PKG_INSTALL py3-pip
            ;;
        macos)
            $PYTHON_CMD -m ensurepip
            ;;
    esac
    PIP_CMD="pip3"
}

# =====================
# INSTALL SYSTEM TOOLS
# =====================
install_system_tools() {
    echo -e "\n${CYAN}🔧 Installing system tools...${NC}"
    
    case $OS in
        debian)
            $PKG_UPDATE
            $PKG_INSTALL nmap curl wget netcat-openbsd dnsutils traceroute openssh-client git python3-pip python3-dev build-essential libssl-dev libffi-dev
            ;;
        redhat)
            $PKG_INSTALL nmap curl wget nc bind-utils traceroute openssh-clients git python3-pip python3-devel gcc openssl-devel libffi-devel
            ;;
        arch)
            $PKG_INSTALL nmap curl wget openbsd-netcat bind traceroute openssh git python-pip base-devel
            ;;
        alpine)
            $PKG_UPDATE
            $PKG_INSTALL nmap curl wget netcat-openbsd bind-tools traceroute openssh-client git py3-pip python3-dev build-base openssl-dev libffi-dev
            ;;
        macos)
            # Install Homebrew if not present
            if ! command -v brew &> /dev/null; then
                echo -e "${YELLOW}⚠️  Homebrew not found. Installing...${NC}"
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            $PKG_UPDATE
            $PKG_INSTALL nmap curl wget netcat bind traceroute openssh git python3
            ;;
        *)
            echo -e "${YELLOW}⚠️  Please install system tools manually: nmap, curl, wget, netcat, dig, traceroute, ssh, git${NC}"
            ;;
    esac
    
    echo -e "${GREEN}✅ System tools installed${NC}"
}

# =====================
# INSTALL PYTHON PACKAGES
# =====================
install_python_packages() {
    echo -e "\n${CYAN}📦 Installing Python packages...${NC}"
    
    # Upgrade pip
    $PIP_CMD install --upgrade pip setuptools wheel
    
    # Install core requirements
    if [ -f "requirements-full.txt" ]; then
        echo -e "${CYAN}Installing from requirements-full.txt...${NC}"
        $PIP_CMD install -r requirements-full.txt
    elif [ -f "requirements.txt" ]; then
        echo -e "${CYAN}Installing from requirements.txt...${NC}"
        $PIP_CMD install -r requirements.txt
    else
        # Install manually if no requirements file
        echo -e "${YELLOW}⚠️  No requirements file found. Installing essential packages...${NC}"
        $PIP_CMD install requests colorama psutil scapy paramiko dnspython flask flask-socketio flask-cors discord.py telethon slack-sdk selenium webdriver-manager pynput pyautogui pyperclip pillow matplotlib seaborn numpy pandas reportlab python-dotenv pyyaml python-dateutil python-nmap whois pyshorteners qrcode
    fi
    
    echo -e "${GREEN}✅ Python packages installed${NC}"
}

# =====================
# INSTALL DOCKER (OPTIONAL)
# =====================
install_docker() {
    echo -e "\n${CYAN}🐳 Installing Docker...${NC}"
    
    read -p "Install Docker? (y/n): " install_docker_choice
    if [[ "$install_docker_choice" =~ ^[Yy]$ ]]; then
        case $OS in
            debian)
                $PKG_UPDATE
                $PKG_INSTALL docker.io docker-compose
                sudo systemctl enable docker
                sudo systemctl start docker
                sudo usermod -aG docker $USER
                ;;
            redhat)
                $PKG_INSTALL docker docker-compose
                sudo systemctl enable docker
                sudo systemctl start docker
                sudo usermod -aG docker $USER
                ;;
            arch)
                $PKG_INSTALL docker docker-compose
                sudo systemctl enable docker
                sudo systemctl start docker
                sudo usermod -aG docker $USER
                ;;
            alpine)
                $PKG_INSTALL docker docker-compose
                sudo rc-update add docker default
                sudo service docker start
                sudo addgroup $USER docker
                ;;
            macos)
                $PKG_INSTALL docker docker-compose
                ;;
        esac
        echo -e "${GREEN}✅ Docker installed${NC}"
    else
        echo -e "${YELLOW}⚠️  Docker installation skipped${NC}"
    fi
}

# =====================
# INSTALL OPTIONAL TOOLS
# =====================
install_optional_tools() {
    echo -e "\n${CYAN}🔧 Installing optional security tools...${NC}"
    
    read -p "Install optional security tools (hashcat, nikto)? (y/n): " install_optional
    if [[ "$install_optional" =~ ^[Yy]$ ]]; then
        case $OS in
            debian)
                $PKG_INSTALL hashcat nikto
                ;;
            redhat)
                $PKG_INSTALL hashcat nikto
                ;;
            arch)
                $PKG_INSTALL hashcat nikto
                ;;
            alpine)
                $PKG_INSTALL hashcat
                ;;
            macos)
                $PKG_INSTALL hashcat nikto
                ;;
        esac
        echo -e "${GREEN}✅ Optional tools installed${NC}"
    else
        echo -e "${YELLOW}⚠️  Optional tools installation skipped${NC}"
    fi
}

# =====================
# CREATE DIRECTORIES
# =====================
create_directories() {
    echo -e "\n${CYAN}📁 Creating directories...${NC}"
    
    mkdir -p .cyclopus_bot_v1
    mkdir -p .cyclopus_bot_v1/payloads
    mkdir -p .cyclopus_bot_v1/workspaces
    mkdir -p .cyclopus_bot_v1/scans
    mkdir -p .cyclopus_bot_v1/phishing_pages
    mkdir -p .cyclopus_bot_v1/phishing_templates
    mkdir -p .cyclopus_bot_v1/captured_credentials
    mkdir -p .cyclopus_bot_v1/ssh_keys
    mkdir -p .cyclopus_bot_v1/traffic_logs
    mkdir -p .cyclopus_bot_v1/nikto_results
    mkdir -p cyclopus_reports
    mkdir -p cyclopus_reports/graphics
    mkdir -p cyclopus_reports/pdf_reports
    mkdir -p temp
    mkdir -p .cyclopus_bot_v1/web_templates
    mkdir -p .cyclopus_bot_v1/sessions
    mkdir -p .cyclopus_bot_v1/spear_phishing
    mkdir -p .cyclopus_bot_v1/email_templates
    mkdir -p .cyclopus_bot_v1/dos_logs
    mkdir -p .cyclopus_bot_v1/agents
    mkdir -p .cyclopus_bot_v1/c2_logs
    mkdir -p .cyclopus_bot_v1/modules
    mkdir -p .cyclopus_bot_v1/network_monitor
    mkdir -p .cyclopus_bot_v1/keylog_exfil
    mkdir -p .cyclopus_bot_v1/deployments
    mkdir -p .cyclopus_bot_v1/domain_hosting
    mkdir -p .cyclopus_bot_v1/cracking
    mkdir -p .cyclopus_bot_v1/arp_logs
    mkdir -p .cyclopus_bot_v1/mac_logs
    mkdir -p .cyclopus_bot_v1/nat_logs
    mkdir -p .cyclopus_bot_v1/animation_cache
    mkdir -p .cyclopus_bot_v1/platform_logs
    mkdir -p .cyclopus_bot_v1/docker_scans
    mkdir -p .cyclopus_bot_v1/email_composer
    mkdir -p .cyclopus_bot_v1/templates
    mkdir -p .cyclopus_bot_v1/custom_templates
    
    echo -e "${GREEN}✅ Directories created${NC}"
}

# =====================
# VERIFY INSTALLATION
# =====================
verify_installation() {
    echo -e "\n${CYAN}🔍 Verifying installation...${NC}"
    
    $PYTHON_CMD requirements-check.py
    
    echo -e "\n${GREEN}✅ Installation verification complete${NC}"
}

# =====================
# MAIN
# =====================
main() {
    print_banner
    
    echo -e "${PURPLE}This script will install CYCLOPUS-BOT-V1 and all dependencies.${NC}"
    echo -e "${PURPLE}Some operations may require sudo/admin privileges.${NC}\n"
    
    read -p "Continue with installation? (y/n): " confirm
    if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Installation cancelled.${NC}"
        exit 0
    fi
    
    detect_os
    check_python
    install_system_tools
    install_python_packages
    install_optional_tools
    install_docker
    create_directories
    
    # Copy main script if not present
    if [ ! -f "cyclopus_bot_v1.py" ]; then
        echo -e "${YELLOW}⚠️  cyclopus_bot_v1.py not found in current directory${NC}"
        echo -e "${YELLOW}   Please ensure the main script is in the current directory.${NC}"
    fi
    
    verify_installation
    
    echo -e "\n${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║        ✅ CYCLOPUS-BOT-V1 Installation Complete!            ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
    
    echo -e "\n${CYAN}To start CYCLOPUS-BOT-V1:${NC}"
    echo -e "${PURPLE}  python3 cyclopus_bot_v1.py${NC}"
    echo -e "\n${CYAN}To run tests:${NC}"
    echo -e "${PURPLE}  python3 test-commands.py${NC}"
    echo -e "\n${CYAN}To check dependencies:${NC}"
    echo -e "${PURPLE}  python3 requirements-check.py${NC}"
    
    echo -e "\n${YELLOW}⚠️  For full functionality, run with sudo/admin privileges.${NC}\n"
}

# Run main
main "$@"
