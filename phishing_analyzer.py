print("PHISHING AWARENESS ANALYZER")

msg = input("Enter Email or Message to analyze: ")

msgLower = msg.lower()

flags = 0

print("PHISHING ANALYSIS REPORT")

if "urgent" in msgLower:
    print("Urgent language detected")
    flags = flags + 1

if "password" in msgLower:
    print("Password request detected")
    flags = flags + 1

if "otp" in msgLower:
    print("OTP request detected")
    flags = flags + 1

if "bank" in msgLower:
    print("Banking information mentioned")
    flags = flags + 1

if "http://" in msgLower or "https://" in msgLower:
    print("Link detected")
    flags = flags + 1

print("Total Red Flags Found:", flags)

if flags >= 4:
    print("Risk Level: HIGH")
    print("Warning: This message appears to be a phishing attempt.")

elif flags >= 2:
    print("Risk Level: MEDIUM")
    print("Caution: This message contains suspicious elements.")

else:
    print("Risk Level: LOW")
    print("No major phishing indicators detected.")