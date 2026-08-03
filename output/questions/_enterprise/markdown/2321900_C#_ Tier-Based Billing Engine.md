# C#: Tier-Based Billing Engine

## Metadata

- **ID:** 2321900
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Object Oriented Programming, Inheritance, Polymorphism, Easy, C#
- **Skills:** C# (Basic)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates inheritance, polymorphism, and interface implementation concepts, ideal for junior-level roles. The problem requires implementing classes for an API billing system that calculates costs based on client types and connection information.

## Problem Statement

An API platform computes per-request billing for API clients that are connection-aware:

Billing Rules:

	
- 
Each request has a baseCost.

	
- 
Each client has a connectionInfo object with a region ∈ {US, EU, APAC} and a network tier ∈ {SHARED, DEDICATED}.

	
- 
adjustedCost = baseCost * regionMultiplier * tierMultiplier.

	
- 
Regular client final cost = adjustedCost.

	
- 
Premium client final cost = adjustedCost * (1 − discountRate/100).

Multipliers:

	
- 
Region: US = 1.00, EU = 1.05, APAC = 0.98.

	
- 
Network Tier: SHARED = 1.00, DEDICATED = 1.10.

Implement the following classes: RegularApiClient, PremiumApiClient, and BillingBatch. RegularApiClient and PremiumApiClient inherit from the abstract base class ApiClient; BillingBatch implements the IBillingBatch interface as follows:

	
- 
ApiClient (abstract class): Represents a connection-aware API client. Declares double CalculateBill(double baseCost), which subclasses implement (Regular: return adjusted cost; Premium: return discounted adjusted cost). RegularApiClient and PremiumApiClient extend this class.

	
- 
IBillingBatch (interface): Declares void AddRequest(ApiClient client, double baseCost) and double GetTotalBill(). BillingBatch implements this interface.

	
- 
RegularApiClient class (extends ApiClient):
	
		
- 
RegularApiClient(string name, ConnectionInfo connection): Constructor for Regular Clients.

		
- 
double CalculateBill(double baseCost): Returns the adjustedCost.

	
	
	
- 
PremiumApiClient class (extends ApiClient):
	
		
- 
PremiumApiClient(string name, ConnectionInfo connection, double discountRate): Constructor for Premium Clients.

		
- 
double CalculateBill(double baseCost): Returns the discounted adjustedCost (i.e. adjustedCost × (1 − discountRate/100)).

	
	
	
- 
BillingBatch class (implements IBillingBatch):
	
		
- 
void AddRequest(ApiClient client, double baseCost): Adds a billing request to the batch.

		
- 
double GetTotalBill(): Computes the sum of all client bills in the batch.

	
	

The following are denoted by: 

	
- 
type: 1 = RegularApiClient, 2 = PremiumApiClient

	
- region: 1 = US, 2 = EU, 3 = APAC
	
- tier: 1 = SHARED, 2 = DEDICATED

 

Example 1

Input: 

`2
2 2 2 1000 20
1 1 1 500`
```

Output: 

`Total Bill:1424.00`
```

Explanation:

Interpretation

	
- 
Line 1: Number of billing requests, i.e., n = 2

	
- 
Line 2: Type of client: 2 = PremiumApiClient, EU + DEDICATED, baseCost = 1000, discountRate = 20%

	
- 
Line 3: Type of client: 1 = RegularApiClient, US + SHARED, baseCost = 500

Calculations

	
- Premium: 1000 × 1.05 × 1.10 × (1 − 0.20) = 924.00
	
- Regular: 500 × 1.00 × 1.00 = 500.00
	
- Total Bill:1424.00

 

Example 2 

Input: 

`4
2 2 2 1000 20
1 1 1 500
2 1 1 200 50
1 3 2 350`
```

Output: 

`Total Bill:1901.30`
```

Explanation:

	
- 
Premium (EU, DEDICATED), baseCost = 1000, discountRate = 20 % → 1000 * 1.05 * 1.10 * 0.80 = 924.00.

	
- 
Regular (US, SHARED), baseCost  = 500 → 500 * 1.00 * 1.00 = 500.00

	
- 
Premium (US, SHARED), baseCost  = 200, discountRate  = 50% → 200 * 1 * 1 * 0.50 = 100.00

	
- 
Regular (APAC, DEDICATED), baseCost  = 350 → 350 * 0.98 * 1.10 = 377.30

	
- Total Bill = 924.00 + 500.00 + 100.00 + 377.30 = 1901.30.

 

Constraints

	
- 
1 ≤ n (number of billed requests) ≤ 10

	
- 
0 ≤ baseCost ≤ 109

	
- 
0 ≤ discountRate ≤ 100

 

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

	
- First line: integer n

	
- Next n lines: type region tier baseCost [discountRate], where discountRate is provided only when type = 2 (PremiumApiClient).

## Sample Input/Output

## Preview

An API platform computes per-request billing for API clients that are connecti
