import random
import string
passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

letter_replacement = {}
all_replacement = set()

for i in range(5):
    while True:
        letter = input(f"Enter a lowercase {i+1}: ")
        if len(letter) == 1 and letter in string.ascii_lowercase :
            if letter not in letter_replacement:
                letter_replacement[letter] = []
                break
            else:
                print(f"You've already chosen '{letter}'. Please choose a different letter.")
        else:
            print("Please enter a single lowercase letter.")

    for j in range(3):
        while True:
            replacement = input(f"Enter a replacement {j+1}: ")
            if len(replacement) == 1 and replacement not in all_replacement :
                letter_replacement[letter].append(replacement)
                all_replacement.add(replacement)
                break
            else:
                print("Please enter a single character that hasn't been used before.")

processed_passwords = []

for password in passwords:
    processed_password = ""
    for char in password:
        if char in letter_replacement:
            processed_password += random.choice(letter_replacement[char])
        else:
            processed_password += char
    processed_passwords.append(processed_password)

categorized_passwords = {"strong": [], "weak": []}

for password in processed_passwords:
    replaced_count = 0
    for char in password:
        if char in all_replacement:
            replaced_count += 1

    if replaced_count > 4:
        categorized_passwords["strong"].append(password)
    else:
        categorized_passwords["weak"].append(password)

print("\nGenerated Passwords:")
print("STRONG PASSWORDS:")
for password in categorized_passwords["strong"]:
    print(password)

print("WEAK PASSWORDS:")
for password in categorized_passwords["weak"]:
    print(password)

    special_chars = set('!@#$%^&*()_+-={}[]|\\:;"\'<>,.?/')
    categorized_passwords_bonus = {"strong": [], "weak": []}

    for password in processed_passwords:
        special_count = sum(1 for char in password if char in special_chars)
        if special_count > 4:
            categorized_passwords_bonus["strong"].append(password)
        else:
            categorized_passwords_bonus["weak"].append(password)

    print("\nBonus - Categorized by Special Characters:")
    print("STRONG PASSWORDS:")
    for password in categorized_passwords_bonus["strong"]:
        print(password)

    print("WEAK PASSWORDS:")
    for password in categorized_passwords_bonus["weak"]:
        print(password)
