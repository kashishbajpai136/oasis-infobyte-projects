import random
import string

print("🔐 Password Generator")

length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

characters = ""

if use_letters:
    characters += string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("❌ Please select at least one character type.")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print("✅ Generated Password:", password)