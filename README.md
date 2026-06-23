# Phishing Awareness Analysis

## Project Description

This project analyzes emails and messages to identify potential phishing attempts.

The program searches for common phishing indicators such as urgent language, password requests, OTP requests, banking-related content, and suspicious links.

## Features

* Detects phishing indicators
* Identifies suspicious links
* Calculates total red flags
* Classifies risk level as Low, Medium, or High
* Provides security warnings

## Technologies Used

* Python 3
* VS Code

## How to Run

1. Open terminal.
2. Run:

```bash
python phishing_analyzer.py
```

3. Enter an email or message for analysis.

## Sample Output

```text
PHISHING AWARENESS ANALYZER

Enter Email or Message to analyze:
URGENT! Your bank account will be blocked. Click http://fakebank.com and enter your password immediately.

PHISHING ANALYSIS REPORT

Urgent language detected
Password request detected
Banking information mentioned
Link detected

Total Red Flags Found: 4

Risk Level: HIGH
Warning: This message appears to be a phishing attempt.
```

## Author

Kinza Noor
