# api-security-SumanthReddy

# API Security - Healthcare Weather Alerts

## Changes Implemented:

**Task 1 - Security Fix**  
- Removed hardcoded API key  
- Now loading securely from `.env` using `python-dotenv`

**Task 2 - Rate Limiting**  
- Added proper handling for HTTP 429 (Too Many Requests) with a clear user message

**Task 3 - Privacy Protection**  
- Removed logging of user's searched city  
- Added comment explaining why location data must not be logged in a healthcare app

## Privacy & Security Notes:

**Why no logging of city names?**  
In a healthcare context, even basic location data can be considered sensitive. Logging it violates the **data minimization** principle under **GDPR** and can breach healthcare privacy standards.

**Real-world consequences of exposing an API key on GitHub:**  
- Attackers can steal the key and exhaust your free quota or incur high costs  
- The key can be abused for malicious requests  
- In a healthcare startup, it risks compliance violations and potential legal/financial damage

## Files in this repo:
- `weather.py`
- `.env.example`
- `.gitignore`
- `README.md`

`.env` is **not** committed (verified in GitHub file tree).
