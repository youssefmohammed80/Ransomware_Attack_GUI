
# 🔒 Ransomware Simulation Attack

![Security Awareness](https://img.shields.io/badge/Security-Awareness-red?style=for-the-badge\&logo=hackaday)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Linux-Compatible-yellow?style=for-the-badge\&logo=linux)
![Educational](https://img.shields.io/badge/Use-Educational-green?style=for-the-badge\&logo=bookstack)

---

## ⚠️ Disclaimer

This attack is created **strictly for educational and awareness purposes only**. It simulates the behavior of a ransomware attack to demonstrate the **risks of downloading software from untrusted or pirated sources**. Do **NOT** misuse this attack for malicious purposes. The author is not responsible for any damages caused by misuse.

---

## 📝 Overview

This repository simulates a basic ransomware attack with a **GUI-based interface**. The purpose is to **educate** users about the dangers of ransomware and the importance of safe downloading habits.

### Main Components:

* **encrypt.py**: Encrypts files in the current directory and sends the encryption key to the attacker.
* **decrypt.py**: Decrypts the encrypted files using the key retrieved from the attacker.
* **receive_key.py**: A simple HTTP server running on the attacker machine to receive and store the encryption key.

---

## ⚙️ How It Works

1. The **attacker machine** must run the key receiver first to receive and store the encryption key.
2. The **encryptor** script encrypts all files in the working directory (except the scripts themselves) and sends the key to the attacker.
3. The **decryptor** script restores the files using the saved key.

---

## 🚀 Setup & Execution

### 1. Clone the Repository

```bash
git clone https://github.com/youssefmohammed80/Ransomware_Attack_GUI.git
cd Ransomware_Attack_GUI
```

### 2. Run the Key Receiver (on Attacker Machine)

On the **attacker machine** (Linux recommended), run:

```bash
python3 receive_key.py
```

This will start listening on port **8080** by default.

### 3. Configure Encryptor (on Victim Machine)

Edit **encrypt.py** and replace:

```python
SERVER_URL = "http://your-ip:8080/upload"
```

with the IP address of the **attacker machine**.

Example:

```python
SERVER_URL = "http://192.168.1.100:8080/upload"
```

### 4. Run Encryptor (on Victim Machine)

On the **victim simulation machine**, run:

```bash
python3 encrypt.py
```

All files in the directory will be encrypted.

### 5. Run Decryptor (on Victim Machine)

Once the key has been retrieved by the attacker, place the file `received_key.key` into the victim’s directory and run:

```bash
python3 decrypt.py
```

This will restore all encrypted files.

---

## 📌 Notes

* This is a **controlled simulation** only. Do not use on sensitive or personal data.
* Best used in a **virtual machine environment** for demonstrations.
* Teaches employees how **real ransomware** can lock files and why **safe downloading habits** are essential.

---

## 📂 Project Structure

```
.
├─ assets/
│  └─ screenshot-ui.png   # Your project screenshot
├─ ransomware_simulator.py   # The ransomware simulator script
├─ ransomware_sim_safe.py    # Safe, non-destructive version for simulation
├─ requirements.txt
└─ README.md                # This file
```

---

## 🔒 How the Ransomware Simulator Works

The simulator uses the **tkinter** GUI to present a "compromised" system and walk the user through encryption and decryption. It mimics the steps a real ransomware attack would take, but in a controlled environment.

### Key Features:

* **System Locking**: When the system is compromised, it simulates encrypting files with a **Fernet** key.
* **GUI Notification**: The GUI displays a **"SYSTEM COMPROMISED"** message, along with the encryption status.
* **Recovery Process**: A recovery key is required to decrypt files and restore them.
* **Network Exfiltration Simulation**: The encryption key is "sent" to a remote server via an HTTP POST request, which simulates data exfiltration.

---

## ⚙️ GUI Elements

* **Title**: "SYSTEM COMPROMISED" (changes to "SYSTEM RESTORED" on success).
* **Information**: Dynamic updates on system status and encryption.
* **Logs**: A scrolling text area for runtime logs and file status.
* **Key Entry**: A field to input the recovery key.
* **Decrypt Button**: To restore encrypted files.

---

## 🛡️ Safe Defaults & Recommendations

* **Set a safe default for `WEBHOOK_URL`:**

```python
WEBHOOK_URL = "DISABLED_FOR_SAFETY"
```

or use a local testing endpoint:

```python
WEBHOOK_URL = "http://127.0.0.1:5000/test"
```

* **Simulation Mode**: Implement a `--sim` mode that logs the intended actions but does **not** encrypt files.
* **CLI for Dry Run**: A `--dry-run` mode to check what files would be targeted without performing any actions.
* **Clear Warnings**: Ensure all users are aware that this is a simulation and cannot be used for malicious purposes.

---

## 📈 Defensive Notes

This simulator is also useful for **detection** and **defense** training:

* **Marker File Creation**: Files marked with `.encrypted_flag` can be used to detect ransomware activity.
* **Burst File Modifications**: Rapid changes in many files can be indicative of ransomware.
* **Outbound HTTP Requests**: Detecting unauthorized HTTP POST requests after encryption may help identify malicious exfiltration.
* **Alerting GUI**: The unexpected appearance of a ransom message on the screen is a clear indication of a possible attack.

---

## 📜 License & Contributions

This repository is licensed under the **MIT License**. Contributions are welcome as long as they follow the educational and defensive usage guidelines.

---

### Final Notes:

* **This README** serves to guide users in **simulating ransomware attacks** safely and for educational purposes.
* **Never deploy real encryption** on live systems.
* Always use isolated environments (e.g., **VMs**) for testing.

---

### If you need help with:

1. Creating a **non-destructive version** of the script.
2. Replacing the `WEBHOOK_URL` with local testing endpoints.
3. Translating the README or creating a **one-page summary**.

Let me know which follow-up you'd prefer!


