#!/bin/sh
# crypticx.sh - Animated fake-boot + auto system/phone details + banner
# POSIX-compatible (for iSH / BusyBox). Some info may not be available inside iSH.

ESC=$(printf '\033')
RESET="${ESC}[0m"
BOLD="${ESC}[1m"
GREEN="${ESC}[32m"
CYAN="${ESC}[36m"
YELLOW="${ESC}[33m"
GRAY="${ESC}[90m"

# ---------- Helper: typewriter print ----------
type_line() {
  text="$1"
  delay="${2:-0.03}"
  i=0
  len=${#text}
  while [ $i -lt $len ]; do
    printf "%s" "${text:$i:1}"
    i=$((i+1))
    sleep "$delay"
  done
  printf "\n"
}

# ---------- Gather system info (best-effort) ----------
# whoami / hostname / date / uptime / kernel / arch / shell
USERNM=$(whoami 2>/dev/null || printf "%s" "$USER" || printf "unknown")
HOSTN=$(hostname 2>/dev/null || printf "ish")
DATENOW=$(date "+%Y-%m-%d %H:%M:%S" 2>/dev/null || date 2>/dev/null || printf "unknown")
UPTIME_INFO=$(uptime 2>/dev/null || cat /proc/uptime 2>/dev/null | awk '{print $1 "s"}' 2>/dev/null || printf "n/a")
KERNEL=$(uname -s 2>/dev/null || printf "n/a")
ARCH=$(uname -m 2>/dev/null || printf "n/a")
SHELLX=$(printf "%s" "$SHELL" 2>/dev/null || printf "sh")

# Try to get IP address (prefer ip, then ifconfig, then hostname -I)
IP_ADDR=""
if command -v ip >/dev/null 2>&1; then
  IP_ADDR=$(ip -4 addr show 2>/dev/null | awk '/inet / && !/127.0.0.1/ {gsub(/\/.*/,"",$2); print $2; exit}' || true)
fi
if [ -z "$IP_ADDR" ] && command -v ifconfig >/dev/null 2>&1; then
  IP_ADDR=$(ifconfig 2>/dev/null | awk '/inet / && $2!="127.0.0.1" {print $2; exit}' || true)
fi
if [ -z "$IP_ADDR" ]; then
  IP_ADDR=$(hostname -I 2>/dev/null | awk '{print $1}' || true)
fi
[ -z "$IP_ADDR" ] && IP_ADDR="unknown"

# Disk and memory (best-effort)
DISK_USAGE=$(df -h / 2>/dev/null | awk 'NR==2{print $3 " used / " $2 " total (" $5 " used)"}' || printf "n/a")
MEM_INFO=$(free -h 2>/dev/null | awk 'NR==2{print $3 " used / " $2 " total"}' || cat /proc/meminfo 2>/dev/null | awk '/MemTotal/ {tot=$2} /MemFree/ {free=$2} END{if(tot) printf "%.0fMB used",(tot-free)/1024; else print "n/a"}' 2>/dev/null || printf "n/a")

# Custom per-device info file (optional)
# If you create ~/.crypticx_info with lines like:
# PHONE_MODEL="iPhone 11 Pro"
# OS_VERSION="iOS 17.4"
# BATTERY="85%"
# then the script will display them.
CRYPTIC_INFO_FILE="$HOME/.crypticx_info"
PHONE_MODEL=""
OS_VERSION=""
BATTERY=""
if [ -f "$CRYPTIC_INFO_FILE" ]; then
  # shellcheck disable=SC1090
  . "$CRYPTIC_INFO_FILE" 2>/dev/null || true
fi

# If not set, try to infer minimal info from environment (best-effort)
[ -z "$PHONE_MODEL" ] && PHONE_MODEL="${DEVICE_MODEL:-unknown}"
[ -z "$OS_VERSION" ] && OS_VERSION="${PLATFORM_VERSION:-unknown}"
[ -z "$BATTERY" ] && BATTERY="n/a"

# ---------- Fake boot lines ----------
boot_lines=(
"Initializing CrypticX Environment..."
"Loading system modules..."
"Checking network interfaces..."
"Gathering system information..."
"Applying user profile settings..."
"Starting virtual daemon..."
"Decrypting environment variables..."
"Mounting /root/crypticx ..."
"System ready ✓"
)

# ---------- Start animation ----------
clear
printf "%b" "${GRAY}${BOLD}"
for line in "${boot_lines[@]}"; do
  type_line "$line" 0.02
  sleep 0.12
done
printf "%b" "${RESET}"
sleep 0.7
clear

# ---------- Show gathered device/system details ----------
printf "%b" "${GREEN}${BOLD}"
type_line "=== Device & System Info ===" 0.008
printf "%b" "${RESET}"

type_line "User: $USERNM" 0.008
type_line "Host: $HOSTN" 0.008
type_line "Date: $DATENOW" 0.008
type_line "Uptime: $UPTIME_INFO" 0.008
type_line "Kernel: $KERNEL ($ARCH)" 0.008
type_line "Shell: $SHELLX" 0.008
type_line "IP: $IP_ADDR" 0.008
type_line "Disk: $DISK_USAGE" 0.008
type_line "Memory: $MEM_INFO" 0.008

# Optional phone-specific lines (from ~/.crypticx_info if provided)
if [ -n "$PHONE_MODEL" ] && [ "$PHONE_MODEL" != "unknown" ]; then
  type_line "Phone Model: $PHONE_MODEL" 0.008
fi
if [ -n "$OS_VERSION" ] && [ "$OS_VERSION" != "unknown" ]; then
  type_line "OS Version: $OS_VERSION" 0.008
fi
type_line "Battery: $BATTERY" 0.008

printf "%b\n" "${YELLOW}"
sleep 0.2

# ---------- Banner ----------
cat <<'EOF'
 ██████╗██████╗ ██╗   ██╗ ██████╗ ████████╗██╗ ██████╗██╗  ██╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗██╔╝
██║     ██████╔╝ ╚████╔╝ ██║   ██║   ██║   ██║██║      ╚███╔╝ 
██║     ██╔══██╗  ╚██╔╝  ██║   ██║   ██║   ██║██║      ██╔██╗ 
╚██████╗██║  ██║   ██║   ╚██████╔╝   ██║   ██║╚██████╗██╔╝ ██╗
 ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝    ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝
EOF
printf "%b" "${RESET}"
type_line "WELCOME CRYPTICX," 0.01
type_line "JOINING DATE:- 07 August 2025" 0.01
type_line "JOINING TIME:- 07:49:47 AM" 0.01
printf "%s\n" "--------------------------------------------------"
