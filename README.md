
# Classical & Modern Cryptography in Python

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Status-Active-success.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)]()

A hands-on collection of Python implementations for **classical** and **modern** cryptographic algorithms.  
Each project is written with clarity for learners while preserving accurate, working code.


## Why This Repository?

Cryptography is at the core of secure systems — from protecting passwords to enabling secure communication across the internet.  
This repository demonstrates **how common algorithms work** and **why they matter** by implementing them step by step in Python.

Algorithms included:

- **Hill Cipher** — classical, matrix-based substitution
- **Caesar Cipher** — classical, simple shift cipher
- **RSA** — modern, asymmetric encryption
- **AES** — modern, symmetric encryption

Use this repository to **learn**, **experiment**, or **adapt** for small-scale projects.

## Repository Structure

```

cryptography-python/
│
├── hill\_cipher/
│   ├── hill\_cipher.py
│   └── README.md
│
├── caesar\_cipher/
│   ├── caesar\_cipher.py
│   └── README.md
│
├── rsa\_password/
│   ├── rsa\_password.py
│   └── README.md
│
├── aes\_password/
│   ├── aes\_password.py
│   └── README.md
│
└── main\_README.md   # This document



## Algorithms Explained

### 1. Hill Cipher
- **What**: A **polygraphic substitution cipher** that encrypts blocks of letters using **matrix multiplication** and modular arithmetic.
- **Why**: Shows how **linear algebra** can be applied to cryptography; historically important in early 20th-century ciphers.
- **Key Points**:
  - Works on **pairs** or **triplets** of letters.
  - Requires an **invertible matrix** as the encryption key.
  - Decryption uses the **inverse matrix modulo 26**.

> Example: Encrypting “HELLO” with  
> key `[[3,3],[2,5]]` produces ciphertext such as `TFJJZ`.


### 2. Caesar Cipher
- **What**: A **monoalphabetic cipher** that shifts letters by a fixed number in the alphabet.
- **Why**: One of the earliest and simplest ciphers; useful for **introducing substitution** and modular arithmetic concepts.
- **Key Points**:
  - Fixed shift (often 3).
  - Easy to break but perfect for **demonstration**.
  - Basis for understanding **frequency analysis**.

---

### 3. RSA (Public-Key Cryptography)
- **What**: A modern **asymmetric algorithm** using **two keys**:
  - **Public Key** for encryption
  - **Private Key** for decryption
- **Why**: RSA secures data over insecure channels without exchanging a shared secret; fundamental to HTTPS, digital signatures, and more.
- **Key Points**:
  - Relies on the difficulty of factoring **large prime numbers**.
  - Forms the backbone of **secure key exchange** on the web.
  - Encrypts sensitive strings (like passwords) safely.

> Example: Encrypting `Instagram@123` produces unreadable bytes.  
> Only the holder of the **private key** can recover the original password.

---

### 4. AES (Advanced Encryption Standard)
- **What**: A **symmetric** block cipher that encrypts data using the **same key** for encryption and decryption.
- **Why**: AES is the **industry standard** for securing sensitive data (banking, Wi-Fi, VPNs, file storage).
- **Key Points**:
  - Implements **AES-128** here (128-bit keys).
  - Uses **EAX mode** for authenticated encryption.
  - Protects against tampering and ensures confidentiality.

> AES is far stronger than classical ciphers and forms the core of many secure systems, including disk encryption, encrypted messaging, and cloud storage.

---

## Getting Started

### Installation
```bash
git clone https://github.com/yourusername/cryptography-python.git
cd cryptography-python
pip install -r requirements.txt
````

If requirements are separate per project:

```bash
pip install numpy pycryptodome
```

### Running an Algorithm

```bash
cd hill_cipher
python hill_cipher.py
```

---

## Example: Hill Cipher

```
Plaintext : HELLO
Ciphertext: TFJJZ
```

---

## Educational Focus

* Demonstrates **core principles** behind both classical and modern cryptography.
* Written to be **clear, documented, and modifiable**.
* Suitable for **students**, **security beginners**, and anyone curious about **how ciphers work**.

---

## Roadmap

* [ ] Implement **AES-256**
* [ ] Add **hybrid RSA-AES** demonstration
* [ ] Provide **unit tests** for each algorithm
* [ ] Expand into **hashing** (SHA-256, SHA-3)

---

## License

MIT License — free for personal, academic, or commercial use.

---

## References

* Bruce Schneier, *Applied Cryptography*
* William Stallings, *Cryptography and Network Security*
* [NIST AES Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)

```

---


