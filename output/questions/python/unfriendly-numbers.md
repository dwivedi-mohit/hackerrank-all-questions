# Unfriendly Numbers

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.30816714150047486
- **Total Submissions:** 4212
- **Solved Count:** 1298
- **URL:** https://www.hackerrank.com/challenges/unfriendly-numbers

## Problem Statement

Given $1$ *friendly* number and $n$ *unfriendly* numbers, determine how many numbers are divisors of the friendly number but *not* the unfriendly numbers.

## Input Format

The first line contains $2$ space-separated integers, $n$ (the number of unfriendly numbers) and $f$ (the friendly number), respectively. 
The second line contains $n$ space-separated unfriendly numbers.

## Output Format

Print the the number of unique divisors of $f$ (i.e.: divisors that are not shared with those of the unfriendly numbers) as a single integer.

## Constraints

- $1 \le n \le 10^6$
- $1 \le f \le 10^{13}$
- $1 \le \textit{unfriendly numbers} \le 10^{18}$

## Sample Input

8 16
2 5 7 4 3 8 3 18

## Explanation

There are  unfriendly numbers: .

Our friendly number, , is , and its even divisors are .

Let  be the number of friendly divisors that are not also unfriendly divisors. Let's determine which divisors of  are not also divisors of the unfriendly numbers:

-  is a divisor of all unfriendly numbers, so we disregard it.

-  is a divisor of unfriendly numbers , , and , so we disregard it.

-  is a divisor of unfriendly numbers  and , so we disregard it.

-  is a divisor of unfriendly number , so we disregard it.

-  is not a divisor of any unfriendly number, so we increment  to .

As there are no more friendly divisors to check, we print the value of  (which is ) on a new line.
