from port_scanner import scan_ports  # Import the port scanner
from brute_forcer import brute_force_simulation

def main():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Brute Force Simulator")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Call the port scanner function
            target = input("Enter IP or domain to scan: ")
            scan_ports(target)

        elif choice == "2":
            username = input("Enter username to attack: ")
            wordlist = ["admin", "123456", "letmein", "password123", "qwerty"]
            brute_force_simulation(username, wordlist)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
