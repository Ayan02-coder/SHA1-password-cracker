# SHA1-password-cracker

## Overview

This project is a Python-based password cracker designed to find passwords from their SHA-1 hashes. It uses a list of commonly used passwords and can optionally apply known salts to increase its effectiveness. This project demonstrates basic password cracking techniques and hashing in Python 2.7.

## Features

- **Password Cracking:** Attempts to crack SHA-1 hashed passwords using a list of the top 10,000 passwords.
- **Salting Option:** Can use a list of known salts to prepend and append to passwords before hashing to enhance cracking.
- **User Input:** Allows users to input hashed passwords and specify whether to use salts.

## Requirements

- Python 2.7
- `top-10000-passwords.txt`: A file containing the top 10,000 commonly used passwords (one per line).
- `known-salts.txt`: A file containing known salts (one per line), used if salting is enabled.

## Installation

1. Ensure Python 2.7 is installed on your system.
2. Place the `top-10000-passwords.txt` and `known-salts.txt` files in the same directory as the script files.

## Usage

### Running the Main Script

To run the main script and perform predefined tests as well as allow user input, execute:

```bash
python main.py
```
### Testing

To run unit tests to validate the functionality of the password cracker, use:

```bash
python test_module.py
```

## Code Description
- `password_cracker.py `: Contains the hash_password and crack_password functions. hash_password hashes a given password using SHA-1, and crack_password attempts to match a hashed password against a list of known passwords, with optional salting.
- `main.py`: Runs predefined tests, allows user input for password cracking, and executes unit tests.
- `test_module.py`: Contains unit tests to ensure the correctness of the password-cracking functions.
## Example
Here's how to use the password cracker:

1. Run Predefined Tests:

```bash
python main.py
```

2. User Input Example:

```bash
python main.py
```
When prompted:
```plaintext
Enter the SHA-1 hashed password: 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
Use salts? (yes/no): no
```
The output will be:

```plaintext
Cracked password for hash '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8' with salts=False: password
```
