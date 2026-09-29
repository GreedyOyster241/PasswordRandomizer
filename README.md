# Password Randomizer

A simple password generator built with Python and Streamlit. This application allows users to generate random passwords based on customizable character types and password lengths.

## Features

* **Uppercase Letters:** Include uppercase letters (A–Z).
* **Lowercase Letters:** Include lowercase letters (a–z).
* **Digits:** Include numbers (0–9).
* **Punctuation:** Include special characters.
* **Custom Password Length:** Choose a password length between 8 and 32 characters.
* **Saved Passwords:** Automatically save generated passwords during the current session.
* **Clear Saved Passwords:** Remove all saved passwords with a single button.

## Technologies Used

* Python
* Streamlit

## Installation

1. Clone or download this repository.
2. Install the required dependencies:

   ```bash
   pip install streamlit pandas
   ```

## Usage

1. Run the application:

   ```bash
   streamlit run main.py
   ```

   Replace `main.py` with the name of your Python file if it is different.

2. Select the character types you want to include.

3. Choose your desired password length.

4. Click **Generate Password** to create a random password.

5. View your generated password and access previously generated passwords in the **Saved Passwords** section.

6. Click **Clear Saved Passwords** to remove all saved passwords.

## How It Works

The application uses Python's `random` module to generate passwords from the selected character types.

Streamlit's Session State stores generated passwords during the current session, allowing users to access them even when the application reruns.

## Notes

* Saved passwords are stored in memory and are not permanently saved to a file or database.
* Saved passwords are cleared when the session ends or when the user clears them manually.
* This project is intended for educational purposes.
