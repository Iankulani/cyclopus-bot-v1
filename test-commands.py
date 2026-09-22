#!/usr/bin/env python3
"""
🐙 CYCLOPUS-BOT-V1 - Comprehensive Test Suite
Author: Ian Carter Kulani, MSc
Version: 1.0.0

This script tests all major commands and features of CYCLOPUS-BOT-V1.
"""

import os
import sys
import time
import json
import socket
import platform
import subprocess
import unittest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
# TEST CONFIGURATION
# =====================
TEST_CONFIG = {
    'test_ip': '127.0.0.1',
    'test_domain': 'example.com',
    'test_port': 80,
    'test_duration': 1,
    'test_threads': 2,
    'timeout': 30
}

# =====================
# TEST RESULTS TRACKER
# =====================
class TestResults:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.errors = []
        self.start_time = time.time()
    
    def add_pass(self, test_name):
        self.passed += 1
        print(f"  {Colors.GREEN}✅ PASS{Colors.RESET}: {test_name}")
    
    def add_fail(self, test_name, error):
        self.failed += 1
        self.errors.append((test_name, error))
        print(f"  {Colors.RED}❌ FAIL{Colors.RESET}: {test_name}")
        print(f"     {Colors.RED}Error: {error}{Colors.RESET}")
    
    def add_skip(self, test_name, reason):
        self.skipped += 1
        print(f"  {Colors.YELLOW}⚠️  SKIP{Colors.RESET}: {test_name} - {reason}")
    
    def summary(self):
        elapsed = time.time() - self.start_time
        print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}📊 TEST SUMMARY{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
        print(f"  {Colors.GREEN}Passed: {self.passed}{Colors.RESET}")
        print(f"  {Colors.RED}Failed: {self.failed}{Colors.RESET}")
        print(f"  {Colors.YELLOW}Skipped: {self.skipped}{Colors.RESET}")
        print(f"  Total: {self.passed + self.failed + self.skipped}")
        print(f"  Time: {elapsed:.2f}s")
        
        if self.errors:
            print(f"\n{Colors.RED}Errors:{Colors.RESET}")
            for name, error in self.errors:
                print(f"  • {name}: {error}")
        
        return self.failed == 0

results = TestResults()

# =====================
# HELPER FUNCTIONS
# =====================

def run_command(cmd, timeout=30):
    """Run a shell command and return result"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            'success': result.returncode == 0,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Timeout'}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def import_module(module_name):
    """Safely import a module"""
    try:
        return __import__(module_name)
    except ImportError:
        return None

# =====================
# TEST CLASSES
# =====================

class TestCoreDependencies(unittest.TestCase):
    """Test core dependencies"""
    
    def test_requests(self):
        """Test requests library"""
        try:
            import requests
            response = requests.get('https://httpbin.org/get', timeout=10)
            self.assertEqual(response.status_code, 200)
            results.add_pass('requests library')
        except Exception as e:
            results.add_fail('requests library', str(e))
    
    def test_colorama(self):
        """Test colorama"""
        try:
            import colorama
            results.add_pass('colorama')
        except ImportError:
            results.add_skip('colorama', 'Not installed')
    
    def test_psutil(self):
        """Test psutil"""
        try:
            import psutil
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory().percent
            self.assertIsInstance(cpu, float)
            self.assertIsInstance(mem, float)
            results.add_pass('psutil')
        except ImportError:
            results.add_skip('psutil', 'Not installed')
        except Exception as e:
            results.add_fail('psutil', str(e))


class TestNetworkTools(unittest.TestCase):
    """Test network tools"""
    
    def test_ping(self):
        """Test ping command"""
        if not shutil.which('ping'):
            results.add_skip('ping', 'ping not installed')
            return
        
        result = run_command(f'ping -c 1 -W 2 {TEST_CONFIG["test_ip"]}')
        if result['success']:
            results.add_pass('ping command')
        else:
            results.add_fail('ping command', result.get('error', 'Failed'))
    
    def test_nmap(self):
        """Test nmap"""
        if not shutil.which('nmap'):
            results.add_skip('nmap', 'nmap not installed')
            return
        
        result = run_command(f'nmap -F {TEST_CONFIG["test_ip"]}', timeout=60)
        if result['success']:
            results.add_pass('nmap command')
        else:
            results.add_fail('nmap command', result.get('error', 'Failed'))
    
    def test_curl(self):
        """Test curl"""
        if not shutil.which('curl'):
            results.add_skip('curl', 'curl not installed')
            return
        
        result = run_command('curl -s -o /dev/null -w "%{http_code}" https://example.com')
        if result['success'] and result['stdout'].strip() == '200':
            results.add_pass('curl command')
        else:
            results.add_fail('curl command', f"Status: {result.get('stdout', 'N/A')}")
    
    def test_wget(self):
        """Test wget"""
        if not shutil.which('wget'):
            results.add_skip('wget', 'wget not installed')
            return
        
        result = run_command('wget --spider -q https://example.com')
        if result['success']:
            results.add_pass('wget command')
        else:
            results.add_fail('wget command', result.get('error', 'Failed'))
    
    def test_traceroute(self):
        """Test traceroute"""
        traceroute = shutil.which('traceroute') or shutil.which('tracert')
        if not traceroute:
            results.add_skip('traceroute', 'traceroute not installed')
            return
        
        result = run_command(f'traceroute -m 3 {TEST_CONFIG["test_ip"]}', timeout=30)
        if result['success']:
            results.add_pass('traceroute command')
        else:
            results.add_fail('traceroute command', result.get('error', 'Failed'))
    
    def test_dns(self):
        """Test DNS lookup"""
        dig = shutil.which('dig') or shutil.which('nslookup')
        if not dig:
            results.add_skip('DNS lookup', 'dig/nslookup not installed')
            return
        
        result = run_command(f'dig +short {TEST_CONFIG["test_domain"]}')
        if result['success'] and result['stdout'].strip():
            results.add_pass('DNS lookup')
        else:
            results.add_fail('DNS lookup', result.get('error', 'Failed'))
    
    def test_whois(self):
        """Test whois"""
        if not shutil.which('whois'):
            results.add_skip('whois', 'whois not installed')
            return
        
        result = run_command(f'whois {TEST_CONFIG["test_domain"]}', timeout=30)
        if result['success']:
            results.add_pass('whois command')
        else:
            results.add_fail('whois command', result.get('error', 'Failed'))


class TestPythonModules(unittest.TestCase):
    """Test Python modules used by CYCLOPUS-BOT-V1"""
    
    def test_scapy(self):
        """Test scapy"""
        try:
            import scapy
            from scapy.all import IP, TCP, ICMP
            packet = IP(dst="127.0.0.1")/ICMP()
            self.assertIsNotNone(packet)
            results.add_pass('scapy')
        except ImportError:
            results.add_skip('scapy', 'Not installed')
        except Exception as e:
            results.add_fail('scapy', str(e))
    
    def test_paramiko(self):
        """Test paramiko"""
        try:
            import paramiko
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            results.add_pass('paramiko')
        except ImportError:
            results.add_skip('paramiko', 'Not installed')
        except Exception as e:
            results.add_fail('paramiko', str(e))
    
    def test_flask(self):
        """Test flask"""
        try:
            from flask import Flask
            app = Flask(__name__)
            self.assertIsNotNone(app)
            results.add_pass('flask')
        except ImportError:
            results.add_skip('flask', 'Not installed')
        except Exception as e:
            results.add_fail('flask', str(e))
    
    def test_pynput(self):
        """Test pynput"""
        try:
            from pynput import keyboard
            results.add_pass('pynput (keylogger)')
        except ImportError:
            results.add_skip('pynput', 'Not installed')
        except Exception as e:
            results.add_fail('pynput', str(e))
    
    def test_reportlab(self):
        """Test reportlab"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate
            results.add_pass('reportlab (PDF)')
        except ImportError:
            results.add_skip('reportlab', 'Not installed')
        except Exception as e:
            results.add_fail('reportlab', str(e))
    
    def test_matplotlib(self):
        """Test matplotlib"""
        try:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            results.add_pass('matplotlib')
        except ImportError:
            results.add_skip('matplotlib', 'Not installed')
        except Exception as e:
            results.add_fail('matplotlib', str(e))
    
    def test_sqlite3(self):
        """Test sqlite3"""
        try:
            import sqlite3
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE test (id INTEGER)')
            conn.close()
            results.add_pass('sqlite3')
        except Exception as e:
            results.add_fail('sqlite3', str(e))
    
    def test_discord(self):
        """Test discord.py"""
        try:
            import discord
            results.add_pass('discord.py')
        except ImportError:
            results.add_skip('discord.py', 'Not installed')
        except Exception as e:
            results.add_fail('discord.py', str(e))
    
    def test_telethon(self):
        """Test telethon"""
        try:
            from telethon import TelegramClient
            results.add_pass('telethon')
        except ImportError:
            results.add_skip('telethon', 'Not installed')
        except Exception as e:
            results.add_fail('telethon', str(e))
    
    def test_dnspython(self):
        """Test dnspython"""
        try:
            import dns.resolver
            results.add_pass('dnspython')
        except ImportError:
            results.add_skip('dnspython', 'Not installed')
        except Exception as e:
            results.add_fail('dnspython', str(e))


class TestApplicationModules(unittest.TestCase):
    """Test CYCLOPUS-BOT-V1 application modules"""
    
    @classmethod
    def setUpClass(cls):
        """Import main application"""
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import importlib.util
            
            # Try to import the main module
            main_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cyclopus_bot_v1.py')
            if os.path.exists(main_file):
                spec = importlib.util.spec_from_file_location("cyclopus_bot_v1", main_file)
                cls.module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(cls.module)
            else:
                cls.module = None
        except Exception as e:
            cls.module = None
            print(f"{Colors.YELLOW}⚠️  Could not load main module: {e}{Colors.RESET}")
    
    def test_config_manager(self):
        """Test ConfigManager"""
        if not self.module:
            results.add_skip('ConfigManager', 'Module not loaded')
            return
        
        try:
            config = self.module.ConfigManager()
            self.assertIsNotNone(config.config)
            results.add_pass('ConfigManager')
        except Exception as e:
            results.add_fail('ConfigManager', str(e))
    
    def test_database_manager(self):
        """Test DatabaseManager"""
        if not self.module:
            results.add_skip('DatabaseManager', 'Module not loaded')
            return
        
        try:
            db = self.module.DatabaseManager(':memory:')
            stats = db.get_statistics()
            self.assertIsInstance(stats, dict)
            results.add_pass('DatabaseManager')
        except Exception as e:
            results.add_fail('DatabaseManager', str(e))
    
    def test_terminal_animation(self):
        """Test TerminalAnimation"""
        if not self.module:
            results.add_skip('TerminalAnimation', 'Module not loaded')
            return
        
        try:
            anim = self.module.TerminalAnimation
            anim.spinner(0.1, "Test")
            results.add_pass('TerminalAnimation')
        except Exception as e:
            results.add_fail('TerminalAnimation', str(e))
    
    def test_network_tools(self):
        """Test NetworkTools"""
        if not self.module:
            results.add_skip('NetworkTools', 'Module not loaded')
            return
        
        try:
            tools = self.module.NetworkTools()
            local_ip = tools.get_local_ip()
            self.assertIsNotNone(local_ip)
            results.add_pass('NetworkTools')
        except Exception as e:
            results.add_fail('NetworkTools', str(e))
    
    def test_command_handler(self):
        """Test CommandHandler"""
        if not self.module:
            results.add_skip('CommandHandler', 'Module not loaded')
            return
        
        try:
            db = self.module.DatabaseManager(':memory:')
            handler = self.module.CommandHandler(db)
            result = handler.execute('help')
            self.assertTrue(result['success'])
            results.add_pass('CommandHandler')
        except Exception as e:
            results.add_fail('CommandHandler', str(e))


class TestCommandExecution(unittest.TestCase):
    """Test actual command execution"""
    
    @classmethod
    def setUpClass(cls):
        """Set up handler"""
        try:
            import importlib.util
            main_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cyclopus_bot_v1.py')
            if os.path.exists(main_file):
                spec = importlib.util.spec_from_file_location("cyclopus_bot_v1", main_file)
                cls.module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(cls.module)
                
                cls.db = cls.module.DatabaseManager(':memory:')
                cls.handler = cls.module.CommandHandler(cls.db)
            else:
                cls.module = None
                cls.handler = None
        except Exception as e:
            cls.module = None
            cls.handler = None
    
    def test_help_command(self):
        """Test help command"""
        if not self.handler:
            results.add_skip('help command', 'Handler not loaded')
            return
        
        result = self.handler.execute('help')
        if result['success'] and 'CYCLOPUS' in result.get('output', ''):
            results.add_pass('help command')
        else:
            results.add_fail('help command', 'Help output missing')
    
    def test_status_command(self):
        """Test status command"""
        if not self.handler:
            results.add_skip('status command', 'Handler not loaded')
            return
        
        result = self.handler.execute('status')
        if result['success']:
            results.add_pass('status command')
        else:
            results.add_fail('status command', result.get('output', 'Failed'))
    
    def test_system_command(self):
        """Test system command"""
        if not self.handler:
            results.add_skip('system command', 'Handler not loaded')
            return
        
        result = self.handler.execute('system')
        if result['success']:
            results.add_pass('system command')
        else:
            results.add_fail('system command', result.get('output', 'Failed'))
    
    def test_ping_command(self):
        """Test ping command"""
        if not self.handler:
            results.add_skip('ping command', 'Handler not loaded')
            return
        
        result = self.handler.execute(f'ping {TEST_CONFIG["test_ip"]}')
        if result['success']:
            results.add_pass('ping command (handler)')
        else:
            results.add_fail('ping command (handler)', result.get('output', 'Failed'))
    
    def test_traffic_types_command(self):
        """Test traffic types command"""
        if not self.handler:
            results.add_skip('traffic_types command', 'Handler not loaded')
            return
        
        result = self.handler.execute('traffic_types')
        if result['success']:
            results.add_pass('traffic_types command')
        else:
            results.add_fail('traffic_types command', result.get('output', 'Failed'))
    
    def test_list_templates_command(self):
        """Test list_templates command"""
        if not self.handler:
            results.add_skip('list_templates command', 'Handler not loaded')
            return
        
        result = self.handler.execute('list_templates')
        if result['success']:
            results.add_pass('list_templates command')
        else:
            results.add_fail('list_templates command', result.get('output', 'Failed'))


class TestDatabaseOperations(unittest.TestCase):
    """Test database operations"""
    
    @classmethod
    def setUpClass(cls):
        """Set up database"""
        try:
            import importlib.util
            main_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cyclopus_bot_v1.py')
            if os.path.exists(main_file):
                spec = importlib.util.spec_from_file_location("cyclopus_bot_v1", main_file)
                cls.module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(cls.module)
                cls.db = cls.module.DatabaseManager(':memory:')
            else:
                cls.module = None
                cls.db = None
        except Exception as e:
            cls.module = None
            cls.db = None
    
    def test_log_command(self):
        """Test logging a command"""
        if not self.db:
            results.add_skip('log_command', 'DB not loaded')
            return
        
        try:
            self.db.log_command('test command', 'test', 'test', 'user', True, 'output', 0.5)
            results.add_pass('log_command')
        except Exception as e:
            results.add_fail('log_command', str(e))
    
    def test_add_managed_ip(self):
        """Test adding managed IP"""
        if not self.db:
            results.add_skip('add_managed_ip', 'DB not loaded')
            return
        
        try:
            result = self.db.add_managed_ip('192.168.1.100', 'test.local', 'testhost', 'Linux', 'test')
            results.add_pass('add_managed_ip')
        except Exception as e:
            results.add_fail('add_managed_ip', str(e))
    
    def test_get_statistics(self):
        """Test getting statistics"""
        if not self.db:
            results.add_skip('get_statistics', 'DB not loaded')
            return
        
        try:
            stats = self.db.get_statistics()
            self.assertIsInstance(stats, dict)
            results.add_pass('get_statistics')
        except Exception as e:
            results.add_fail('get_statistics', str(e))
    
    def test_phishing_templates(self):
        """Test phishing templates"""
        if not self.db:
            results.add_skip('phishing_templates', 'DB not loaded')
            return
        
        try:
            templates = self.db.get_phishing_templates()
            self.assertGreater(len(templates), 0)
            results.add_pass(f'phishing_templates ({len(templates)} templates)')
        except Exception as e:
            results.add_fail('phishing_templates', str(e))


class TestFileOperations(unittest.TestCase):
    """Test file operations"""
    
    def test_temp_directory_creation(self):
        """Test temp directory creation"""
        try:
            temp_dir = tempfile.mkdtemp()
            self.assertTrue(os.path.exists(temp_dir))
            shutil.rmtree(temp_dir)
            results.add_pass('temp directory creation')
        except Exception as e:
            results.add_fail('temp directory creation', str(e))
    
    def test_file_write_read(self):
        """Test file write/read"""
        try:
            temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
            temp_file.write('test data')
            temp_file.close()
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
            
            self.assertEqual(content, 'test data')
            os.unlink(temp_file.name)
            results.add_pass('file write/read')
        except Exception as e:
            results.add_fail('file write/read', str(e))
    
    def test_json_operations(self):
        """Test JSON operations"""
        try:
            data = {'key': 'value', 'number': 123, 'list': [1, 2, 3]}
            json_str = json.dumps(data)
            parsed = json.loads(json_str)
            self.assertEqual(data, parsed)
            results.add_pass('JSON operations')
        except Exception as e:
            results.add_fail('JSON operations', str(e))


class TestSecurityFeatures(unittest.TestCase):
    """Test security features"""
    
    def test_password_hashing(self):
        """Test password hashing"""
        try:
            import hashlib
            password = "test_password_123"
            hash1 = hashlib.sha256(password.encode()).hexdigest()
            hash2 = hashlib.sha256(password.encode()).hexdigest()
            self.assertEqual(hash1, hash2)
            results.add_pass('password hashing')
        except Exception as e:
            results.add_fail('password hashing', str(e))
    
    def test_ip_validation(self):
        """Test IP validation"""
        try:
            import ipaddress
            ip = ipaddress.ip_address('192.168.1.1')
            self.assertTrue(ip.is_private)
            
            invalid = False
            try:
                ipaddress.ip_address('999.999.999.999')
            except ValueError:
                invalid = True
            self.assertTrue(invalid)
            results.add_pass('IP validation')
        except Exception as e:
            results.add_fail('IP validation', str(e))
    
    def test_mac_address_parsing(self):
        """Test MAC address parsing"""
        try:
            mac = "00:11:22:33:44:55"
            parts = mac.split(':')
            self.assertEqual(len(parts), 6)
            results.add_pass('MAC address parsing')
        except Exception as e:
            results.add_fail('MAC address parsing', str(e))


class TestConcurrency(unittest.TestCase):
    """Test concurrency features"""
    
    def test_threading(self):
        """Test threading"""
        try:
            import threading
            counter = {'value': 0}
            lock = threading.Lock()
            
            def increment():
                for _ in range(100):
                    with lock:
                        counter['value'] += 1
            
            threads = [threading.Thread(target=increment) for _ in range(5)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            
            self.assertEqual(counter['value'], 500)
            results.add_pass('threading')
        except Exception as e:
            results.add_fail('threading', str(e))
    
    def test_queue(self):
        """Test queue operations"""
        try:
            import queue
            q = queue.Queue()
            for i in range(10):
                q.put(i)
            
            items = []
            while not q.empty():
                items.append(q.get())
            
            self.assertEqual(len(items), 10)
            results.add_pass('queue operations')
        except Exception as e:
            results.add_fail('queue operations', str(e))


# =====================
# MAIN TEST RUNNER
# =====================

def run_all_tests():
    """Run all tests"""
    print(f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║{Colors.PURPLE}     🐙 CYCLOPUS-BOT-V1 - Comprehensive Test Suite          {Colors.CYAN}║
║{Colors.PURPLE}     Version: 1.0.0 | Author: Ian Carter Kulani, MSc        {Colors.CYAN}║
╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
""")
    
    print(f"{Colors.CYAN}System: {platform.system()} {platform.release()}{Colors.RESET}")
    print(f"{Colors.CYAN}Python: {sys.version}{Colors.RESET}")
    print(f"{Colors.CYAN}Test IP: {TEST_CONFIG['test_ip']}{Colors.RESET}")
    print()
    
    # Test Core Dependencies
    print(f"\n{Colors.BOLD}🔍 Testing Core Dependencies...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCoreDependencies)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test Network Tools
    print(f"\n{Colors.BOLD}🌐 Testing Network Tools...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNetworkTools)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test Python Modules
    print(f"\n{Colors.BOLD}🐍 Testing Python Modules...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPythonModules)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test Application Modules
    print(f"\n{Colors.BOLD}📦 Testing Application Modules...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApplicationModules)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test Command Execution
    print(f"\n{Colors.BOLD}⚡ Testing Command Execution...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCommandExecution)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test Database Operations
    print(f"\n{Colors.BOLD}💾 Testing Database Operations...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabaseOperations)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test File Operations
    print(f"\n{Colors.BOLD}📁 Testing File Operations...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFileOperations)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test Security Features
    print(f"\n{Colors.BOLD}🔒 Testing Security Features...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSecurityFeatures)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Test Concurrency
    print(f"\n{Colors.BOLD}🔄 Testing Concurrency...{Colors.RESET}")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestConcurrency)
    unittest.TextTestRunner(verbosity=0).run(suite)
    
    # Print summary
    success = results.summary()
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
