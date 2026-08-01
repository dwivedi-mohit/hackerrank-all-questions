# Cheese and Random Toppings

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.5506912442396313
- **Total Submissions:** 1736
- **Solved Count:** 956
- **URL:** https://www.hackerrank.com/challenges/cheese-and-random-toppings

## Problem Statement

*Waiter:* Good day, sir! What would you like to order?  
*Lucas:* One Cheese & Random Toppings (CRT) pizza for me, please.  
*Waiter:* Very good, sir. There are $N$ toppings to choose from, but you can choose only $R$ toppings.     
*Lucas:* Hmm, let's see...  

...Then Lucas started writing down all the ways to choose *R* toppings from *N* toppings in a piece of napkin. Soon he realized that it's impossible to write them all, because there are a lot. So he asked himself: **How many ways are there to choose exactly $R$ toppings from $N$ toppings?**

Since Lucas doesn't have all the time in the world, he only wished to calculate the answer **modulo $M$**, where *M* is a squarefree number whose prime factors are each less than *50*.

Fortunately, Lucas has a Wi-Fi-enabled laptop with him, so he checked the internet and discovered the following useful links:  
[Lucas' theorem](http://en.wikipedia.org/wiki/Lucas'_theorem)  
[Chinese remainder theorem (CRT)](http://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_and_uniqueness)  

**Input Format**  
The first line of input contains $T$, the number of test cases. The following lines describe the test cases.

Each test case consists of one line containing three space-separated integers: $N$, $R$ and $M$.  

**Constraints**  
$1 \le T \le 200$  
$1 \le M \le 10^9$  
$1 \le R \le N \le 10^9$  
$M$ is squarefree and its prime factors are less than $50$

**Output Format**  
For each test case, output one line containing a single integer: the number of ways to choose $R$ toppings from $N$ toppings, modulo $M$.  

**Sample Input**  
    
    6
    5 2 1001
    5 2 6
    10 5 15
    20 6 210
    13 11 21
    10 9 5    

**Sample Output**  

    10
    4
    12
    120
    15
    0
  
**Explanation**  

*Case 1 and 2*: Lucas wants to choose *2* toppings from *5* toppings. There are ten ways, namely (assuming the toppings are **A**, **B**, **C**, **D** and **E**):  

**AB**, **AC**, **AD**, **AE**, **BC**, **BD**, **BE**, **CD**, **CE**, **DE**  

Thus,  
*Case 1*: $10 \bmod 1001 = 10$  
*Case 2*: $10 \bmod 6 = 4$  



*Case 6*: We can choose *9* toppings from *10* by removing only one from our choice. Thus, we have ten ways and $10 \bmod 5 = 0$

## Input Format

The first line of input contains , the number of test cases. The following lines describe the test cases.

Each test case consists of one line containing three space-separated integers: ,  and .

## Output Format

For each test case, output one line containing a single integer: the number of ways to choose  toppings from  toppings, modulo .

## Constraints

is squarefree and its prime factors are less than

## Sample Input

5 2 1001
5 2 6
10 5 15
20 6 210
13 11 21
10 9 5

## Sample Output

4
12
120
15
0

## Explanation

Case 1 and 2: Lucas wants to choose 2 toppings from 5 toppings. There are ten ways, namely (assuming the toppings are A, B, C, D and E):

AB, AC, AD, AE, BC, BD, BE, CD, CE, DE

Thus,

Case 1:

Case 2:

Case 6: We can choose 9 toppings from 10 by removing only one from our choice. Thus, we have ten ways and
