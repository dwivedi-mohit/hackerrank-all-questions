# PKCE Encode

## Metadata

- **ID:** 2119348
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** PKCE, Encoding and Decoding, Node.js, Hard, OAuth2
- **Skills:** Node.js (Advanced)

## Summary

This multiple choice question evaluates PKCE, encoding and decoding, and OAuth2 concepts, ideal for senior-level roles. The problem requires identifying the correct method to construct a valid PKCE code challenge that an identity provider will accept.

## Problem Statement

You construct the PKCE code challenge:

const verifier  = base64url(crypto.randomBytes(32));
const challenge = base64url(crypto.createHash('sha256')
                       .update(verifier).digest());
```

The identity provider rejects the request with “invalid_code_challenge.” what change would you make to ensure the provider accepts your PKCE challenge?

## Preview

You construct the PKCE code challenge:
