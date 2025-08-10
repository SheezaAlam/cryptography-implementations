
# 🔐 AES Password Encryption & Decryption in Python

## 📌 Overview

This project demonstrates **AES-128 encryption** to securely store sensitive information — in this case, a fun example:

```
IGoToTheGym@7pm
```

The same method can be applied to **social media passwords, WiFi keys, API tokens,** or any sensitive string you need to keep private.

> Even if an attacker steals the encrypted data, without the **exact key** and **nonce**, it’s useless.

---

## 🚀 Features

* **AES-128 in EAX mode** (Authenticated Encryption)
* **Secure random key generation**
* **Base64 encoding** for safe storage/transmission
* Simple **Python implementation** with `pycryptodome`

---

## 🛠 Installation

```bash
pip install pycryptodome
```

---

## 🧠 How It Works

1. **Generate Key** → 16 bytes (128 bits) of secure random data.
2. **EAX Mode** → Provides both encryption & authentication.
3. **Encrypt** → Password → Ciphertext + Authentication Tag.
4. **Decrypt** → Requires **exact** Key + Nonce.

---


## 🎯 Future Improvements

* Add **file encryption** (PDF, TXT, Images)
* Implement **AES-256**
* Store & retrieve keys from **secure key vaults**
* Create **CLI tool** for quick encryption tasks

---

## 📜 Caesar Cipher Tool

A simple **Python-based Caesar Cipher** implementation with **encryption** and **decryption** options.
Uses a fixed **key of 3** and wraps around the alphabet (A–Z, a–z).
Perfect for learning basic cryptography concepts.

---

### ✨ Features

* **Encrypt & Decrypt** messages with ease
* Fixed shift key: **3**
* Handles **uppercase** and **lowercase** letters
* Preserves spaces, numbers, and punctuation
* Wraps around alphabet automatically (Z → C)

---

### 📂 Project Structure

```
caesar_cipher.py   # Main Python script
README.md          # Documentation
```

---

### 🚀 How to Run

#### 1️⃣ Clone or Download

Download the file or clone the repository:

```bash
git clone https://github.com/yourusername/caesar-cipher.git
cd caesar-cipher
```

#### 2️⃣ Run the script

```bash
python caesar_cipher.py
```

If `python` doesn’t work, use:

```bash
python3 caesar_cipher.py
```

---

### 🖥 Example Run

```
=================================
       Caesar Cipher Tool        
=================================
Choose an option:
1. Encrypt a message
2. Decrypt a message
Enter 1 or 2: 1
Enter your message: HELLO WORLD

Result:
KHOOR ZRUOG
```

---

### 📖 How It Works

The Caesar Cipher shifts each letter by a fixed number (**key**) through the alphabet.

```python
shifted = (ord(char) - base + key) % 26
```

* `ord(char)` → Get ASCII code of the character
* `base` → ASCII code of 'A' or 'a' (depending on case)
* Subtract `base` to get **0–25 position** in alphabet
* Add `key` to shift
* `% 26` ensures wrap-around (e.g., Z → C)

---

### 🛠 Requirements

* Python **3.x** installed

---

### 📜 License

This project is open-source under the **MIT License**.

