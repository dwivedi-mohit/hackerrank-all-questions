# Membership Access Control

## Metadata

- **ID:** 2458175
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, TypeScript, Classes, OOPS, Maps
- **Skills:** Typescript (Intermediate)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates class design, hierarchical access validation, and event-driven counter management concepts, ideal for mid-level roles. The problem requires implementing a GymAccessSystem to manage member access through a card-based system with specific commands and reporting functionality.

## Problem Statement

A fitness club manages member access through a card-based system. Each member account holds one card identified by a unique accessCardId. Accounts follow a two-tier hierarchy: a PRIMARY account is the root of a family group, and a DEPENDENT account is linked to a PRIMARY parent via parentId, where parentId is the accountId of the parent PRIMARY account

 

All newly registered cards start in the ACTIVE state. Invalid or same-state transitions are silently ignored. The system processes four commands:

	
- SUSPEND: transitions card state from ACTIVE to SUSPENDED.
	
- REINSTATE: transitions card state from SUSPENDED to ACTIVE.
	
- REVOKE: transitions card state to REVOKED permanently. A revoked card can never be reinstated.
	
- SCAN: attempts to grant entry. A PRIMARY scan is allowed only if its card is ACTIVE. A DEPENDENT scan is allowed only if both its card and its parent's card are ACTIVE. Otherwise denied.
	
		
- Every attempt increments scanCount regardless of outcome. If denied, it also increments deniedCount.
		
- Both are handled automatically by recordScan() on the AccessCard.
	
	

 

Implement a GymAccessSystem class with the following methods:

	
- 
register(accountId, tier, accessCardId, parentId?) - registers an account and creates its AccessCard

	
- 
processCardEvent(type, accessCardId) - applies SCAN, SUSPEND, REINSTATE, or REVOKE to the corresponding card
	
- 
getReport() - returns a report sorted by PRIMARY accounts in ascending ASCII order by accountId, with each immediately followed by its DEPENDENT accounts, also sorted by accountId in ascending ASCII order.

 

Example

Input:

`2
p1 PRIMARY C001
d1 DEPENDENT C002 p1
4
REVOKE C001
REINSTATE C001
SCAN C002
SCAN C001`
```

Output:

`p1 C001 REVOKED scans=1 denied=1
  d1 C002 ACTIVE scans=1 denied=1
Issued:2 Revoked:1 Denied:2`
```

Explanation:

	
- p1 (C001) is registered as the PRIMARY account and d1 (C002) as its DEPENDENT. Issued = 2.
	
- REVOKE C001 changes the parent card to REVOKED, and the later REINSTATE C001 is ignored because revoked cards cannot be reinstated.
	
- SCAN C002 is denied because its parent card is not ACTIVE, and SCAN C001 is denied because a primary card must itself be ACTIVE. Final totals: Revoked = 1, Denied = 2.

 

Constraints

	
- 1 ≤ s ≤ 50, where s is the number of accounts
	
- 1 ≤ e ≤ 200, where e is the number of events
	
- 
	
Each PRIMARY appears before its DEPENDENT accounts in the input and has at most 10 dependents.

	
	
- 
accountId and accessCardId are unique, alphanumeric, 1-30 chars
	
- A DEPENDENT's parentId always references the accountId of a valid PRIMARY account

 

Note: The AccessCard class is already implemented in the stub and must not be modified.

 

Input Format for Custom Testing

The first line contains s, the number of accounts. Each of the next s lines contains one of:

	
- <accountId> PRIMARY <accessCardId>
	
- <accountId> DEPENDENT <accessCardId> <parentId>

The next line contains e, the number of events. Each of the next e lines contains one of:

	
- SCAN <accessCardId>
	
- SUSPEND <accessCardId>
	
- REINSTATE <accessCardId>
	
- REVOKE <accessCardId>

## Sample Input/Output

## Preview

A fitness club manages member access through a card-based system. Each member ac
