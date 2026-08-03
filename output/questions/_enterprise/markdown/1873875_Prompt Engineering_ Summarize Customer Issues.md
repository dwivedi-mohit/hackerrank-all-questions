# Prompt Engineering: Summarize Customer Issues

## Metadata

- **ID:** 1873875
- **Type:** prompt_engineering
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Prompt Engineering, Few-Shot Prompting, Profiling Model Responses, Role Prompting
- **Skills:** Prompt Engineering (Basic)

## Summary

This prompt engineering question evaluates prompt creation, information extraction, and data summarization concepts, ideal for junior-level roles. The task involves writing prompts to extract specific customer transaction details from chat transcripts.

## Problem Statement

An analyst working in a bank must understand and address customer issues. The goal is to understand and summarize the information from chat transcripts between customers and support agents regarding payment issues.

 

Task: 

Write prompts to query the customer support chats and extract the following information:

	
- Customer name
	
- Country
	
- Amount debited
	
- Payment mode (CREDIT_CARD/DEBIT_CARD/BANK_TRANSFER)
	
- Date of transaction (in YYYY-MM-DD format; assume the year is 2024 if not mentioned in the chat)

If any field is not present or the user is unsure about them, consider them MISSING.

Extract the above fields and return a separate comma string.

 

NOTE: The {testcase input} field is a placeholder that will be auto-filled with various inputs to test the prompt.

 

Sample Case 1

 

Sample Input

<user>: Hi, my name is Sam Doe from Canada. $150 was debited from my account via CREDIT_CARD on July 25th 2024, and I didn't authorize it.

<agent>: Hi Sam, I'm Alex. I see the transaction and will escalate it to our billing department. They typically respond within 3-5 business days. We'll keep you updated. Is there anything else I can assist you with?

<user>: No, that's all. Thank you.

<agent>: You're welcome, Sam. We apologize for the inconvenience and appreciate your patience. Have a great day!

<user>: You too, bye.
```

 

Sample Output

Sam Doe,Canada,150,CREDIT_CARD,2024-07-25
```

 

Explanation

The user mentioned the name as Sam Doe and the country as Canada. The user also mentioned the transaction amount as 150 in the local currency, which was done via credit card, and the transaction date was 2024-07-25.

 

Sample Case 2

 

Sample Input

<user>: Hello, I need assistance. My name’s Carol, residing in Mexico. Recently, there was a monetary issue with my account.

<agent>: Hi Carol, can you provide details on the problem?

<user>: Certainly. An amount was removed from my account—3000 pesos. The transaction involved some form of bank processing. I think it was in the middle month of this year.

<agent>: Do you have any other information about the transaction date?

<user>: No.

<agent>: Okay, I’ll check the details and get back to you.
```

 

Sample Output

Carol,Mexico,3000,BANK_TRANSFER,MISSING
```

 

Explanation

The user mentioned the name as Carol and the country as Mexico. The user also mentioned the transaction amount as 3000 in the local currency which was done via bank. No exact transaction date was mentioned, so it is assumed as missing.

## Sample Input/Output

## Preview

An analyst working in a bank must understand and address customer issues. The
