# Decoding Base64 Passwords

## Metadata

- **ID:** 1777702
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Easy, Cryptographic Failures, Encoding and Decoding
- **Skills:** OWASP Top 10

## Summary

This multiple choice question evaluates cryptographic failures, encoding and decoding, and Base64 concepts, ideal for junior-level roles. The problem requires identifying the correct method to decode a Base64-encoded password from a code snippet.

## Problem Statement

Consider the following code snippet:

`import base64

def main():
    encoded_password = "cGFzc3dvcmQ="  # Encoded password
    # Decode the password (the correct decoding logic is not shown here)
    decoded_password = ...
    print(decoded_password)

if __name__ == "__main__":
    main()`
```

Which of the following statements correctly decodes the password?

## Preview

Consider the following code snippet:
