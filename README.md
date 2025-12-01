# 🔍 Advanced Multi-Threaded Port Scanner

A fast and efficient Python-based **Port Scanner** that scans a given IP address for open ports using **multi-threading** for high performance.  
This tool is useful for learning networking concepts, ethical testing, and cybersecurity fundamentals.

---

## 🚀 Features
- User inputs **only the target IP address**
- Scans **any port range** (1–65535)
- **Multi-threaded** → Extremely fast
- Detects and prints **OPEN** ports
- Clean error handling
- Beginner-friendly and final-sem-ready

---

## 🧠 How It Works
- Uses Python's `socket` module to attempt connections.
- Each port is scanned in a separate **thread**, improving speed.
- Successful connection → **OPEN**
- Connection refused → **CLOSED**

---

## 📌 Usage

### 1️⃣ Run the script:
```bash
python advanced_port_scanner.py
