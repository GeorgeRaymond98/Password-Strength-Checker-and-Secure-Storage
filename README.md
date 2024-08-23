# 🔒 Password Strength Checker & Encryption Tool

Welcome to the **Password Strength Checker & Encryption Tool**! 🚀 This Python script is your go-to solution for ensuring your passwords are not only strong but also securely encrypted. Whether you're looking to enhance your personal security practices or demonstrate your cybersecurity skills, this tool has got you covered.

## 🌟 Features

- 🔍 **Password Strength Checker**: Assess your password's strength with immediate feedback based on length, complexity, and the inclusion of special characters.
- 🛡️ **Secure Password Encryption**: Protect your sensitive data using state-of-the-art symmetric encryption with the `cryptography` library.
- 🧑‍💻 **User-Friendly Interface**: Input your password securely with `getpass`, ensuring it stays hidden from prying eyes.

## 🛠️ How It Works

1. **Password Strength Evaluation**:
   - The script evaluates your password based on these five critical criteria:
     - **Length**: Minimum of 8 characters.
     - **Numeric Digits**: Includes at least one number.
     - **Uppercase Letters**: Contains at least one uppercase letter.
     - **Lowercase Letters**: Contains at least one lowercase letter.
     - **Special Characters**: Includes at least one special character (`!@#$%^&*()-_`).
   - Your password is scored out of 5 based on how many of these criteria it meets.

2. **Encryption Process**:
   - A secure encryption key is generated.
   - The password is encrypted using the **Fernet** symmetric encryption algorithm.
   - The encrypted password is output as a secure byte string, ready for safe storage.

## 📦 Prerequisites

Ensure you have Python 3.x installed, along with the `cryptography` library:

```bash
pip install cryptography
```

## 🛠️ Usage

1. Clone the repository or download the script.
    ```bash
    ```

2. Run the script using Python:
    ```bash
   python password_encryption.py
    ```

3.Enter your password when prompted. The script will evaluate the strength of your password and encrypt it for secure storage.

## 📝 Example Output

Enter a password: ********
Password strength: 4/5
Encrypted password: b'gAAAAABiAdo_kjTeDgt8ZlE-4Ibs_fXeQx6pXQNYxHzv0y4LzhKLcy-5HQTrZ9cU1y5oZ1Ov8SPkktEGAOK7vZ8SBvApVZdBpg=='


## 🧩 How It Works

1. Enter a password: ********
2. Password strength: 4/5
3. Encrypted password: b'gAAAAABiAdo_kjTeDgt8ZlE-4Ibs_fXeQx6pXQNYxHzv0y4LzhKLcy-5HQTrZ9cU1y5oZ1Ov8SPkktEGAOK7vZ8SBvApVZdBpg=='

## 🎨  Why This Tool?
This tool is perfect for:

1. Demonstrating your understanding of password security in interviews.
2. Enhancing your own security practices by evaluating and encrypting your passwords.
3. Learning the basics of encryption and password management in Python.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This `README.md` is designed to be both informative and visually appealing.

---

Made with ❤️ by [George Raymond]([https://github.com/your-username](https://github.com/GeorgeRaymond98))
