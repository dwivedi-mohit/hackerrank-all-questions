# Tries: Contacts

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.6604661421954268
- **Total Submissions:** 40803
- **Solved Count:** 26949
- **URL:** https://www.hackerrank.com/challenges/ctci-contacts

## Problem Statement

We're going to make our own *Contacts* application! The application must perform two types of operations:

1. `add name`, where $name$ is a string denoting a contact name. This must store $name$ as a new contact in the application.  
2. `find partial`, where $partial$ is a string that denotes a partial name to search the application for. It must count the number of contacts starting with $partial$ and print the count on a new line.

Given $n$ sequential *add* and *find* operations, perform each operation in order.



## Input Format

The first line contains a single integer, $n$, the number of operations to perform.  
Each line $i$ of the $n$ subsequent lines contains an operation in one of the two forms defined above.  

## Output Format

For each `find partial` operation, print the number of contact names starting with $partial$ on a new line.

## Constraints

- $1 \le n \le 10^5$  
- $1 \le |name| \le 21$  
- $1 \le |partial| \le 21$  
- It is guaranteed that $name$ and $partial$ contain lowercase English letters only.
- The input does not have any duplicate $name$ for the $add$ operation.

## Sample Input

add hack
add hackerrank
find hac
find hak

## Sample Output

0

## Explanation

We perform the following sequence of operations:

- Add a contact named hack.

- Add a contact named hackerrank.

- Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print  on a new line.

- Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
