import time

def brute_force_simulation(username, wordlist):
    print(f"[+] Starting brute-force attack for user: {username}")

    for password in wordlist:
        print(f"Trying password: {password}")  # <-- This prints each try
        time.sleep(0.01)
        if password == "password123":
            print(f"[SUCCESS] Password found: {password}")
            return password

    print("[FAILED] Password not found in wordlist.")
    return None
