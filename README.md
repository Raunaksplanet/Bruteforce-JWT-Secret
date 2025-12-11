# Bruteforce-JWT-Secret

A simple Python script to brute-force the secret key of a JWT using a wordlist.

## Features

- Supports JWTs signed with HS256
- Reads secrets from a custom wordlist
- Prints the decoded payload if the key is found

## Requirements

- Python 3.x
- PyJWT (`pip install PyJWT`)

## Usage

```bash
python3 main.py
