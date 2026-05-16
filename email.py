import re

print("===== EMAIL RISK ANALYZER =====\n")

email = input("Paste Email Content:\n").lower()

risk_score = 0
reasons = []

# Suspicious urgent words
urgent_words = [
    "urgent", "immediately", "act now",
    "verify now", "limited time", "asap"
]

# Sensitive information requests
sensitive_words = [
    "password", "otp", "credit card",
    "bank details", "cvv", "pin"
]

# Threatening / scam words
scam_words = [
    "account suspended",
    "won prize",
    "claim reward",
    "lottery",
    "free money"
]

# Check urgent words
for word in urgent_words:
    if word in email:
        risk_score += 2
        reasons.append(f"Urgent phrase detected: {word}")

# Check sensitive words
for word in sensitive_words:
    if word in email:
        risk_score += 3
        reasons.append(f"Sensitive info request: {word}")

# Check scam phrases
for word in scam_words:
    if word in email:
        risk_score += 2
        reasons.append(f"Possible scam phrase: {word}")

# Detect links
links = re.findall(r'https?://\S+|www\.\S+', email)

if links:
    risk_score += len(links)
    reasons.append(f"Suspicious links found: {len(links)}")

# Detect email addresses
emails = re.findall(r'\S+@\S+', email)

if emails:
    reasons.append(f"Email addresses detected: {len(emails)}")

# Detect excessive symbols
if email.count("!") >= 3:
    risk_score += 1
    reasons.append("Too many exclamation marks")

# Final Risk Level
print("\n===== ANALYSIS REPORT =====\n")

if reasons:
    for r in reasons:
        print("•", r)
else:
    print("No suspicious activity detected.")

print("\nTotal Risk Score:", risk_score)

if risk_score >= 7:
    print("Risk Level : HIGH")
elif risk_score >= 4:
    print("Risk Level : MEDIUM")
else:
    print("Risk Level : LOW")

print("\n===== SCAN COMPLETED =====")