import secrets
import string
from english_words import get_english_words_set
from termcolor import colored
import pyfiglet


def gather_personal_information():
    """
    Collect non-sensitive personal information through command-line prompts.

    This function prompts the user for various personal details across multiple
    categories including personal, partner, child, and additional information.
    For privacy protection, all fields are optional and can be skipped by
    pressing Enter.

    Categories of information collected:
        - Personal: Basic personal details
        - Partner: Partner's information
        - Child: Child's information
        - Additional: Miscellaneous information like favorite phrases

    Returns:
        dict: A dictionary containing field names as keys and user responses
            as values. Empty responses are stored as empty strings.
    """
    print(
        colored(
            "Please provide the following details. (PRESS ENTER to SKIP ALL FIELDS FOR PRIVACY.)",
            color="cyan",
            attrs=["bold"],
        )
    )

    personal_data_fields = [
        "First Name",
        "Last Name",
        "Nickname",
        "Day of Birth (DD)",
        "Month of Birth (MM)",
        "Year of Birth",
    ]

    information_categories = {
        "Personal": personal_data_fields,
        "Partner": [f"Partner's {field}" for field in personal_data_fields],
        "Child": [f"Child's {field}" for field in personal_data_fields],
        "Additional": ["Favorite Word or Phrase", "Pet Name", "Company Name"],
    }

    collected_information = {}

    for category_name, input_fields in information_categories.items():
        print(f"\n{colored(category_name + ' Information:', 'green')}")
        for field_name in input_fields:
            while True:
                user_response = input(colored(f"  {field_name}: ", "yellow")).strip()
                if user_response:
                    print(
                        colored(
                            "  Warning: Do not enter sensitive information. Please press Enter to skip.",
                            "red",
                            attrs=["bold"],
                        )
                    )
                else:
                    collected_information[field_name] = user_response
                    break

    print(colored("\nThank you! Proceeding to password generation...", "cyan"))
    return collected_information


def replace_random_letter(word):
    """
    Replace a random letter in the word with a random lowercase letter.

    Args:
        word (str): The input word to modify
        random_generator: Random number generator instance

    Returns:
        str: Word with one random letter replaced, or empty string if input is empty
    """
    if not word:
        return word

    letter_position = secrets.randbelow(len(word))
    random_lowercase = secrets.choice(string.ascii_lowercase)

    return word[:letter_position] + random_lowercase + word[letter_position + 1 :]


def get_random_word_with_constraints(
    available_words,
    minimum_length=4,
    maximum_length=8,
    should_capitalize=False,
):
    """
    Select a random word within length constraints and optionally modify it.

    Args:
        available_words (set): Collection of words to choose from
        random_generator: Random number generator instance
        minimum_length (int): Minimum allowed word length
        maximum_length (int): Maximum allowed word length
        should_capitalize (bool): Whether to capitalize the final word

    Returns:
        str: Selected and potentially modified word
    """
    words_matching_length_criteria = [
        word
        for word in available_words
        if minimum_length <= len(word) <= maximum_length
    ]

    selected_word = secrets.choice(words_matching_length_criteria)
    modified_word = replace_random_letter(selected_word)

    return modified_word.capitalize() if should_capitalize else modified_word


def generate_secure_number(digits=3):
    """
    Generate a cryptographically secure random number with specified number of digits.

    Args:
        digits (int): Number of digits in the generated number

    Returns:
        str: String representation of the random number
    """
    return str(secrets.randbelow(10**digits)).zfill(digits)


def generate_password():
    """
    Generate a secure password containing two words, two numbers, and a special character
    in random order using a single random number generator for consistency.

    Returns:
        str: A randomly generated password following the specified format
    """
    dictionary_words = get_english_words_set(["web2"], lower=True)
    allowed_special_characters = "!@#$%^&*()-_=+[]{}|;:<>,.?/"

    password_parts = [
        get_random_word_with_constraints(dictionary_words, should_capitalize=True),
        get_random_word_with_constraints(dictionary_words),
        generate_secure_number(),
        generate_secure_number(),
        secrets.choice(allowed_special_characters),
    ]

    shuffled_parts = []
    remaining_parts = password_parts.copy()

    for _ in range(len(password_parts)):
        index = secrets.randbelow(len(remaining_parts))
        shuffled_parts.append(remaining_parts.pop(index))

    return "".join(shuffled_parts)


def main():
    app_banner = pyfiglet.figlet_format("unupg", font="roman")
    print(colored(app_banner, "yellow"))
    gather_personal_information()
    print(colored("\nGenerating password...", "cyan"))
    password = generate_password()
    print(
        colored("Generated password: ", "green", attrs=["bold"])
        + colored(password, "white", attrs=["bold"])
    )


if __name__ == "__main__":
    main()
