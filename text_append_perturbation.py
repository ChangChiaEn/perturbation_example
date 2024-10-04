import random
import string

class Malware:
    def __init__(self, code):
        """
        Initialize the Malware instance with the original code.

        Args:
        - code (str): The initial malware code.
        """
        self.original_code = code  # Store the original code for later comparison
        self.code = code           # The working copy of the code that will be modified

    def append_perturbation(self, perturbation):
        """
        Append a non-malicious perturbation text to the malware code.

        Args:
        - perturbation (str): The perturbation text to be appended.
        """
        self.code += perturbation

    def insert_random_text(self, length):
        """
        Insert random non-malicious text into the malware code.

        Args:
        - length (int): The length of the random text to be inserted.
        """
        # Generate a random string of specified length
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        # Choose a random position in the code to insert the text
        position = random.randint(0, len(self.code))
        # Insert the random text at the chosen position
        self.code = self.code[:position] + random_text + self.code[position:]

    def insert_pattern_text(self, repeat):
        """
        Insert a specific pattern text into the text.

        Args:
        - repeat (int): The number of times the pattern is repeated.
        """
        # Define various patterns for perturbation
        patterns = {
            'NOP': 'NOP',
            'ZERO': '0',
            'ONE': '1',
            'ASCII': string.ascii_letters,
            'NUM': string.digits
        }
        # Randomly choose one of the pattern types
        pattern_type = random.choice(list(patterns.keys()))
        # Create the pattern text by repeating the chosen pattern
        pattern = patterns[pattern_type] * repeat
        # Choose a random position in the code to insert the pattern
        position = random.randint(0, len(self.code))
        # Insert the pattern text at the chosen position
        self.code = self.code[:position] + pattern + self.code[position:]

    def get_modified_code(self):
        """
        Return the modified text.

        Returns:
        - str: The modified text.
        """
        return self.code

# Sample malware code for demonstration purposes
sample_malware_code = "This is a sample text."

# Create a Malware instance with the sample code
malware = Malware(sample_malware_code)

# Apply different perturbations
malware.append_perturbation("This is a harmless addition.")  # Append a harmless line
malware.insert_random_text(10)  # Insert a random text of 10 characters
malware.insert_pattern_text(5)  # Insert a pattern, randomly chosen, repeated 5 times

# Print the original and modified malware code for comparison
print("Original text:\n", malware.original_code)
print("\nModified text:\n", malware.get_modified_code())

while True:
    user_input = input("\nEnter k and Enter to continue, or just q to exit: ")
    if user_input == "k":
        print("Continuing...")
        print("Original text:\n", malware.original_code)
        print("\nModified text:\n", malware.get_modified_code())
    elif user_input == "q":
        print("Exiting...")
        exit()
    else:
        print("Invalid input. Please try again.")