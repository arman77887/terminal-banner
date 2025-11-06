#!/usr/bin/env python3
import time
import os
import sys

class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

class CompactBanner:
    def __init__(self):
        self.colors = Colors()
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_ascii_banner(self):
        ascii_art = f"""
{self.colors.CYAN}
      █████████  ███████████   █████ █████ ███████████  ███████████ █████   █████████  █████ █████
  ███░░░░░███░░███░░░░░███ ░░███ ░░███ ░░███░░░░░███░█░░░███░░░█░░███   ███░░░░░███░░███ ░░███ 
 ███     ░░░  ░███    ░███  ░░███ ███   ░███    ░███░   ░███  ░  ░███  ███     ░░░  ░░███ ███  
░███          ░██████████    ░░█████    ░██████████     ░███     ░███ ░███           ░░█████   
░███          ░███░░░░░███    ░░███     ░███░░░░░░      ░███     ░███ ░███            ███░███  
░░███     ███ ░███    ░███     ░███     ░███            ░███     ░███ ░░███     ███  ███ ░░███ 
 ░░█████████  █████   █████    █████    █████           █████    █████ ░░█████████  █████ █████
  ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░    ░░░░░           ░░░░░    ░░░░░   ░░░░░░░░░   ░░░░░░   ░░░░░░░░░
                                                                                               
{self.colors.GREEN}  ═════ iOS TERMINAL ═════
{self.colors.RESET}"""
        print(ascii_art)
    
    def quick_scan(self):
        print(f"{self.colors.YELLOW}🛡️  Quick Scan...", end="", flush=True)
        
        for i in range(3):
            print(f"{self.colors.GREEN} ✓", end="", flush=True)
            time.sleep(0.3)
        
        print(f"{self.colors.RESET}")
    
    def system_status(self):
        status = f"""
{self.colors.BLUE}┌─────── STATUS ───────┐
{self.colors.GREEN}│ 🔐 Security: ACTIVE  │
{self.colors.GREEN}│ 📱 Device:  READY    │
{self.colors.GREEN}│ 💻 Shell:   iSH      │
{self.colors.BLUE}└──────────────────────┘{self.colors.RESET}
"""
        print(status)
    
    def mini_loading(self):
        print(f"{self.colors.YELLOW}Initializing", end="", flush=True)
        
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.4)
        
        print(f" {self.colors.GREEN}DONE!{self.colors.RESET}")
    
    def show_prompt(self):
        prompt = f"{self.colors.RED}➜ {self.colors.CYAN}${self.colors.RESET} "
        print(prompt, end="")

def main():
    banner = CompactBanner()
    
    try:
        banner.clear_screen()
        banner.print_ascii_banner()
        banner.quick_scan()
        banner.system_status()
        banner.mini_loading()
        banner.show_prompt()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Session ended{Colors.RESET}")

if __name__ == "__main__":
    main()
