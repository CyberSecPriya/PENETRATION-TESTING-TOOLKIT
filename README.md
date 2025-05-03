# PENETRATION-TESTING-TOOLKIT

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : PRIYA BABARE

*INTERN ID* : CT04DA834 

*DOMAIN* : CYBER  SECURITY & ETHICAL  HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

# DESCRIPTION

This Penetration Testing Toolkit is a Python-based project developed as part of a cybersecurity internship. The main aim of this toolkit is to help beginners understand how penetration testing works using simple, educational simulations. It consists of two main modules: a Port Scanner and a Brute Force Password Simulator. These tools are not meant for real hacking, but to demonstrate how ethical hackers think and test systems for vulnerabilities in a legal and responsible way.

The toolkit is built using Python and works entirely in the terminal. The port scanner scans the most common 1024 ports on a given IP address or domain to find which ones are open. Open ports can reveal information about running services and possible entry points. The brute-force simulator attempts to "guess" a password from a given wordlist and shows how weak passwords can be cracked using this technique.

The entire tool is modular. Each function is written in its own file (`port_scanner.py`, `brute_forcer.py`) and combined together in `main.py`. This project helped me gain hands-on experience in Python scripting, understanding penetration testing basics, and organizing clean, understandable code.

# FEATURES

The toolkit currently includes two main modules:

1. **Port Scanner**  
   Scans common TCP ports (1–1024) on a given IP address or domain to identify open ports.

2. **Brute Force Simulator**  
   Simulates a password brute-force attack by trying a list of potential passwords (wordlist) against a target username.

# FILES INCLUDED

- `main.py` → The main program that connects all modules and provides a menu-based interface.
- `port_scanner.py` → Contains the code for scanning open ports on a given host.
- `brute_forcer.py` → Contains the brute-force simulation function.

# HOW IT RUNS

To run this toolkit, follow these steps:

1. Make sure Python is installed on your system (python --version).

2. Clone the repository or download all three .py files into a folder.

3. Open a terminal in that folder and run the main.py file: **python main.py**

4. You will see a menu with three choices:

- Port Scanner

- Brute Force Simulator

- Exit

5. Enter the number of your choice to start using the tool.

Make sure you have internet access if you are scanning a domain name, and only use this tool on networks you have permission to test.
  
