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

# OUTPUT 

1. **MAIN MENU**

 Displays the main options of the Penetration Testing Toolkit:

- `Port Scanner`: Scans for open ports on a target.

- `Brute Force Simulator`: Simulates a brute-force attack on a given username.

- `Exit`: Closes the program.  

![Image](https://github.com/user-attachments/assets/9c13285a-1bc2-42ed-b04b-21ea6b7ba110)

2. **PORT SCANNER OUTPUT**

- Target: `127.0.0.1` (localhost)

- Result: Found two open ports –

  - Port 135 (used for RPC)

  - Port 445 (used for SMB file sharing)   

![Image](https://github.com/user-attachments/assets/8ef01f93-2a6d-4253-8358-4d3cebf72ba6)   

4. **BRUTE FORCE SIMULATOR OUTPUT**

- Target User: `admin`

- Action: Initiated a simulated brute-force attack, trying different passwords for the `admin` 
  user.

 ![Image](https://github.com/user-attachments/assets/b163afa1-8a27-415e-b1bc-93a91d1bdc89)  

# WHAT I LEARNED

Through this project, I gained hands-on experience with:

- Python scripting for cybersecurity purposes

- Modular programming

- Network sockets and TCP port scanning

- Basic brute-force attack logic

- Structuring a command-line interface

- Git and GitHub version control

# NOTE

This project is created for educational purposes. Please use it ethically and responsibly.

# CONCLUSION

This project taught me the basics of how penetration testing tools are structured and used. I learned how to write Python scripts that interact with networks and simulate brute-force attacks in a controlled and safe way. It improved my programming skills, my understanding of cybersecurity concepts, and how to create clean, modular code.

By working on this toolkit, I also understood how simple tools used by ethical hackers can reveal weak points in a system such as open ports or weak passwords. I feel more confident in my journey to becoming a Cyber Threat Intelligence Analyst or an Ethical Hacker.

Thanks to my internship mentor and program for giving me the opportunity to build this toolkit. It has been a great learning experience. This is just the beginning of my journey into ethical hacking and cybersecurity, and I plan to keep learning, improving this toolkit, and building more advanced tools in the future.
