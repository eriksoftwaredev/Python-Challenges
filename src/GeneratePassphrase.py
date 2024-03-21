import secrets

def generate_passphrase(num_phrases):
    phrases = [
        "apple", "banana", "orange", "grape", "pineapple", 
        "watermelon", "strawberry", "blueberry", "kiwi", "mango"
    ]
    passphrase = " ".join(secrets.choice(phrases) for _ in range(num_phrases))
    return passphrase

# Test the function:
num_phrases = int(input("Enter the number of phrases for the passphrase: "))
passphrase = generate_passphrase(num_phrases)
print("Generated passphrase:", passphrase)
