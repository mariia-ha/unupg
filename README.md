# Uncommon User Password Generator - UNUPG

## Overview

The **Uncommon User Password Generator** is a tool designed to create random, strong passwords while allowing users to evaluate and bypass traditional personal information commonly used in password creation. This is a "reverse tool" compared to [CUPP](https://github.com/Mebus/cupp), focusing on generating secure passwords that are completely unrelated to personal details.

---

## Features

- **Interactive Input:** Asks for commonly used personal information (e.g., pet's name, birthdate, etc.) to demonstrate how insecure such passwords might be.
- **Skip Option:** Users can skip specific questions if they don't want to provide information.
- **Strong Password Generation:** Produces random, strong passwords that are unrelated to personal information.
- **User Awareness:** Educates users about the risks of using personal details in passwords.

---

## Installation

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/mariia-ha/unupg.git
   ```
2. Navigate to the directory:
   ```bash
   cd unupg
   ```
3. Install dependencies:

   ```bash
   poetry install
   ```

---

## Usage

Run the application using:

```bash
poetry run python3 main.py
```

### Workflow

1. **Start the Tool:** You will be prompted with questions about personal information:

   - "What is your pet's name?"
   - "What is your favorite word or phrase?"
   - "What is your child's name?"

2. **Provide or Skip Information:**

   - Enter your answer or click enter to bypass the question.
   - The app ensures you acknowledge each prompt before moving forward.

3. **Generate Password:**

   - Once all questions are answered or skipped, the app will generate a random, strong password unrelated to the provided inputs.

---

## Motivation

Many people unknowingly create passwords based on personal information, making them vulnerable to attacks. The **Uncommon User Profile Generator** emphasizes the importance of strong, random passwords by contrasting user-provided personal details with unrelated secure outputs.
