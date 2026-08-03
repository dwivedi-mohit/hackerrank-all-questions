# Java Threads: Transactions

## Metadata

- **ID:** 417443
- **Type:** approx
- **Difficulty:** 8.61111111111111
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Language Proficiency, Java, Multithreading, Medium, Problem Solving
- **Skills:** Java (Intermediate)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates Java, multithreading, and problem-solving concepts, ideal for mid-level roles. The problem requires simulating a banking system with Account and Transaction classes that handle deposits and withdrawals in a thread-safe manner.

## Problem Statement

In this challenge, simulate a banking system. Create the Account and Transaction classes.

	
- The Account class has a data member int balance, initially assigned to zero. The class should implement the following three methods:

	
		
- 
String deposit(int money) to add money to the balance. This method should return a string that describes the deposit transaction, i.e., "Depositing $money".
		
- 
String withdraw(int money) to subtract money from the balance. This method should return a string that describes the withdraw transaction, i.e., "Withdrawing $money". Note that, if there is insufficient balance to successfully withdraw the desired amount, then the balance should not be adjusted, and the returned string should be "Withdrawing $money (Insufficient Balance)".
		
- 
int getBalance() to return the account balance.
	
	
	
- The Transaction class has two data members Account account and List<String> transactions. The class should implement the following three methods:
	
		
- 
void deposit(int money) to invoke the deposit method in the Account class. This should add the transaction message to the transactions list.
		
- 
void withdraw(int money) to invoke the withdraw method in the Account class. This should add the transaction message to the transactions list.
		
- 
List<String> getTransaction() to return the transactions.
	
	

 

Evaluation

The locked stub code in the editor validates the correctness of the Account and Transaction class implementations by making deposit and withdrawal transactions using threads. The locked stub code prints each transaction followed by the account balance. The output of the execution is non-deterministic, so the checker performs each of the transactions in the provided order. If all the transactions are executed correctly given a starting balance of $0, then the checker considers such transactions valid. For example, the following list of transactions is valid:

Depositing $59
Withdrawing $2
Depositing $62
Depositing $16
```

But the following list of transactions is not:

Withdrawing $59
Withdrawing $2
Depositing $62
Depositing $16
```

The first two withdrawals should not have occurred. Rather, they should have returned:

Withdrawing $59 (Insufficient Balance)
Withdrawing $2 (Insufficient Balance)

```

 

Constraints

	
- 1 ≤ threadsCount ≤ 10
	
- 1 ≤ money ≤ 100
	
- Each thread makes no more than 104 transactions.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains the value of threadsCount describing the total number of threads.

Each of the next threadsCount lines contains an integer transactionsCount, the total number of transactions performed by each of the threads.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input 0

2
3
2
```

Sample Output 0

Depositing $59
Withdrawing $2
Depositing $62
Depositing $16
Withdrawing $52
Balance $83
```

Explanation 0

Note that this execution is never deterministic. Each execution with the same input could generate different output. For example, the following is also a valid output:

Withdrawing $67 (Insufficient Balance)
Depositing $35
Depositing $7
Depositing $80
Depositing $45
Balance $167
```

## Sample Input/Output

## Preview

In this challenge, simulate a banking system. Create the Account and Transacti
