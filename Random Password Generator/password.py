import random
import string
def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Creates a random password based on user's choices.
    
    Parameters:
    - length: How long the password should be (default is 12)
    - use_letters: Include letters? (True or False)
    - use_numbers: Include numbers? (True or False)
    - use_symbols: Include symbols? (True or False)
    
    Returns:
    - A password string
    """
    
    # Choose characters based on user's input
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_symbols else ''
    
    # Combine all selected characters
    all_chars = letters + numbers + symbols

    # If no options selected, show an error message
    if not all_chars:
        return "Please select at least one character type (letters, numbers, symbols)."
    
    # Pick random characters for the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def get_user_choices():
    """
    Ask the user what kind of password they want.
    Returns the length and character choices.
    """
    print(" Welcome to the Password Generator ")
    
    # Ask for password length
    while True:
        try:
            length = int(input("Enter password length (between 8 and 32): "))
            if 8 <= length <= 32:
                break
            print("Please enter a number between 8 and 32.")
        except ValueError:
            print("That's not a number. Try again.")
    
    # Ask for character types
    print("\nWhat should your password include?")
    letters = input("Include letters (a-z, A-Z)? (y/n): ").strip().lower() == 'y'
    numbers = input("Include numbers (0-9)? (y/n): ").strip().lower() == 'y'
    symbols = input("Include symbols (!@#$...)? (y/n): ").strip().lower() == 'y'
    
    return length, letters, numbers, symbols

def main():
    # Get user preferences
    length, letters, numbers, symbols = get_user_choices()
    
    # Generate password
    password = generate_password(length, letters, numbers, symbols)
    
    # Show result
    print("\nYour new password is:")
    print(password)

    # Try copying to clipboard
    try:
        import pyperclip
        pyperclip.copy(password)
        print("(Copied to clipboard )")
    except:
        print("(Tip: You can install clipboard support by running `pip install pyperclip`)")

# Run the program
if __name__ == "__main__":
    main()
