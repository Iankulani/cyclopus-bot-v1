#!/usr/bin/env python3
"""
🐙 CYCLOPUS-BOT-V1 - Dependency Checker & Installer
Author: Ian Carter Kulani, MSc
Version: 1.0.0

This script checks all dependencies and provides installation instructions.
"""

import os
import sys
import subprocess
import importlib
import platform
import shutil
from pathlib import Path

# =====================
# COLORS
# =====================
class Colors:
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# =====================
# DEPENDENCY DEFINITIONS
# =====================
PYTHON_PACKAGES = {
    # Core
    'requests': {'version': '2.28.0', 'required': True, 'description': 'HTTP library for Python'},
    'urllib3': {'version': '1.26.0', 'required': True, 'description': 'HTTP client for Python'},
    
    # Terminal & UI
    'colorama': {'version': '0.4.6', 'required': False, 'description': 'Cross-platform colored terminal text'},
    'tabulate': {'version': '0.9.0', 'required': False, 'description': 'Pretty-print tabular data'},
    'tqdm': {'version': '4.65.0', 'required': False, 'description': 'Progress bar library'},
    'rich': {'version': '13.0.0', 'required': False, 'description': 'Rich text and beautiful formatting'},
    'questionary': {'version': '2.0.0', 'required': False, 'description': 'Interactive command-line prompts'},
    'pyfiglet': {'version': '0.8.0', 'required': False, 'description': 'ASCII art text generator'},
    
    # Cryptography
    'cryptography': {'version': '41.0.0', 'required': False, 'description': 'Cryptographic recipes and primitives'},
    'passlib': {'version': '1.7.4', 'required': False, 'description': 'Password hashing library'},
    'bcrypt': {'version': '4.0.0', 'required': False, 'description': 'Password hashing'},
    
    # Networking
    'scapy': {'version': '2.5.0', 'required': False, 'description': 'Packet manipulation library'},
    'paramiko': {'version': '3.3.0', 'required': False, 'description': 'SSH2 protocol library'},
    'dnspython': {'version': '2.4.0', 'required': False, 'description': 'DNS toolkit for Python'},
    'netifaces': {'version': '0.11.0', 'required': False, 'description': 'Portable network interface information'},
    'netaddr': {'version': '0.9.0', 'required': False, 'description': 'Network address manipulation'},
    'macaddress': {'version': '2.0.0', 'required': False, 'description': 'MAC address handling'},
    'aiohttp': {'version': '3.8.0', 'required': False, 'description': 'Async HTTP client/server'},
    'httpx': {'version': '0.24.0', 'required': False, 'description': 'Next generation HTTP client'},
    
    # Web Framework
    'flask': {'version': '2.3.0', 'required': False, 'description': 'Micro web framework'},
    'flask_socketio': {'version': '5.3.0', 'required': False, 'description': 'Socket.IO integration for Flask'},
    'flask_cors': {'version': '4.0.0', 'required': False, 'description': 'CORS support for Flask'},
    'gunicorn': {'version': '21.0.0', 'required': False, 'description': 'WSGI HTTP Server'},
    'eventlet': {'version': '0.33.0', 'required': False, 'description': 'Concurrent networking library'},
    
    # Bot Integrations
    'discord': {'version': '2.3.0', 'required': False, 'description': 'Discord API wrapper'},
    'telethon': {'version': '1.31.0', 'required': False, 'description': 'Telegram client library'},
    'slack_sdk': {'version': '3.23.0', 'required': False, 'description': 'Slack SDK for Python'},
    'selenium': {'version': '4.14.0', 'required': False, 'description': 'Browser automation'},
    'webdriver_manager': {'version': '4.0.0', 'required': False, 'description': 'WebDriver manager'},
    
    # Keylogger & Monitoring
    'pynput': {'version': '1.7.6', 'required': False, 'description': 'Keyboard and mouse control'},
    'pyautogui': {'version': '0.9.54', 'required': False, 'description': 'GUI automation'},
    'pyperclip': {'version': '1.8.2', 'required': False, 'description': 'Clipboard access'},
    'psutil': {'version': '5.9.0', 'required': False, 'description': 'System monitoring'},
    'PIL': {'version': '10.0.0', 'required': False, 'description': 'Python Imaging Library', 'package': 'pillow'},
    
    # Data & Visualization
    'matplotlib': {'version': '3.7.0', 'required': False, 'description': 'Plotting library'},
    'seaborn': {'version': '0.12.0', 'required': False, 'description': 'Statistical data visualization'},
    'numpy': {'version': '1.24.0', 'required': False, 'description': 'Numerical computing'},
    'pandas': {'version': '2.0.0', 'required': False, 'description': 'Data analysis library'},
    
    # PDF & Reports
    'reportlab': {'version': '4.0.0', 'required': False, 'description': 'PDF generation'},
    'fpdf2': {'version': '2.7.0', 'required': False, 'description': 'PDF generation library'},
    
    # Email
    'email_validator': {'version': '2.1.0', 'required': False, 'description': 'Email validation'},
    
    # Database
    'sqlalchemy': {'version': '2.0.0', 'required': False, 'description': 'SQL toolkit and ORM'},
    'redis': {'version': '5.0.0', 'required': False, 'description': 'Redis client'},
    'pymongo': {'version': '4.5.0', 'required': False, 'description': 'MongoDB driver'},
    
    # Utilities
    'dotenv': {'version': '1.0.0', 'required': False, 'description': 'Environment variable management', 'package': 'python-dotenv'},
    'yaml': {'version': '6.0', 'required': False, 'description': 'YAML parser', 'package': 'pyyaml'},
    'dateutil': {'version': '2.8.0', 'required': False, 'description': 'Date utilities', 'package': 'python-dateutil'},
    
    # Network Tools
    'nmap': {'version': '0.7.1', 'required': False, 'description': 'Nmap integration', 'package': 'python-nmap'},
    'whois': {'version': '0.9.0', 'required': False, 'description': 'WHOIS client'},
    'pyshorteners': {'version': '1.0.1', 'required': False, 'description': 'URL shortening'},
    'qrcode': {'version': '7.4.0', 'required': False, 'description': 'QR code generator'},
    'validators': {'version': '0.22.0', 'required': False, 'description': 'Data validation'},
    'fake_useragent': {'version': '1.4.0', 'required': False, 'description': 'User agent generation'},
    
    # Security
    'jwt': {'version': '2.8.0', 'required': False, 'description': 'JWT implementation', 'package': 'pyjwt'},
    'pyotp': {'version': '2.9.0', 'required': False, 'description': 'OTP generation'},
    
    # Docker
    'docker': {'version': '6.1.0', 'required': False, 'description': 'Docker SDK'},
    
    # Logging
    'loguru': {'version': '0.7.0', 'required': False, 'description': 'Logging made simple'},
}

SYSTEM_TOOLS = {
    'ping': {'required': True, 'description': 'Network ping utility'},
    'nmap': {'required': False, 'description': 'Network scanner'},
    'curl': {'required': True, 'description': 'URL transfer tool'},
    'wget': {'required': False, 'description': 'File downloader'},
    'nc': {'required': False, 'description': 'Netcat network utility'},
    'dig': {'required': False, 'description': 'DNS lookup utility'},
    'traceroute': {'required': False, 'description': 'Network path tracer'},
    'ssh': {'required': False, 'description': 'SSH client'},
    'docker': {'required': False, 'description': 'Docker container platform'},
    'hashcat': {'required': False, 'description': 'Password cracking tool'},
    'nikto': {'required': False, 'description': 'Web vulnerability scanner'},
    'signal-cli': {'required': False, 'description': 'Signal messaging CLI'},
    'git': {'required': False, 'description': 'Version control system'},
    'python3': {'required': True, 'description': 'Python interpreter'},
    'pip3': {'required': True, 'description': 'Python package installer'},
}

# =====================
# CHECK FUNCTIONS
# =====================

def check_python_version():
    """Check Python version"""
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}🐍 Python Version Check{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 7:
        print(f"{Colors.GREEN}✅ Python {version_str} - OK (3.7+ required){Colors.RESET}")
        return True
    else:
        print(f"{Colors.RED}❌ Python {version_str} - FAILED (3.7+ required){Colors.RESET}")
        return False


def check_pip():
    """Check pip availability"""
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}📦 PIP Check{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    
    pip_path = shutil.which('pip3') or shutil.which('pip')
    if pip_path:
        try:
            result = subprocess.run([pip_path, '--version'], capture_output=True, text=True, timeout=10)
            print(f"{Colors.GREEN}✅ {result.stdout.strip()}{Colors.RESET}")
            return True
        except:
            pass
    
    print(f"{Colors.RED}❌ pip not found{Colors.RESET}")
    return False


def check_python_package(package_name, package_info):
    """Check if a Python package is installed"""
    import_name = package_info.get('package', package_name)
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, None


def check_system_tool(tool_name):
    """Check if a system tool is available"""
    return shutil.which(tool_name) is not None


def check_all_python_packages():
    """Check all Python packages"""
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}🐍 Python Packages{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    
    installed = []
    missing_required = []
    missing_optional = []
    
    for package_name, package_info in PYTHON_PACKAGES.items():
        is_installed, version = check_python_package(package_name, package_info)
        
        if is_installed:
            installed.append((package_name, version))
            print(f"{Colors.GREEN}✅ {package_name:<25} {version}{Colors.RESET}")
        else:
            if package_info.get('required', False):
                missing_required.append(package_name)
                print(f"{Colors.RED}❌ {package_name:<25} MISSING (REQUIRED){Colors.RESET}")
            else:
                missing_optional.append(package_name)
                print(f"{Colors.YELLOW}⚠️  {package_name:<25} MISSING (optional){Colors.RESET}")
    
    return installed, missing_required, missing_optional


def check_all_system_tools():
    """Check all system tools"""
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}🔧 System Tools{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    
    installed = []
    missing_required = []
    missing_optional = []
    
    for tool_name, tool_info in SYSTEM_TOOLS.items():
        is_installed = check_system_tool(tool_name)
        
        if is_installed:
            installed.append(tool_name)
            print(f"{Colors.GREEN}✅ {tool_name:<25} {tool_info['description']}{Colors.RESET}")
        else:
            if tool_info.get('required', False):
                missing_required.append(tool_name)
                print(f"{Colors.RED}❌ {tool_name:<25} MISSING (REQUIRED){Colors.RESET}")
            else:
                missing_optional.append(tool_name)
                print(f"{Colors.YELLOW}⚠️  {tool_name:<25} MISSING (optional){Colors.RESET}")
    
    return installed, missing_required, missing_optional


def generate_install_command(missing_packages):
    """Generate pip install command for missing packages"""
    if not missing_packages:
        return None
    
    packages = []
    for pkg in missing_packages:
        info = PYTHON_PACKAGES.get(pkg, {})
        package_name = info.get('package', pkg)
        version = info.get('version')
        if version:
            packages.append(f"{package_name}>={version}")
        else:
            packages.append(package_name)
    
    return f"pip install {' '.join(packages)}"


def generate_system_install_commands(missing_tools):
    """Generate system tool installation commands"""
    if not missing_tools:
        return {}
    
    system = platform.system().lower()
    commands = {}
    
    if system == 'linux':
        # Detect package manager
        if shutil.which('apt-get'):
            packages = []
            for tool in missing_tools:
                pkg_map = {
                    'nmap': 'nmap',
                    'curl': 'curl',
                    'wget': 'wget',
                    'nc': 'netcat-openbsd',
                    'dig': 'dnsutils',
                    'traceroute': 'traceroute',
                    'ssh': 'openssh-client',
                    'docker': 'docker.io',
                    'hashcat': 'hashcat',
                    'nikto': 'nikto',
                    'git': 'git',
                    'python3': 'python3',
                    'pip3': 'python3-pip',
                }
                if tool in pkg_map:
                    packages.append(pkg_map[tool])
            if packages:
                commands['apt'] = f"sudo apt-get install -y {' '.join(packages)}"
        
        elif shutil.which('yum'):
            packages = []
            for tool in missing_tools:
                pkg_map = {
                    'nmap': 'nmap',
                    'curl': 'curl',
                    'wget': 'wget',
                    'nc': 'nc',
                    'dig': 'bind-utils',
                    'traceroute': 'traceroute',
                    'ssh': 'openssh-clients',
                    'docker': 'docker',
                    'hashcat': 'hashcat',
                    'git': 'git',
                    'python3': 'python3',
                    'pip3': 'python3-pip',
                }
                if tool in pkg_map:
                    packages.append(pkg_map[tool])
            if packages:
                commands['yum'] = f"sudo yum install -y {' '.join(packages)}"
        
        elif shutil.which('pacman'):
            packages = []
            for tool in missing_tools:
                pkg_map = {
                    'nmap': 'nmap',
                    'curl': 'curl',
                    'wget': 'wget',
                    'nc': 'openbsd-netcat',
                    'dig': 'bind',
                    'traceroute': 'traceroute',
                    'ssh': 'openssh',
                    'docker': 'docker',
                    'hashcat': 'hashcat',
                    'nikto': 'nikto',
                    'git': 'git',
                    'python3': 'python',
                    'pip3': 'python-pip',
                }
                if tool in pkg_map:
                    packages.append(pkg_map[tool])
            if packages:
                commands['pacman'] = f"sudo pacman -S --noconfirm {' '.join(packages)}"
    
    elif system == 'darwin':
        packages = []
        for tool in missing_tools:
            pkg_map = {
                'nmap': 'nmap',
                'curl': 'curl',
                'wget': 'wget',
                'nc': 'netcat',
                'dig': 'bind',
                'traceroute': 'traceroute',
                'ssh': 'openssh',
                'docker': 'docker',
                'hashcat': 'hashcat',
                'nikto': 'nikto',
                'git': 'git',
                'python3': 'python3',
                'pip3': 'python3',
            }
            if tool in pkg_map:
                packages.append(pkg_map[tool])
        if packages:
            commands['brew'] = f"brew install {' '.join(packages)}"
    
    elif system == 'windows':
        commands['choco'] = f"choco install -y {' '.join(missing_tools)}"
        commands['scoop'] = f"scoop install {' '.join(missing_tools)}"
    
    return commands


def print_summary(installed_pkgs, missing_required_pkgs, missing_optional_pkgs,
                  installed_tools, missing_required_tools, missing_optional_tools):
    """Print summary of dependency check"""
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}📊 DEPENDENCY CHECK SUMMARY{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}✅ Python Packages: {len(installed_pkgs)} installed{Colors.RESET}")
    if missing_required_pkgs:
        print(f"{Colors.RED}❌ Missing Required: {len(missing_required_pkgs)}{Colors.RESET}")
        for pkg in missing_required_pkgs:
            print(f"   • {pkg}")
    if missing_optional_pkgs:
        print(f"{Colors.YELLOW}⚠️  Missing Optional: {len(missing_optional_pkgs)}{Colors.RESET}")
        for pkg in missing_optional_pkgs[:10]:
            print(f"   • {pkg}")
        if len(missing_optional_pkgs) > 10:
            print(f"   ... and {len(missing_optional_pkgs) - 10} more")
    
    print(f"\n{Colors.GREEN}✅ System Tools: {len(installed_tools)} installed{Colors.RESET}")
    if missing_required_tools:
        print(f"{Colors.RED}❌ Missing Required: {len(missing_required_tools)}{Colors.RESET}")
        for tool in missing_required_tools:
            print(f"   • {tool}")
    if missing_optional_tools:
        print(f"{Colors.YELLOW}⚠️  Missing Optional: {len(missing_optional_tools)}{Colors.RESET}")
        for tool in missing_optional_tools[:10]:
            print(f"   • {tool}")
        if len(missing_optional_tools) > 10:
            print(f"   ... and {len(missing_optional_tools) - 10} more")
    
    # Generate installation commands
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}🔧 INSTALLATION COMMANDS{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    
    all_missing_pkgs = missing_required_pkgs + missing_optional_pkgs
    if all_missing_pkgs:
        pip_cmd = generate_install_command(all_missing_pkgs)
        print(f"\n{Colors.PURPLE}Python Packages:{Colors.RESET}")
        print(f"  {pip_cmd}")
    
    all_missing_tools = missing_required_tools + missing_optional_tools
    if all_missing_tools:
        sys_commands = generate_system_install_commands(all_missing_tools)
        if sys_commands:
            print(f"\n{Colors.PURPLE}System Tools:{Colors.RESET}")
            for manager, cmd in sys_commands.items():
                print(f"  {cmd}")
    
    # Final status
    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
    if not missing_required_pkgs and not missing_required_tools:
        print(f"{Colors.GREEN}🎉 All required dependencies are installed!{Colors.RESET}")
        print(f"{Colors.GREEN}✅ CYCLOPUS-BOT-V1 is ready to run!{Colors.RESET}")
    else:
        print(f"{Colors.RED}❌ Some required dependencies are missing.{Colors.RESET}")
        print(f"{Colors.YELLOW}⚠️  Please install them using the commands above.{Colors.RESET}")
    
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}\n")


def main():
    """Main entry point"""
    print(f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║{Colors.PURPLE}     🐙 CYCLOPUS-BOT-V1 - Dependency Checker                {Colors.CYAN}║
║{Colors.PURPLE}     Version: 1.0.0 | Author: Ian Carter Kulani, MSc        {Colors.CYAN}║
╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
""")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check pip
    if not check_pip():
        print(f"{Colors.YELLOW}⚠️  pip not found. Please install pip first.{Colors.RESET}")
    
    # Check Python packages
    installed_pkgs, missing_required_pkgs, missing_optional_pkgs = check_all_python_packages()
    
    # Check system tools
    installed_tools, missing_required_tools, missing_optional_tools = check_all_system_tools()
    
    # Print summary
    print_summary(
        installed_pkgs, missing_required_pkgs, missing_optional_pkgs,
        installed_tools, missing_required_tools, missing_optional_tools
    )
    
    # Ask to install missing packages
    all_missing = missing_required_pkgs + missing_optional_pkgs
    if all_missing:
        try:
            response = input(f"{Colors.PURPLE}Install missing Python packages now? (y/n): {Colors.RESET}").strip().lower()
            if response == 'y':
                cmd = generate_install_command(all_missing)
                print(f"\n{Colors.CYAN}Running: {cmd}{Colors.RESET}\n")
                subprocess.run(cmd, shell=True)
                print(f"\n{Colors.GREEN}✅ Installation complete!{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Cancelled.{Colors.RESET}")


if __name__ == "__main__":
    main()
