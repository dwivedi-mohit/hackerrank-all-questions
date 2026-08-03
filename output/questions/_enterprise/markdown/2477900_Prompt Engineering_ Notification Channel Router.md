# Prompt Engineering: Notification Channel Router

## Metadata

- **ID:** 2477900
- **Type:** prompt_engineering
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Prompt Engineering, Easy
- **Skills:** Prompt Engineering (Basic)

## Summary

This prompt engineering question evaluates notification routing, channel definitions, and user preferences concepts, ideal for junior-level roles. The task requires writing a prompt that determines the correct delivery channel based on structured notification records and specified routing rules.

## Problem Statement

A platform communications system must route each outgoing notification to the correct delivery channel based on the notification type and user preference. The candidate must write a prompt that reads a structured notification record and outputs exactly one channel label.

 

Task

Write a prompt that reads a structured notification record and outputs exactly one channel label by applying the routing rules below in priority order.

 

Channel definitions:

	
- 
	
SMS — For security-critical and account-action notifications that require immediate delivery regardless of user preference

	
	
- 
	
SUPPRESS — For marketing or promotional notifications when the user has opted out

	
	
- 
	
PUSH — For time-sensitive but non-critical activity and delivery updates

	
	
- 
	
EMAIL — For detailed transactional and financial notifications

	
	
- 
	
IN_APP — For social interactions and engagement notifications

	

 

Routing rules (apply in priority order — stop at first match):

	
- 
	
SMS — Notification Type is one of: password_reset, login_attempt, account_locked, payment_failed

	
	
- 
	
SUPPRESS — User Preference is opt_out AND Notification Type is one of: promotional, newsletter, survey

	
	
- 
	
PUSH — Notification Type is one of: order_shipped, delivery_update, flash_sale, appointment_reminder

	
	
- 
	
EMAIL — Notification Type is one of: invoice_ready, subscription_renewal, weekly_report, account_statement

	
	
- 
	
IN_APP — Notification Type is one of: new_message, comment, like, follow, mention

	

 

Allowed output values:

	
- 
	
SMS

	
	
- 
	
SUPPRESS

	
	
- 
	
PUSH

	
	
- 
	
EMAIL

	
	
- 
	
IN_APP

	

Rules:

	
- 
	
Apply rules in the order listed above. Stop at the first rule that matches.

	
	
- 
	
Output must be exactly one channel label. No explanation, no punctuation, no other text.

	

 

NOTE: The {testcase input} field is a placeholder that will be auto-filled with various inputs to test the prompt.

 

Sample Case 1

 

Sample Input

`Notification Type: password_reset
Urgency: critical
User Preference: opt_in`
```

 

Sample Output

`SMS`
```

 

Explanation

password_reset is a security-critical notification type. Rule 1 (SMS) fires immediately → SMS.

Sample Case 2

 

Sample Input

`Notification Type: invoice_ready
Urgency: medium
User Preference: opt_in`
```

 

Sample Output

`EMAIL`
```

 

Explanation

invoice_ready does not match the SMS types (rule 1). It matches the EMAIL rule (rule 4) → EMAIL.

## Sample Input/Output

## Preview

A platform communications system must route each outgoing notification to t
