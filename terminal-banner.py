#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Professional Terminal Banner with Big ASCII Art
"""

import os
import datetime
import random
import sys
import time

class ProfessionalBanner:
    def __init__(self):
        # 🔄 এখানে আপনার নাম লিখুন
        self.your_name = "CRYPTICX"
        
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'magenta': '\033[95m',
            'white': '\033[97m',
            'bold': '\033[1m',
            'underline': '\033[4m',
            'end': '\033[0m'
        }
        
        # ASCII Art Styles
        self.ascii_styles = [
            self.style_1,
            self.style_2,
            self.style_3
        ]
    
    def clear_screen(self):
        os.system('clear')
    
    def get_current_time(self):
        now = datetime.datetime.now()
        return {
            'time': now.strftime("%H:%M:%S"),
            'date': now.strftime("%d-%m-%Y"),
            'day': now.strftime("%A"),
            'full_date': now.strftime("%B %d, %Y")
        }
    def get_random_color(self):
        color_keys = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'magenta']
        return self.colors[random.choice(color_keys)]
    
    def style_1(self, name):
        """Big Block Letters"""
        return f"""
{self.colors['bold']}{self.get_random_color()}
    ░██████  ░█████████  ░██     ░██ ░█████████  ░██████████░██████  ░██████  ░██    ░██ 
 ░██   ░██ ░██     ░██  ░██   ░██  ░██     ░██     ░██      ░██   ░██   ░██  ░██  ░██  
░██        ░██     ░██   ░██ ░██   ░██     ░██     ░██      ░██  ░██          ░██░██   
░██        ░█████████     ░████    ░█████████      ░██      ░██  ░██           ░███    
░██        ░██   ░██       ░██     ░██             ░██      ░██  ░██          ░██░██   
 ░██   ░██ ░██    ░██      ░██     ░██             ░██      ░██   ░██   ░██  ░██  ░██  
  ░██████  ░██     ░██     ░██     ░██             ░██    ░██████  ░██████  ░██    ░██ 
                                                                                       
{self.colors['end']}"""
    
    def style_2(self, name):
        """Shadow Effect"""
        return f"""
{self.colors['bold']}{self.colors['blue']}
 ░█▀▀░█▀▄░█░█░█▀█░▀█▀░▀█▀░█▀▀░█░█
░█░░░█▀▄░░█░░█▀▀░░█░░░█░░█░░░▄▀▄
░▀▀▀░▀░▀░░▀░░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀

{self.colors['yellow']}
  ░██████  ░█████████  ░██     ░██ ░█████████  ░██████████░██████  ░██████  ░██    ░██ 
 ░██   ░██ ░██     ░██  ░██   ░██  ░██     ░██     ░██      ░██   ░██   ░██  ░██  ░██  
░██        ░██     ░██   ░██ ░██   ░██     ░██     ░██      ░██  ░██          ░██░██   
░██        ░█████████     ░████    ░█████████      ░██      ░██  ░██           ░███    
░██        ░██   ░██       ░██     ░██             ░██      ░██  ░██          ░██░██   
 ░██   ░██ ░██    ░██      ░██     ░██             ░██      ░██   ░██   ░██  ░██  ░██  
  ░██████  ░██     ░██     ░██     ░██             ░██    ░██████  ░██████  ░██    ░██ 
                                                                                       
{self.colors['end']}"""
    
    def style_3(self, name):
        """3D Effect"""
        return f"""
{self.colors['bold']}{self.colors['cyan']}
  ░██████  ░█████████  ░██     ░██ ░█████████  ░██████████░██████  ░██████  ░██    ░██ 
 ░██   ░██ ░██     ░██  ░██   ░██  ░██     ░██     ░██      ░██   ░██   ░██  ░██  ░██  
░██        ░██     ░██   ░██ ░██   ░██     ░██     ░██      ░██  ░██          ░██░██   
░██        ░█████████     ░████    ░█████████      ░██      ░██  ░██           ░███    
░██        ░██   ░██       ░██     ░██             ░██      ░██  ░██          ░██░██   
 ░██   ░██ ░██    ░██      ░██     ░██             ░██      ░██   ░██   ░██  ░██  ░██  
  ░██████  ░██     ░██     ░██     ░██             ░██    ░██████  ░██████  ░██    ░██ 
                                                                                       
{self.colors['end']}"""
    def print_banner(self):
        time_data = self.get_current_time()
        selected_style = random.choice(self.ascii_styles)       
        # Main Banner
        banner = f"""
{selected_style(self.your_name)}

{self.colors['bold']}{self.get_random_color()}╔══════════════════════════════════════════════════════════════════╗{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║                       W E L C O M E                             ║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║                                                                  ║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║          {self.colors['bold']}{self.colors['yellow']}» {self.your_name.upper()} «{self.get_random_color()}          ║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║                                                                  ║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}╠══════════════════════════════════════════════════════════════════╣{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║                                                                  ║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║   🕐 {self.colors['green']}TIME:    {time_data['time']}{self.get_random_color()}{' ' * (35 - len(time_data['time']))}║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║   📅 {self.colors['yellow']}DATE:    {time_data['date']}{self.get_random_color()}{' ' * (35 - len(time_data['date']))}║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║   🌟 {self.colors['cyan']}DAY:     {time_data['day']}{self.get_random_color()}{' ' * (35 - len(time_data['day']))}║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║                                                                  ║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║   💻 {self.colors['red']}SYSTEM:  Termux Android{self.get_random_color()}{' ' * (25)}║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║   🐍 {self.colors['purple']}PYTHON:  v{sys.version.split()[0]}{self.get_random_color()}{' ' * (30 - len(sys.version.split()[0]))}║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║   👤 {self.colors['magenta']}USER:    {self.your_name}{self.get_random_color()}{' ' * (30 - len(self.your_name))}║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}║                                                                  ║{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}╚══════════════════════════════════════════════════════════════════╝{self.colors['end']}

{self.colors['bold']}{self.get_random_color()}🚀 Professional Hacker • Python Developer • Security Researcher{self.colors['end']}
{self.colors['bold']}{self.get_random_color()}💻 Ready for some serious terminal work!{self.colors['end']}
"""
        print(banner)
    def print_system_info(self):
        try:
            print(f"\n{self.colors['bold']}{self.colors['cyan']}📊 SYSTEM INFORMATION:{self.colors['end']}")
            
            # Hostname
            hostname = os.uname().nodename
            print(f"   {self.colors['yellow']}🏠 Hostname: {self.colors['white']}{hostname}{self.colors['end']}")
            
            # System
            system = os.uname().sysname
            release = os.uname().release
            print(f"   {self.colors['green']}🐧 System: {self.colors['white']}{system} {release}{self.colors['end']}")
            
            # Current Directory
            current_dir = os.getcwd()
            print(f"   {self.colors['blue']}📁 Directory: {self.colors['white']}{current_dir}{self.colors['end']}")
            
            # Python Info
            python_version = sys.version.split()[0]
            print(f"   {self.colors['purple']}🐍 Python: {self.colors['white']}v{python_version}{self.colors['end']}")
            
        except Exception as e:
            print(f"   {self.colors['red']}Error getting system info: {e}{self.colors['end']}")
    
    def print_quick_stats(self):
        print(f"\n{self.colors['bold']}{self.colors['green']}⚡ QUICK STATS:{self.colors['end']}")
        
        stats = [
            f"{self.colors['yellow']}• {self.colors['white']}Active Sessions: {self.colors['cyan']}1{self.colors['end']}",
            f"{self.colors['yellow']}• {self.colors['white']}Battery: {self.colors['green']}Optimal{self.colors['end']}",
            f"{self.colors['yellow']}• {self.colors['white']}Connection: {self.colors['blue']}Secure{self.colors['end']}",
            f"{self.colors['yellow']}• {self.colors['white']}Status: {self.colors['green']}Ready{self.colors['end']}"
        ]
        
        for stat in stats:
            print(f"   {stat}")

def main():
    banner = ProfessionalBanner()
    
    while True:
        banner.clear_screen()
        banner.print_banner()
        banner.print_system_info()
        banner.print_quick_stats()
        
        print(f"\n{banner.colors['bold']}{banner.colors['red']}Press 'q' to quit, 'r' to refresh, Enter to continue...{banner.colors['end']}")
        
        user_input = input().strip().lower()
        
        if user_input == 'q':
            print(f"\n{banner.colors['bold']}{banner.colors['green']}👋 Goodbye {banner.your_name}! Happy hacking! 🚀{banner.colors['end']}")
            break
        elif user_input == 'r':
            continue
        else:
            break

if __name__ == "__main__":
    main()