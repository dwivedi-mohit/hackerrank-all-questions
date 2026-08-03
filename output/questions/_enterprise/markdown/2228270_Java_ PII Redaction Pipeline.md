# Java: PII Redaction Pipeline

## Metadata

- **ID:** 2228270
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, Easy, Polymorphism, Encapsulation, OOP
- **Skills:** Java (Basic)
- **Languages:** j, a, v, a, 8, ,, j, a, v, a

## Summary

This coding question evaluates redaction rules, regular expressions, and object-oriented programming concepts, ideal for junior-level roles. The problem requires implementing a system to redact sensitive data from logs using specified rules in a defined order.

## Problem Statement

Your application forwards logs from multiple services to a monitoring provider. Before sending, it must redact sensitive data like emails, credit card numbers, and API keys, using modular, order-dependent redaction rules applied in the given order.

 

Redaction Rules

You must implement a redaction system supporting three types of rules:

	
- 
Email Addresses:

	
		
- Replace all email addresses with [REDACTED_EMAIL].
		
- 
Use a precompiled, case-insensitive regex pattern to match standard email addresses of the form local@domain.extension, where:
		
			
- local part: can include one or more letters, digits, underscores, dots, percent, plus, or minus signs.
			
- domain part: can include one or more letters, digits, dots, or hyphens.
			
- extension part: includes one or more letters.
		
		
	
	
	
- 
Payment Card Numbers:
	
		
- Replace all 13–19 digit sequences (single space or a dash is allowed between the digits) with [REDACTED_CARD], only if the number passes the Luhn checksum.
		
- 
Luhn Checksum Definition:
		
			
- Starting from the rightmost digit, double every second digit.
			
- If doubling results in a number greater than 9, subtract 9 from it.
			
- Sum all digits — if the total is divisible by 10, the number passes the check.
		
		
	
	
	
- 
API Keys:
	
		
- 
Replaces labeled API key assignments where a label like api_key, api-key, or apikey is followed by : (colon) or = (equal to), optional whitespace, then a token (the key) made up of 8–64 characters from [A-Z a-z 0-9 _ -] with <label>: [REDACTED_KEY], keeping the label intact and normalizing the separator to a colon (:).

	
	

All patterns must be precompiled and case-insensitive where appropriate. Rules are applied in order, using a Redactor that applies each RedactionRule sequentially.

 

Implement the following classes: RedactionRule, EmailRedaction, CardRedaction, ApiKeyRedaction, and Redactor, to transform a log line by applying rules in sequence.

 

Class Definitions:

	
- 
EmailRedaction Class

	
		
- 
Pattern EMAIL: Precompiled regex for detecting email addresses (case-insensitive)

		
- 
String apply(String input): Replace all detected emails with [REDACTED_EMAIL].

	
	
	
- 
CardRedaction Class
	
		
- 
Pattern DIGIT_BLOB: Precompiled regex to find 13–19 digits with optional spaces/dashes.

		
- 
String apply(String input): For each match, strip non‑digits and perform a Luhn check; Redact only if passesLuhn() returns true.

		
- 
boolean passesLuhn(String digits): Implements the Luhn checksum validation

	
	
	
- 
ApiKeyRedaction Class
	
		
- 
Pattern API_KEY: Precompiled, case‑insensitive regex capturing the label (api_key, API-KEY, apikey).

		
- Replaces the whole key with <label>: [REDACTED_KEY].
	
	
	
- 
Redactor Class
	
		
- 
Constructor: Redactor(List<RedactionRule> rules). Store an immutable copy of rules to preserve order.

		
- 
String redact(String input): Applies each rule sequentially.

	
	

 

Example

Input:

3
1 2 3
1
User alice@example.com paid with 4111-1111-1111-1111. api_key=AbCdEf1234567890 sent to /checkout
```

Output:

User [REDACTED_EMAIL] paid with [REDACTED_CARD]. api_key: [REDACTED_KEY] sent to /checkout
```

Explanation:

Interpretation:

	
- 
Line 1: r = number of active rules

	
- Line 2: order of rules (space‑separated) where: 1 = EmailRedaction, 2 = CardRedaction, 3 = ApiKeyRedaction.
	
- 
Line 3: n = number of log lines to process

	
- 
Next n lines: single log line (may contain spaces)

Calculations

	
- Email first (rule 1) finds "alice@example.com" → [REDACTED_EMAIL].
	
- Card next (rule 2) matches 4111‑1111‑1111‑1111, strips separators → 4111111111111111, passes Luhn → [REDACTED_CARD].
	
- API key last (rule 3) matches api_key=..., keeps label, normalizes to colon → api_key: [REDACTED_KEY].

 

Luhn Check for 4111111111111111:

	
- Digits (from right): 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 4
	
- Now doubling every second digit from right → [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 8] → subtracting 9 where needed: (no changes here since all doubles ≤ 9).
	
- Sum = 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 8 = 30. Since 30 is divisible by 10, it passes the Luhn check.

 

Example 2

Input:

3
2 1 3
4
Charge 5555 5555 5555 4444, by bob@example.com
Noise digits 1234-5678-9012-3456 remain; API-KEY: ABCD-1234-XYZ_9876
Contact us at Support@Example.org or api_key=short
Card 4242-4242-4242-4242; api_key = AAAA1111BBBB2222
```

Output:

Charge [REDACTED_CARD], by [REDACTED_EMAIL]
Noise digits 1234-5678-9012-3456 remain; API-KEY: [REDACTED_KEY]
Contact us at [REDACTED_EMAIL] or api_key=short
Card [REDACTED_CARD]; api_key: [REDACTED_KEY]
```

Explanation:

	
- Card first (rule 2): 5555 5555 5555 4444 and 4242‑4242‑4242‑4242 pass Luhn → redacted.
	
- Email next (rule 1): both emails → redacted.
	
- API keys last (rule 3): label kept, value replaced.
	
- The sequence 1234‑5678‑9012‑3456 fails Luhn → not redacted.
	
- api_key=short has a value shorter than 8 chars → not redacted.

 

Constraints:

	
- 
1 ≤ r ≤ 3

	
- 
1 ≤ n ≤ 6

	
- 
1 ≤ ∣logLine∣ ≤ 106

 

Input Format for Custom Testing

The first line contains an integer r — the number of active rules (1..3).

The second line contains r integers describing the order of rules (space‑separated):

	
- 1 = EmailRedaction, 2 = CardRedaction, 3 = ApiKeyRedaction.

The third line contains an integer n — the number of log lines to process.

Each of the next n lines contains a single log line (may contain spaces).

## Sample Input/Output

## Preview

Your application forwards logs from multiple services to a monitoring provider
