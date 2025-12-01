🔍 Advanced Multi-Threaded Networking Port Scanner

A fast and efficient Python-based Networking Port Scanner that scans a given IP address for open ports using multi-threading for high performance.
This tool is ideal for learning networking concepts, ethical security testing, and understanding port communication.

🚀 Features

User inputs only the target IP address

Scans any port range (1–65535)

Multi-threaded → extremely fast output

Prints only OPEN ports

Clean and simple error handling

Final-semester–ready project

🧠 How It Works

Uses Python’s built-in socket module to test port connections

Each port runs in a separate thread → massive speed improvement

If a connection succeeds → Port OPEN

If it fails → port is closed (not printed)

📂 Project Structure
Networking-Port-Scanner/
│── Networking Port Scanner.py
│── README.md
│── requirements.txt
│── .gitignore
│── output_example.txt

🛠 Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/networking-port-scanner.git

2️⃣ Navigate into the folder
cd networking-port-scanner

3️⃣ Run the script
python "Networking Port Scanner.py"

📌 Usage Example

When the program starts, it asks:

Enter the IP address to scan: 192.168.1.10
Enter starting port: 1
Enter ending port: 1000

📤 Example Output
========================================================
            ⚡ Advanced Multi-Threaded Port Scanner
========================================================

Enter the IP address to scan: 192.168.1.10
Enter starting port: 1
Enter ending port: 1000

Scanning 192.168.1.10 from port 1 to 1000...

Port 21  ➜  OPEN
Port 22  ➜  OPEN
Port 80  ➜  OPEN
Port 443 ➜  OPEN

Scan complete ✔
========================================================


👉 Full output stored in: output_example.txt

🧾 Requirements

Your program uses only built-in Python modules, so no pip installs are required.

requirements.txt should contain:

# No external dependencies required

⚠️ Legal & Ethical Notice

This tool is intended for learning and authorized testing only.
Do NOT scan networks without permission.

⭐ Author

Nayanika – CSE Student | Networking & Cybersecurity Enthusiast
