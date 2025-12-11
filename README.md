# Bruteforce‑JWT‑Secret

A simple Python tool that brute‑forces the secret key of an HMAC‑signed JWT using a wordlist. Supports HS256, HS384, and HS512.

## Features

* Manually computes HMAC signatures
* Supports URL‑safe base64 handling
* Works with any custom wordlist
* Status updates every 1000 attempts

---

## Example JWT

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCJ9.UF3opocnYSRNeqS5Csnan8AdqtLTrzuxvoXz-DBzC40
```

### Example Wordlist

```
admin
test
secret
mysecret123
password
qwerty
123456
letmein
```

---

## Usage

Save the JWT in a file (`jwt_token.txt`) and the wordlist in another file (`Wordlist1`).

Run:

```
python3 main.py -m jwt_token.txt -s Wordlist1
```
